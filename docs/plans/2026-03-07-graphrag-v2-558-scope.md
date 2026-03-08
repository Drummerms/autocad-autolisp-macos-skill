# GraphRAG v2: 558-Doc Scope — Implementation Plan

> **Status: COMPLETE** (2026-03-08). All 9 tasks implemented and verified. Full build: 560 docs → 2,828 nodes, 2,261 relationships. MCP server tested end-to-end. Docs removed from repo (maintained in separate docs repo).

**Goal:** Revert all GraphRAG v1 commits, then re-implement GraphRAG scoped to only the 558 AutoLISP function docs that have `*Supported Platforms:*` markers — fixing all 5 Kuzu API bugs from the start.

**Architecture:** `build_graph.py` filters docs to 558 with platform markers, calls Haiku to extract entities/relationships, generates MiniLM embeddings, stores in Kuzu. `mcp_server.py` serves semantic search + graph traversal via FastMCP. All Kuzu API fixes (vector extension, QUERY_VECTOR_INDEX, variable-length paths, parameterized queries) are pre-applied.

**Tech Stack:** Python 3.12, Kuzu (with vector extension), sentence-transformers (all-MiniLM-L6-v2), Anthropic SDK (Claude Haiku), MCP (FastMCP), python-dotenv, tqdm

**Design doc:** `docs/plans/2026-03-07-graphrag-v2-558-scope-design.md`

---

### Task 1: Revert all GraphRAG v1 commits

**Files:**
- Modify: all files changed between `076e326` and `HEAD`

This reverts 11 commits: `ffe7e23`, `1ad3a7c`, `a30e630`, `995bada`, `0738193`, `baaf17a`, `bf7998d`, `1147534`, `6c1bd70`, `d1d2f81`, `bd392e0`, `5386592`, `d3926a8`, `2b6d909`.

**Step 1: Revert to the target commit**

Run:
```bash
git revert --no-commit HEAD~13..HEAD
```

This stages a revert of all 13 commits after `076e326` without creating individual revert commits. (13 commits = from `2b6d909` through `ffe7e23`.)

If any conflicts arise, resolve them by accepting the `076e326` version (the "theirs" in a revert is the old state).

**Step 2: Verify the working tree matches the target**

Run:
```bash
git diff --stat 076e326 -- . ':!docs/plans/2026-03-07-graphrag-v2*'
```

Expected: Only the v2 design doc should differ. All other files should match `076e326`.

**Step 3: Commit the revert**

```bash
git commit -m "revert: remove GraphRAG v1 implementation (preparing for v2 scoped rebuild)"
```

**Step 4: Verify clean state**

Run:
```bash
ls build_graph.py mcp_server.py requirements.txt .mcp.json CLAUDE.md 2>/dev/null && echo "FILES STILL EXIST" || echo "CLEAN"
```

Expected: `CLEAN` (all GraphRAG files removed). The `docs/` directory with 4,510 markdown files should still exist.

---

### Task 2: Clean up artifacts and set up environment

**Files:**
- Modify: `.gitignore`

**Step 1: Delete local artifacts from v1**

Run:
```bash
rm -rf autolisp.db/ .venv/ __pycache__/ .env
```

**Step 2: Update .gitignore for GraphRAG v2**

The current `.gitignore` after revert only has `.DS_Store`. Add the entries needed for v2:

```
# macOS
.DS_Store

# Python venv
.venv/

# GraphRAG
autolisp.db/
__pycache__/
*.pyc
.env
```

**Step 3: Create .env with placeholder**

Create `.env` at project root:

```
ANTHROPIC_API_KEY=your-key-here
```

**Step 4: Commit**

```bash
git add .gitignore
git commit -m "chore: update .gitignore for GraphRAG v2 artifacts"
```

---

### Task 3: Create requirements.txt and set up Python 3.12 venv

**Files:**
- Create: `requirements.txt`

**Step 1: Create requirements.txt**

```
kuzu>=0.7.0
anthropic>=0.40.0
sentence-transformers>=3.0.0
mcp>=1.0.0
tqdm>=4.66.0
python-dotenv>=1.0.0
```

**Step 2: Create Python 3.12 venv and install**

Kuzu 0.11.3 has no pre-built wheels for Python 3.14 (Homebrew default). Must use Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If `python3.12` is not installed:
```bash
brew install python@3.12
```

**Step 3: Verify imports**

Run:
```bash
.venv/bin/python3 -c "
import kuzu
import anthropic
import sentence_transformers
import mcp.server.fastmcp
import dotenv
import tqdm
print('All imports OK')
"
```

Expected: `All imports OK`

**Step 4: Verify Kuzu vector extension**

Run:
```bash
.venv/bin/python3 -c "
import kuzu
db = kuzu.Database('./test_kuzu_check')
conn = kuzu.Connection(db)
conn.execute('INSTALL vector; LOAD vector;')
print('Vector extension OK')
" && rm -rf ./test_kuzu_check
```

Expected: `Vector extension OK`

**Step 5: Commit**

```bash
git add requirements.txt
git commit -m "chore: add requirements.txt for GraphRAG v2"
```

---

### Task 4: Create build_graph.py with 558-doc filter

**Files:**
- Create: `build_graph.py`

**Step 1: Create the complete build script**

```python
"""
build_graph.py
--------------
Ingests AutoLISP function docs into a Kuzu graph database.
Only processes the ~558 docs that have *Supported Platforms:* markers
(function reference pages with structured metadata).

Uses Claude Haiku to extract entities and relationships from each file.

Usage:
    python build_graph.py --docs ./docs --db ./autolisp.db
    python build_graph.py --docs ./docs --db ./autolisp.db --limit 10
"""

import os
from dotenv import load_dotenv
import json
import re
import argparse
import hashlib
from pathlib import Path
from tqdm import tqdm
import kuzu
import anthropic
from sentence_transformers import SentenceTransformer

load_dotenv()

# -- Config --

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EXTRACTION_PROMPT = """\
You are processing AutoCAD/AutoLISP documentation. Extract structured data from
the markdown below. Return ONLY valid JSON with this exact schema:

{
  "entities": [
    {
      "name": "string",
      "type": "function|command|variable|concept|dialog|object",
      "summary": "string",
      "platform": "both|mac|windows_only",
      "mac_safe": true|false,
      "syntax": "string|null"
    }
  ],
  "relationships": [
    {
      "from": "entity_name",
      "to": "entity_name",
      "type": "calls|returns|parameter_of|alternative_to|related_to|requires"
    }
  ]
}

Rules:
- mac_safe=false for anything vlax-*, vlr-*, acet-*, vl-load-com
- platform="windows_only" for those same functions
- Extract ALL functions/commands mentioned, not just the primary one
- Keep summaries factual and brief

Markdown to process:
"""


# -- Database Schema --

def init_db(db_path: str) -> tuple:
    """Initialize Kuzu database and return (db, conn) tuple."""
    db = kuzu.Database(db_path)
    conn = kuzu.Connection(db)
    conn.execute("INSTALL vector; LOAD vector;")

    conn.execute("""
        CREATE NODE TABLE IF NOT EXISTS DocNode (
            id STRING PRIMARY KEY,
            name STRING,
            type STRING,
            summary STRING,
            platform STRING,
            mac_safe BOOLEAN,
            syntax STRING,
            embedding FLOAT[384],
            source_file STRING
        )
    """)

    conn.execute("""
        CREATE REL TABLE IF NOT EXISTS Relationship (
            FROM DocNode TO DocNode,
            type STRING
        )
    """)

    return db, conn


# -- Doc Filtering --

def has_platform_marker(filepath: Path) -> bool:
    """Check if a doc has a *Supported Platforms:* line (function reference)."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="ignore")
        return "*Supported Platforms:*" in text
    except Exception:
        return False


# -- Extraction --

def extract_entities(content: str, client: anthropic.Anthropic) -> dict:
    """Call Claude Haiku to extract entities and relationships."""
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": EXTRACTION_PROMPT + content[:4000]
            }]
        )
        text = response.content[0].text.strip()
        text = re.sub(r"^```json\s*|```$", "", text, flags=re.MULTILINE).strip()
        return json.loads(text)
    except Exception as e:
        print(f"  Warning: Extraction failed: {e}")
        return {"entities": [], "relationships": []}


def make_node_id(name: str, source_file: str) -> str:
    """Stable unique ID for a node."""
    return hashlib.md5(f"{name}::{source_file}".encode()).hexdigest()[:16]


# -- Ingestion --

def ingest_docs(docs_dir: str, db_path: str, limit: int = 0):
    print(f"Initialising database at {db_path}")
    db, conn = init_db(db_path)

    print(f"Loading embedding model: {EMBEDDING_MODEL}")
    embedder = SentenceTransformer(EMBEDDING_MODEL)

    client = anthropic.Anthropic()

    # Find all markdown files, then filter to function reference docs
    all_md = list(Path(docs_dir).rglob("*.md"))
    print(f"Found {len(all_md)} total markdown files")

    md_files = [f for f in all_md if has_platform_marker(f)]
    print(f"Filtered to {len(md_files)} function reference docs (have *Supported Platforms:*)")

    if limit > 0:
        md_files = md_files[:limit]
        print(f"   (limited to {limit} files for testing)")

    node_registry = {}

    for md_file in tqdm(md_files, desc="Ingesting docs"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        if len(content.strip()) < 50:
            continue

        extracted = extract_entities(content, client)

        for entity in extracted.get("entities", []):
            name = entity.get("name", "").strip()
            if not name:
                continue

            node_id = make_node_id(name, str(md_file))
            node_registry[name] = node_id

            summary = entity.get("summary", "")
            embedding = embedder.encode(f"{name} {summary}").tolist()

            try:
                conn.execute("""
                    MERGE (n:DocNode {id: $id})
                    SET n.name = $name,
                        n.type = $type,
                        n.summary = $summary,
                        n.platform = $platform,
                        n.mac_safe = $mac_safe,
                        n.syntax = $syntax,
                        n.embedding = $embedding,
                        n.source_file = $source_file
                """, {
                    "id": node_id,
                    "name": name,
                    "type": entity.get("type", "function"),
                    "summary": summary,
                    "platform": entity.get("platform", "both"),
                    "mac_safe": entity.get("mac_safe", True),
                    "syntax": entity.get("syntax") or "",
                    "embedding": embedding,
                    "source_file": str(md_file)
                })
            except Exception as e:
                print(f"  Warning: Node insert failed for {name}: {e}")

        for rel in extracted.get("relationships", []):
            from_name = rel.get("from", "")
            to_name = rel.get("to", "")
            rel_type = rel.get("type", "related_to")

            if from_name in node_registry and to_name in node_registry:
                try:
                    conn.execute("""
                        MATCH (a:DocNode {id: $from_id}), (b:DocNode {id: $to_id})
                        MERGE (a)-[:Relationship {type: $type}]->(b)
                    """, {
                        "from_id": node_registry[from_name],
                        "to_id": node_registry[to_name],
                        "type": rel_type
                    })
                except Exception as e:
                    print(f"  Warning: Relationship insert failed: {e}")

    print(f"\nIngestion complete.")
    result = conn.execute("MATCH (n:DocNode) RETURN count(n)").get_next()
    print(f"   Nodes: {result[0]}")
    result = conn.execute("MATCH ()-[r:Relationship]->() RETURN count(r)").get_next()
    print(f"   Relationships: {result[0]}")

    print("Creating vector index...")
    try:
        conn.execute("""
            CALL CREATE_VECTOR_INDEX('DocNode', 'doc_vec_index', 'embedding')
        """)
        print("   Vector index created.")
    except Exception as e:
        print(f"   Warning: Vector index creation failed (may already exist): {e}")


# -- Entry Point --

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build GraphRAG database from AutoLISP docs")
    parser.add_argument("--docs", default="./docs", help="Path to docs directory")
    parser.add_argument("--db",   default="./autolisp.db", help="Output Kuzu DB path")
    parser.add_argument("--limit", type=int, default=0,
                        help="Limit number of files to process (0 = all)")
    args = parser.parse_args()

    ingest_docs(args.docs, args.db, args.limit)
```

**Step 2: Verify syntax**

Run:
```bash
.venv/bin/python3 -c "import ast; ast.parse(open('build_graph.py').read()); print('OK')"
```

Expected: `OK`

**Step 3: Verify the filter finds ~558 docs**

Run:
```bash
.venv/bin/python3 -c "
from pathlib import Path
files = [f for f in Path('docs').rglob('*.md')
         if '*Supported Platforms:*' in f.read_text(encoding='utf-8', errors='ignore')]
print(f'Function reference docs: {len(files)}')
"
```

Expected: `Function reference docs: 558` (approximately)

**Step 4: Commit**

```bash
git add build_graph.py
git commit -m "feat: add build_graph.py v2 — scoped to 558 function docs with Kuzu fixes"
```

---

### Task 5: Create mcp_server.py with correct Kuzu API calls

**Files:**
- Create: `mcp_server.py`

**Step 1: Create the complete MCP server**

```python
"""
mcp_server.py
-------------
FastMCP server exposing GraphRAG search over the AutoLISP knowledge graph.
Claude calls this tool during skill execution instead of reading local docs.

Usage:
    AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py

Configure in Claude Code via .mcp.json (auto-discovered).
"""

import os
from typing import Optional
import kuzu
from sentence_transformers import SentenceTransformer
from mcp.server.fastmcp import FastMCP

# -- Init --

DB_PATH = os.environ.get("AUTOLISP_DB_PATH", "./autolisp.db")

print(f"Loading graph DB from {DB_PATH}...")
db = kuzu.Database(DB_PATH)
conn = kuzu.Connection(db)
conn.execute("INSTALL vector; LOAD vector;")

print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

mcp = FastMCP("autolisp_docs")

# -- Helpers --


def vector_search(query: str, top_k: int = 8) -> list[dict]:
    """Find semantically similar nodes using vector index."""
    query_embedding = embedder.encode(query).tolist()

    result = conn.execute(f"""
        CALL QUERY_VECTOR_INDEX('DocNode', 'doc_vec_index', $embedding, {top_k})
        WITH node, distance
        RETURN node.id, node.name, node.type, node.summary, node.platform,
               node.mac_safe, node.syntax, node.source_file, distance
        ORDER BY distance ASC
    """, {"embedding": query_embedding})

    nodes = []
    while result.has_next():
        row = result.get_next()
        nodes.append({
            "id":          row[0],
            "name":        row[1],
            "type":        row[2],
            "summary":     row[3],
            "platform":    row[4],
            "mac_safe":    row[5],
            "syntax":      row[6],
            "source_file": row[7],
            "score":       round(row[8], 3)
        })
    return nodes


def graph_expand(node_ids: list[str], depth: int) -> list[dict]:
    """Traverse the graph outward from seed nodes up to `depth` hops."""
    if not node_ids or depth < 1:
        return []

    result = conn.execute(f"""
        MATCH (seed:DocNode)-[:Relationship*1..{depth}]->(n:DocNode)
        WHERE seed.id IN $seed_ids
        RETURN DISTINCT n.id, n.name, n.type, n.summary,
                        n.platform, n.mac_safe, n.syntax
    """, {"seed_ids": node_ids})

    neighbors = []
    while result.has_next():
        row = result.get_next()
        neighbors.append({
            "id":       row[0],
            "name":     row[1],
            "type":     row[2],
            "summary":  row[3],
            "platform": row[4],
            "mac_safe": row[5],
            "syntax":   row[6]
        })
    return neighbors


def format_node(node: dict, label: str = "") -> str:
    """Format a node for readable output to Claude."""
    mac_tag = "Mac-safe" if node.get("mac_safe") else "Windows only"
    platform = node.get("platform", "unknown")
    syntax = f"\n  Syntax:   {node['syntax']}" if node.get("syntax") else ""
    score = f"  [distance: {node['score']}]" if "score" in node else ""
    prefix = f"[{label}] " if label else ""

    return (
        f"{prefix}**{node['name']}** ({node['type']}) -- {mac_tag} | platform: {platform}{score}"
        f"\n  Summary:  {node.get('summary', 'N/A')}"
        f"{syntax}"
    )


# -- MCP Tool --

@mcp.tool()
def search(
    query: str,
    depth: int = 2,
    filter: Optional[str] = None
) -> str:
    """
    Search the AutoLISP/AutoCAD documentation knowledge graph.

    Args:
        query:  What you want to know -- function name, concept, question,
                or a list of function names separated by spaces.
        depth:  Graph traversal depth after vector search seed.
                1 = direct matches only (fast)
                2 = matches + related functions/commands (default)
                3 = broad exploration -- use for architectural questions
        filter: Optional platform filter.
                "mac"          -> only Mac-safe nodes
                "windows_only" -> only Windows-only nodes
                "both"         -> no filter (default)

    Returns:
        Formatted documentation context with platform compatibility info.
    """
    depth = max(1, min(depth, 3))

    seeds = vector_search(query, top_k=8)

    if not seeds:
        return f"No documentation found matching: {query}"

    if filter == "mac":
        seeds = [n for n in seeds if n.get("mac_safe") is True]
    elif filter == "windows_only":
        seeds = [n for n in seeds if n.get("mac_safe") is False]

    neighbors = []
    if depth >= 2:
        seed_ids = [n["id"] for n in seeds]
        raw_neighbors = graph_expand(seed_ids, depth - 1)

        if filter == "mac":
            raw_neighbors = [n for n in raw_neighbors if n.get("mac_safe") is True]
        elif filter == "windows_only":
            raw_neighbors = [n for n in raw_neighbors if n.get("mac_safe") is False]

        seed_ids_set = {n["id"] for n in seeds}
        neighbors = [n for n in raw_neighbors if n["id"] not in seed_ids_set]

    lines = [
        f"## GraphRAG Results for: `{query}`",
        f"_Depth: {depth} | Filter: {filter or 'none'} | "
        f"Seeds: {len(seeds)} | Related: {len(neighbors)}_\n",
        "### Direct Matches\n"
    ]

    for node in seeds[:6]:
        lines.append(format_node(node, label="MATCH"))
        lines.append("")

    if neighbors:
        lines.append(f"\n### Related Nodes (graph neighbors)\n")
        for node in neighbors[:10]:
            lines.append(format_node(node, label="RELATED"))
            lines.append("")

    return "\n".join(lines)


# -- Run --

if __name__ == "__main__":
    mcp.run()
```

**Step 2: Verify syntax**

Run:
```bash
.venv/bin/python3 -c "import ast; ast.parse(open('mcp_server.py').read()); print('OK')"
```

Expected: `OK`

**Step 3: Commit**

```bash
git add mcp_server.py
git commit -m "feat: add mcp_server.py v2 — QUERY_VECTOR_INDEX, variable-length paths, parameterized queries"
```

---

### Task 6: Create .mcp.json and update project docs

**Files:**
- Create: `.mcp.json`
- Create: `CLAUDE.md`
- Modify: `SKILL.md`
- Modify: `README.md`

**Step 1: Create .mcp.json**

```json
{
  "mcpServers": {
    "autolisp_docs": {
      "command": ".venv/bin/python3",
      "args": ["mcp_server.py"],
      "env": {
        "AUTOLISP_DB_PATH": "./autolisp.db"
      }
    }
  }
}
```

Note: Uses `.venv/bin/python3` because Kuzu requires Python 3.12 venv (no wheels for 3.14).

**Step 2: Create CLAUDE.md**

Read the current `SKILL.md` and `README.md` first to understand existing content, then create `CLAUDE.md` with:

- Project overview (AI skill, not runnable app)
- Architecture section describing all files
- Commands section with validation scripts and GraphRAG commands
- Key Mac compatibility rules
- Doc file lookup convention
- LSP code conventions

The `CLAUDE.md` should reference the GraphRAG v2 setup: `build_graph.py` filters to ~558 function docs, `mcp_server.py` serves search, `.mcp.json` configures auto-discovery.

Include the GraphRAG commands:
```bash
# Build the knowledge graph (one-time, requires ANTHROPIC_API_KEY)
python build_graph.py --docs ./docs --db ./autolisp.db

# Build with limit for testing
python build_graph.py --docs ./docs --db ./autolisp.db --limit 10

# Test the MCP server locally
AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py

# Install Python dependencies
pip install -r requirements.txt
```

**Step 3: Update SKILL.md**

Update version to `3.0.0` and add MCP server references in the YAML metadata and body. Key additions:
- Add `mcp_server: mcp_server.py` to metadata
- Add section about GraphRAG MCP search tool
- Note that the MCP server provides semantic search over 558 function docs

**Step 4: Update README.md**

Add GraphRAG v2 setup instructions:
- Prerequisites (Python 3.12, ANTHROPIC_API_KEY)
- Build command
- File tree showing new files
- Note about ~558 function docs (not all 4,510)

**Step 5: Commit**

```bash
git add .mcp.json CLAUDE.md SKILL.md README.md
git commit -m "feat: add MCP config and update project docs for GraphRAG v2"
```

---

### Task 7: Pre-flight test with --limit 10

**Prerequisites:** `.env` has a valid `ANTHROPIC_API_KEY`

**Step 1: Run ingestion on 10 docs**

Run:
```bash
source .venv/bin/activate && python3 build_graph.py --docs ./docs --db ./test_autolisp.db --limit 10
```

Expected output (approximate):
```
Initialising database at ./test_autolisp.db
Loading embedding model: all-MiniLM-L6-v2
Found 4510 total markdown files
Filtered to 558 function reference docs (have *Supported Platforms:*)
   (limited to 10 files for testing)
Ingesting docs: 100%|..........| 10/10
Ingestion complete.
   Nodes: <some number > 0>
   Relationships: <some number >= 0>
Creating vector index...
   Vector index created.
```

If this fails, note the exact error and stop.

**Step 2: Verify DB contents**

Run:
```bash
.venv/bin/python3 -c "
import kuzu
db = kuzu.Database('./test_autolisp.db')
conn = kuzu.Connection(db)
conn.execute('INSTALL vector; LOAD vector;')
result = conn.execute('MATCH (n:DocNode) RETURN count(n)').get_next()
print(f'Nodes: {result[0]}')
result = conn.execute('MATCH ()-[r:Relationship]->() RETURN count(r)').get_next()
print(f'Relationships: {result[0]}')
"
```

Expected: Nodes > 0.

**Step 3: Test vector search**

Run:
```bash
.venv/bin/python3 -c "
import kuzu
from sentence_transformers import SentenceTransformer
db = kuzu.Database('./test_autolisp.db')
conn = kuzu.Connection(db)
conn.execute('INSTALL vector; LOAD vector;')
embedder = SentenceTransformer('all-MiniLM-L6-v2')
vec = embedder.encode('entity modification').tolist()
result = conn.execute('''
    CALL QUERY_VECTOR_INDEX(\"DocNode\", \"doc_vec_index\", \$embedding, 3)
    WITH node, distance
    RETURN node.name, node.summary, distance
    ORDER BY distance ASC
''', {'embedding': vec})
while result.has_next():
    row = result.get_next()
    print(f'  {row[0]}: {row[1][:60]}... (dist={row[2]:.3f})')
print('Vector search OK')
"
```

Expected: 1-3 results with names, summaries, and distances.

**Step 4: Clean up test DB**

Run:
```bash
rm -rf ./test_autolisp.db
```

---

### Task 8: Full build — all 558 docs

**Prerequisites:** Pre-flight test passed, `.env` has valid key, ~$1.73 budget approved.

**Step 1: Run the full build**

Run:
```bash
source .venv/bin/activate && python3 build_graph.py --docs ./docs --db ./autolisp.db
```

Expected:
- Filters to ~558 docs
- Takes ~26 minutes
- Completes without errors
- Creates vector index

**Step 2: Verify final DB**

Run:
```bash
.venv/bin/python3 -c "
import kuzu
db = kuzu.Database('./autolisp.db')
conn = kuzu.Connection(db)
conn.execute('INSTALL vector; LOAD vector;')
nodes = conn.execute('MATCH (n:DocNode) RETURN count(n)').get_next()
rels = conn.execute('MATCH ()-[r:Relationship]->() RETURN count(r)').get_next()
mac = conn.execute('MATCH (n:DocNode) WHERE n.mac_safe = true RETURN count(n)').get_next()
win = conn.execute('MATCH (n:DocNode) WHERE n.mac_safe = false RETURN count(n)').get_next()
print(f'Total nodes:    {nodes[0]}')
print(f'Relationships:  {rels[0]}')
print(f'Mac-safe:       {mac[0]}')
print(f'Windows-only:   {win[0]}')
"
```

Expected: Hundreds of nodes, mix of Mac-safe and Windows-only.

**Step 3: Test MCP server search**

Run:
```bash
AUTOLISP_DB_PATH=./autolisp.db .venv/bin/python3 -c "
import os
os.environ['AUTOLISP_DB_PATH'] = './autolisp.db'
import importlib.util
spec = importlib.util.spec_from_file_location('mcp_server', './mcp_server.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.search('entmod entity modification', depth=1)
print(result[:500])
print('---')
print('MCP search test OK')
"
```

Expected: Formatted GraphRAG results with entmod and related functions.

---

### Task 9: Final verification and push

**Step 1: Verify git status**

Run:
```bash
git status
```

Expected: Clean working tree. No untracked files except gitignored artifacts (`autolisp.db/`, `.venv/`, `.env`).

**Step 2: Review commit history**

Run:
```bash
git log --oneline -10
```

Expected commits (newest first):
1. `feat: add MCP config and update project docs for GraphRAG v2`
2. `feat: add mcp_server.py v2 — ...`
3. `feat: add build_graph.py v2 — scoped to 558 function docs ...`
4. `chore: add requirements.txt for GraphRAG v2`
5. `chore: update .gitignore for GraphRAG v2 artifacts`
6. `revert: remove GraphRAG v1 implementation ...`

**Step 3: Push**

```bash
git push origin main
```

---

### Summary of changes

| File | Action | Description |
|------|--------|-------------|
| 11 GraphRAG v1 commits | Reverted | Clean slate |
| `.gitignore` | Created | Python venv, Kuzu DB, .env |
| `requirements.txt` | Created | 6 Python dependencies |
| `build_graph.py` | Created | v2: filters to 558 docs, all Kuzu fixes |
| `mcp_server.py` | Created | v2: QUERY_VECTOR_INDEX, variable-length paths |
| `.mcp.json` | Created | MCP auto-discovery config |
| `CLAUDE.md` | Created | Project instructions for Claude Code |
| `SKILL.md` | Modified | v3.0.0 with MCP references |
| `README.md` | Modified | GraphRAG v2 setup instructions |
| `autolisp.db/` | Built | ~558 function docs ingested (gitignored) |

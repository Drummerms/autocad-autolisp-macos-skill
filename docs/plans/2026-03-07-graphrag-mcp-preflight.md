# GraphRAG MCP Pre-flight Fix & Test — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix 5 critical Kuzu API bugs in `build_graph.py` and `mcp_server.py`, then validate end-to-end with a 10-doc ingestion test and MCP server verification.

**Architecture:** `build_graph.py` ingests docs into a Kuzu graph DB with vector embeddings. `mcp_server.py` serves semantic search over that graph via FastMCP. Both files have incorrect Kuzu API calls that must be fixed before first run.

**Tech Stack:** Python 3, Kuzu (with vector extension), sentence-transformers (all-MiniLM-L6-v2), Anthropic SDK, MCP (FastMCP), python-dotenv, tqdm

**Design doc:** `docs/plans/2026-03-07-graphrag-mcp-preflight-design.md`

---

### Task 1: Add python-dotenv to requirements.txt

**Files:**
- Modify: `requirements.txt`

**Step 1: Add the dependency**

Add `python-dotenv>=1.0.0` as line 6 of `requirements.txt`:

```
kuzu>=0.7.0
anthropic>=0.40.0
sentence-transformers>=3.0.0
mcp>=1.0.0
tqdm>=4.66.0
python-dotenv>=1.0.0
```

**Step 2: Verify file**

Run: `cat requirements.txt`
Expected: 6 lines, last one is `python-dotenv>=1.0.0`

**Step 3: Commit**

```bash
git add requirements.txt
git commit -m "chore: add python-dotenv to requirements"
```

---

### Task 2: Fix build_graph.py — vector extension, .env loading, --limit flag, vector index

**Files:**
- Modify: `build_graph.py`

**Step 1: Add .env loading and vector extension init**

Add `dotenv` import at line 14 (after `import os`):

```python
from dotenv import load_dotenv
```

Add `.env` loading at line 26 (before the `# ── Config` section):

```python
load_dotenv()
```

In `init_db()` (line 64-89), add vector extension loading after creating the connection (after line 66):

```python
    conn.execute("INSTALL vector; LOAD vector;")
```

**Step 2: Add --limit flag**

In the argparse block (lines 205-209), add a `--limit` argument:

```python
    parser.add_argument("--limit", type=int, default=0, help="Limit number of files to process (0 = all)")
```

In `ingest_docs()`, update the signature to accept `limit`:

```python
def ingest_docs(docs_dir: str, db_path: str, limit: int = 0):
```

After line 131 (`print(f"Found {len(md_files)} ...")`), add:

```python
    if limit > 0:
        md_files = md_files[:limit]
        print(f"   (limited to {limit} files for testing)")
```

Update the `__main__` call (line 211) to pass limit:

```python
    ingest_docs(args.docs, args.db, args.limit)
```

**Step 3: Add vector index creation after ingestion**

After the final stats printout (after line 200), add:

```python
    print("📐 Creating vector index...")
    try:
        conn.execute("""
            CALL CREATE_VECTOR_INDEX('DocNode', 'doc_vec_index', 'embedding')
        """)
        print("   Vector index created.")
    except Exception as e:
        print(f"   ⚠️  Vector index creation failed (may already exist): {e}")
```

**Step 4: Verify syntax**

Run: `python3 -c "import ast; ast.parse(open('build_graph.py').read()); print('OK')"`
Expected: `OK`

**Step 5: Commit**

```bash
git add build_graph.py
git commit -m "fix: add vector extension init, .env loading, --limit flag, vector index creation"
```

---

### Task 3: Fix mcp_server.py — all Kuzu API bugs

**Files:**
- Modify: `mcp_server.py`

**Step 1: Add vector extension loading at startup**

After line 36 (`conn = kuzu.Connection(db)`), add:

```python
conn.execute("INSTALL vector; LOAD vector;")
```

**Step 2: Replace vector_search with QUERY_VECTOR_INDEX**

Replace the entire `vector_search` function (lines 45-75) with:

```python
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
```

Note: `score` now holds distance (lower = more relevant) instead of cosine similarity (higher = more relevant). The `format_node` function and output formatting will show this as-is — consumers can interpret accordingly.

**Step 3: Replace graph_expand with variable-length path pattern**

Replace the entire `graph_expand` function (lines 78-105) with:

```python
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
```

This fixes:
- Bug 3: `CALL bfs()` → variable-length relationship `*1..{depth}`
- Bug 5: `json.dumps(node_ids)` f-string injection → parameterized `$seed_ids`

Note: `depth` remains an f-string because Kuzu doesn't support parameterized path lengths. This is safe because depth is clamped to 1-3 in the `search()` function (line 149).

**Step 4: Remove unused json import**

Remove `import json` from line 23 (no longer needed after removing `json.dumps` from `graph_expand`).

**Step 5: Verify syntax**

Run: `python3 -c "import ast; ast.parse(open('mcp_server.py').read()); print('OK')"`
Expected: `OK`

**Step 6: Commit**

```bash
git add mcp_server.py
git commit -m "fix: correct Kuzu API calls — vector index search, variable-length paths, parameterized queries"
```

---

### Task 4: Install dependencies and verify imports

**Step 1: Install all dependencies**

Run: `pip install -r requirements.txt`
Expected: All packages install successfully.

**Step 2: Verify all imports work**

Run:
```bash
python3 -c "
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

**Step 3: Verify Kuzu vector extension is available**

Run:
```bash
python3 -c "
import kuzu
db = kuzu.Database('./test_kuzu_check')
conn = kuzu.Connection(db)
conn.execute('INSTALL vector; LOAD vector;')
print('Vector extension OK')
" && rm -rf ./test_kuzu_check
```
Expected: `Vector extension OK`

---

### Task 5: Run build_graph.py with --limit 10

**Prerequisites:** `.env` file has a valid `ANTHROPIC_API_KEY`

**Step 1: Run ingestion on 10 docs**

Run:
```bash
python3 build_graph.py --docs ./docs --db ./test_autolisp.db --limit 10
```

Expected output (approximate):
```
🔧 Initialising database at ./test_autolisp.db
📦 Loading embedding model: all-MiniLM-L6-v2
📂 Found 4510 markdown files
   (limited to 10 files for testing)
Ingesting docs: 100%|██████████| 10/10
✅ Ingestion complete.
   Nodes: <some number > 0>
   Relationships: <some number >= 0>
📐 Creating vector index...
   Vector index created.
```

If this fails, note the exact error and stop — do not proceed to later tasks.

---

### Task 6: Verify DB contents and queries

**Step 1: Check node and relationship counts**

Run:
```bash
python3 -c "
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

**Step 2: Test vector index search**

Run:
```bash
python3 -c "
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
Expected: 1-3 results printed with names, summaries, and distances.

**Step 3: Test graph traversal (if relationships exist)**

Run:
```bash
python3 -c "
import kuzu
db = kuzu.Database('./test_autolisp.db')
conn = kuzu.Connection(db)
result = conn.execute('''
    MATCH (seed:DocNode)-[:Relationship*1..2]->(n:DocNode)
    RETURN DISTINCT seed.name, n.name
    LIMIT 5
''')
count = 0
while result.has_next():
    row = result.get_next()
    print(f'  {row[0]} -> {row[1]}')
    count += 1
if count == 0:
    print('  (no relationships found — OK if test set is small)')
else:
    print(f'Graph traversal OK ({count} paths)')
"
```
Expected: Either paths printed or "no relationships found" message.

---

### Task 7: Test MCP server startup and tool invocation

**Step 1: Verify the MCP server module loads without errors**

Run:
```bash
AUTOLISP_DB_PATH=./test_autolisp.db python3 -c "
import os
os.environ['AUTOLISP_DB_PATH'] = './test_autolisp.db'
# Import the module (triggers init block)
import importlib.util
spec = importlib.util.spec_from_file_location('mcp_server', './mcp_server.py')
mod = importlib.util.find_spec('mcp_server') or spec
loader = importlib.util.LazyLoader(spec.loader)
spec.loader = loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
# Test the search function directly
result = mod.search('entmod entity modification', depth=1)
print(result[:500])
print('---')
print('MCP tool test OK')
"
```
Expected: GraphRAG formatted results printed, ending with `MCP tool test OK`.

If direct import is tricky, alternatively test via `fastmcp call`:

```bash
AUTOLISP_DB_PATH=./test_autolisp.db fastmcp call mcp_server.py search query="entmod" depth=1
```

---

### Task 8: Cleanup test database

**Step 1: Remove test DB**

Run:
```bash
rm -rf ./test_autolisp.db
```

**Step 2: Verify clean state**

Run:
```bash
test -d ./test_autolisp.db && echo "STILL EXISTS" || echo "CLEAN"
```
Expected: `CLEAN`

**Step 3: Verify git status is clean (no untracked test artifacts)**

Run: `git status`
Expected: Only the committed changes from Tasks 1-3. No untracked `test_autolisp.db/`.

---

### Summary of changes

| File | Changes |
|------|---------|
| `requirements.txt` | Added `python-dotenv>=1.0.0` |
| `build_graph.py` | Added `.env` loading, `INSTALL vector; LOAD vector;`, `--limit` flag, `CREATE_VECTOR_INDEX` after ingestion |
| `mcp_server.py` | Added `INSTALL vector; LOAD vector;`, replaced `list_cosine_similarity` brute-force with `QUERY_VECTOR_INDEX`, replaced `CALL bfs()` with `*1..N` variable-length paths, parameterized `$seed_ids`, removed unused `json` import |

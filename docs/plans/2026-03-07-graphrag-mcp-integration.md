# GraphRAG MCP Integration — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Integrate the GraphRAG MCP server files into the repo root, replacing local docs/ grep with `autolisp_docs.search()` via Kuzu + FastMCP.

**Architecture:** `build_graph.py` ingests 4,500+ markdown docs into a Kuzu embedded graph DB using Claude Haiku for entity extraction and MiniLM for embeddings. `mcp_server.py` serves the graph as an MCP tool that Claude calls instead of grepping `docs/`. `.mcp.json` enables Claude Code auto-discovery.

**Tech Stack:** Python 3, Kuzu, sentence-transformers (all-MiniLM-L6-v2), Anthropic SDK, FastMCP, tqdm

**Design doc:** `docs/plans/2026-03-07-graphrag-mcp-integration-design.md`

---

### Task 1: Copy core GraphRAG files to repo root

**Files:**
- Copy: `graph-mcp-context-files/build_graph.py` → `build_graph.py`
- Copy: `graph-mcp-context-files/mcp_server.py` → `mcp_server.py`
- Copy: `graph-mcp-context-files/requirements.txt` → `requirements.txt`

**Step 1: Copy the three files**

```bash
cp graph-mcp-context-files/build_graph.py ./build_graph.py
cp graph-mcp-context-files/mcp_server.py ./mcp_server.py
cp graph-mcp-context-files/requirements.txt ./requirements.txt
```

**Step 2: Verify files exist at root**

```bash
ls -la build_graph.py mcp_server.py requirements.txt
```
Expected: All three files listed.

**Step 3: Commit**

```bash
git add build_graph.py mcp_server.py requirements.txt
git commit -m "feat: add GraphRAG build script, MCP server, and requirements"
```

---

### Task 2: Create `.mcp.json`

**Files:**
- Create: `.mcp.json`

**Step 1: Create the MCP config file**

Write `.mcp.json` at repo root:

```json
{
  "mcpServers": {
    "autolisp_docs": {
      "command": "python3",
      "args": ["mcp_server.py"],
      "env": {
        "AUTOLISP_DB_PATH": "./autolisp.db"
      }
    }
  }
}
```

**Step 2: Verify valid JSON**

```bash
python3 -c "import json; json.load(open('.mcp.json')); print('valid')"
```
Expected: `valid`

**Step 3: Commit**

```bash
git add .mcp.json
git commit -m "feat: add .mcp.json for MCP server auto-discovery"
```

---

### Task 3: Replace `SKILL.md` with GraphRAG version

**Files:**
- Replace: `SKILL.md` (current v2.0.0 → v3.0.0 from `graph-mcp-context-files/SKILL.md`)

**Step 1: Replace the file**

```bash
cp graph-mcp-context-files/SKILL.md ./SKILL.md
```

**Step 2: Verify version bump**

```bash
head -15 SKILL.md
```
Expected: YAML frontmatter showing `version: 3.0.0` and `retrieval: graphrag-mcp`.

**Step 3: Commit**

```bash
git add SKILL.md
git commit -m "feat: update SKILL.md to v3.0.0 with GraphRAG MCP references"
```

---

### Task 4: Update `.gitignore`

**Files:**
- Modify: `.gitignore`

**Step 1: Append new entries**

Add these lines to `.gitignore` (currently only has `.DS_Store`):

```
# GraphRAG
autolisp.db/
__pycache__/
*.pyc
.env
```

**Step 2: Verify**

```bash
cat .gitignore
```
Expected: Original `.DS_Store` line plus the new entries.

**Step 3: Commit**

```bash
git add .gitignore
git commit -m "chore: add GraphRAG artifacts to .gitignore"
```

---

### Task 5: Update `README.md`

**Files:**
- Modify: `README.md`

**Step 1: Update description**

Change line 3 from:
```
A comprehensive skill for creating AutoLISP scripts compatible with AutoCAD for Mac. Includes 4,500+ official AutoCAD documentation files for platform compatibility verification.
```
To:
```
A comprehensive skill for creating AutoLISP scripts compatible with AutoCAD for Mac. Includes a GraphRAG MCP server backed by 4,500+ official AutoCAD documentation files for semantic search with platform compatibility verification.
```

**Step 2: Add GraphRAG Setup section**

Insert after the `## Usage` section (after line 77) and before `## What's Included`:

```markdown
## GraphRAG Setup

The skill includes a GraphRAG MCP server that provides semantic search over the documentation via a Kuzu graph database.

### 1. Install Python dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Build the knowledge graph

Requires `ANTHROPIC_API_KEY` set in your environment. This is a one-time operation (~2-4 hours, ~$2-5 USD at Haiku rates):

\`\`\`bash
export ANTHROPIC_API_KEY=sk-ant-...
python build_graph.py --docs ./docs --db ./autolisp.db
\`\`\`

### 3. Wire up the MCP server

The repo includes `.mcp.json` for Claude Code auto-discovery. For other tools, add to your MCP config:

\`\`\`json
{
  "mcpServers": {
    "autolisp_docs": {
      "command": "python3",
      "args": ["/absolute/path/to/mcp_server.py"],
      "env": {
        "AUTOLISP_DB_PATH": "/absolute/path/to/autolisp.db"
      }
    }
  }
}
\`\`\`

### Rebuilding after doc updates

Re-run ingestion — it uses `MERGE` so existing nodes are updated, not duplicated:

\`\`\`bash
python build_graph.py --docs ./docs --db ./autolisp.db
\`\`\`
```

**Step 3: Update the "What's Included" tree**

Replace the tree (lines 94-113) with:

```
autocad-autolisp-macos/
├── SKILL.md              # Main skill file (v3 - GraphRAG)
├── build_graph.py        # One-time: docs → Kuzu graph DB
├── mcp_server.py         # MCP server for Claude integration
├── requirements.txt      # Python dependencies
├── .mcp.json             # MCP auto-discovery config
├── docs/                 # 4,500+ AutoCAD documentation files
├── scripts/
│   ├── validate_lisp.py          # AutoLISP validator (offline)
│   └── compatibility_checker.py  # Function compatibility checker (offline)
├── references/
│   ├── function-compatibility.md # Complete compatibility tables
│   ├── dxf-codes.md              # DXF code reference
│   ├── mac-alternatives.md       # Windows-to-Mac alternatives
│   └── dcl-mac-limitations.md    # DCL support on Mac
├── assets/templates/
│   ├── basic-command.lsp         # Basic command template
│   ├── selection-processor.lsp   # Selection set processing
│   ├── batch-plot.lsp            # Batch plotting
│   └── entity-creator.lsp        # Entity creation with entmake
├── install.sh            # Cross-platform installer
└── README.md             # This file
```

**Step 4: Commit**

```bash
git add README.md
git commit -m "docs: update README with GraphRAG setup and updated file tree"
```

---

### Task 6: Update `CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md`

**Step 1: Update Project Overview (line 7)**

Change to:
```
This is an **AI skill/plugin** (not a runnable application) that helps AI assistants generate AutoLISP code compatible with AutoCAD for Mac. It includes a GraphRAG MCP server backed by 4,500+ official AutoCAD documentation files, validation scripts, compatibility references, and LSP templates. It follows the Agent Skills Open Standard and supports Claude Code, Cursor, GitHub Copilot, Windsurf, Cline, Codex CLI, and Gemini CLI.
```

**Step 2: Add GraphRAG entries to Architecture section**

Insert after the `SKILL.md` bullet (after line 13):

```markdown
- **`build_graph.py`** — One-time ingestion script. Reads all markdown files from `docs/`, calls Claude Haiku to extract entities (functions, commands, variables) and relationships, generates MiniLM embeddings, and stores everything in a Kuzu embedded graph database at `autolisp.db/`. Uses MERGE so re-runs are safe.
- **`mcp_server.py`** — FastMCP server exposing `autolisp_docs.search(query, depth, filter)`. Performs vector similarity search over node embeddings, then expands results via graph traversal. Served to Claude via MCP protocol.
- **`.mcp.json`** — MCP server configuration for Claude Code auto-discovery. Points to `mcp_server.py` with `AUTOLISP_DB_PATH` env var.
- **`requirements.txt`** — Python dependencies: kuzu, anthropic, sentence-transformers, mcp, tqdm.
```

**Step 3: Add GraphRAG commands to Commands section**

Insert after the existing commands block (after line 44, before the `## Key Mac Compatibility Rules` heading):

```markdown
### GraphRAG Commands

\`\`\`bash
# Build the knowledge graph (one-time, requires ANTHROPIC_API_KEY)
python build_graph.py --docs ./docs --db ./autolisp.db

# Test the MCP server locally
AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py

# Install Python dependencies
pip install -r requirements.txt
\`\`\`

The MCP server is auto-discovered by Claude Code via `.mcp.json`. The generated `autolisp.db/` directory is gitignored — each user builds locally.
```

**Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md with GraphRAG architecture and commands"
```

---

### Task 7: Delete `graph-mcp-context-files/`

**Files:**
- Delete: `graph-mcp-context-files/` (entire directory)

**Step 1: Verify all contents have been copied**

```bash
diff graph-mcp-context-files/build_graph.py build_graph.py
diff graph-mcp-context-files/mcp_server.py mcp_server.py
diff graph-mcp-context-files/requirements.txt requirements.txt
diff graph-mcp-context-files/SKILL.md SKILL.md
```
Expected: No diff output for any of the four commands.

**Step 2: Remove the directory**

```bash
rm -rf graph-mcp-context-files/
```

**Step 3: Verify it's gone**

```bash
ls graph-mcp-context-files/ 2>&1
```
Expected: `No such file or directory`

**Step 4: Commit**

```bash
git add -A graph-mcp-context-files/
git commit -m "chore: remove graph-mcp-context-files (moved to repo root)"
```

---

### Task 8: Final verification

**Step 1: Check repo structure**

```bash
ls -la build_graph.py mcp_server.py requirements.txt .mcp.json SKILL.md .gitignore
```
Expected: All files present.

**Step 2: Verify no leftover context files directory**

```bash
test -d graph-mcp-context-files && echo "STILL EXISTS" || echo "CLEAN"
```
Expected: `CLEAN`

**Step 3: Verify Python syntax**

```bash
python3 -c "import ast; ast.parse(open('build_graph.py').read()); print('build_graph.py OK')"
python3 -c "import ast; ast.parse(open('mcp_server.py').read()); print('mcp_server.py OK')"
```
Expected: Both print `OK`.

**Step 4: Verify .gitignore works**

```bash
mkdir -p autolisp.db && touch autolisp.db/test && git status autolisp.db/
```
Expected: No untracked files shown (gitignored). Then clean up:
```bash
rm -rf autolisp.db
```

**Step 5: Check git log for all commits**

```bash
git log --oneline -8
```
Expected: 7 new commits from Tasks 1-7.

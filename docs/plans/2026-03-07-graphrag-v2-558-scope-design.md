# GraphRAG v2: 558-Doc Scope — Design Document

> **Status: COMPLETE** (2026-03-08). Implementation delivered per this design.

## Problem

GraphRAG v1 attempted to ingest all 4,516 docs via sequential Haiku API calls. This took ~30 hours and cost ~$14, making it impractical. Only 558 of 4,516 docs are AutoLISP function references with platform compatibility data — the rest are Commands, System Variables, and conceptual docs that don't contain the structured function metadata the GraphRAG pipeline extracts.

## Decision

Revert GraphRAG v1 entirely (11 commits), then re-implement with an identical architecture scoped to only the 558 function docs that have `*Supported Platforms:*` markers. This reduces build time from ~30 hours to ~26 minutes and cost from ~$14 to ~$1.73.

## Scope: Which 558 Docs

All docs in `docs/` that contain the line `*Supported Platforms:*` are AutoLISP function reference pages. They break down as:

| Category | Count | `mac_safe` | Example |
|----------|-------|------------|---------|
| AutoLISP (core) | ~250 | mostly true | `entmod`, `defun`, `setq` |
| AutoLISP/ActiveX | ~100 | all false | `vlax-get-property`, `vlr-*` |
| AutoLISP/DCL | ~28 | all true | `load_dialog`, `new_dialog` |
| AutoLISP/Express Tools | ~50 | all false | `acet-str-find`, `acet-file-*` |
| DCL Tiles/Attributes | ~70 | all true | `edit_box`, `slider`, `toggle` |
| Other (External, Visual LISP IDE) | ~10 | varies | `cal`, `vlisp-compile` |

Detection: `grep -l '^\*Supported Platforms:\*' docs/*.md` returns exactly these 558 files.

## Architecture (Unchanged from v1)

```
docs/*.md  -->  build_graph.py  -->  autolisp.db/ (Kuzu)
                  |                       |
                  | Haiku extraction       | Vector + Graph
                  | MiniLM embeddings      |
                  v                       v
              Kuzu DB <---- mcp_server.py (FastMCP)
                               |
                               v
                         Claude Code (MCP client)
```

### build_graph.py
- Reads docs, filters to 558 with `*Supported Platforms:*`
- Calls Claude Haiku to extract entities and relationships
- Generates MiniLM-L6-v2 embeddings (384-dim, local)
- Stores in Kuzu with MERGE (idempotent, re-runnable)
- Creates vector index after ingestion

### mcp_server.py
- FastMCP server exposing `search(query, depth, filter)` tool
- Vector similarity search via `QUERY_VECTOR_INDEX`
- Graph expansion via variable-length paths `*1..N`
- Returns formatted results with platform compatibility info

## Kuzu API Fixes (Pre-applied)

Five bugs from v1 are fixed before first run:

1. **Vector extension**: `INSTALL vector; LOAD vector;` on every connection
2. **Vector search**: `QUERY_VECTOR_INDEX` (not `list_cosine_similarity`)
3. **Graph traversal**: `MATCH (a)-[*1..N]->(b)` (not `CALL bfs()`)
4. **Parameterized queries**: `$seed_ids` (not `json.dumps` f-string injection)
5. **Missing .env loading**: `load_dotenv()` for ANTHROPIC_API_KEY

## File Changes

### Removed (via revert)
- `build_graph.py` (v1)
- `mcp_server.py` (v1)
- `requirements.txt` (v1)
- `.mcp.json` (v1)
- `docs/plans/2026-03-07-graphrag-mcp-preflight-design.md`
- `docs/plans/2026-03-07-graphrag-mcp-preflight.md`
- `docs/plans/2026-03-07-graphrag-integration-plan.md`
- Changes to `SKILL.md`, `CLAUDE.md`, `README.md`, `.gitignore`

### Added (fresh implementation)
- `build_graph.py` (v2 — with 558-doc filter, all Kuzu fixes)
- `mcp_server.py` (v2 — with correct Kuzu API calls)
- `requirements.txt` (kuzu, anthropic, sentence-transformers, mcp, tqdm, python-dotenv)
- `.mcp.json` (pointing to `.venv/bin/python3`)
- `.gitignore` updates (autolisp.db/, .venv/, __pycache__/, .env)
- `SKILL.md` updates (v3.0.0 with MCP references)
- `CLAUDE.md` updates (GraphRAG commands section)
- `README.md` updates (GraphRAG setup, file tree)
- This design doc

## Build Estimates

| Metric | Value |
|--------|-------|
| Docs processed | 558 |
| Haiku API calls | 558 |
| Build time (sequential) | ~26 minutes |
| Haiku cost | ~$1.73 |
| Embedding model | all-MiniLM-L6-v2 (local, free) |
| DB size | ~60 MB |
| Python version | 3.12 (venv, Kuzu compatibility) |

## Dependencies

```
kuzu>=0.7.0
anthropic>=0.40.0
sentence-transformers>=3.0.0
mcp>=1.0.0
tqdm>=4.66.0
python-dotenv>=1.0.0
```

## Success Criteria

1. `build_graph.py` completes in <30 minutes for all 558 docs
2. Kuzu DB contains nodes with embeddings and relationships
3. `QUERY_VECTOR_INDEX` returns relevant results for test queries
4. Graph traversal returns connected nodes
5. MCP server `search()` tool returns formatted results with platform info
6. Claude Code can discover and use the MCP server via `.mcp.json`

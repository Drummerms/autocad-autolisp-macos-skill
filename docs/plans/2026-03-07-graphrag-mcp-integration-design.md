# GraphRAG MCP Integration Design

**Date:** 2026-03-07
**Status:** Approved

## Summary

Integrate a GraphRAG MCP server into the `autocad-autolisp-macos` skill. This replaces local `docs/` grep-based lookups with semantic vector search + graph traversal over a Kuzu embedded database, served to Claude via FastMCP.

## Stack

| Layer | Tool | Rationale |
|---|---|---|
| Graph DB | Kuzu | Embedded (no server daemon), fast, free |
| Embeddings | all-MiniLM-L6-v2 | Local, no API cost, 384-dim |
| Entity extraction | Claude Haiku | Fast + cheap for bulk ingestion |
| MCP server | FastMCP | Native Claude integration |

## Approach

**Approach A (selected):** Integrate directly into repo root. `build_graph.py`, `mcp_server.py`, and `requirements.txt` become first-class project files alongside existing `scripts/`, `references/`, and `docs/`.

Rejected alternatives:
- **B: Subdirectory (`graphrag/`)** — unnecessary indirection, two competing SKILL.md files
- **C: Keep context-files dir** — feels unintegrated, awkward naming

## File Changes

### New files (repo root)
- `build_graph.py` — ingests 4,500+ docs into Kuzu graph via Haiku extraction + MiniLM embeddings
- `mcp_server.py` — FastMCP server exposing `autolisp_docs.search(query, depth, filter)` tool
- `requirements.txt` — Python dependencies (kuzu, anthropic, sentence-transformers, mcp, tqdm)
- `.mcp.json` — MCP server config for Claude Code auto-discovery

### Modified files
- `SKILL.md` — replaced with GraphRAG version (v2.0.0 -> v3.0.0), references `autolisp_docs.search()` instead of local file lookups
- `.gitignore` — add `autolisp.db/`, `__pycache__/`, `*.pyc`, `.env`
- `README.md` — add GraphRAG setup section, update architecture description
- `CLAUDE.md` — add GraphRAG architecture, commands, and notes

### Deleted
- `graph-mcp-context-files/` — contents moved to root

### Unchanged
- `scripts/` — validation scripts remain as offline tools
- `references/` — static reference docs
- `assets/templates/` — LSP templates
- `docs/` — raw markdown docs (ingestion source)
- `install.sh` — still useful for non-GraphRAG installs

## MCP Configuration (`.mcp.json`)

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

## Known Issues

- `mcp_server.py` `graph_expand()` uses `CALL bfs()` syntax that may not match Kuzu's actual recursive path API. Needs testing and fix.

## User Setup Flow

1. `pip install -r requirements.txt`
2. `export ANTHROPIC_API_KEY=sk-ant-...`
3. `python build_graph.py --docs ./docs --db ./autolisp.db` (~2-4 hours, ~$2-5 USD)
4. MCP server auto-discovered by Claude Code via `.mcp.json`

## Key Design Decisions

- MERGE on insert so re-ingestion is safe (no duplicates)
- `depth=2` default: seeds + 1-hop neighbors
- `filter` param: `"mac"` | `"windows_only"` | `null`
- Haiku for extraction (fast/cheap), MiniLM for embeddings (local/free)
- `autolisp.db/` is gitignored — each user builds locally

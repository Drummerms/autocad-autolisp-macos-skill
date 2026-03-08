# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **AI skill/plugin** (not a runnable application) that helps AI assistants generate AutoLISP code compatible with AutoCAD for Mac. It includes a GraphRAG MCP server backed by ~560 AutoLISP function reference docs, validation scripts, compatibility references, and LSP templates. It follows the Agent Skills Open Standard and supports Claude Code, Cursor, GitHub Copilot, Windsurf, Cline, Codex CLI, and Gemini CLI.

The entry point for the skill is `SKILL.md` (YAML frontmatter + markdown instructions that AI assistants consume).

## Architecture

- **`SKILL.md`** — Main skill definition with YAML metadata (name, version, platforms) and instructions for AI assistants: compatibility tables, forbidden function patterns, Mac-safe alternatives, validation workflow, and code templates.
- **`build_graph.py`** — One-time ingestion script. Filters docs to ~560 function references (those with `*Supported Platforms:*` markers), calls Claude Haiku to extract entities and relationships, generates MiniLM embeddings, and stores everything in a Kuzu embedded graph database at `autolisp.db/`. Uses MERGE so re-runs are safe.
- **`mcp_server.py`** — FastMCP server exposing `autolisp_docs.search(query, depth, filter)`. Performs vector similarity search over node embeddings, then expands results via graph traversal. Served to Claude via MCP protocol.
- **`.mcp.json`** — MCP server configuration for Claude Code auto-discovery. Points to `mcp_server.py` with `AUTOLISP_DB_PATH` env var.
- **`requirements.txt`** — Python dependencies: kuzu, anthropic, sentence-transformers, mcp, tqdm, python-dotenv.
- **`docs/`** — 4,500+ markdown files scraped from official Autodesk AutoCAD help. Each file covers one command, system variable, function, or dialog. ~560 of these are function reference docs with `*Supported Platforms:*` markers used by the GraphRAG pipeline.
- **`scripts/`** — Python 3 CLI tools (no dependencies beyond stdlib):
  - `validate_lisp.py` — Scans `.lsp` files for Windows-only patterns and reports errors/warnings with Mac-safe alternatives.
  - `compatibility_checker.py` — Offline database + doc-backed lookup for individual function compatibility.
- **`references/`** — Curated reference docs: `function-compatibility.md`, `dxf-codes.md`, `mac-alternatives.md`, `dcl-mac-limitations.md`.
- **`assets/templates/`** — Four `.lsp` template files for common tasks.
- **`install.sh`** — Cross-platform installer that symlinks or copies files for each platform.

## Commands

```bash
# Validate a single AutoLISP file for Mac compatibility
python3 scripts/validate_lisp.py your-script.lsp

# Validate all .lsp files in a directory (recursive)
python3 scripts/validate_lisp.py ./my-scripts/

# Check a specific function's compatibility
python3 scripts/validate_lisp.py --check-function vlax-get

# Look up a function in the compatibility database
python3 scripts/compatibility_checker.py <function_name>

# List all known Mac-incompatible functions
python3 scripts/compatibility_checker.py --list-incompatible

# List all known Mac-compatible functions
python3 scripts/compatibility_checker.py --list-compatible

# Install the skill for a specific platform
./install.sh --platform claude
```

### GraphRAG Commands

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

The MCP server is auto-discovered by Claude Code via `.mcp.json`. The generated `autolisp.db/` directory is gitignored — each user builds locally.

## Key Mac Compatibility Rules

When writing or modifying AutoLISP code in this project, these patterns are **Windows-only and must never be used**:
- `vlax-*` (ActiveX/COM) — replace with `entget`/`entmod` + DXF codes
- `vlr-*` (Reactors) — replace with polling or command wrappers
- `acet-*` (Express Tools) — reimplement with standard AutoLISP
- `vl-load-com` (COM loading) — remove entirely
- `vl-vbaload` (VBA) — rewrite in pure AutoLISP
- `vl-registry-*` (Windows Registry) — use config files
- `acad_colordlg`, `acad_truecolordlg` — use `getint` for color input

DCL dialogs (`load_dialog`, `new_dialog`) work on AutoCAD Mac but **not** AutoCAD LT Mac.

## Doc File Lookup Convention

To verify a function's platform support, search `docs/` using the naming pattern:
```
docs/{function-name}-AutoLISP.md
docs/{function-name}-AutoLISP-ActiveX.md
docs/{function-name}-AutoLISP-DCL.md
docs/{function-name}-AutoLISP-Express-Tools.md
```
Look for the `*Supported Platforms:*` line in the matched file.

## LSP Code Conventions

All AutoLISP code in this repo follows a standard header format:
```lisp
;;; FILENAME.LSP
;;; Description
;;; Compatibility: AutoCAD for Windows and Mac
;;; Author: Name
;;; Version: X.Y.Z
```
Commands are defined with `(defun c:COMMANDNAME (/ local-vars) ...)` and files end with `(princ)` for clean loading.

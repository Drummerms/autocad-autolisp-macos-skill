# Documentation Refresh — Design

**Date:** 2026-03-08
**Status:** APPROVED
**Approach:** Targeted Fix — fix inaccuracies, fill gaps, preserve existing structure

## Motivation

After completing the GraphRAG v2 migration and repo restructure, documentation has drifted from the actual codebase. A systematic audit comparing every doc against the code revealed 14 discrepancies ranging from stale references to missing features.

## Scope

### Section 1: README.md

1. Replace placeholder GitHub URLs (`yourusername/`) with `Drummerms/autocad-autolisp-macos-skill`
2. Fix install.sh reference to "4,500+ docs" — update to reflect pre-built DB
3. Add version number (v3.0.0) near the top
4. Add Python 3.12 venv requirement to prerequisites
5. Document undocumented CLI flags (`--verbose`, `--json`, `--docs-path`) for both scripts
6. Add link to separate docs repo (https://github.com/Drummerms/autocad-htm-to-markdown-converter.git) for rebuilding the graph
7. Add local MCP server testing command

### Section 2: SKILL.md

1. Add `acad_helpdlg` to forbidden patterns / Critical Mac Incompatibilities
2. Add `compatibility_checker.py` to Validation Scripts section with usage examples
3. Document `--verbose`, `--json`, `--docs-path` flags for validate_lisp.py
4. Add MCP server local testing note

### Section 3: CLAUDE.md

1. Add `acad_helpdlg` to Mac Compatibility Rules
2. Add Python 3.12 venv requirement and activation steps to GraphRAG Commands
3. Add undocumented CLI flags (`--verbose`, `--json`, `--docs-path`) to Commands section
4. Fix LSP header format to match expanded template format (with Usage section)
5. Add MCP server local testing command
6. Add build time/cost estimates (~26 min, ~$1.73)

### Section 4: Code Fixes

1. Fix `compatibility_checker.py` docstring (line 11) — change `--list-safe` to `--list-compatible`
2. Add `vl-vbaload` to `compatibility_checker.py` database for consistency
3. Fix `install.sh` — update "4,500+ docs" message to reflect pre-built DB

## Out of Scope

- Full doc rewrites
- New reference documents
- Changes to reference docs (audit found them accurate)
- Test suite creation
- Feature additions

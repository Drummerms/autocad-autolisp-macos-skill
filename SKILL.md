---
name: autocad-autolisp-macos-skill
description: >-
  Create AutoLISP scripts compatible with AutoCAD for Mac. Uses a GraphRAG
  knowledge graph (built from ~560 official AutoLISP function reference docs)
  to check function compatibility. Validates against ActiveX (vlax-*), Express
  Tools (acet-*), COM, and other Windows-only features. Provides Mac-safe
  alternatives and cross-platform code patterns for AutoCAD development on macOS.
license: MIT
metadata:
  author: Michael Sablatura
  version: 3.0.0
  graphrag_functions: 560
  platforms:
    - Claude Code
    - GitHub Copilot
    - Cursor
    - Windsurf
    - Cline
  mcp_server: mcp_server.py
---

## When to Use This Skill

Invoke this skill when:

- User asks to write, create, or modify AutoLISP code
- User mentions AutoCAD for Mac, Mac compatibility, or cross-platform
- User asks about AutoLISP functions and their Mac support
- User needs to validate existing AutoLISP for Mac compatibility

## Quick Start

1. **Identify functions** you plan to use
2. **Verify compatibility** using the GraphRAG MCP search tool
3. **Use alternatives** for Windows-only features
4. **Test on Mac** before deployment

## Platform Compatibility at a Glance

| Category | Mac Support | Windows Only |
|----------|-------------|--------------|
| Core AutoLISP | Full support | - |
| `command`, `entmake`, `entmod` | Full support | - |
| `vl-file-*` functions | Full support | - |
| User input (`getpoint`, `ssget`, etc.) | Full support | - |
| ActiveX (`vlax-*`) | - | Windows only |
| Reactors (`vlr-*`) | - | Windows only |
| Express Tools (`acet-*`) | - | Windows only |
| COM (`vl-load-com`) | - | Windows only |
| DCL dialogs | Supported* | Full support |
| Visual LISP IDE | - | Windows only |
| `.vlx` compiled | - | Windows only |

*DCL supported on AutoCAD for Mac, but NOT on AutoCAD LT for Mac

## Critical Mac Incompatibilities

**NEVER use these - they will fail on Mac:**

```
vlax-*          ActiveX/COM - no Mac support
vlr-*           Reactors - no Mac support
acet-*          Express Tools - Windows only
vl-load-com     COM loading - not available on Mac
vl-vbaload      VBA - not available on Mac
acad_colordlg   Windows-only dialog
acad_truecolordlg Windows-only dialog
acad_helpdlg    Windows-only help dialog
```

## Mac-Safe Alternatives

| Windows Feature | Mac Alternative |
|-----------------|-----------------|
| `vlax-get` / `vlax-put` | Use `entget` / `entmod` with DXF codes |
| `vlax-create-object` | Use `command` function or external scripts |
| `acad_colordlg` | Use `(getint "\nEnter color number: ")` |
| Registry functions | Use external config files (JSON/LSP) |
| `vlr-*` reactors | Polling with timers or command wrappers |

## Before Writing Any AutoLISP Code

1. **List all functions** you plan to use
2. **Search the GraphRAG knowledge graph** using the MCP `search` tool:
   - `search(query="function-name", filter="mac")` for Mac-safe results
   - `search(query="function-name", depth=2)` to see related functions
3. **Replace incompatible functions** with Mac-safe alternatives
4. **Document any limitations** in the code header

## Code Template

```lisp
;;; FILENAME.LSP
;;; Brief description
;;; Compatibility: AutoCAD for Windows and Mac
;;; Author: Your Name
;;; Version: 1.0.0

(defun c:COMMANDNAME (/ local-vars)
  ;; Implementation using Mac-compatible functions only
  (vl-load-all)  ;; Safe - loads Visual LISP extensions
  (princ)
)

(princ "\nType COMMANDNAME to run")
(princ)
```

## Validation Scripts

This skill includes validation tools in `scripts/`:

### validate_lisp.py — File/Directory Validation

```bash
# Validate a single file
python3 scripts/validate_lisp.py your-script.lsp

# Validate all .lsp files in a directory (recursive)
python3 scripts/validate_lisp.py ./my-scripts/

# Check a specific function
python3 scripts/validate_lisp.py --check-function vlax-get

# Verbose output
python3 scripts/validate_lisp.py -v your-script.lsp

# JSON output for programmatic use
python3 scripts/validate_lisp.py --json your-script.lsp
```

### compatibility_checker.py — Function Lookup

```bash
# Look up a function
python3 scripts/compatibility_checker.py command

# List all known Mac-incompatible functions
python3 scripts/compatibility_checker.py --list-incompatible

# List all known Mac-compatible functions
python3 scripts/compatibility_checker.py --list-compatible
```

## GraphRAG MCP Search

This skill includes a GraphRAG-powered MCP server that provides semantic search over ~560 AutoLISP function reference docs. When the MCP server is running, Claude Code can search the knowledge graph directly.

The MCP server exposes a `search(query, depth, filter)` tool:
- `query`: Function name, concept, or natural language question
- `depth`: 1 (direct matches), 2 (+ related), 3 (broad exploration)
- `filter`: "mac" (Mac-safe only), "windows_only", or "both" (default)

Setup: See README.md for GraphRAG build instructions.

To test the MCP server locally: `AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py`

## Documentation Index

| Reference | Description |
|-----------|-------------|
| `references/function-compatibility.md` | Complete function compatibility tables |
| `references/dxf-codes.md` | DXF code reference for `entmake`/`entmod` |
| `references/mac-alternatives.md` | Detailed Mac-safe alternatives |
| `references/dcl-mac-limitations.md` | DCL support on Mac |
| `assets/templates/` | Ready-to-use LSP templates |

## Example: Mac-Compatible Script

```lisp
;;; BATCH-PLOT.LSP
;;; Plots all layouts to PDF
;;; Compatibility: AutoCAD for Windows and Mac

(defun c:BATCHPLOT (/ layout-name layouts i)
  (vl-load-all)

  (setq layouts (layoutlist))
  (setq i 0)

  (foreach layout-name layouts
    (setvar "CTAB" layout-name)
    (command "._PLOT" "Y" "" "DWG To PDF.pc3" "" "N" "N" "N")
    (setq i (1+ i))
  )

  (princ (strcat "\nPlotted " (itoa i) " layouts."))
  (princ)
)
```

## Pre-Commit Checklist

- [ ] No `vlax-*` or `vlr-*` functions used
- [ ] No `acet-*` Express Tools functions
- [ ] No `vl-load-com` or COM functions
- [ ] No Windows-only dialogs (`acad_colordlg`, etc.)
- [ ] All functions verified via GraphRAG MCP search
- [ ] Compatibility header included
- [ ] Tested on Mac (or documented limitations)

---
name: autocad-autolisp-macos
description: >-
  Create AutoLISP scripts compatible with AutoCAD for Mac. Automatically checks
  function compatibility against 4,500+ official AutoCAD documentation files via
  GraphRAG knowledge graph. Validates against ActiveX (vlax-*), Express Tools
  (acet-*), COM, and other Windows-only features. Provides Mac-safe alternatives
  and cross-platform code patterns for AutoCAD development on macOS.
license: MIT
metadata:
  author: Michael Sablatura
  version: 3.0.0
  documentation_files: 4510
  platforms:
    - Claude Code
    - GitHub Copilot
    - Cursor
    - Windsurf
    - Cline
  retrieval: graphrag-mcp
---

## When to Use This Skill

Invoke this skill when:

- User asks to write, create, or modify AutoLISP code
- User mentions AutoCAD for Mac, Mac compatibility, or cross-platform
- User asks about AutoLISP functions and their Mac support
- User needs to validate existing AutoLISP for Mac compatibility

---

## Knowledge Retrieval via GraphRAG

You have access to a GraphRAG MCP tool: **`autolisp_docs`**

This tool queries a knowledge graph built from 4,500+ official AutoCAD documentation
files. Unlike simple search, it traverses relationships between functions, commands,
parameters, and platform constraints — surfacing related context you wouldn't find
with keyword matching alone.

### ALWAYS call `autolisp_docs.search` before:
- Writing any AutoLISP function you are not 100% certain is Mac-safe
- Answering questions about platform support
- Suggesting alternatives to Windows-only features
- Validating any function against Mac compatibility

### Tool Usage

```
autolisp_docs.search(
  query   = "<function name, concept, or question>",
  depth   = 2,          # 1=direct match, 2=related context (default), 3=broad exploration
  filter  = "mac"       # optional: "mac", "windows", "both" — filters by platform tag
)
```

### Retrieval Examples

| Task | Tool Call |
|------|-----------|
| Check if `vlax-get` works on Mac | `search(query="vlax-get platform support", filter="mac")` |
| Find Mac-safe alternatives to reactors | `search(query="vlr reactor alternatives mac", depth=2)` |
| Understand entmod DXF code usage | `search(query="entmod DXF codes layer color", depth=2)` |
| Validate a full function list | Call `search` once per function group |

### Graph Depth Guide

- **depth=1** → Direct documentation match only. Use for quick platform lookups.
- **depth=2** → Match + related functions, parameters, and see-also links. *Recommended default.*
- **depth=3** → Broad graph traversal. Use for "how does X relate to Y?" or architectural questions.

---

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

---

## Critical Mac Incompatibilities

**NEVER use these — they will fail on Mac:**

```
vlax-*          ActiveX/COM - no Mac support
vlr-*           Reactors - no Mac support
acet-*          Express Tools - Windows only
vl-load-com     COM loading - not available on Mac
vl-vbaload      VBA - not available on Mac
acad_colordlg   Windows-only dialog
acad_truecolordlg Windows-only dialog
```

> When in doubt, call `autolisp_docs.search(query="<function> mac support")` to verify.

---

## Mac-Safe Alternatives

| Windows Feature | Mac Alternative |
|-----------------|-----------------|
| `vlax-get` / `vlax-put` | Use `entget` / `entmod` with DXF codes |
| `vlax-create-object` | Use `command` function or external scripts |
| `acad_colordlg` | Use `(getint "\nEnter color number: ")` |
| Registry functions | Use external config files (JSON/LSP) |
| `vlr-*` reactors | Polling with timers or command wrappers |

---

## Before Writing Any AutoLISP Code

1. **List all functions** you plan to use
2. **Query the knowledge graph** for each function or function group:
   ```
   autolisp_docs.search(query="entmake entmod layer DXF mac", depth=2)
   ```
3. **Verify platform support** — look for `platform: mac` or `platform: windows_only` in results
4. **Replace incompatible functions** with Mac-safe alternatives from the graph results
5. **Document any limitations** in the code header

---

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

---

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

---

## Pre-Commit Checklist

- [ ] `autolisp_docs.search` called for all non-trivial functions used
- [ ] No `vlax-*` or `vlr-*` functions used
- [ ] No `acet-*` Express Tools functions
- [ ] No `vl-load-com` or COM functions
- [ ] No Windows-only dialogs (`acad_colordlg`, etc.)
- [ ] Compatibility header included
- [ ] Tested on Mac (or documented limitations)

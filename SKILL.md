---
name: autocad-autolisp-macos
description: >-
  Create AutoLISP scripts compatible with AutoCAD for Mac. Automatically checks
  function compatibility against 4,500+ official AutoCAD documentation files.
  Validates against ActiveX (vlax-*), Express Tools (acet-*), COM, and other
  Windows-only features. Provides Mac-safe alternatives and cross-platform
  code patterns for AutoCAD development on macOS.
license: MIT
metadata:
  author: Michael Sablatura
  version: 2.0.0
  documentation_files: 4510
  platforms:
    - Claude Code
    - GitHub Copilot
    - Cursor
    - Windsurf
    - Cline
---

## When to Use This Skill

Invoke this skill when:

- User asks to write, create, or modify AutoLISP code
- User mentions AutoCAD for Mac, Mac compatibility, or cross-platform
- User asks about AutoLISP functions and their Mac support
- User needs to validate existing AutoLISP for Mac compatibility

## Quick Start

1. **Identify functions** you plan to use
2. **Verify compatibility** using the docs in `docs/` directory
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
2. **Check each function** in `docs/` directory:
   ```bash
   grep -l "function-name-AutoLISP" docs/*.md
   ```
3. **Verify platform support** - look for `*Supported Platforms:*` line
4. **Replace incompatible functions** with Mac-safe alternatives
5. **Document any limitations** in the code header

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

- `validate_lisp.py` - Validates AutoLISP files for Mac compatibility
- `compatibility_checker.py` - Checks individual function compatibility

```bash
python3 scripts/validate_lisp.py your-script.lsp
```

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
- [ ] All functions verified in `docs/` documentation
- [ ] Compatibility header included
- [ ] Tested on Mac (or documented limitations)

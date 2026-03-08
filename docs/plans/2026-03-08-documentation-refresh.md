# Documentation Refresh Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix all documentation inaccuracies and gaps identified by audit, syncing docs with codebase reality after GraphRAG v2 migration.

**Architecture:** Targeted edits across README.md, SKILL.md, CLAUDE.md, compatibility_checker.py, and install.sh. No structural changes — fix what's wrong, fill what's missing.

**Tech Stack:** Markdown, Python, Bash

---

### Task 1: Fix README.md — Replace placeholder GitHub URLs

**Files:**
- Modify: `README.md:29,35,41`

**Step 1: Replace placeholder URLs**

Replace the three manual installation clone URLs:

Line 29 — change:
```
git clone https://github.com/yourusername/autocad-autolisp-macos.git ~/.claude/skills/autocad-autolisp-macos
```
to:
```
git clone https://github.com/Drummerms/autocad-autolisp-macos-skill.git ~/.claude/skills/autocad-autolisp-macos
```

Line 35 — change:
```
git clone https://github.com/yourusername/autocad-autolisp-macos.git .cursor/rules/autocad-autolisp-macos
```
to:
```
git clone https://github.com/Drummerms/autocad-autolisp-macos-skill.git .cursor/rules/autocad-autolisp-macos
```

Line 41 — change:
```
git clone https://github.com/yourusername/autocad-autolisp-macos.git .github/skills/autocad-autolisp-macos
```
to:
```
git clone https://github.com/Drummerms/autocad-autolisp-macos-skill.git .github/skills/autocad-autolisp-macos
```

**Step 2: Verify the edits**

Run: `grep -n "yourusername" README.md`
Expected: No matches

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs(readme): replace placeholder GitHub URLs with actual repo"
```

---

### Task 2: Fix README.md — Add version, docs repo link, CLI flags, MCP testing

**Files:**
- Modify: `README.md:1-3,66-90,120-152`

**Step 1: Add version badge after title**

After line 1 (`# AutoCAD AutoLISP Mac Compatibility Skill`), add a blank line and version line so lines 1-4 become:

```markdown
# AutoCAD AutoLISP Mac Compatibility Skill

**v3.0.0** | [Skill Definition](SKILL.md)

A comprehensive skill for creating AutoLISP scripts compatible with AutoCAD for Mac. Includes a GraphRAG knowledge graph built from ~560 official AutoLISP function reference docs for platform compatibility verification via semantic search.
```

(This replaces the existing blank line + description on lines 2-3.)

**Step 2: Add undocumented CLI flags to validate_lisp.py section**

After line 76 (`python3 scripts/validate_lisp.py --check-function vlax-get`), add:

```bash

# Verbose output with detailed results
python3 scripts/validate_lisp.py -v your-script.lsp

# JSON output for programmatic use
python3 scripts/validate_lisp.py --json your-script.lsp

# Specify a custom docs path for doc-backed lookups
python3 scripts/validate_lisp.py --docs-path /path/to/docs your-script.lsp
```

**Step 3: Add --docs-path to compatibility checker section**

After line 89 (`python3 scripts/compatibility_checker.py --list-compatible`), add:

```bash

# Specify a custom docs path for doc-backed lookups
python3 scripts/compatibility_checker.py --docs-path /path/to/docs command
```

**Step 4: Add docs repo link to GraphRAG section**

Replace line 124:
```
The documentation source files are maintained in a separate repository. You need to provide the path to the docs directory when building.
```
with:
```
The documentation source files are maintained in a separate repository: [autocad-htm-to-markdown-converter](https://github.com/Drummerms/autocad-htm-to-markdown-converter.git). Clone that repo and provide the path to its output directory when building.
```

**Step 5: Add MCP server local testing command**

After line 152 (the paragraph about pre-built autolisp.db), add:

```markdown

### Test MCP Server Locally

```bash
# Activate the venv and run the server
source .venv/bin/activate
AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py
```
```

**Step 6: Verify edits**

Run: `grep -n "yourusername\|--list-safe" README.md`
Expected: No matches

**Step 7: Commit**

```bash
git add README.md
git commit -m "docs(readme): add version, docs repo link, CLI flags, MCP testing"
```

---

### Task 3: Fix SKILL.md — Add acad_helpdlg, compatibility_checker.py, CLI flags

**Files:**
- Modify: `SKILL.md:57-69,109-118`

**Step 1: Add acad_helpdlg to forbidden patterns**

In the "Critical Mac Incompatibilities" code block (lines 61-69), add `acad_helpdlg` after `acad_truecolordlg`:

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

**Step 2: Expand Validation Scripts section**

Replace the current validation section (lines 109-118):

```markdown
## Validation Scripts

This skill includes validation tools in `scripts/`:

- `validate_lisp.py` - Validates AutoLISP files for Mac compatibility
- `compatibility_checker.py` - Checks individual function compatibility

```bash
python3 scripts/validate_lisp.py your-script.lsp
```
```

with:

```markdown
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
```

**Step 3: Add MCP server local testing note**

After the GraphRAG MCP Search section (after line 129), add:

```markdown

To test the MCP server locally: `AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py`
```

**Step 4: Verify**

Run: `grep -n "acad_helpdlg" SKILL.md`
Expected: One match in the forbidden patterns block

**Step 5: Commit**

```bash
git add SKILL.md
git commit -m "docs(skill): add acad_helpdlg, compatibility_checker docs, CLI flags"
```

---

### Task 4: Fix CLAUDE.md — Add acad_helpdlg, venv steps, CLI flags, header format, build estimates

**Files:**
- Modify: `CLAUDE.md:51-66,70-81,93-104`

**Step 1: Add acad_helpdlg to Mac Compatibility Rules**

In the compatibility rules list (lines 73-79), add after `acad_colordlg`, `acad_truecolordlg` line:

```markdown
- `acad_colordlg`, `acad_truecolordlg`, `acad_helpdlg` — use `getint` for color input
```

(Merge the new function into the existing dialog line.)

**Step 2: Add undocumented CLI flags to Commands section**

After line 45 (`python3 scripts/compatibility_checker.py --list-compatible`), add:

```bash

# Additional flags for validate_lisp.py:
#   -v, --verbose     Detailed output
#   --json            JSON output for programmatic use
#   --docs-path PATH  Custom docs directory for doc-backed lookups

# Additional flags for compatibility_checker.py:
#   --docs-path PATH  Custom docs directory for doc-backed lookups
```

**Step 3: Add Python 3.12 venv setup to GraphRAG Commands**

Replace lines 51-66 with:

````markdown
### GraphRAG Commands

```bash
# Set up Python 3.12 venv (Kuzu requires <=3.13)
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Build the knowledge graph (one-time, requires ANTHROPIC_API_KEY)
# Docs repo: https://github.com/Drummerms/autocad-htm-to-markdown-converter.git
# Full build: ~26 minutes, ~$1.73 USD (Claude Haiku extraction)
python build_graph.py --docs /path/to/autocad-docs --db ./autolisp.db

# Build with limit for testing
python build_graph.py --docs /path/to/autocad-docs --db ./autolisp.db --limit 10

# Test the MCP server locally
AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py

# Install Python dependencies
pip install -r requirements.txt
```

The MCP server is auto-discovered by Claude Code via `.mcp.json`. The pre-built `autolisp.db` database is included in the repo.
````

**Step 4: Fix LSP header format to match templates**

Replace lines 95-102:

```lisp
;;; FILENAME.LSP
;;; Description
;;; Compatibility: AutoCAD for Windows and Mac
;;; Author: Name
;;; Version: X.Y.Z
```

with:

```lisp
;;; FILENAME.LSP
;;; Brief description
;;; Compatibility: AutoCAD for Windows and Mac
;;;
;;; Description: Full description of what this command does
;;; Author: Your Name
;;; Version: 1.0.0
;;;
;;; Usage:
;;;   Load: (load "filename.lsp")
;;;   Run: COMMANDNAME
```

**Step 5: Verify**

Run: `grep -n "acad_helpdlg" CLAUDE.md`
Expected: One match in the compatibility rules

**Step 6: Commit**

```bash
git add CLAUDE.md
git commit -m "docs(claude): add acad_helpdlg, venv steps, CLI flags, fix header format"
```

---

### Task 5: Fix compatibility_checker.py — Docstring and vl-vbaload

**Files:**
- Modify: `scripts/compatibility_checker.py:11,415-416`

**Step 1: Fix docstring**

Replace line 11:
```python
    python3 compatibility_checker.py --list-safe
```
with:
```python
    python3 compatibility_checker.py --list-compatible
```

**Step 2: Add vl-vbaload to COMPATIBILITY_DB**

After the `vl-registry-write` entry (after line 415), add:

```python
    # === VBA - Windows Only ===
    "vl-vbaload": FunctionCompatibility(
        name="vl-vbaload",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="VBA not available on Mac",
        alternative="Rewrite functionality in pure AutoLISP",
        category="VBA"
    ),
```

**Step 3: Verify**

Run: `python3 scripts/compatibility_checker.py vl-vbaload`
Expected: Shows "INCOMPATIBLE" status

Run: `grep "list-safe" scripts/compatibility_checker.py`
Expected: No matches

**Step 4: Commit**

```bash
git add scripts/compatibility_checker.py
git commit -m "fix: correct docstring typo, add vl-vbaload to compatibility DB"
```

---

### Task 6: Fix install.sh — Update stale docs/ message

**Files:**
- Modify: `install.sh:186`

**Step 1: Replace stale docs message**

Replace line 186:
```bash
    print_msg "$BLUE" "  - docs/ (4,500+ AutoCAD documentation files)"
```
with:
```bash
    print_msg "$BLUE" "  - autolisp.db (pre-built GraphRAG knowledge graph)"
```

**Step 2: Verify**

Run: `grep "4,500" install.sh`
Expected: No matches

**Step 3: Commit**

```bash
git add install.sh
git commit -m "fix(install): replace stale docs reference with pre-built DB"
```

---

### Task 7: Final verification

**Step 1: Run validation to ensure nothing is broken**

```bash
python3 scripts/validate_lisp.py assets/templates/
python3 scripts/compatibility_checker.py --list-incompatible
python3 scripts/compatibility_checker.py --list-compatible
python3 scripts/compatibility_checker.py vl-vbaload
```

Expected: All templates pass, vl-vbaload shows as INCOMPATIBLE

**Step 2: Verify no stale references remain**

```bash
grep -rn "yourusername" README.md SKILL.md CLAUDE.md install.sh
grep -rn "list-safe" scripts/compatibility_checker.py
grep -rn "4,500" install.sh
```

Expected: No matches for any of these

**Step 3: Review git log**

```bash
git log --oneline -7
```

Expected: 6 new commits (Tasks 1-6) plus the design doc commit

**Step 4: Mark design plan as complete**

Add `**Status:** COMPLETE` to the header of `docs/plans/2026-03-08-documentation-refresh-design.md`

**Step 5: Commit**

```bash
git add docs/plans/2026-03-08-documentation-refresh-design.md
git commit -m "chore: mark documentation refresh design as complete"
```

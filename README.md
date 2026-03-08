# AutoCAD AutoLISP Mac Compatibility Skill

A comprehensive skill for creating AutoLISP scripts compatible with AutoCAD for Mac. Includes a GraphRAG knowledge graph built from ~560 official AutoLISP function reference docs for platform compatibility verification via semantic search.

## Features

- **Platform Compatibility Checking**: Validates AutoLISP code against Mac compatibility
- **GraphRAG Knowledge Graph**: Semantic search over ~560 AutoLISP function docs via MCP
- **Validation Scripts**: Python tools to check your AutoLISP files
- **LSP Templates**: Ready-to-use templates for common tasks
- **Cross-Platform Support**: Works with Claude Code, Cursor, GitHub Copilot, and more

## Quick Start

### Option 1: Automatic Installation

```bash
./install.sh
```

The installer will auto-detect your platform and install accordingly.

### Option 2: Manual Installation

#### Claude Code

```bash
# Clone or copy to your skills directory
git clone https://github.com/Drummerms/autocad-autolisp-macos-skill.git ~/.claude/skills/autocad-autolisp-macos
```

#### Cursor

```bash
git clone https://github.com/Drummerms/autocad-autolisp-macos-skill.git .cursor/rules/autocad-autolisp-macos
```

#### GitHub Copilot

```bash
git clone https://github.com/Drummerms/autocad-autolisp-macos-skill.git .github/skills/autocad-autolisp-macos
```

## Usage

### With AI Assistants

The skill activates automatically when you:

- Ask to write or modify AutoLISP code
- Mention AutoCAD for Mac or Mac compatibility
- Ask about AutoLISP function compatibility
- Request validation of existing AutoLISP code

Example prompts:

```
Write an AutoLISP script to batch plot all layouts
Create a Mac-compatible AutoLISP function to change entity colors
Is vlax-get supported on AutoCAD for Mac?
Validate this AutoLISP file for Mac compatibility
```

### Command Line Tools

#### Validate AutoLISP Files

```bash
# Validate a single file
python3 scripts/validate_lisp.py your-script.lsp

# Validate all .lsp files in a directory
python3 scripts/validate_lisp.py ./my-scripts/

# Check a specific function
python3 scripts/validate_lisp.py --check-function vlax-get
```

#### Check Function Compatibility

```bash
# Check a specific function
python3 scripts/compatibility_checker.py command

# List all known Mac-incompatible functions
python3 scripts/compatibility_checker.py --list-incompatible

# List all known Mac-compatible functions
python3 scripts/compatibility_checker.py --list-compatible
```

## What's Included

```
autocad-autolisp-macos/
├── SKILL.md              # Main skill file
├── docs/plans/           # Design documents and implementation plans
├── scripts/
│   ├── validate_lisp.py          # AutoLISP validator
│   └── compatibility_checker.py  # Function compatibility checker
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
├── build_graph.py        # GraphRAG ingestion (558 function docs)
├── mcp_server.py         # MCP server for semantic search
├── requirements.txt      # Python dependencies
├── .mcp.json             # MCP auto-discovery config
├── CLAUDE.md             # Claude Code project instructions
└── README.md             # This file
```

## GraphRAG Setup (Optional)

The GraphRAG MCP server provides semantic search over ~560 AutoLISP function reference docs. It requires a one-time build step.

The documentation source files are maintained in a separate repository. You need to provide the path to the docs directory when building.

### Prerequisites

- Python 3.12 (Kuzu requires pre-built wheels not available on 3.14)
- An Anthropic API key (for Claude Haiku extraction, ~$1.73 for full build)
- AutoCAD documentation markdown files (from the companion docs repo)

### Build

```bash
# Create Python 3.12 venv
python3.12 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set your API key
echo "ANTHROPIC_API_KEY=your-key" > .env

# Build the knowledge graph (~26 minutes)
python build_graph.py --docs /path/to/autocad-docs --db ./autolisp.db

# Test with a small subset first
python build_graph.py --docs /path/to/autocad-docs --db ./autolisp.db --limit 10
```

The MCP server is auto-discovered by Claude Code via `.mcp.json`. The pre-built `autolisp.db` database is included in the repo (23MB), so the MCP server works out of the box without running the build step.

## Mac Compatibility Overview

### Fully Compatible

| Category | Examples |
|----------|----------|
| Core AutoLISP | `defun`, `setq`, `if`, `while`, `foreach` |
| Command Execution | `command`, `command-s`, `vl-cmdf` |
| Entity Functions | `entmake`, `entget`, `entmod`, `entdel` |
| Selection Sets | `ssget`, `ssadd`, `ssdel`, `sslength` |
| User Input | `getpoint`, `getdist`, `getstring`, `ssget` |
| File Operations | `open`, `close`, `vl-file-*` |
| Visual LISP | `vl-load-all`, `vl-sort`, `vl-remove` |

### Windows Only (Avoid on Mac)

| Category | Examples | Alternative |
|----------|----------|-------------|
| ActiveX/COM | `vlax-*` | Use `entget`/`entmod` with DXF codes |
| Reactors | `vlr-*` | Use polling or command wrappers |
| Express Tools | `acet-*` | Implement with standard AutoLISP |
| Registry | `vl-registry-*` | Use config files |
| Dialogs | `acad_colordlg` | Use `getint` |

## Example: Mac-Compatible AutoLISP

```lisp
;;; BATCH-PLOT.LSP
;;; Plots all layouts to PDF
;;; Compatibility: AutoCAD for Windows and Mac

(defun c:BATCHPLOT (/ layout-name layouts i)
  (vl-load-all)  ;; Mac-compatible

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

## Common Conversions

### ActiveX to DXF

| Windows (ActiveX) | Mac (DXF) |
|-------------------|-----------|
| `(vlax-get obj 'Radius)` | `(cdr (assoc 40 (entget ent)))` |
| `(vlax-put obj 'Radius 10)` | `(entmod (subst (cons 40 10) (assoc 40 data) data))` |

### Dialogs to Command Line

| Windows | Mac |
|---------|-----|
| `(acad_colordlg 1)` | `(getint "\nColor number: ")` |

## Platform Support

| Platform | Install Location |
|----------|-----------------|
| Claude Code | `~/.claude/skills/` |
| GitHub Copilot | `.github/skills/` |
| Cursor | `.cursor/rules/` |
| Windsurf | `.windsurf/skills/` |
| Cline | `.clinerules/` |
| Codex CLI | `.codex/skills/` |
| Gemini CLI | `.gemini/skills/` |

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions welcome! Please ensure any AutoLISP code is Mac-compatible.

## Credits

- Documentation sourced from official Autodesk AutoCAD help files
- Built following the Agent Skills Open Standard

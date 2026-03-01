#!/bin/bash
#
# AutoCAD AutoLISP Mac Compatibility Skill Installer
# Cross-platform installer for Claude Code, Cursor, GitHub Copilot, and more
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
PLATFORM=""
SKILL_NAME="autocad-autolisp-macos"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Print colored message
print_msg() {
    local color=$1
    local msg=$2
    echo -e "${color}${msg}${NC}"
}

# Print usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --platform PLATFORM   Target platform (claude, copilot, cursor, windsurf, cline, codex, gemini)"
    echo "  --help               Show this help message"
    echo ""
    echo "Platforms:"
    echo "  claude    Claude Code (~/.claude/skills/)"
    echo "  copilot   GitHub Copilot (.github/skills/)"
    echo "  cursor    Cursor (.cursor/rules/)"
    echo "  windsurf  Windsurf (.windsurf/skills/)"
    echo "  cline     Cline (.clinerules/)"
    echo "  codex     Codex CLI (.codex/skills/)"
    echo "  gemini    Gemini CLI (.gemini/skills/)"
    echo ""
    echo "If no platform is specified, auto-detects from current directory."
    echo ""
    echo "Examples:"
    echo "  $0                      # Auto-detect platform"
    echo "  $0 --platform claude    # Install for Claude Code"
    echo "  $0 --platform cursor    # Install for Cursor"
    exit 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --platform)
            PLATFORM="$2"
            shift 2
            ;;
        --help|-h)
            usage
            ;;
        *)
            print_msg "$RED" "Unknown option: $1"
            usage
            ;;
    esac
done

# Auto-detect platform if not specified
detect_platform() {
    if [[ -d ".claude" ]] || [[ -f ".claude/settings.local.json" ]]; then
        echo "claude"
    elif [[ -d ".github" ]]; then
        echo "copilot"
    elif [[ -d ".cursor" ]]; then
        echo "cursor"
    elif [[ -d ".windsurf" ]]; then
        echo "windsurf"
    elif [[ -d ".clinerules" ]]; then
        echo "cline"
    elif [[ -d ".codex" ]]; then
        echo "codex"
    elif [[ -d ".gemini" ]]; then
        echo "gemini"
    else
        echo "claude"  # Default to Claude Code
    fi
}

# Get installation path for platform
get_install_path() {
    local platform=$1
    case $platform in
        claude)
            echo "$HOME/.claude/skills/$SKILL_NAME"
            ;;
        copilot)
            echo "$(pwd)/.github/skills/$SKILL_NAME"
            ;;
        cursor)
            echo "$(pwd)/.cursor/rules/$SKILL_NAME"
            ;;
        windsurf)
            echo "$(pwd)/.windsurf/skills/$SKILL_NAME"
            ;;
        cline)
            echo "$(pwd)/.clinerules/$SKILL_NAME"
            ;;
        codex)
            echo "$(pwd)/.codex/skills/$SKILL_NAME"
            ;;
        gemini)
            echo "$(pwd)/.gemini/skills/$SKILL_NAME"
            ;;
        *)
            echo "$HOME/.claude/skills/$SKILL_NAME"
            ;;
    esac
}

# Main installation logic
main() {
    # Auto-detect platform if not specified
    if [[ -z "$PLATFORM" ]]; then
        PLATFORM=$(detect_platform)
        print_msg "$YELLOW" "Auto-detected platform: $PLATFORM"
    fi

    INSTALL_PATH=$(get_install_path "$PLATFORM")

    print_msg "$BLUE" "=========================================="
    print_msg "$BLUE" "AutoCAD AutoLISP Mac Compatibility Skill"
    print_msg "$BLUE" "=========================================="
    echo ""
    print_msg "$GREEN" "Platform: $PLATFORM"
    print_msg "$GREEN" "Install path: $INSTALL_PATH"
    echo ""

    # Check if source directory exists
    if [[ ! -f "$SCRIPT_DIR/SKILL.md" ]]; then
        print_msg "$RED" "Error: SKILL.md not found in $SCRIPT_DIR"
        exit 1
    fi

    # Create parent directory if needed
    PARENT_DIR=$(dirname "$INSTALL_PATH")
    if [[ ! -d "$PARENT_DIR" ]]; then
        print_msg "$YELLOW" "Creating parent directory: $PARENT_DIR"
        mkdir -p "$PARENT_DIR"
    fi

    # Check if skill already exists
    if [[ -d "$INSTALL_PATH" ]] || [[ -L "$INSTALL_PATH" ]]; then
        print_msg "$YELLOW" "Skill already exists at $INSTALL_PATH"
        read -p "Overwrite? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_msg "$RED" "Installation cancelled."
            exit 1
        fi
        rm -rf "$INSTALL_PATH"
    fi

    # Create symbolic link or copy
    print_msg "$GREEN" "Installing skill..."

    # For global installations (claude), create a symlink
    # For project installations, copy the files
    if [[ "$PLATFORM" == "claude" ]]; then
        ln -s "$SCRIPT_DIR" "$INSTALL_PATH"
        print_msg "$GREEN" "Created symbolic link: $INSTALL_PATH -> $SCRIPT_DIR"
    else
        cp -r "$SCRIPT_DIR" "$INSTALL_PATH"
        print_msg "$GREEN" "Copied skill to: $INSTALL_PATH"
    fi

    echo ""
    print_msg "$GREEN" "=========================================="
    print_msg "$GREEN" "Installation complete!"
    print_msg "$GREEN" "=========================================="
    echo ""
    print_msg "$BLUE" "The skill includes:"
    print_msg "$BLUE" "  - SKILL.md (main skill file)"
    print_msg "$BLUE" "  - docs/ (4,500+ AutoCAD documentation files)"
    print_msg "$BLUE" "  - scripts/ (validation tools)"
    print_msg "$BLUE" "  - references/ (detailed documentation)"
    print_msg "$BLUE" "  - assets/templates/ (LSP templates)"
    echo ""
    print_msg "$YELLOW" "Usage:"
    print_msg "$YELLOW" "  The skill will activate automatically when you ask about"
    print_msg "$YELLOW" "  AutoLISP, AutoCAD for Mac, or cross-platform compatibility."
    echo ""
    print_msg "$YELLOW" "Validate AutoLISP files:"
    print_msg "$YELLOW" "  python3 scripts/validate_lisp.py your-file.lsp"
    echo ""
    print_msg "$YELLOW" "Check function compatibility:"
    print_msg "$YELLOW" "  python3 scripts/compatibility_checker.py vlax-get"
}

# Run main
main

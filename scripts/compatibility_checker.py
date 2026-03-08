#!/usr/bin/env python3
"""
AutoLISP Function Compatibility Checker

Provides quick lookup of AutoLISP function compatibility with AutoCAD for Mac.
Can search the included documentation or provide offline lookups for known functions.

Usage:
    python3 compatibility_checker.py <function_name>
    python3 compatibility_checker.py --list-incompatible
    python3 compatibility_checker.py --list-compatible
"""

import os
import re
import sys
import glob
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class Compatibility(Enum):
    FULL = "full"           # Works on Mac with full functionality
    PARTIAL = "partial"     # Works on Mac with limitations
    WINDOWS_ONLY = "windows_only"  # Does not work on Mac
    UNKNOWN = "unknown"     # Not documented


@dataclass
class FunctionCompatibility:
    """Compatibility information for an AutoLISP function."""
    name: str
    compatibility: Compatibility
    platforms: str
    notes: str = ""
    alternative: str = ""
    category: str = ""


# Pre-defined compatibility database for common functions
# This provides fast offline lookups
COMPATIBILITY_DB: Dict[str, FunctionCompatibility] = {
    # === CORE AUTOLISP - Fully Compatible ===
    "command": FunctionCompatibility(
        name="command",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Command Execution"
    ),
    "command-s": FunctionCompatibility(
        name="command-s",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Command Execution"
    ),
    "vl-cmdf": FunctionCompatibility(
        name="vl-cmdf",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Command Execution"
    ),
    "entmake": FunctionCompatibility(
        name="entmake",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Entity Functions"
    ),
    "entmakeX": FunctionCompatibility(
        name="entmakeX",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Entity Functions"
    ),
    "entget": FunctionCompatibility(
        name="entget",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Entity Functions"
    ),
    "entmod": FunctionCompatibility(
        name="entmod",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Entity Functions"
    ),
    "entdel": FunctionCompatibility(
        name="entdel",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Entity Functions"
    ),
    "entnext": FunctionCompatibility(
        name="entnext",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Entity Functions"
    ),
    "entsel": FunctionCompatibility(
        name="entsel",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Entity Functions"
    ),

    # === USER INPUT - Fully Compatible ===
    "getpoint": FunctionCompatibility(
        name="getpoint",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getcorner": FunctionCompatibility(
        name="getcorner",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getdist": FunctionCompatibility(
        name="getdist",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getangle": FunctionCompatibility(
        name="getangle",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getorient": FunctionCompatibility(
        name="getorient",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getint": FunctionCompatibility(
        name="getint",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getreal": FunctionCompatibility(
        name="getreal",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getstring": FunctionCompatibility(
        name="getstring",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getkword": FunctionCompatibility(
        name="getkword",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),
    "getfiled": FunctionCompatibility(
        name="getfiled",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="User Input"
    ),

    # === SELECTION SETS - Fully Compatible ===
    "ssget": FunctionCompatibility(
        name="ssget",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Selection Sets"
    ),
    "ssadd": FunctionCompatibility(
        name="ssadd",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Selection Sets"
    ),
    "ssdel": FunctionCompatibility(
        name="ssdel",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Selection Sets"
    ),
    "sslength": FunctionCompatibility(
        name="sslength",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Selection Sets"
    ),
    "ssname": FunctionCompatibility(
        name="ssname",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Selection Sets"
    ),

    # === FILE OPERATIONS - Fully Compatible ===
    "open": FunctionCompatibility(
        name="open",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "close": FunctionCompatibility(
        name="close",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "read-line": FunctionCompatibility(
        name="read-line",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "write-line": FunctionCompatibility(
        name="write-line",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "findfile": FunctionCompatibility(
        name="findfile",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "vl-file-list": FunctionCompatibility(
        name="vl-file-list",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "vl-file-delete": FunctionCompatibility(
        name="vl-file-delete",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "vl-file-rename": FunctionCompatibility(
        name="vl-file-rename",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "vl-file-copy": FunctionCompatibility(
        name="vl-file-copy",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),
    "vl-directory-files": FunctionCompatibility(
        name="vl-directory-files",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="File I/O"
    ),

    # === VISUAL LISP EXTENSIONS - Fully Compatible ===
    "vl-load-all": FunctionCompatibility(
        name="vl-load-all",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Visual LISP"
    ),
    "vl-sort": FunctionCompatibility(
        name="vl-sort",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Visual LISP"
    ),
    "vl-remove": FunctionCompatibility(
        name="vl-remove",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Visual LISP"
    ),
    "vl-position": FunctionCompatibility(
        name="vl-position",
        compatibility=Compatibility.FULL,
        platforms="Windows, Mac OS, and Web",
        category="Visual LISP"
    ),

    # === ACTIVEX/COM - Windows Only ===
    "vl-load-com": FunctionCompatibility(
        name="vl-load-com",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="COM is not supported on Mac",
        alternative="Use entget/entmod or command function",
        category="ActiveX/COM"
    ),
    "vlax-get": FunctionCompatibility(
        name="vlax-get",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="ActiveX not supported on Mac",
        alternative="Use (cdr (assoc 40 (entget entity))) for properties",
        category="ActiveX/COM"
    ),
    "vlax-put": FunctionCompatibility(
        name="vlax-put",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="ActiveX not supported on Mac",
        alternative="Use entmod with modified association list",
        category="ActiveX/COM"
    ),
    "vlax-create-object": FunctionCompatibility(
        name="vlax-create-object",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="AutoCAD for Windows only",
        notes="COM object creation not available on Mac",
        alternative="Use external scripts or command function",
        category="ActiveX/COM"
    ),
    "vlax-get-acad-object": FunctionCompatibility(
        name="vlax-get-acad-object",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="ActiveX not supported on Mac",
        alternative="Not available - use standard AutoLISP functions",
        category="ActiveX/COM"
    ),

    # === REACTORS - Windows Only ===
    "vlr-object-reactor": FunctionCompatibility(
        name="vlr-object-reactor",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="Reactors not supported on Mac",
        alternative="Use polling or command wrappers",
        category="Reactors"
    ),
    "vlr-command-reactor": FunctionCompatibility(
        name="vlr-command-reactor",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="Reactors not supported on Mac",
        alternative="Use command wrappers or UNDO markers",
        category="Reactors"
    ),

    # === EXPRESS TOOLS - Windows Only ===
    "acet-sys-wait": FunctionCompatibility(
        name="acet-sys-wait",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="AutoCAD for Windows only; not available in AutoCAD LT, Mac OS or Web",
        notes="Express Tools not available on Mac",
        alternative="Implement equivalent with standard AutoLISP",
        category="Express Tools"
    ),
    "acet-str-replace": FunctionCompatibility(
        name="acet-str-replace",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="AutoCAD for Windows only",
        notes="Express Tools not available on Mac",
        alternative="Use vl-string-subst recursively",
        category="Express Tools"
    ),

    # === DIALOGS ===
    "acad_colordlg": FunctionCompatibility(
        name="acad_colordlg",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only",
        notes="Windows-only color dialog",
        alternative="(getint \"\\nEnter color number (1-256): \")",
        category="Dialogs"
    ),
    "acad_truecolordlg": FunctionCompatibility(
        name="acad_truecolordlg",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only",
        notes="Windows-only true color dialog",
        alternative="(getint \"\\nEnter color number: \")",
        category="Dialogs"
    ),
    "load_dialog": FunctionCompatibility(
        name="load_dialog",
        compatibility=Compatibility.PARTIAL,
        platforms="Windows, Mac OS, and Web",
        notes="DCL supported on AutoCAD Mac, but NOT on AutoCAD LT Mac",
        category="DCL Dialogs"
    ),
    "new_dialog": FunctionCompatibility(
        name="new_dialog",
        compatibility=Compatibility.PARTIAL,
        platforms="Windows, Mac OS, and Web",
        notes="DCL supported on AutoCAD Mac, but NOT on AutoCAD LT Mac",
        category="DCL Dialogs"
    ),

    # === REGISTRY - Windows Only ===
    "vl-registry-read": FunctionCompatibility(
        name="vl-registry-read",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS",
        notes="Windows Registry not available on Mac",
        alternative="Use external config files (JSON, LSP, or INI)",
        category="Registry"
    ),
    "vl-registry-write": FunctionCompatibility(
        name="vl-registry-write",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS",
        notes="Windows Registry not available on Mac",
        alternative="Use external config files (JSON, LSP, or INI)",
        category="Registry"
    ),

    # === VBA - Windows Only ===
    "vl-vbaload": FunctionCompatibility(
        name="vl-vbaload",
        compatibility=Compatibility.WINDOWS_ONLY,
        platforms="Windows only; not available on Mac OS or Web",
        notes="VBA not available on Mac",
        alternative="Rewrite functionality in pure AutoLISP",
        category="VBA"
    ),
}


class CompatibilityChecker:
    """Check AutoLISP function compatibility with AutoCAD for Mac."""

    def __init__(self, docs_path: Optional[str] = None):
        """
        Initialize the compatibility checker.

        Args:
            docs_path: Optional path to the AutoCAD documentation directory.
        """
        self.docs_path = docs_path or self._find_docs_path()

    def _find_docs_path(self) -> Optional[str]:
        """Find the docs directory."""
        script_dir = Path(__file__).parent
        candidates = [
            script_dir.parent / "docs",
            script_dir.parent.parent / "docs",
            Path.cwd() / "docs",
        ]
        for candidate in candidates:
            if candidate.exists():
                return str(candidate)
        return None

    def check_function(self, func_name: str) -> FunctionCompatibility:
        """
        Check the Mac compatibility of an AutoLISP function.

        Args:
            func_name: Name of the function to check.

        Returns:
            FunctionCompatibility with compatibility information.
        """
        # Normalize function name
        func_name = func_name.lower().strip('-')

        # Check offline database first
        if func_name in COMPATIBILITY_DB:
            return COMPATIBILITY_DB[func_name]

        # Check for pattern matches (e.g., vlax-*, vlr-*, acet-*)
        if func_name.startswith('vlax-') or func_name.startswith('vlax_'):
            return FunctionCompatibility(
                name=func_name,
                compatibility=Compatibility.WINDOWS_ONLY,
                platforms="Windows only; not available on Mac OS or Web",
                notes="ActiveX/COM functions are not available on Mac",
                alternative="Use entget/entmod with DXF codes or command function",
                category="ActiveX/COM"
            )

        if func_name.startswith('vlr-') or func_name.startswith('vlr_'):
            return FunctionCompatibility(
                name=func_name,
                compatibility=Compatibility.WINDOWS_ONLY,
                platforms="Windows only; not available on Mac OS or Web",
                notes="Reactor functions are not available on Mac",
                alternative="Use polling or command wrappers",
                category="Reactors"
            )

        if func_name.startswith('acet-') or func_name.startswith('acet_'):
            return FunctionCompatibility(
                name=func_name,
                compatibility=Compatibility.WINDOWS_ONLY,
                platforms="AutoCAD for Windows only",
                notes="Express Tools are not available on Mac",
                alternative="Implement equivalent functionality with standard AutoLISP",
                category="Express Tools"
            )

        if func_name.startswith('vl-registry-'):
            return FunctionCompatibility(
                name=func_name,
                compatibility=Compatibility.WINDOWS_ONLY,
                platforms="Windows only",
                notes="Windows Registry not available on Mac",
                alternative="Use external config files",
                category="Registry"
            )

        # Try to find in documentation
        if self.docs_path:
            doc_result = self._check_docs(func_name)
            if doc_result:
                return doc_result

        return FunctionCompatibility(
            name=func_name,
            compatibility=Compatibility.UNKNOWN,
            platforms="Unknown",
            notes="Function not found in compatibility database"
        )

    def _check_docs(self, func_name: str) -> Optional[FunctionCompatibility]:
        """Check function in the AutoCAD documentation files."""
        patterns = [
            f"{func_name}-AutoLISP.md",
            f"{func_name}-AutoLISP-ActiveX.md",
            f"{func_name}-AutoLISP-DCL.md",
            f"{func_name}-AutoLISP-Express-Tools.md",
        ]

        for pattern in patterns:
            matches = glob.glob(str(Path(self.docs_path) / pattern))
            if matches:
                return self._parse_doc_file(matches[0], func_name)

        return None

    def _parse_doc_file(self, filepath: str, func_name: str) -> FunctionCompatibility:
        """Parse documentation file for platform information."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find platform support line
            match = re.search(
                r'\*Supported Platforms:\*\s*(.+?)(?:\n|$)',
                content,
                re.IGNORECASE
            )

            if match:
                platforms = match.group(1).strip()

                if 'windows only' in platforms.lower() and 'mac' not in platforms.lower():
                    return FunctionCompatibility(
                        name=func_name,
                        compatibility=Compatibility.WINDOWS_ONLY,
                        platforms=platforms
                    )
                elif 'mac' in platforms.lower():
                    # Check for limitations
                    note_match = re.search(r'NOTE:(.*(?:mac|lt)[^\n]*)', content, re.IGNORECASE)
                    notes = note_match.group(1).strip() if note_match else ""
                    return FunctionCompatibility(
                        name=func_name,
                        compatibility=Compatibility.FULL if not notes else Compatibility.PARTIAL,
                        platforms=platforms,
                        notes=notes
                    )

            return FunctionCompatibility(
                name=func_name,
                compatibility=Compatibility.UNKNOWN,
                platforms="Could not determine from documentation"
            )

        except Exception as e:
            return FunctionCompatibility(
                name=func_name,
                compatibility=Compatibility.UNKNOWN,
                platforms=f"Error reading docs: {str(e)}"
            )

    def list_incompatible(self) -> List[str]:
        """Return a list of known Mac-incompatible functions."""
        return sorted([
            name for name, info in COMPATIBILITY_DB.items()
            if info.compatibility == Compatibility.WINDOWS_ONLY
        ])

    def list_compatible(self) -> List[str]:
        """Return a list of known Mac-compatible functions."""
        return sorted([
            name for name, info in COMPATIBILITY_DB.items()
            if info.compatibility in (Compatibility.FULL, Compatibility.PARTIAL)
        ])


def print_function_info(info: FunctionCompatibility):
    """Print formatted function compatibility information."""
    # Status emoji/color
    status = {
        Compatibility.FULL: "COMPATIBLE",
        Compatibility.PARTIAL: "PARTIAL",
        Compatibility.WINDOWS_ONLY: "INCOMPATIBLE",
        Compatibility.UNKNOWN: "UNKNOWN"
    }[info.compatibility]

    print(f"\n{'='*60}")
    print(f"Function: {info.name}")
    print(f"Status: {status}")
    print(f"Platforms: {info.platforms}")

    if info.category:
        print(f"Category: {info.category}")

    if info.notes:
        print(f"Notes: {info.notes}")

    if info.alternative:
        print(f"Mac Alternative: {info.alternative}")

    print(f"{'='*60}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Check AutoLISP function compatibility with AutoCAD for Mac'
    )
    parser.add_argument(
        'function',
        nargs='?',
        help='Function name to check'
    )
    parser.add_argument(
        '--list-incompatible',
        action='store_true',
        help='List all known Mac-incompatible functions'
    )
    parser.add_argument(
        '--list-compatible',
        action='store_true',
        help='List all known Mac-compatible functions'
    )
    parser.add_argument(
        '--docs-path',
        help='Path to AutoCAD documentation directory'
    )

    args = parser.parse_args()

    checker = CompatibilityChecker(docs_path=args.docs_path)

    if args.list_incompatible:
        funcs = checker.list_incompatible()
        print(f"\nKnown Mac-incompatible functions ({len(funcs)}):")
        for func in funcs:
            print(f"  - {func}")
        return 0

    if args.list_compatible:
        funcs = checker.list_compatible()
        print(f"\nKnown Mac-compatible functions ({len(funcs)}):")
        for func in funcs:
            print(f"  - {func}")
        return 0

    if args.function:
        info = checker.check_function(args.function)
        print_function_info(info)
        return 0 if info.compatibility != Compatibility.WINDOWS_ONLY else 1

    parser.print_help()
    return 0


if __name__ == '__main__':
    sys.exit(main())

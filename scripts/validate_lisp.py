#!/usr/bin/env python3
"""
AutoLISP Mac Compatibility Validator

Validates AutoLISP files for Mac compatibility by checking for
Windows-only functions and providing suggestions for alternatives.

Usage:
    python3 validate_lisp.py <file.lsp>
    python3 validate_lisp.py <directory>
    python3 validate_lisp.py --check-function vlax-get
"""

import os
import re
import sys
import glob
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
from enum import Enum


class CompatibilityLevel(Enum):
    MAC_COMPATIBLE = "mac_compatible"
    WINDOWS_ONLY = "windows_only"
    PARTIAL = "partial"  # Works on Mac with limitations
    UNKNOWN = "unknown"


@dataclass
class FunctionInfo:
    """Information about an AutoLISP function's Mac compatibility."""
    name: str
    compatibility: CompatibilityLevel
    notes: str = ""
    alternative: str = ""


# Known Windows-only function patterns
WINDOWS_ONLY_PATTERNS = {
    # ActiveX/COM functions
    r'\bvlax-\w+\b': FunctionInfo(
        name="vlax-*",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="ActiveX functions are not available on Mac",
        alternative="Use entget/entmod with DXF codes or command function"
    ),
    # Reactor functions
    r'\bvlr-\w+\b': FunctionInfo(
        name="vlr-*",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="Reactor functions are not available on Mac",
        alternative="Use polling or command wrappers instead"
    ),
    # Express Tools
    r'\bacet-\w+\b': FunctionInfo(
        name="acet-*",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="Express Tools are Windows only",
        alternative="Implement equivalent functionality with standard AutoLISP"
    ),
    # COM loading
    r'\bvl-load-com\b': FunctionInfo(
        name="vl-load-com",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="COM is not available on Mac",
        alternative="Not available - remove this call"
    ),
    # VBA
    r'\bvl-vbaload\b': FunctionInfo(
        name="vl-vbaload",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="VBA is not available on Mac",
        alternative="Rewrite in pure AutoLISP"
    ),
    # Windows-only dialogs
    r'\bacad_colordlg\b': FunctionInfo(
        name="acad_colordlg",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="Windows-only color dialog",
        alternative="Use (getint \"\\nEnter color number: \")"
    ),
    r'\bacad_truecolordlg\b': FunctionInfo(
        name="acad_truecolordlg",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="Windows-only true color dialog",
        alternative="Use (getint \"\\nEnter color number: \")"
    ),
    # Registry functions
    r'\bvl-registry-\w+\b': FunctionInfo(
        name="vl-registry-*",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="Windows Registry is not available on Mac",
        alternative="Use external config files (JSON/LSP)"
    ),
    # Help dialog
    r'\bacad_helpdlg\b': FunctionInfo(
        name="acad_helpdlg",
        compatibility=CompatibilityLevel.WINDOWS_ONLY,
        notes="Windows-only help dialog",
        alternative="Use (help) function or external documentation"
    ),
}

# Functions that work on Mac but with limitations
PARTIAL_SUPPORT = {
    r'\bload_dialog\b': FunctionInfo(
        name="load_dialog",
        compatibility=CompatibilityLevel.PARTIAL,
        notes="DCL supported on AutoCAD Mac, but NOT on AutoCAD LT Mac",
        alternative="Command-line input for LT compatibility"
    ),
    r'\bnew_dialog\b': FunctionInfo(
        name="new_dialog",
        compatibility=CompatibilityLevel.PARTIAL,
        notes="DCL supported on AutoCAD Mac, but NOT on AutoCAD LT Mac",
        alternative="Command-line input for LT compatibility"
    ),
}

# Safe functions (for reference/documentation)
SAFE_FUNCTIONS = {
    'command', 'command-s', 'vl-cmdf',
    'entmake', 'entmakeX', 'entget', 'entmod', 'entdel', 'entnext', 'entsel', 'entupd',
    'ssget', 'ssadd', 'ssdel', 'sslength', 'ssname', 'sssetfirst', 'ssgetfirst',
    'getpoint', 'getcorner', 'getdist', 'getangle', 'getorient',
    'getint', 'getreal', 'getstring', 'getkword', 'getfiled',
    'setvar', 'getvar',
    'vl-load-all', 'vl-sort', 'vl-sort-i', 'vl-remove', 'vl-remove-if', 'vl-remove-if-not',
    'vl-member-if', 'vl-member-if-not', 'vl-position', 'vl-every', 'vl-some',
    'vl-file-', 'vl-directory-files', 'vl-filename-',
    'open', 'close', 'read-line', 'write-line', 'read-char', 'write-char',
    'princ', 'prin1', 'print', 'prompt',
    'defun', 'setq', 'if', 'cond', 'while', 'repeat', 'foreach', 'mapcar', 'lambda',
    'car', 'cdr', 'cadr', 'caddr', 'cadddr', 'caar', 'cdar', 'cadar', 'cddr', 'caddar',
    'cons', 'list', 'append', 'reverse', 'length', 'nth', 'assoc', 'subst', 'member',
    '+', '-', '*', '/', '1+', '1-', 'abs', 'sin', 'cos', 'atan', 'sqrt', 'expt', 'log', 'exp',
    'fix', 'float', 'itoa', 'atoi', 'rtos', 'atof', 'angtos', 'angtof', 'distof',
    'strcat', 'strlen', 'substr', 'strcase', 'vl-string-', 'wcmatch',
    '=', '/=', '<', '>', '<=', '>=', 'eq', 'equal', 'null', 'not', 'and', 'or',
    'type', 'boundp', 'numberp', 'listp', 'atom', 'minusp', 'zerop',
    'eval', 'apply', 'quote', 'function',
    'layoutlist', 'vla-get-', 'vla-put-', 'vla-',
}


class AutoLISPValidator:
    """Validates AutoLISP code for Mac compatibility."""

    def __init__(self, docs_path: str = None):
        """
        Initialize the validator.

        Args:
            docs_path: Path to the AutoCAD documentation directory.
                       If None, will try to find it relative to this script.
        """
        self.docs_path = docs_path or self._find_docs_path()
        self.doc_cache: Dict[str, FunctionInfo] = {}

    def _find_docs_path(self) -> str:
        """Find the docs directory relative to this script or skill."""
        # Check common locations
        script_dir = Path(__file__).parent
        candidates = [
            script_dir.parent / "docs",  # scripts/../docs
            script_dir.parent.parent / "docs",  # scripts/../../docs
            Path.cwd() / "docs",  # current working directory
        ]

        for candidate in candidates:
            if candidate.exists() and candidate.is_dir():
                return str(candidate)

        return None

    def check_function_in_docs(self, func_name: str) -> FunctionInfo:
        """
        Check function compatibility in the AutoCAD documentation.

        Args:
            func_name: Name of the function to check.

        Returns:
            FunctionInfo with compatibility information.
        """
        if not self.docs_path:
            return FunctionInfo(
                name=func_name,
                compatibility=CompatibilityLevel.UNKNOWN,
                notes="Documentation path not found"
            )

        # Try to find the function's documentation file
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

        return FunctionInfo(
            name=func_name,
            compatibility=CompatibilityLevel.UNKNOWN,
            notes=f"Documentation not found for {func_name}"
        )

    def _parse_doc_file(self, filepath: str, func_name: str) -> FunctionInfo:
        """Parse an AutoCAD documentation file for platform support info."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Look for platform support line
            support_match = re.search(
                r'\*Supported Platforms:\*\s*(.+?)(?:\n|$)',
                content,
                re.IGNORECASE
            )

            if support_match:
                platforms = support_match.group(1).strip()

                if 'windows only' in platforms.lower() and 'not available on mac' in platforms.lower():
                    return FunctionInfo(
                        name=func_name,
                        compatibility=CompatibilityLevel.WINDOWS_ONLY,
                        notes=platforms
                    )
                elif 'mac' in platforms.lower():
                    return FunctionInfo(
                        name=func_name,
                        compatibility=CompatibilityLevel.MAC_COMPATIBLE,
                        notes=platforms
                    )

            # Look for NOTE about Mac limitations
            note_match = re.search(
                r'NOTE:.*(?:mac|mac os)',
                content,
                re.IGNORECASE
            )

            if note_match:
                return FunctionInfo(
                    name=func_name,
                    compatibility=CompatibilityLevel.PARTIAL,
                    notes=note_match.group(0)[:200]
                )

            return FunctionInfo(
                name=func_name,
                compatibility=CompatibilityLevel.UNKNOWN,
                notes=f"Platform support not clearly documented"
            )

        except Exception as e:
            return FunctionInfo(
                name=func_name,
                compatibility=CompatibilityLevel.UNKNOWN,
                notes=f"Error reading documentation: {str(e)}"
            )

    def validate_code(self, code: str) -> Tuple[List[Tuple[str, FunctionInfo]], List[str]]:
        """
        Validate AutoLISP code for Mac compatibility.

        Args:
            code: The AutoLISP code to validate.

        Returns:
            Tuple of (issues found, summary messages)
        """
        issues = []
        messages = []

        # Check for Windows-only patterns
        for pattern, info in WINDOWS_ONLY_PATTERNS.items():
            matches = re.findall(pattern, code, re.IGNORECASE)
            if matches:
                for match in set(matches):
                    issues.append((match, info))
                    messages.append(
                        f"ERROR: '{match}' - {info.notes}"
                    )
                    if info.alternative:
                        messages.append(f"       Alternative: {info.alternative}")

        # Check for partial support patterns
        for pattern, info in PARTIAL_SUPPORT.items():
            matches = re.findall(pattern, code, re.IGNORECASE)
            if matches:
                for match in set(matches):
                    issues.append((match, info))
                    messages.append(
                        f"WARNING: '{match}' - {info.notes}"
                    )

        return issues, messages

    def validate_file(self, filepath: str) -> Dict:
        """
        Validate an AutoLISP file for Mac compatibility.

        Args:
            filepath: Path to the .lsp file.

        Returns:
            Dictionary with validation results.
        """
        result = {
            'file': filepath,
            'errors': [],
            'warnings': [],
            'compatible': True,
            'issues_count': 0
        }

        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()

            issues, messages = self.validate_code(code)

            for match, info in issues:
                if info.compatibility == CompatibilityLevel.WINDOWS_ONLY:
                    result['errors'].append({
                        'function': match,
                        'message': info.notes,
                        'alternative': info.alternative
                    })
                    result['compatible'] = False
                elif info.compatibility == CompatibilityLevel.PARTIAL:
                    result['warnings'].append({
                        'function': match,
                        'message': info.notes
                    })

            result['issues_count'] = len(result['errors']) + len(result['warnings'])

        except Exception as e:
            result['errors'].append({
                'function': 'N/A',
                'message': f"Failed to read file: {str(e)}",
                'alternative': ''
            })
            result['compatible'] = False

        return result

    def validate_directory(self, dirpath: str) -> List[Dict]:
        """
        Validate all AutoLISP files in a directory.

        Args:
            dirpath: Path to the directory.

        Returns:
            List of validation results for each file.
        """
        results = []

        for ext in ['*.lsp', '*.LSP']:
            for filepath in glob.glob(str(Path(dirpath) / '**' / ext), recursive=True):
                results.append(self.validate_file(filepath))

        return results


def print_report(result: Dict, verbose: bool = False):
    """Print a validation report for a single file."""
    print(f"\n{'='*60}")
    print(f"File: {result['file']}")
    print(f"{'='*60}")

    if result['compatible']:
        print("Status: COMPATIBLE with AutoCAD for Mac")
    else:
        print("Status: INCOMPATIBLE with AutoCAD for Mac")

    if result['errors']:
        print(f"\nErrors ({len(result['errors'])}):")
        for error in result['errors']:
            print(f"  - {error['function']}: {error['message']}")
            if error['alternative'] and verbose:
                print(f"    Alternative: {error['alternative']}")

    if result['warnings']:
        print(f"\nWarnings ({len(result['warnings'])}):")
        for warning in result['warnings']:
            print(f"  - {warning['function']}: {warning['message']}")

    if not result['errors'] and not result['warnings']:
        print("\nNo Mac compatibility issues found.")


def main():
    """Main entry point for the validator."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate AutoLISP files for Mac compatibility'
    )
    parser.add_argument(
        'path',
        help='Path to an AutoLISP file or directory'
    )
    parser.add_argument(
        '--check-function',
        metavar='FUNC',
        help='Check a specific function for Mac compatibility'
    )
    parser.add_argument(
        '--docs-path',
        help='Path to AutoCAD documentation directory'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON'
    )

    args = parser.parse_args()

    validator = AutoLISPValidator(docs_path=args.docs_path)

    # Check a specific function
    if args.check_function:
        info = validator.check_function_in_docs(args.check_function)
        print(f"\nFunction: {info.name}")
        print(f"Compatibility: {info.compatibility.value}")
        print(f"Notes: {info.notes}")
        if info.alternative:
            print(f"Alternative: {info.alternative}")
        return 0

    # Validate a file or directory
    path = Path(args.path)

    if path.is_file():
        result = validator.validate_file(str(path))
        if args.json:
            import json
            print(json.dumps(result, indent=2))
        else:
            print_report(result, verbose=args.verbose)
        return 0 if result['compatible'] else 1

    elif path.is_dir():
        results = validator.validate_directory(str(path))

        if args.json:
            import json
            print(json.dumps(results, indent=2))
        else:
            compatible_count = sum(1 for r in results if r['compatible'])
            print(f"\nValidated {len(results)} AutoLISP files")
            print(f"Compatible: {compatible_count}")
            print(f"Incompatible: {len(results) - compatible_count}")

            if args.verbose:
                for result in results:
                    print_report(result, verbose=True)

            # Show summary of issues
            all_errors = {}
            for result in results:
                for error in result['errors']:
                    func = error['function']
                    all_errors[func] = all_errors.get(func, 0) + 1

            if all_errors:
                print("\nMost common incompatible functions:")
                for func, count in sorted(all_errors.items(), key=lambda x: -x[1]):
                    print(f"  - {func}: found in {count} file(s)")

        return 0 if all(r['compatible'] for r in results) else 1

    else:
        print(f"Error: Path not found: {args.path}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())

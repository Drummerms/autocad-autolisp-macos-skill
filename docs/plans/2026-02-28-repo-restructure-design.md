# Design: Repo Restructure to `autocad-autolisp-macos-skill`

**Date:** 2026-02-28

## Overview

Rename and restructure the `autocad-autolisp-macos` repository to `autocad-autolisp-macos-skill` with all content moved into a subfolder.

## Approach

Fresh start approach - create new structure without preserving git history.

## Target Structure

```
autocad-autolisp-macos-skill/
├── autocad-autolisp-macos-skill/    # All content moved here
│   ├── .claude/
│   ├── assets/
│   ├── docs/
│   ├── references/
│   ├── scripts/
│   ├── SKILL.md
│   ├── README.md
│   └── install.sh
└── .git/                             # Fresh git init
```

## Execution Steps

1. Create temp directory at `/tmp/autocad-autolisp-macos-skill`
2. Copy all content into subfolder structure
3. Initialize fresh git repo with single commit
4. Delete old remote repo `Drummerms/autocad-autolisp-macos` via GitHub API
5. Create new remote repo `Drummerms/autocad-autolisp-macos-skill` via GitHub API
6. Push to new remote
7. Update local workspace

## Success Criteria

- Old repo `Drummerms/autocad-autolisp-macos` is deleted
- New repo `Drummerms/autocad-autolisp-macos-skill` exists with all content in subfolder
- Fresh git history (single initial commit)

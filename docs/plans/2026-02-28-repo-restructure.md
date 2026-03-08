# Repo Restructure Implementation Plan

> **Status: COMPLETE** (2026-02-28). Repo renamed to `autocad-autolisp-macos-skill` and pushed to GitHub.

**Goal:** Rename repo to `autocad-autolisp-macos-skill`, move all content into a subfolder, and push to a new GitHub repository.

**Architecture:** Fresh start approach - create new directory structure, copy files, initialize fresh git repo, delete old remote, create new remote, push.

**Tech Stack:** Git, GitHub CLI/API, Bash

---

## Task 1: Create New Directory Structure

**Files:**
- Create: `/tmp/autocad-autolisp-macos-skill/`
- Create: `/tmp/autocad-autolisp-macos-skill/autocad-autolisp-macos-skill/`

**Step 1: Create temp directory with subfolder**

```bash
mkdir -p /tmp/autocad-autolisp-macos-skill/autocad-autolisp-macos-skill
```

**Step 2: Verify directory structure**

Run: `ls -la /tmp/autocad-autolisp-macos-skill/`
Expected: Directory contains `autocad-autolisp-macos-skill/` subfolder

---

## Task 2: Copy All Content to Subfolder

**Files:**
- Source: `/Users/michaelsablatura/Github/autocad-autolisp-macos/` (all files except .git)
- Destination: `/tmp/autocad-autolisp-macos-skill/autocad-autolisp-macos-skill/`

**Step 1: Copy all content except .git directory**

```bash
rsync -av --exclude='.git' /Users/michaelsablatura/Github/autocad-autolisp-macos/ /tmp/autocad-autolisp-macos-skill/autocad-autolisp-macos-skill/
```

**Step 2: Verify files copied correctly**

Run: `ls -la /tmp/autocad-autolisp-macos-skill/autocad-autolisp-macos-skill/`
Expected: See `docs/`, `scripts/`, `assets/`, `references/`, `.claude/`, `SKILL.md`, `README.md`, `install.sh`

**Step 3: Remove .DS_Store files (optional cleanup)**

```bash
find /tmp/autocad-autolisp-macos-skill -name '.DS_Store' -delete
```

---

## Task 3: Initialize Fresh Git Repository

**Files:**
- Initialize: `/tmp/autocad-autolisp-macos-skill/`

**Step 1: Initialize git repo**

```bash
cd /tmp/autocad-autolisp-macos-skill && git init
```

**Step 2: Stage all files**

```bash
git add .
```

**Step 3: Create initial commit**

```bash
git commit -m "Initial commit: AutoCAD AutoLISP Mac Compatibility Skill

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Step 4: Rename branch to main**

```bash
git branch -M main
```

**Step 5: Verify commit**

Run: `git log --oneline`
Expected: Single commit with message "Initial commit: AutoCAD AutoLISP Mac Compatibility Skill"

---

## Task 4: Delete Old Remote Repository

**Step 1: Delete old repo via GitHub MCP**

Use `mcp__plugin_github_github__delete_file` or GitHub web interface to delete `Drummerms/autocad-autolisp-macos`

Note: GitHub API doesn't support direct repo deletion. User must delete manually at:
`https://github.com/Drummerms/autocad-autolisp-macos/settings`

Scroll to bottom "Danger Zone" → "Delete this repository"

**Step 2: Confirm deletion**

User confirms repo is deleted before proceeding.

---

## Task 5: Create New Remote Repository

**Step 1: Create new repo via GitHub MCP**

Using `mcp__plugin_github_github__create_repository`:
- name: `autocad-autolisp-macos-skill`
- description: `AutoCAD AutoLISP Mac Compatibility Skill`
- private: false

**Step 2: Verify repo created**

Run: `gh repo view Drummerms/autocad-autolisp-macos-skill`
Expected: Repo details displayed

---

## Task 6: Push to New Remote

**Step 1: Add remote origin**

```bash
cd /tmp/autocad-autolisp-macos-skill && git remote add origin https://github.com/Drummerms/autocad-autolisp-macos-skill.git
```

**Step 2: Push to remote**

```bash
git push -u origin main
```

**Step 3: Verify push**

Run: `git remote -v`
Expected: origin points to `Drummerms/autocad-autolisp-macos-skill.git`

---

## Task 7: Update Local Workspace

**Step 1: Remove old local repo**

```bash
rm -rf /Users/michaelsablatura/Github/autocad-autolisp-macos
```

**Step 2: Move new repo to Github folder**

```bash
mv /tmp/autocad-autolisp-macos-skill /Users/michaelsablatura/Github/
```

**Step 3: Verify final structure**

Run: `ls -la /Users/michaelsablatura/Github/autocad-autolisp-macos-skill/`
Expected: `autocad-autolisp-macos-skill/` subfolder and `.git/`

---

## Success Verification

- [ ] Old repo `Drummerms/autocad-autolisp-macos` deleted from GitHub
- [ ] New repo `Drummerms/autocad-autolisp-macos-skill` exists on GitHub
- [ ] All content is inside `autocad-autolisp-macos-skill/` subfolder
- [ ] Fresh git history with single initial commit
- [ ] Local workspace updated at `/Users/michaelsablatura/Github/autocad-autolisp-macos-skill`

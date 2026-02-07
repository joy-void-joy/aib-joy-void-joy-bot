---
allowed-tools: Bash(git:*), Bash(uv run pyright), Bash(uv run ruff:*), Bash(uv run pytest:*), Read, Grep, Glob
description: Create a clean rebase branch with atomic commits and merge to main
---

# Rebase and Merge

Create a temporary rebase branch with a clean, logical commit history, then merge directly to main.

**Scope:** Only rebase changes since the branch diverged from the base branch (typically `main`). Do not touch commits that already exist on the base branch.

## Pre-rebase Validation

Before starting the rebase, ensure the branch is clean and passing all checks.

1. **Merge local settings into shared config**:
   Check if `.claude/settings.local.json` exists. If it does, review it and merge all sensible settings into `.claude/settings.json` — including permissions (allow/deny/ask rules), auto-accept patterns, and any other configuration that would benefit all contributors. Skip anything user-specific (e.g., personal paths, tokens). Commit the settings update as a separate commit.

2. **Merge main into feature branch**:
   ```bash
   # Fetch and merge main to get latest changes
   git fetch origin main
   git merge origin/main
   ```
   Resolve any merge conflicts before proceeding. This ensures the rebase branch will be up-to-date.

3. **Run all checks**:
   ```bash
   uv run pyright
   uv run ruff check .
   uv run ruff format --check .
   uv run pytest
   ```
   Fix any issues found. The rebase branch should only contain passing code.

4. **Commit remaining changes**:
   ```bash
   git status
   # Stage and commit any uncommitted work
   git add <files>
   git commit -m "fix: address pyright/ruff/test issues"
   ```
   All changes must be committed before rebasing. Don't leave uncommitted work.

---

## Process

1. **Sync main with remote**:
   ```bash
   git fetch origin main
   git checkout main && git merge --ff-only origin/main
   ```
   Ensure local main is up-to-date before creating the rebase branch.

2. **Gather context**:
   - Identify the current branch and its base (typically `main`)
   - Review the full diff from base to HEAD: `git diff main...HEAD`
   - List existing commits: `git log --oneline main..HEAD`

3. **Understand all changes**:
   - Read the changed files to understand the complete set of modifications
   - Think about what logical units of work exist (features, refactors, fixes, tests, docs)
   - **Ignore the existing commit history** — focus on what makes sense as a clean sequence

4. **Create rebase branch**:
   ```bash
   git checkout -b <branch>-rebase main
   ```

5. **Build clean commits**:
   - For each logical unit of work, cherry-pick or manually stage the relevant changes
   - Create atomic commits with clear messages
   - Order commits logically (dependencies first, then features, then polish)
   - Use conventional commit format: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`

6. **Merge to main**:
   ```bash
   git checkout main
   git merge --no-ff <branch>-rebase
   ```
   Use `--no-ff` to preserve the branch history as a merge commit.

7. **Push main and clean up**:
   ```bash
   git push origin main
   git branch -d <branch>-rebase
   ```

## Guidelines

- **Fresh perspective** — Don't feel bound by how commits were originally organized
- **Logical ordering** — Put foundational changes before features that depend on them
- **Atomic commits** — Each commit should compile/run independently if possible
- **Meaningful messages** — Commit messages should explain *what* and *why*

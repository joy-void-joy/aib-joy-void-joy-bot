---
allowed-tools: Bash(git:*), Bash(uv run pyright), Bash(uv run ruff:*), Bash(uv run pytest:*), Read, Grep, Glob
description: Create a clean rebase branch with atomic commits and merge to parent
---

# Rebase and Merge

Create a temporary rebase branch with a clean, logical commit history, then merge to the parent branch.

**Scope:** Only rebase changes since the branch diverged from the parent branch. The parent is determined by `git merge-base` — typically `main`, but may be another feature branch if the current branch was forked from one.

## Pre-rebase Validation

Before starting the rebase, ensure the branch is clean and passing all checks.

1. **Merge local settings into shared config**:
   Check if `.claude/settings.local.json` exists. If it does, review it and merge all sensible settings into `.claude/settings.json` — including permissions (allow/deny/ask rules), auto-accept patterns, and any other configuration that would benefit all contributors. Skip anything user-specific (e.g., personal paths, tokens). Commit the settings update as a separate commit.

2. **Merge parent into feature branch**:
   ```bash
   # Determine the parent branch (use git merge-base to find the fork point)
   git merge <parent-branch>
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

1. **Identify the parent branch**:
   ```bash
   # Find the fork point to determine the parent branch
   git merge-base HEAD main
   git merge-base HEAD <other-candidate>
   ```
   The parent is the branch whose merge-base is closest to HEAD (fewest commits between them). For worktrees forked from a feature branch, the parent is that feature branch, not main.

2. **Gather context**:
   - Identify the current branch and its parent
   - Review the full diff from parent to HEAD: `git diff <parent>..HEAD`
   - List existing commits: `git log --oneline <parent>..HEAD`

3. **Understand all changes**:
   - Read the changed files to understand the complete set of modifications
   - Think about what logical units of work exist (features, refactors, fixes, tests, docs)
   - **Ignore the existing commit history** — focus on what makes sense as a clean sequence

4. **Create rebase branch**:
   ```bash
   git checkout -b <branch>-rebase <parent-branch>
   ```

5. **Build clean commits**:
   - For each logical unit of work, cherry-pick or manually stage the relevant changes
   - Create atomic commits with clear messages
   - Order commits logically (dependencies first, then features, then polish)
   - Use conventional commit format: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`

6. **Merge to parent branch**:
   ```bash
   git checkout <parent-branch>
   git merge --no-ff <branch>-rebase
   ```
   Use `--no-ff` to preserve the branch history as a merge commit.

7. **Clean up**:
   ```bash
   git branch -d <branch>-rebase
   ```

## Guidelines

- **Fresh perspective** — Don't feel bound by how commits were originally organized
- **Logical ordering** — Put foundational changes before features that depend on them
- **Atomic commits** — Each commit should compile/run independently if possible
- **Meaningful messages** — Commit messages should explain *what* and *why*

---
allowed-tools: Bash(git:*), Bash(gh:*), Bash(uv run pyright), Bash(uv run ruff:*), Bash(uv run pytest:*), Read, Grep, Glob
description: Clean up commit history on the feature branch and open/update a PR
---

# Rebase and PR

Clean up the commit history on the current feature branch, push it, and open (or update) a PR.

**Scope:** Only rebase changes since the branch diverged from the base branch (typically `main`). Do not touch commits that already exist on the base branch.

## Pre-rebase Validation

Before starting the rebase, ensure the branch is clean and passing all checks.

1. **Merge local settings into shared config**:
   Check if `.claude/settings.local.json` exists. If it does, review it and merge all sensible settings into `.claude/settings.json` — including permissions (allow/deny/ask rules), auto-accept patterns, and any other configuration that would benefit all contributors. Skip anything user-specific (e.g., personal paths, tokens). Commit the settings update as a separate commit.

2. **Merge main into feature branch**:
   ```bash
   # Update local main worktree and merge into feature branch
   cd ../main
   git pull
   git push
   cd -
   git merge main
   ```
   Resolve any merge conflicts before proceeding. This ensures the branch is up-to-date.

3. **Run all checks**:
   ```bash
   uv run pyright
   uv run ruff check .
   uv run ruff format --check .
   uv run pytest
   ```
   Fix any issues found. The rebased branch should only contain passing code.

4. **Check AGENT_VERSION bump**:
   If the branch includes changes to agent behavior (prompts, tools, subagents, scoring logic), verify that `AGENT_VERSION` in `src/aib/version.py` has been bumped. This is required for regression tracking. Data-only or infrastructure changes do not need a version bump.

5. **Commit remaining changes**:
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
   cd ../main
   git pull
   git push
   cd -
   ```
   Ensure local main is up-to-date before rebasing.

2. **Push and open PR** (if not already open):

   Push the feature branch:
   ```bash
   git push -u origin <branch>
   ```

   Check if a PR already exists:
   ```bash
   gh pr list --head "<branch>" --state open --json number,url
   ```

   **If no PR exists** (first run):
   ```bash
   gh pr create --title "<conventional commit style title>" --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullet points describing the changes>
   EOF
   )"
   ```

   **If a PR already exists**, skip this step — we'll force-push the cleaned history later.

3. **Gather context**:
   - Identify the current branch and its base (typically `main`)
   - Review the full diff from base to HEAD: `git diff main...HEAD`
   - List existing commits: `git log --oneline main..HEAD`

4. **Understand all changes**:
   - Read the changed files to understand the complete set of modifications
   - Think about what logical units of work exist (features, refactors, fixes, tests, docs)
   - **Ignore the existing commit history** — focus on what makes sense as a clean sequence

5. **Reset and rebuild commits**:

   Reset all commits back to staged changes:
   ```bash
   git reset --soft main
   ```

   Now all changes are staged. For each logical unit of work:
   - Selectively unstage with `git reset HEAD <files>`, then stage and commit the relevant pieces
   - Or use `git commit` with specific files to build atomic commits
   - Order commits logically (dependencies first, then features, then polish)
   - Use conventional commit format: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`

6. **Force push to update the PR**:
   ```bash
   git push --force-with-lease
   ```

   Return the PR URL to the user when done. Include a commit list in the PR body:
   ```bash
   gh pr edit <PR_NUMBER> --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullet points describing the changes>

   ## Commits
   <list each commit with its message>
   EOF
   )"
   ```

## Guidelines

- **Fresh perspective** — Don't feel bound by how commits were originally organized
- **Logical ordering** — Put foundational changes before features that depend on them
- **Atomic commits** — Each commit should compile/run independently if possible
- **Meaningful messages** — Commit messages should explain *what* and *why*

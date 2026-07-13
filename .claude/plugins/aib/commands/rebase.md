---
allowed-tools: Bash(git:*), Bash(gh:*), Bash(uv run pyright), Bash(uv run ruff:*), Bash(uv run pytest:*), Read, Grep, Glob, AskUserQuestion
argument-hint: [target-branch]
description: Clean up commit history on the feature branch and open/update a PR
---

# Rebase and PR

Clean up the commit history on the current feature branch, push it, and open (or update) a PR.

## Determine Branches

### Base branch (`<base>`)

Auto-detect the base branch — the branch this feature branch diverged from. This is **not always `main`** — worktree branches are often forked from other feature branches.

**Detection strategy:**

1. List all local branches (excluding current) and count how many commits on HEAD are not reachable from each:
   ```bash
   git branch --format='%(refname:short)' | while read branch; do
     [ "$branch" = "$(git branch --show-current)" ] && continue
     count=$(git rev-list --count "$branch"..HEAD 2>/dev/null) || continue
     echo "$count $branch"
   done | sort -n | head -5
   ```

2. If one branch has a **strictly lower** count than all others, use it as `<base>`.

3. If **multiple branches tie** for the lowest count, the merge-base is shared and git cannot determine the true parent. **Use `AskUserQuestion`** to ask the user which branch is the parent, presenting the tied candidates as options.

### PR target (`<target>`)

If a target branch was provided as an argument, use it as the PR target. Otherwise, `<target>` defaults to `<base>`.

**Scope:** Only rebase changes since the branch diverged from `<base>`. Do not touch commits that already exist on `<base>`.

## Pre-rebase Validation

Before starting the rebase, ensure the branch is clean and passing all checks.

1. **Merge local settings into shared config**:
   Check if `.claude/settings.local.json` exists. If it does, review it and merge all sensible settings into `.claude/settings.json` — including permissions (allow/deny/ask rules), auto-accept patterns, and any other configuration that would benefit all contributors. Skip anything user-specific (e.g., personal paths, tokens). Commit the settings update as a separate commit.

2. **Merge `<base>` into feature branch**:
   ```bash
   # Update local <base> and merge into feature branch
   cd ../<base>
   git pull
   git push
   cd -
   git merge <base>
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

4. **Check AGENT_VERSION bump and CHANGELOG**:
   If the branch includes changes to agent behavior (prompts, tools, subagents, scoring logic), verify that `AGENT_VERSION` in `src/aib/version.py` has been bumped. This is required for regression tracking. Data-only or infrastructure changes do not need a version bump. **Every version bump must include a corresponding `CHANGELOG.md` entry** — use `uv run lup-devtools version bump` or manually add an entry following the existing format (one-line summary + bullet list of changes).

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

1. **Publish `<base>` before opening the PR** — this is load-bearing, not hygiene:
   ```bash
   git -C ../<base> pull
   git -C ../<base> push
   git fetch origin
   # Must print nothing. Anything here is a data commit the remote has never seen.
   git log --oneline origin/<base>..<base>
   ```
   The forecast loop commits `notes/` data straight to local `<base>`, so `<base>`
   drifts ahead of the remote. A branch cut from that `<base>` inherits those
   commits. If they are not on `origin/<base>` when the PR is opened, GitHub
   computes the merge base against the stale remote and folds every inherited
   data file into the merge — landing hundreds of `notes/` files in a code PR
   with no shared ancestry, which then collides add/add against the real commits
   on local `<base>` forever.

   **Do not open or update the PR until `git log origin/<base>..<base>` is empty.**
   The `pre-push` hook enforces this, but check it here so it fails early.

2. **Push and open PR** (if not already open):

   Push the feature branch:
   ```bash
   git push -u origin <branch>
   ```

   Check if a PR already exists:
   ```bash
   gh pr list --head "<branch>" --base "<target>" --state open --json number,url
   ```

   **If no PR exists** (first run):
   ```bash
   gh pr create --base "<target>" --title "<conventional commit style title>" --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullet points describing the changes>
   EOF
   )"
   ```

   **If a PR already exists**, skip this step — we'll force-push the cleaned history later.

3. **Gather context**:
   - Identify the current branch and confirm `<base>`
   - Review the full diff from base to HEAD: `git diff <base>...HEAD`
   - List existing commits: `git log --oneline <base>..HEAD`

4. **Understand all changes**:
   - Read the changed files to understand the complete set of modifications
   - Think about what logical units of work exist (features, refactors, fixes, tests, docs)
   - **Ignore the existing commit history** — focus on what makes sense as a clean sequence

5. **Reset and rebuild commits**:

   Reset all commits back to staged changes. Squash against the **fork point**,
   not the `<base>` ref — a stale ref silently pulls `<base>`'s own commits into
   the squash:
   ```bash
   git reset --soft "$(git merge-base HEAD origin/<base>)"
   ```

   Then confirm the staged diff is code only. If `notes/` appears here, `<base>`
   was not published in step 1 — stop and fix that first:
   ```bash
   git diff --cached --name-only -- notes/   # must print nothing
   ```

   Now all changes are staged. For each logical unit of work:
   - Selectively unstage with `git reset HEAD <files>`, then stage and commit the relevant pieces
   - Or use `git commit` with specific files to build atomic commits
   - Order commits logically (dependencies first, then features, then polish)
   - Use conventional commit format: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`

6. **Force push to update the PR**:
   ```bash
   git push --force
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

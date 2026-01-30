---
description: Complete TDD workflow - rebase, run checks, prepare for PR
allowed-tools: Bash(git:*, uv:*, pytest:*, rm:*), Read, Edit
---

Complete the TDD workflow and prepare for pull request.

## Steps

### 1. Deactivate TDD Mode

Remove the TDD mode flag file to allow normal test editing again:
```bash
rm -f .tdd-mode
```

### 2. Verify State

Check current branch and working tree status:
!`git branch --show-current`
!`git status --short`

If there are uncommitted changes, ask the user what to do before proceeding.

### 2. Run Quality Checks

Run all checks in sequence. If any fail, attempt auto-fix where possible:

**Type checking (pyright):**
```bash
uv run pyright
```
If pyright fails, analyze errors and fix them.

**Formatting (ruff):**
```bash
uv run ruff format .
```
This auto-fixes formatting issues.

**Linting (ruff check):**
```bash
uv run ruff check . --fix
```
Fix any remaining lint issues.

**Tests:**
```bash
uv run pytest
```
If tests fail, investigate and fix. Do NOT modify test expectations unless the user explicitly approves.

### 3. Interactive Rebase (if needed)

If there are multiple commits on this branch, offer to rebase into atomic commits:

1. Show commit history: `git log --oneline main..HEAD`
2. If more than one commit, suggest interactive rebase to squash/reorganize
3. Help craft meaningful commit messages that explain the "why"

### 4. Final Verification

After all fixes:
1. Re-run all checks to confirm they pass
2. Show final git status
3. Confirm ready for push/PR

### 5. Next Steps

Once everything passes, inform the user:
- Branch is ready to push: `git push -u origin <branch-name>`
- Or create PR directly: `gh pr create`

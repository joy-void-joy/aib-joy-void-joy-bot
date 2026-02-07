---
allowed-tools: Bash(git:*), AskUserQuestion
description: Clean up local branches deleted on remote and their worktrees
---

# Clean Gone Branches

Remove local branches marked as `[gone]` (deleted on remote) and their associated worktrees.

## Process

1. **Fetch and prune** remote tracking info:
   ```bash
   git fetch --prune
   ```

2. **List gone branches**:
   ```bash
   git branch -vv | grep ': gone]'
   ```

3. **Check for associated worktrees**:
   ```bash
   git worktree list
   ```
   Cross-reference gone branches with active worktrees.

4. **Confirm with user**: Use AskUserQuestion to show which branches (and worktrees) will be removed. Do not proceed without confirmation.

5. **Remove worktrees first** (if any):
   ```bash
   git worktree remove <path>
   ```

6. **Delete branches**:
   ```bash
   git branch -d <branch-name>
   ```
   Use `-d` (not `-D`) to prevent deleting unmerged work. If a branch fails to delete, report it to the user.

7. **Report results**: List what was cleaned up.

## Guidelines

- Never force-delete (`-D`) without explicit user approval
- Always confirm before deleting anything
- Skip the current branch if it's marked as gone — warn the user instead

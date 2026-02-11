---
allowed-tools: Bash(git:*), Bash(gh:*), AskUserQuestion
description: Review branches/worktrees and clean up merged ones
---

# Clean Merged Branches

Review all local branches and worktrees. Identify branches that are fully merged (into main or any other active branch) or have completed PRs. Present the merge graph and ask before deleting.

## Process

1. **Fetch and prune** remote tracking info:
   ```bash
   git fetch --prune
   ```

2. **Inventory** all local branches and worktrees:
   ```bash
   git branch -vv
   git worktree list
   ```

3. **Check containment** — for every pair of branches, check if one is an ancestor of another:
   ```bash
   git merge-base --is-ancestor <branch> <target>
   ```
   A branch is "consumed" if it's fully contained in main OR any other active branch (not just main).

4. **Check PR status** for branches that aren't ancestors of anything:
   ```bash
   gh pr list --state all --json number,title,headRefName,state,mergedAt
   ```
   A branch is also deletable if:
   - It has a merged PR (direct or via a `-rebase` suffix branch)
   - Its corresponding rebase branch's PR was merged (content reached main through rebased commits)

5. **Categorize** each branch:
   - **DELETE** — fully contained in another branch, or PR merged
   - **KEEP** — has unique commits not captured elsewhere, or has an open PR
   - **CURRENT** — the branch we're on (never delete, warn if it qualifies)

6. **Present the merge graph** showing:
   - Which branches are contained in which (use `⊂` notation)
   - PR status for each branch
   - Which have worktrees
   - Proposed action (DELETE/KEEP) with reason
   - Format as a table for DELETE candidates and a tree for the merge flow

7. **Confirm with user** via AskUserQuestion before deleting anything.

8. **Remove worktrees first** (if any):
   ```bash
   git worktree remove <path>
   ```

9. **Delete branches**:
   ```bash
   git branch -d <branch-name>
   ```
   Use `-d` (not `-D`). If `-d` fails (branch not recognized as merged due to rebase), report to user and ask if `-D` is acceptable.

10. **Delete remote branches** if they still exist:
    ```bash
    git push origin --delete <branch-name>
    ```

11. **Report results**: List what was cleaned up.

## Guidelines

- Never force-delete (`-D`) without explicit user approval for that specific branch
- Always confirm before deleting anything
- Skip the current branch — warn the user instead
- A branch merged into ANY other active branch counts as consumed (not just main)
- For rebased branches: the original feature branch content is in main via the rebase PR, even though `--is-ancestor` returns false (commits were rewritten)

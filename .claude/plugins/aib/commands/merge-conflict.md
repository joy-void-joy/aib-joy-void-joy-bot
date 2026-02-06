---
allowed-tools: Bash(git:*), Read, Grep, Glob, Edit, Write
description: Resolve merge conflicts after a failed merge attempt
argument-hint: [context about the merge and priorities]
---

# Resolve Merge Conflicts

Resolve all merge conflicts in the working tree after a failed merge or rebase.

**User-provided context:** $ARGUMENTS

## Process

1. **Assess the situation**:
   ```bash
   # Determine if we're in a merge, rebase, or cherry-pick
   git status

   # List all conflicted files
   git diff --name-only --diff-filter=U
   ```

2. **Understand the merge direction**:
   - Identify which branch is being merged into which
   - Check `git log --oneline -5 HEAD` and `git log --oneline -5 MERGE_HEAD` (or `REBASE_HEAD`) to understand both sides
   - Use the user-provided context above to understand priorities (e.g., "prefer our changes for X", "main has the correct version of Y")

3. **For each conflicted file**:
   - Read the full file to see all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   - Understand what each side changed and why by reading the surrounding code
   - Check `git log --oneline -5 -- <file>` on both sides to understand the history
   - Resolve the conflict by choosing the correct version or merging both changes
   - **Never blindly pick one side** — understand the intent of both changes
   - Remove all conflict markers after resolution

4. **Validate the resolution**:
   - Read each resolved file to confirm no remaining conflict markers
   - Ensure the resolved code is syntactically correct and logically sound
   - Check for duplicate imports, repeated function definitions, or other merge artifacts

5. **Stage and verify**:
   ```bash
   # Stage resolved files
   git add <resolved-files>

   # Verify no conflicts remain
   git diff --name-only --diff-filter=U

   # Show what will be committed
   git diff --cached --stat
   ```

6. **Complete the merge** (only if all conflicts are resolved):
   ```bash
   # For a merge:
   git commit --no-edit

   # For a rebase: git rebase --continue
   # For a cherry-pick: git cherry-pick --continue
   ```

## Resolution Guidelines

- **Understand intent over syntax** — A conflict between two different implementations of the same feature should be resolved by picking the better one or combining strengths, not by concatenating both
- **Preserve both additions** — When both sides add new, non-overlapping code (e.g., new functions, new imports), keep both
- **Favor the target branch for structure** — When both sides refactor the same code differently, prefer the structure of the branch being merged *into* unless the user's context says otherwise
- **Watch for semantic conflicts** — Even after resolving textual conflicts, check that the combined code makes sense (e.g., a renamed variable on one side but old name used on the other)
- **Check adjacent code** — Sometimes conflicts reveal that nearby (non-conflicting) code also needs updating for consistency

---
description: Start TDD workflow on a new feature branch using git worktree
argument-hint: <feature-name>
allowed-tools: Bash(git:*, touch:*, echo:*, cd:*, ls:*), Read, Write
---

Initialize a Test-Driven Development workflow for feature: $ARGUMENTS

## Steps

1. **Check current state**

Check current branch and existing worktrees:
!`git branch --show-current`
!`git worktree list`

2. **Create or switch to feature worktree**

The worktree should be at `../aib-feat-$ARGUMENTS` with branch `feat/$ARGUMENTS`.

**If worktree doesn't exist:**
```bash
git worktree add ../aib-feat-$ARGUMENTS -b feat/$ARGUMENTS
```

**If worktree already exists:**
Inform the user the worktree exists and they should `cd` to it:
```
cd ../aib-feat-$ARGUMENTS
```

**If already in the correct worktree:** Confirm and continue.

**Important:** After creating/switching to worktree, all subsequent commands must run in that directory.

3. **Activate TDD mode**

Create the TDD mode flag file to enable test file protection:
```bash
touch .tdd-mode
echo "Feature: $ARGUMENTS" > .tdd-mode
echo "Started: $(date)" >> .tdd-mode
```

This flag enables hard blocking of test file edits during the implementation phase.

4. **Create or update PLAN.md**

If PLAN.md doesn't exist, create it with this template:
```markdown
# Feature: $ARGUMENTS

## Goal
[What this feature accomplishes]

## Design
[High-level approach]

## Implementation Status
- [ ] Tests written
- [ ] Implementation complete
- [ ] Refactoring done
- [ ] Quality checks pass

## Notes
[Any important decisions or considerations]
```

If PLAN.md already exists, review it and confirm it's appropriate for this feature.

5. **Confirm ready state**

Verify the working tree is clean and we're on the correct branch.

## TDD Workflow Reminder

Now that you're set up, follow the red-green-refactor cycle:

1. **RED**: Write failing tests first that describe expected *behavior* (what outputs we expect), not implementation details
2. **GREEN**: Use the `implementer` agent to write code that passes tests (it cannot modify test files while TDD mode is active)
3. **REFACTOR**: Clean up code while keeping tests green

If tests need to change, the implementer agent will return a detailed report explaining why. You can then make the test changes yourself in the main conversation.

**Important**: Keep PLAN.md updated as you make progress. Before stopping or pushing, the system will verify PLAN.md reflects the current implementation.

When finished, use `/tdd:finish` to prepare for PR.

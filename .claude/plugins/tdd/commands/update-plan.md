---
description: Update PLAN.md to reflect current implementation status
allowed-tools: Read, Edit, Write, Glob, Grep, Bash(git:*)
argument-hint: [status update or section]
---

Update `PLAN.md` to reflect the current state of the feature implementation.

## Steps

1. **Check if PLAN.md exists**

If PLAN.md doesn't exist, create it with this template:
```markdown
# Feature: [Feature Name]

## Goal
[What this feature accomplishes]

## Design
[High-level approach and key decisions]

## Implementation Status
- [ ] Tests written
- [ ] Implementation complete
- [ ] Refactoring done
- [ ] Quality checks pass

## Files Changed
[List of files added or modified]

## Notes
[Important decisions, trade-offs, or considerations]
```

2. **Read current state**

If PLAN.md exists, read it:
@PLAN.md

Also check what's changed:
!`git diff --name-only main...HEAD 2>/dev/null || git diff --name-only HEAD~5...HEAD 2>/dev/null || echo "Unable to determine changes"`

3. **Determine what to update**

If `$ARGUMENTS` is provided, use that as the update context.

Otherwise, analyze:
- What tests have been added?
- What implementation work is done?
- What's still pending?
- Any blockers or decisions made?

4. **Update PLAN.md**

Update the relevant sections:

**Implementation Status:** Check off completed items, add new items if needed.

**Files Changed:** Update the list of modified files.

**Notes:** Add any important decisions, trade-offs, or blockers discovered.

**Design:** Update if the approach changed from the original plan.

5. **Show summary**

Display what was updated and the current status of the feature.

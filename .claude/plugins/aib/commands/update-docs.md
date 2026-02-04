---
allowed-tools: Read, Edit, Write, Glob, Grep
description: Update CLAUDE.md and/or PLAN.md with modifications
argument-hint: <instructions for what to add/change>
---

# Update Project Documentation

You are updating the project's core documentation files based on user instructions.

## Target Files
- `.claude/CLAUDE.md` - Project instructions for Claude Code
- `PLAN.md` - Implementation plan and task tracking

## Instructions from User
$ARGUMENTS

## Process

1. **Read current state**: Read both files to understand current content and organization
2. **Determine scope**: Based on the instructions, decide which file(s) need changes
   - CLAUDE.md: For coding standards, workflows, tool usage, project context
   - PLAN.md: For implementation tasks, phases, architecture decisions, status tracking
3. **Make modifications**: Apply the requested changes
4. **Refactor for coherence**: After making changes, review the modified file(s) to ensure:
   - Sections are logically ordered
   - No duplicate information
   - Consistent formatting and style
   - Information is in the appropriate file (not mixing concerns)
5. **Report changes**: Summarize what was modified

## Guidelines
- Keep CLAUDE.md focused on "how to work in this codebase"
- Keep PLAN.md focused on "what to build and current status"
- Maintain existing section structure where possible
- Use consistent markdown formatting
- Preserve any existing conventions (checkboxes, tables, etc.)

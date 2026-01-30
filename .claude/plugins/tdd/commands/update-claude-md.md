---
description: Update CLAUDE.md with learnings from this session
allowed-tools: Read, Edit, Write, Glob, Grep
argument-hint: [topic or section to update]
---

Update `.claude/CLAUDE.md` based on learnings from this session.

## Steps

1. **Read current CLAUDE.md**

Read the existing CLAUDE.md to understand its structure:
@.claude/CLAUDE.md

2. **Analyze session context**

Review what was learned or decided during this session that should be documented:
- New coding patterns or conventions discovered
- Commands or workflows that should be documented
- Dependencies or tools added
- Important architectural decisions
- Common pitfalls to avoid

3. **Determine what to update**

If `$ARGUMENTS` is provided, focus on that topic/section.

Otherwise, ask the user what aspect of CLAUDE.md needs updating:
- Project overview
- Commands section
- Code style & dependencies
- Git workflow
- New section

4. **Make the update**

Edit CLAUDE.md to add or modify the relevant section. Follow the existing format and style of the file.

**Guidelines:**
- Keep entries concise and actionable
- Use imperative voice ("Use X", "Run Y", not "You should use X")
- Include examples where helpful
- Don't duplicate existing content
- Maintain consistent formatting with rest of file

5. **Confirm the change**

Show the user what was changed and ask if it looks correct.

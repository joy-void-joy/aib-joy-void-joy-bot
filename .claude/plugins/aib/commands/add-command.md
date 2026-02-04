---
allowed-tools: Write, Read, Glob
description: Create a new slash command
argument-hint: <command-name> <description of what the command should do>
---

# Create New Slash Command

## Your Task

**IMPORTANT**: The user wants to CREATE a new slash command. They are NOT asking you to perform the action described—they want a command that will do it in the future.

**Arguments provided**: $ARGUMENTS

### How to Parse Arguments

The first word is the **command name**. Everything after is the **description of what the command should do**.

Example: `/add-command commit Please review all diffs and commit atomically`
- Command name: `commit`
- Description: "Please review all diffs and commit atomically"

### Steps

1. Parse the command name and description from the arguments
2. Design a command that accomplishes the described behavior
3. Write the command file to `.claude/commands/<command-name>.md` (project) or ask if they prefer `~/.claude/commands/` (personal)
4. Include appropriate `allowed-tools` in frontmatter based on what the command needs
5. Confirm the command was created and show how to use it

### If No Arguments Provided

If `$ARGUMENTS` is empty, ask the user:
- What should the command be called?
- What should it do?

---

# Reference: Command Syntax

Use the reference below to write well-structured commands.

## Command Locations
- **Personal**: `~/.claude/commands/` (available across all projects)
- **Project**: `.claude/commands/` (shared with team, shows "(project)")

## Basic Structure

```markdown
---
allowed-tools: Read, Edit, Write, Bash(git:*)
description: Brief description of what this command does
argument-hint: [required-arg] [optional-arg]
model: claude-3-5-sonnet-20241022
---

# Command Title

Your command instructions here.

Arguments: $ARGUMENTS

File reference: @path/to/file.js

Bash command output: (exclamation)git status(backticks)
```

## ⚠️ Security Restrictions

**Bash Commands (exclamation prefix)**: Limited to current working directory only.
- ✅ Works: `! + backtick + git status + backtick` (in project dir)
- ❌ Blocked: `! + backtick + ls /outside/project + backtick` (outside project)  
- ❌ Blocked: `! + backtick + pwd + backtick` (if referencing dirs outside project)

**File References (`@` prefix)**: No directory restrictions.
- ✅ Works: `@/path/to/system/file.md`
- ✅ Works: `@../other-project/file.js`

## Common Patterns

### Simple Command
```bash
echo "Review this code for bugs and suggest fixes" > ~/.claude/commands/review.md
```

### Command with Arguments
```markdown
Fix issue #$ARGUMENTS following our coding standards
```

### Command with File References
```markdown
Compare @src/old.js with @src/new.js and explain differences
```

### Command with Bash Output (Project Directory Only)
```markdown
---
allowed-tools: Bash(git:*)
---
Current status: (!)git status(`)
Current branch: (!)git branch --show-current(`)
Recent commits: (!)git log --oneline -5(`)

Create commit for these changes.
```

**Note**: Only works with commands in the current project directory.

### Namespaced Command
```bash
mkdir -p ~/.claude/commands/ai
echo "Ask GPT-5 about: $ARGUMENTS" > ~/.claude/commands/ai/gpt5.md
# Creates: /ai:gpt5
```

## Frontmatter Options
- `allowed-tools`: Tools this command can use
- `description`: Brief description (shows in /help)
- `argument-hint`: Help text for arguments
- `model`: Specific model to use

## Best Practices

### Safe Commands (No Security Issues)
```markdown
# System prompt editor (file reference only)  
(@)path/to/system/prompt.md

Edit your system prompt above.
```

### Project-Specific Commands (Bash OK)
```markdown
---
allowed-tools: Bash(git:*), Bash(npm:*)
---
Current git status: (!)git status(`)
Package info: (!)npm list --depth=0(`)

Review project state and suggest next steps.
```

### Cross-Directory File Access (Use @ not !)
```markdown
# Compare config files
Compare (@)path/to/system.md with (@)project/config.md

Show differences and suggest improvements.
```

## Usage
After creating: `/<command-name> [arguments]`

Example: `/review` or `/ai:gpt5 "explain this code"`

---
allowed-tools: Read, Edit, Write, Glob, Grep, AskUserQuestion, Task, Bash(mkdir:*, cp:*, mv:*, rm:*, find:*, ls:*)
description: Review and modify .claude structure, brainstorm improvements interactively
argument-hint: <problem or area to explore>
---

# Meta: .claude Structure Review & Improvement

You are reviewing the `.claude/` directory structure and brainstorming improvements with the user.

## User's Direction

$ARGUMENTS

## Your Task

Based on the user's input above, explore the relevant parts of `.claude/` and brainstorm solutions. The `.claude/` directory contains:

- `CLAUDE.md` - Project instructions and documentation
- `commands/` - Slash commands
- `settings.json` - Permissions and plugin configuration
- `plugins/aib/` - Main project plugin with all commands, scripts, and workflows

Read the relevant files based on what the user is asking about, then use AskUserQuestion to propose specific changes or additions.

## Consulting External Documentation

When the user's question involves Claude Code, Agent SDK, or the Claude API:

1. **Use the claude-code-guide subagent** via Task tool:
   ```
   Task(subagent_type="claude-code-guide", prompt="<specific question about SDK/API>")
   ```

2. **Fetch docs directly** for specific pages:
   - Agent SDK: `WebFetch(url="https://docs.claude.com/en/agent-sdk/<topic>")`
   - Claude Code: `WebFetch(url="https://docs.claude.com/en/claude-code/<topic>")`

When the user provides documentation links or references external docs, incorporate that knowledge into improvements to CLAUDE.md or this command.

## Reference: Plugin Structure

All project-specific commands and scripts live in `.claude/plugins/aib/`:

```
plugins/aib/
├── plugin.json           # Plugin metadata
├── commands/             # Slash commands (/aib:commit, /aib:feedback, etc.)
├── scripts/              # Python CLI tools
├── agents/               # Agent definitions
└── hooks/                # Git and workflow hooks
```

### When to Add to the Plugin

- **Commands**: Reusable workflows invoked via `/aib:command-name`
- **Scripts**: Python CLI tools run via `uv run python .claude/plugins/aib/scripts/X.py`
- **Agents**: Subagent definitions for specialized tasks

### Settings (`settings.json`)
- Permission allow/deny lists
- Plugin configuration
- Should prefer project-level over user-level

## Brainstorming Principles

- **Propose, don't assume**: Always use AskUserQuestion before making changes
- **Show context**: When proposing changes, show the relevant current state first
- **Group related changes**: Batch related improvements into single proposals
- **Explain rationale**: Every suggestion should include why it would help
- **Offer alternatives**: When there are multiple valid approaches, present options

## Command Evolution

**After every command invocation**, reflect on how it was actually used:

1. **Compare intent vs usage**: Did the user use the command as documented, or did they adapt it?
2. **Notice patterns**: If the user provides documentation, links, or redirects the command's focus, that's a signal the command should evolve.
3. **Proactively propose updates**: When you notice the command being used differently than documented:
   - Use AskUserQuestion to propose updating the command
   - Include the specific usage pattern you observed
   - Suggest concrete changes to the command file

**Examples of evolution signals:**
- User provides external docs → Add doc-fetching guidance to command
- User corrects your approach → Update command to prevent future errors
- User asks for something the command should have covered → Expand command scope
- User repeatedly ignores a section → Consider removing or simplifying it

## Process

1. Read relevant files based on the user's direction
2. Consult external docs if the question involves SDK/API/Claude Code
3. Analyze and identify potential improvements
4. Use AskUserQuestion to propose specific changes with rationale
5. Implement approved changes immediately
6. **Reflect on this command's execution** and propose updates to meta.md if warranted
7. Continue brainstorming or summarize changes made

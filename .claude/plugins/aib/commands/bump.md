---
allowed-tools: Bash(git:*), Bash(uv:*), Read, Grep, Glob, AskUserQuestion
description: Review changes since last bump and bump agent version
argument-hint: [patch|minor|major]
---

# Version Bump

Review changes since the last version bump and bump `AGENT_VERSION` accordingly.

## Input

**Bump level** (optional): $ARGUMENTS

If no level is provided, determine the appropriate level from the changes.

## Process

### 1. Gather context

Run these in parallel:

- Read `src/aib/version.py` to get the current version
- Run `git tag --list 'v*' --sort=-version:sort` to find the latest version tag
- Run `git log --oneline` (limited to last 50 commits) to see recent history

### 2. Find changes since last bump

Using the latest version tag (e.g., `v1.1.0`):

- Run `git log --oneline <tag>..HEAD` to see all commits since the last bump
- Run `git diff --stat <tag>..HEAD` to see which files changed

If no version tag exists, use the commit that last modified `src/aib/version.py`:
- `git log -1 --format=%H -- src/aib/version.py`

### 3. Classify changes

Read through the commits and categorize them:

- **Behavior changes** (require a bump): prompt changes, new/modified tools, scoring logic, subagent changes
- **Data changes** (no bump needed): forecast outputs, session notes, resolution updates
- **Infrastructure changes** (no bump needed): dependencies, CI, scripts, CLAUDE.md

If there are NO behavior changes since the last bump, inform the user and stop — no bump is needed.

### 4. Determine bump level

Apply the bump rules from `src/aib/version.py`:

| Level | When | Examples |
|-------|------|----------|
| **patch** | Bug fixes, config tweaks, tool fixes | Fixed API error handling, adjusted timeout |
| **minor** | Prompt changes, new tools, tool modifications | Added web search tool, rewrote system prompt |
| **major** | Architecture changes | New LLM, new framework, fundamental redesign |

If the user provided a level in `$ARGUMENTS`, use it. Otherwise, recommend a level based on the changes and confirm with `AskUserQuestion`.

### 5. Compose summary

Write a concise one-line summary of the behavioral changes. If there are multiple distinct changes, prepare `--detail` items (comma-separated).

### 6. Execute bump

```bash
uv run aib-devtools dev version-bump <level> "<summary>" [--detail "<a>, <b>, <c>"]
```

### 7. Verify and report

- Read the updated `src/aib/version.py` to confirm the new version
- Read the updated `CHANGELOG.md` to confirm the entry
- Show the user what was bumped and the changelog entry

## Guidelines

- **Only bump for behavior changes** — Data, docs, and infra commits don't warrant a bump
- **Summarize what changed for the agent**, not for the codebase — focus on how forecasting behavior differs
- **When in doubt, ask** — Use AskUserQuestion if the level is ambiguous
- **Don't tag yet** — This command bumps the version; tagging happens separately or during `/rebase`

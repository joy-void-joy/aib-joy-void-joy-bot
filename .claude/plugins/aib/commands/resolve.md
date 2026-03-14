---
allowed-tools: Bash(uv run aib-devtools:*), Read, Grep, Glob, AskUserQuestion, WebSearch, WebFetch
description: Attempt early resolution of unresolved forecasts using AI agents
argument-hint: [post_id1] [post_id2] [--dry-run]
---

# Resolve: Early Resolution Checker

Attempt to resolve unresolved forecasts by checking their resolution criteria against real-world data. Uses AI agents (via devtools) to search the web, fetch APIs, and check financial/government data.

## Process

### Phase 1: Survey unresolved forecasts

```bash
uv run aib-devtools resolution status
```

Review the count of unresolved forecasts. If the user provided specific post IDs via $ARGUMENTS, parse them. Otherwise, check what's available.

### Phase 2: Run the resolver

Based on user direction, run the resolver with appropriate flags:

```bash
# Dry run all unresolved (recommended first step)
uv run aib-devtools resolution resolve --dry-run

# Resolve specific posts
uv run aib-devtools resolution resolve 42115 42395 --dry-run

# Apply with custom confidence threshold
uv run aib-devtools resolution resolve --min-confidence 0.8
```

**Default workflow:**
1. Start with `--dry-run` to preview what would be resolved
2. Review the results with the user
3. If results look good, run without `--dry-run`

### Phase 3: Review results

After the resolver runs, review the output for:

- **Low confidence verdicts**: Questions where the agent wasn't sure. Use AskUserQuestion to ask the user whether to apply these.
- **Surprising resolutions**: If a verdict seems wrong based on the question context, flag it.
- **Missing resolutions**: Questions the agent couldn't resolve. Check if the resolution criteria reference data sources the agent doesn't have access to.

For any questionable results, investigate further:
- Fetch the question page to read full criteria
- Web search for the specific resolution event
- Check `uv run aib-devtools api post <post_id>` for API-level details

### Phase 4: Official resolution check

After applying tentative resolutions, run the official check to ensure authoritative resolutions override any tentative ones:

```bash
uv run aib-devtools resolution check
```

This scrapes the user's Metaculus profile page for resolutions and scores. Profile-sourced resolutions (source=scrape) always take precedence over tentative ones.

### Phase 5: Score update

If resolutions were applied, optionally update scores:

```bash
uv run aib-devtools scores show --resolved
```

## Resolution Source Priority

Resolutions are tracked with a `resolution_source` field:

| Source | Priority | Set by |
|--------|----------|--------|
| `scrape` | Highest | `resolution check` / `scores scrape` (from track record page) |
| `manual` | Medium | `resolution set` (human override) |
| `tentative` | Low | `resolution resolve` (AI agent check) |

Higher-priority sources always overwrite lower ones.

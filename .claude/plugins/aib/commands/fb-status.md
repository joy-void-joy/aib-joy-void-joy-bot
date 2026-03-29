---
allowed-tools: Bash(uv run aib-devtools:*), Read, Grep, Glob, AskUserQuestion
description: Feedback loop entry point — status, resolutions, and target selection
argument-hint: [post_id1 post_id2 ...] [--refresh]
---

# Status: Feedback Loop Entry Point

Get the current state of the forecasting system and select analysis targets. Resolution data comes first — it drives the rest of the session.

## Process

### 1. Sync resolutions

Always sync first (unless offline). This is the most important data source.

```bash
uv run aib-devtools resolution sync
```

### 2. Dashboard

```bash
uv run aib-devtools analysis dashboard
```

Shows: version, forecast counts, unanalyzed count, summary.json coverage, tool health flags, git status, last analysis file.

### 3. What resolved since last session?

Surface resolved forecasts with scores, annotated by version. Check both:
- Devtools: `uv run aib-devtools scores show --resolved`
- Direct: scan forecast JSON files for resolution values (devtools may have filtering bugs)

```bash
uv run aib-devtools calibration summary --version all
```

### 4. Previous session

Read the most recent analysis doc in `notes/feedback_loop/`:

```bash
ls -t notes/feedback_loop/*_analysis.md notes/feedback_loop/**/*_analysis.md 2>/dev/null | head -1
```

If it exists, read it. Note what was already fixed — don't re-investigate.

### 5. Select targets

If post IDs were provided via $ARGUMENTS, use those. Otherwise, prioritize:
1. Resolved forecasts not yet analyzed (highest value)
2. Recent forecasts with summary.json available
3. Forecasts flagged by the reviewer

```bash
uv run aib-devtools analysis status
```

### 6. Gate

Use AskUserQuestion to present:
- Resolution summary: how many resolved, by version, headline scores
- Dashboard summary
- Target post IDs with scores
- What was done last session

Options: "Proceed with these targets" / "Change target selection" / "Custom"

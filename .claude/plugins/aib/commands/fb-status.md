---
allowed-tools: Bash(uv run aib-devtools:*), Read, Grep, Glob, AskUserQuestion
description: Feedback loop entry point — status, targets, and previous session context
argument-hint: [post_id1 post_id2 ...] [--refresh]
---

# Status: Feedback Loop Entry Point

Get the current state of the forecasting system and select analysis targets.

## Process

### 1. Dashboard

```bash
uv run aib-devtools analysis dashboard
```

Shows: version, forecast counts, unanalyzed count, summary.json coverage, tool health flags, git status, last analysis file.

### 2. Previous session

Read the most recent `*_analysis.md` in `notes/feedback_loop/`:

```bash
ls -t notes/feedback_loop/*_analysis.md 2>/dev/null | head -1
```

If it exists, read it. Note what was already fixed — don't re-investigate.

### 3. Resolution sync (if --refresh or stale)

If $ARGUMENTS contains `--refresh`, or if the user requests it:

```bash
uv run aib-devtools resolution sync
uv run aib-devtools resolution tentative --all
```

### 4. Select targets

If post IDs were provided via $ARGUMENTS, use those. Otherwise, use unanalyzed forecasts:

```bash
uv run aib-devtools analysis status
```

### 5. Scores for targets

```bash
uv run aib-devtools scores show <target_ids> --no-refresh
```

### 6. Gate

Use AskUserQuestion to present:
- Dashboard summary
- Target post IDs with scores
- What was done last session

Options: "Proceed with these targets" / "Change target selection" / "Custom"

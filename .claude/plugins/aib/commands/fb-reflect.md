---
allowed-tools: Bash(uv run aib-devtools:*), Read, Grep, Glob, Edit, Write, AskUserQuestion
description: Meta and meta-meta reflection on the feedback loop process itself
---

# Reflect: Process Quality Assessment

Two levels of reflection: is the agent tracking enough data (meta), and is the feedback loop itself working (meta-meta)?

## Meta Level

### 1. Tracking data quality

```bash
uv run aib-devtools analysis tracking-gaps
```

Is the agent emitting enough data? Check coverage of: summary.json, reflection.yaml, tool_metrics, token_usage.

### 2. Summary.json schema review

Is the ForecastSummary schema capturing what we need? Are the tool assessments useful? Is anything consistently missing?

### 3. Actionable insight check

Did this session surface specific, actionable improvements? If findings are circular ("agent should be better at X" without a concrete tool/capability to build), the schema or reviewer prompt needs improvement.

## Meta-Meta Level

### 4. Prompt health

```bash
uv run aib-devtools analysis prompt-health
```

Is the forecasting prompt accumulating patches? Check line count and section count trends.

### 5. Subcommand assessment

Were the `/fb-*` subcommands helpful? Anything confusing, missing, or redundant? Update the subcommand files with learnings.

### 6. Devtools assessment

Any repetitive analysis that should be automated as a devtools command? Any fields missing from summary.json or reflection.yaml?

## Periodic (every 3rd session)

7. Reread all subcommand files (`/fb-status`, `/fb-investigate`, `/fb-analyze`, `/fb-reflect`, `/fb-implement`, `/fb-retrodict`)
8. Prompt health audit — read the full `src/aib/agent/prompts.py`
9. Clean up `notes/` — archive old files, ensure consistent naming
10. Sync learnings to CLAUDE.md

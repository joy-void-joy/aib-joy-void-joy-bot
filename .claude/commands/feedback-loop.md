---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, Task, WebSearch
description: Analyze resolved forecasts and improve agent based on calibration data
---

# Feedback Loop: Analyze and Improve

Collect resolved forecast data, analyze calibration, and improve the forecasting agent based on patterns in past performance.

## Step 1: Collect Feedback Data

Run the feedback collection script to gather metrics from resolved questions:

```bash
uv run python .claude/scripts/feedback_collect.py --all-time
```

This fetches resolved questions from Metaculus, matches them to our past forecasts, and computes:
- Brier scores and log scores for binary forecasts
- Calibration buckets (forecasted probability vs actual resolution rate)
- Per-question results

## Step 2: Read the Metrics

Read the latest metrics file from `notes/feedback_loop/`:
- Look at `notes/feedback_loop/last_run.json` to find the latest metrics file
- Read the full metrics JSON to understand performance patterns

Key things to look for:
- **Average Brier score**: Lower is better. 0.25 is random, 0 is perfect.
- **Calibration buckets**: Are we overconfident (resolution rate < forecasted probability) or underconfident?
- **Outliers**: Which specific forecasts had the worst scores?

## Step 3: Review Session Notes

Check `notes/sessions/` for meta-commentary from forecasting sessions:
- Research strategies that worked or failed
- Factors the agent emphasized or missed
- Edge cases or resolution criteria issues

## Step 4: Review Recent Code Changes

Run `git log --oneline -20 -- src/aib/` to see recent agent code changes.
Understand what has been tried and what the current state of the agent is.

## Step 5: Analyze Patterns

Based on the data, identify:

1. **Calibration issues**:
   - Overconfidence in high-probability forecasts?
   - Underconfidence in certain domains?
   - Systematic bias toward certain outcomes?

2. **Research gaps**:
   - Are certain question types performing worse?
   - Are we missing key information sources?
   - Are the research tools being used effectively?

3. **Prompt issues**:
   - Are the system prompts guiding toward the right behaviors?
   - Are the output formats capturing the right information?
   - Are subagent prompts well-calibrated?

## Step 6: Make Improvements

Based on your analysis, make targeted improvements to:

### Prompts (`src/aib/agent/prompts.py`)
- Adjust guidance for probability calibration
- Add domain-specific instructions based on weak areas
- Refine research depth guidance

### Subagents (`src/aib/agent/subagents.py`)
- Add new subagents for identified gaps
- Modify existing subagent prompts
- Adjust model selection (Haiku vs Sonnet)

### Tools (`src/aib/tools/`)
- Add new tools for missing capabilities
- Improve existing tool implementations
- Fix tools that are returning unhelpful results

### Models (`src/aib/agent/models.py`)
- Adjust output formats to capture better reasoning
- Add fields for tracking confidence or uncertainty

## Step 7: Document

After making changes:
1. Write a summary of findings to `notes/feedback_loop/<timestamp>_analysis.md`
2. Update PLAN.md if architectural changes were made
3. Commit changes with message format: `meta(feedback): <what was improved>`

## Guidelines

- **Be conservative**: Small, targeted changes are better than sweeping rewrites
- **Test changes**: If possible, re-run on a few questions to verify improvements
- **Document reasoning**: The analysis file should explain *why* changes were made
- **Track experiments**: Each feedback loop run is an experiment—keep notes

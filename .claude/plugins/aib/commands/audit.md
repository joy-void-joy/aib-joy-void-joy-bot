---
allowed-tools: Read, Grep, Glob, Bash(uv run lup-devtools:*, grep AGENT_VERSION:*, uv run python tmp/*.py), Write(tmp/*.py), Task, AskUserQuestion, WebSearch
description: Focused audit of specific forecasts — traces, reasoning, and version comparison
argument-hint: <post_id1> [post_id2] [...up to 10]
---

# Audit: Focused Forecast Feedback

Analyze specific forecasts in depth: trace reasoning and tool use quality, compare the generating version's scaffolding against current, and report what has been fixed, what has regressed, and what strengths to preserve.

## Input

**Post IDs**: $ARGUMENTS

Parse the space-separated post IDs (1-10). If none provided, use AskUserQuestion to ask which forecasts to audit.

## Phase 1: Discovery

Gather metadata for each post ID and group by version.

### 1a. Metadata collection

```bash
uv run lup-devtools analysis dashboard
```

For each post ID:
```bash
uv run lup-devtools trace show <post_id>
uv run lup-devtools scores show --post-id <post_id>
```

Extract: `agent_version`, question type, forecast value, score (if resolved).

### 1b. Current version

```bash
grep AGENT_VERSION src/aib/version.py
```

### 1c. Group by version

Build a version → post IDs mapping and report it before proceeding:
```
v2.0.0: [41906]
v3.0.0: [42233, 42122]
Current (v3.1.0): [42500]
```

### 1d. Missing traces

If any post IDs lack trace data, report and exclude them. If ALL lack traces, inform the user and stop.

## Phase 2: Resolution Investigation

For each **resolved** question, investigate the real-world outcome by looking at the actual data. Skip unresolved questions with a note.

### 2a. Fetch resolution details

```bash
# Update forecast JSONs with any new resolutions first
uv run lup-devtools resolution sync

# Then inspect the full API data for each resolved question
uv run lup-devtools api post <post_id>
```

Extract: resolution value, resolution criteria, close date, question text.

### 2b. Investigate the underlying data

Start from the data sources relevant to the question — the same kinds the agent used (Google Trends, stock prices, FRED, earnings reports, etc.) and anything else that helps. Use all available tools: WebSearch, data APIs, fetching pages, running analysis scripts. The goal is to build a first-hand understanding of what happened, not just read the resolution value.

Investigate:
- How did the underlying data evolve? What was the trajectory before, during, and after the forecast period?
- At what point did the outcome become clear from the data?
- Was the direction predictable from data available at forecast time, or was there a genuine surprise?

When investigation needs computation (trend analysis, CDF comparison, threshold checks), write and run a tmp script:
```bash
uv run python tmp/analyze_resolution.py
```

### 2c. Error classification

Classify each resolved forecast:

| Error Type | Description |
|---|---|
| **Wrong base rate** | Bad prior, missed relevant reference classes |
| **Missed key data** | A specific data source existed but wasn't found or used |
| **Stale data** | Used outdated information when fresher data was available |
| **Misunderstood scope** | Misinterpreted question criteria or resolution conditions |
| **Overconfident CDF** | Directionally correct but tails too narrow |
| **Underconfident CDF** | Directionally correct but distribution too diffuse |
| **Directionally wrong** | Forecast pointed the wrong way entirely |
| **Timing error** | Right prediction, wrong timeframe |
| **Good forecast** | Well-calibrated given available information |

### 2d. Counterfactual

For each error, ground the counterfactual in what the data investigation revealed:
- "The data showed [trajectory] — querying [source] at forecast time would have shown [signal]"
- "The trend was already [direction] by [date], but the agent used [stale/wrong data point]"
- "The outcome was a genuine surprise — [data] shifted after [event] on [date], post-forecast"
- "Narrower/wider CDF tails around [value] — the data supported a tighter/looser range"

Carry this into Phase 3 — the trace explorer needs it.

### Phase 2 Gate (MANDATORY)

Before launching subagents, use **AskUserQuestion** to present:

1. **Post-mortem table** (Post ID, Version, Type, Forecast, Resolution, Score, Error Type)
2. **For each resolved post**: 1-2 sentence summary of what happened and error classification
3. **Counterfactuals**: What data/tool would have prevented each error?

Options: "Proceed to trace analysis" / "Investigate [post] deeper first"

**Do NOT launch subagents until the user confirms.** The trace explorer needs this resolution context — rushing past it produces shallow analysis.

## Phase 3: Analysis

### 3a. Read summary.json files

For each post ID, find and read the summary.json from the session directory. Extract:
- `tool_audit.by_tool` — per-tool qualitative assessment
- `tool_audit.capability_gaps` and `subtle_bugs`
- `reasoning` — evidence quality, logical coherence, calibration sense
- `workflow` — info gathering, structured reasoning, self-correction, efficiency
- `future_leak` — for retrodict traces
- `notable_observations` and `actionable_improvements`

Cross-reference with Phase 2 resolution investigation — where does the summary align or disagree with what actually happened?

If summary.json is missing for any post, note it. If needed for deeper investigation, use `uv run lup-devtools trace log <post_id>`.

### 3b. Version Explorer

**Skip if all forecasts are from the current version.** Note this in the report — the audit becomes a trace analysis without version comparison.

Otherwise:

```
Task(subagent_type="aib-workflow:version-explorer", prompt="""
Compare these versions against HEAD:
[For each unique version != current: "v[X] vs HEAD"]

Focus on:
- src/aib/agent/prompts.py (most important)
- src/aib/agent/core.py
- src/aib/agent/tool_policy.py
- src/aib/agent/numeric.py
- src/aib/agent/hooks.py

For each comparison, return:
1. Prompt changes (grouped by theme)
2. Tool policy changes (added/removed/modified)
3. Orchestration changes (agent flow, subagent usage)
4. Impact: what would the current version do differently on the same question?
""")
```

## Phase 4: Synthesis

Cross-reference trace findings with version diffs and resolution investigation. This is the audit's unique value.

### 4a. Map issues to version changes

For each issue found in summary.json or trace analysis:

1. Check the version diff — is the cause in scaffolding that changed?
2. Classify:
   - **Fixed**: Issue existed in v[old], diff shows it was addressed
   - **Unaddressed**: Issue existed in v[old], no relevant change in current
   - **Current-version issue**: Forecast from current version, no diff to check

### 4b. Map strengths to version changes

For each strength found in summary.json or trace analysis:

1. Check the version diff — is the enabling scaffolding still present?
2. Classify:
   - **Preserved**: Scaffolding intact in current
   - **At risk**: Scaffolding modified — verify relevant parts survived
   - **Lost**: Scaffolding removed or substantially rewritten

### 4c. Recommendations

For each unaddressed issue, formulate an actionable recommendation following the Bitter Lesson:
- Prefer tools/capabilities over prompt patches
- Prefer general principles over specific rules
- Be specific: "build a tool that provides X" not "add a prompt rule about Y"

### Phase 4 Gate (MANDATORY)

Before writing the final report, use **AskUserQuestion** to present:

1. **Fixed issues** — with diff citations (not just descriptions)
2. **Unaddressed issues** — with Bitter Lesson recommendations
3. **Strengths at risk** — scaffolding that may have been removed
4. **Recommended actions** — prioritized

Options: "Write the report" / "Investigate [issue] further" / "Adjust recommendations"

**Do NOT write the report until the user confirms.** The synthesis is the audit's unique value — if "What Has Been Fixed" or "Strengths to Preserve" sections are empty, the cross-referencing wasn't done.

## Phase 5: Report

```markdown
# Audit Report: [N] Forecasts Across [M] Versions

**Post IDs**: [list]
**Versions**: [version (count)] for each
**Current version**: [X.Y.Z]
**Date**: [today]

## Per-Question Overview

| Post ID | Version | Type | Forecast | Resolution | Score | Error Type |
|---------|---------|------|----------|------------|-------|------------|

## Post-Mortem (Resolved Questions)

### Post [ID]: [question title]
- **Forecast**: [prediction]
- **Resolution**: [actual outcome]
- **Error type**: [classification]
- **What happened**: [1-2 sentences — what data/event determined the resolution]
- **Where reasoning diverged**: [specific trace point, or "N/A — good forecast"]
- **What would have helped**: [concrete tool, data source, or reasoning direction]

## What Has Been Fixed

- **[Issue]**: [description]
  - Seen in: post [ID] (v[X.Y.Z])
  - Fixed by: [specific change — cite the diff]

## What Remains Unaddressed

- **[Issue]**: [description]
  - Seen in: post [IDs] (v[X.Y.Z])
  - Recommendation: [capability/tool — Bitter Lesson style]

## Strengths to Preserve

- **[Strength]**: [description with agent quotes]
  - Seen in: post [IDs]
  - Status in current: [preserved / at risk / lost — cite diff]

## Version Delta Summary

### v[X.Y.Z] → v[current] ([N] forecasts)
[Compact: prompt changes, tool changes, scaffolding changes]

## Recommended Actions

1. **[Action]** — type: [tool/capability/principle] — evidence: [N/M traces]
```

## Guidelines

- **Cross-reference is the whole point.** Connecting trace findings to version diffs is what makes this valuable — without it, use `/review` instead.
- **Quote both sides.** Cite trace evidence AND version diff evidence for each finding.
- **Strengths matter as much as weaknesses.** Confirming what works prevents regressions.
- **Be honest about coverage.** If all forecasts are current-version, say so — the audit becomes a trace analysis without version comparison.
- **Mark analyzed.** After the report: `uv run lup-devtools analysis mark <post_ids>`

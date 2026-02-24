---
allowed-tools: Read, Grep, Glob, Bash(uv run aib-devtools:*, grep AGENT_VERSION:*), Task, AskUserQuestion
description: Focused audit of specific forecasts — traces, reasoning, and version comparison
argument-hint: <post_id1> [post_id2] [...up to 10]
---

# Audit: Focused Forecast Feedback

Analyze specific forecasts in depth: trace reasoning and tool use quality, compare the generating version's scaffolding against current, and report what has been fixed, what has regressed, and what strengths to preserve.

## Input

**Post IDs**: $ARGUMENTS

Parse the space-separated post IDs. Expect 1-10 IDs. If none provided, use AskUserQuestion to ask the user which forecasts to audit.

## Phase 1: Discovery

Gather metadata for each post ID and group by version.

### 1a. Metadata collection

For each post ID, run:
```bash
uv run aib-devtools trace show <post_id>
uv run aib-devtools scores show --post-id <post_id>
```

Extract from each: `agent_version`, question type, forecast value, score (if resolved).

### 1b. Current version

```bash
grep AGENT_VERSION src/aib/version.py
```

### 1c. Group by version

Build a version → post IDs mapping. Example:
```
v2.0.0: [41906]
v3.0.0: [42233, 42122]
Current (v3.1.0): [42500]
```

Report this grouping before proceeding.

### 1d. Missing traces

If any post IDs have no trace data, report them and exclude from analysis. If ALL post IDs lack traces, inform the user and stop.

## Phase 2: Parallel Subagent Analysis

Launch both subagents simultaneously — they are independent.

### 2a. Trace Explorer

Launch the trace-explorer to read all traces in its own context:

```
Task(subagent_type="aib-workflow:trace-explorer", prompt="""
Analyze traces for these post IDs: [list all IDs with traces]

Context:
- Version grouping: [from Phase 1c]
- Current agent version: [from Phase 1b]
- Score data: [any scores from Phase 1a]

Focus areas:
- Reasoning quality per forecast — what went WELL and what went POORLY
- Tool use patterns and failures
- Capability requests from meta-reflections
- For each forecast: the 1-2 most notable observations (strength or weakness)

Return the standard pattern report.
""")
```

### 2b. Version Explorer

**Skip entirely if all forecasts are from the current version.** Note in the report that no version comparison is possible.

Otherwise, launch the version-explorer to diff each historical version against HEAD:

```
Task(subagent_type="aib-workflow:version-explorer", prompt="""
Compare these versions against HEAD:
[For each unique version V where V != current]
- v[V] vs HEAD

Focus on the key scaffolding files:
- src/aib/agent/prompts.py (most important — the system prompt)
- src/aib/agent/core.py (orchestration)
- src/aib/agent/tool_policy.py (tool availability)
- src/aib/agent/numeric.py (CDF generation)
- src/aib/agent/hooks.py (agent hooks)

For each version comparison, return:
1. Prompt changes (grouped by theme, not line-by-line)
2. Tool policy changes (tools added/removed/modified)
3. Orchestration changes (agent flow, subagent usage)
4. Impact assessment: what would the current version do differently on the same question?
""")
```

## Phase 3: Synthesis

Cross-reference trace findings with version diffs. This is the unique value of the audit.

### 3a. Map issues to version changes

For each issue the trace-explorer identified:

1. **Check the version diff**: Is the issue caused by scaffolding that changed between the forecast's version and current?
2. **Classify**:
   - **Fixed**: The issue existed in v[old] and the diff shows it was addressed
   - **Unaddressed**: The issue existed in v[old] and no relevant change in current
   - **Current-version issue**: The forecast was made with the current version — no diff to check

### 3b. Map strengths to version changes

For each strength the trace-explorer identified:

1. **Check the version diff**: Is the scaffolding that enabled this strength still present?
2. **Classify**:
   - **Preserved**: The strength-enabling scaffolding is intact in current
   - **At risk**: The scaffolding was modified — verify the relevant parts survived
   - **Lost**: The scaffolding was removed or substantially rewritten

### 3c. Generate recommendations

For each unaddressed issue, formulate an actionable recommendation following the Bitter Lesson:
- Prefer tools/capabilities over prompt patches
- Prefer general principles over specific rules
- Be specific: "build a tool that provides X" not "add a prompt rule about Y"

## Phase 4: Report

### Report structure

```markdown
# Audit Report: [N] Forecasts Across [M] Versions

**Post IDs**: [list]
**Versions**: [version (count)] for each
**Current version**: [X.Y.Z]
**Date**: [today]

## Per-Question Overview

| Post ID | Version | Type | Forecast | Score | Key Finding |
|---------|---------|------|----------|-------|-------------|

## What Has Been Fixed

Issues from historical traces resolved in the current version.

- **[Issue]**: [description from trace]
  - Seen in: post [ID] (v[X.Y.Z])
  - Fixed by: [specific scaffolding change — cite the diff]

## What Remains Unaddressed

Issues from traces that persist in the current version.

- **[Issue]**: [description from trace]
  - Seen in: post [IDs] (v[X.Y.Z])
  - Current status: [still present / never addressed]
  - Recommendation: [capability/tool — Bitter Lesson style]

## Strengths to Preserve

Things the agent did well that should be maintained.

- **[Strength]**: [description with agent quotes]
  - Seen in: post [IDs]
  - Preserved in current: [yes / partially / no — cite the diff]

## Version Delta Summary

### v[X.Y.Z] → v[current] ([N] forecasts from this version)
[Compact summary: prompt changes, tool changes, scaffolding changes]

## Recommended Actions

1. **[Action]** — type: [tool/capability/principle] — evidence: [N/M traces]
2. ...
```

## Guidelines

- **Cross-reference is the whole point.** Connecting "the agent struggled with X" to "the current version does/doesn't address this" is what makes this command valuable.
- **Quote both sides.** Cite trace evidence AND version diff evidence for each finding.
- **Strengths matter as much as weaknesses.** Confirming what works prevents regressions during future rewrites.
- **Bitter Lesson recommendations.** Capabilities and tools over prompt patches. General principles over specific rules.
- **Be honest about coverage.** If all forecasts are from the current version, say so — the audit becomes a focused trace analysis without version comparison.

---
allowed-tools: Bash(uv run lup-devtools:*), Read, Grep, Glob, AskUserQuestion
description: Aggregate tool health, capability gaps, and reasoning patterns — version-annotated
---

# Analyze: Tool Health & Capability Gaps

Aggregate findings from summary.json files and tool_metrics. Cross-reference with investigation findings — did tool failures cause forecast errors?

## Process

### 1. Tool health

```bash
uv run lup-devtools analysis tool-health
```

Shows per-tool call counts, error rates, and qualitative assessments. Flags tools above 10% error rate.

When interpreting error rates, note which versions contribute the errors. A high all-time rate may be fixed in the current version.

### 2. Capability gaps

```bash
uv run lup-devtools analysis tool-needs
```

Aggregates `capability_gaps` from all summary.json files, grouped by frequency. Cluster related gaps into themes (e.g., "options/volatility data" appears under many names).

### 3. Cross-reference with investigation

This is the key step. For each tool health flag or capability gap:
- Did this cause an actual forecast error in a resolved forecast?
- Or is it just friction that the agent worked around?

Tool failures that didn't affect outcomes are low priority. Tool failures that caused wrong forecasts are high priority.

### 4. Trace quality (sample)

If no traces were read during investigation, sample 2-3 recent traces:

```bash
uv run lup-devtools trace log <post_id>
```

Assess: reasoning quality, tool usage patterns, CDF construction, reflection effectiveness.

### 5. Version comparison (if relevant)

If comparing across versions:

```bash
uv run lup-devtools analysis version-diff <v1> <v2>
```

For code-level diffs, launch the version-explorer subagent.

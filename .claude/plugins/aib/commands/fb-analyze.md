---
allowed-tools: Bash(uv run aib-devtools:*), Read, Grep, Glob, AskUserQuestion
description: Aggregate tool health, capability gaps, and reasoning patterns from summary.json
---

# Analyze: Tool Health & Capability Gaps

Aggregate findings from summary.json files to identify systemic patterns.

## Process

### 1. Tool health

```bash
uv run aib-devtools analysis tool-health
```

Shows per-tool call counts, error rates, and qualitative assessments. Flags tools above 10% error rate.

### 2. Capability gaps

```bash
uv run aib-devtools analysis tool-needs
```

Aggregates `capability_gaps` from all summary.json files, grouped by frequency.

### 3. Summarize

From tool-health and tool-needs output:
- Which tools consistently fail? What's the root cause?
- What does the agent need but doesn't have?
- Are there reasoning quality patterns across summaries?

### 4. Version comparison (if relevant)

If comparing across versions:

```bash
uv run aib-devtools analysis version-diff <v1> <v2>
```

For code-level diffs, launch the version-explorer subagent.

### 5. Flag traces for manual reading

If summary.json data raises questions about specific forecasts, note 1-2 traces worth reading in full:

```bash
uv run aib-devtools trace log <post_id>
```

Only read traces with a specific question in mind — don't browse.

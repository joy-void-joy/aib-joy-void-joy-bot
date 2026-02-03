---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, Task, WebSearch
description: Analyze forecasts and improve agent based on calibration and process quality
---

# Feedback Loop: Analyze, Diagnose, and Fix

This command has three phases:
1. **Analyze** - Collect data and identify patterns
2. **Diagnose** - Understand root causes
3. **Fix** - Implement changes to prompts, tools, or architecture

**Important**: This command should result in CODE CHANGES, not just analysis documents. If you identify problems, fix them.

## Phase 1: Collect Data

### 1a. Run Feedback Collection

```bash
uv run python .claude/scripts/feedback_collect.py --all-time
```

This fetches:
- Resolved questions with Brier scores (if any)
- Community prediction comparisons for all forecasts
- Missed questions (resolved without our forecast)

### 1b. Inventory Available Data

```bash
# Count forecasts and meta-reflections
ls notes/forecasts/ | wc -l
ls notes/meta/ | wc -l

# Check latest feedback metrics
cat notes/feedback_loop/last_run.json 2>/dev/null || echo "No previous run"

# Check previous analyses
ls -la notes/feedback_loop/*.md 2>/dev/null | tail -5
```

## Phase 2: Analyze Patterns

### 2a. Community Prediction Divergence (Critical)

**Note**: CP comparison is only available to the feedback loop AFTER forecasts are made. The forecasting agent cannot see community predictions during forecasting (this is an AIB tournament rule). CP comparison is a post-hoc analysis tool.

CP comparison is your most valuable early signal for calibration. Look at the metrics file for:

**Average divergence**:
- Positive = we forecast higher than CP (potential overconfidence)
- Negative = we forecast lower than CP (potential underconfidence)
- >±5% average is a systematic bias signal

**Large divergences (>15pp)**:
For EACH large divergence, read the meta-reflection and answer:
1. What type of question is this? (predictive/definitional/meta/measurement)
2. What's our reasoning for the divergence?
3. Is our reasoning sound, or are we misinterpreting something?

**Divergence patterns by question type**:
| Question Type | Large Divergence Indicates |
|--------------|---------------------------|
| Predictive | Possible overconfidence or information edge |
| Definitional | Likely criteria interpretation difference (RED FLAG) |
| Meta-prediction | May be acceptable (we model CP behavior differently) |
| Measurement | Different data sources or volatility estimates |

**DEFINITIONAL DIVERGENCE IS A RED FLAG**: If we have >20pp divergence on a definitional question ("has X happened?"), we're probably misinterpreting resolution criteria. Investigate thoroughly.

### 2b. Meta-Reflection Patterns

Read 5-10 meta-reflections from `notes/meta/`:

```bash
ls -la notes/meta/ | tail -15
```

Track these specific patterns:

**Subagent Usage** (should be non-zero):
```bash
grep -l "spawn\|subagent" notes/meta/*.md | wc -l
grep -h "Subagent" notes/meta/*.md | head -20
```

If subagent usage is zero/low despite many forecasts:
- The prompts say subagents are MANDATORY for certain question types
- If agents are still not using them, the prompt enforcement is too weak
- Consider adding validation or stronger language

**Tool Failures**:
```bash
grep -h "failed\|error\|didn't work" notes/meta/*.md | head -20
```

**Self-Critique Quality**:
- Are "strongest argument against" sections substantive?
- Are numeric 80% CIs provided?

### 2c. Reasoning Traces (if available)

Full traces in `notes/logs/` show actual tool usage vs. claimed usage:

```bash
ls -la notes/logs/ | tail -10
```

Compare what the trace shows vs. what meta-reflection claims.

### 2d. Calibration (if resolved forecasts available)

Read the metrics file:
```bash
cat notes/feedback_loop/*_metrics.json | jq '.' | tail -50
```

Look for:
- **Average Brier score**: <0.15 good, >0.25 poor
- **Calibration buckets**: Are 70% forecasts resolving at ~70%?
- **Worst performers**: Which forecasts scored worst? Read their meta-reflections.

## Phase 3: Diagnose Root Causes

For each pattern identified, determine the root cause:

| Symptom | Possible Causes |
|---------|-----------------|
| High CP divergence (positive) | Overconfidence, "Nothing Ever Happens" not applied, definitional misinterpretation |
| High CP divergence (negative) | Underconfidence, excessive "Nothing Ever Happens" |
| Zero subagent usage | Prompt too advisory, perceived overhead, time pressure |
| Tool failures | API issues, missing keys, JavaScript rendering |
| Formulaic meta-reflections | Template too long, not enforced, low value perceived |

**Ask**: "If I changed X, would the agent behave differently?"

## Phase 4: Implement Fixes

**This is the most important phase.** Don't just document problems - fix them.

### Priority Order

1. **Prompt changes** (`src/aib/agent/prompts.py`) - Highest leverage, immediate effect
2. **Subagent changes** (`src/aib/agent/subagents.py`) - Medium leverage
3. **Tool changes** (`src/aib/tools/`) - High effort but sometimes necessary
4. **Meta-reflection template** - Affects future feedback loops

### Making Prompt Changes

Common prompt fixes:

| Problem | Fix Location | Change |
|---------|-------------|--------|
| Calibration bias | "Nothing Ever Happens" section | Adjust logit recommendations |
| Missing question type guidance | Add new section | Google Trends, meta-predictions, etc. |
| Subagent underuse | "When to Use Subagents" | Make MANDATORY for certain types |
| CP divergence ignored | Add "Large Divergence Warning" | Require investigation when >20pp |
| Definitional misinterpretation | Add dedicated section | Criteria parsing guidance |

After making changes:
```bash
# Verify syntax
uv run pyright src/aib/agent/prompts.py

# Review the change
git diff src/aib/agent/prompts.py
```

### Making Tool Changes

If a tool consistently fails:
1. Check if it's an API key issue (`.env.local`)
2. Check if it's a library issue (update via `uv add`)
3. If structural, modify `src/aib/tools/`

### Commit Strategy

Make atomic commits:
```bash
git add <specific-files>
git commit -m "meta(feedback): <what changed and why>"
```

**One logical change per commit** so we can track what helped.

## Phase 5: Document

Write analysis to `notes/feedback_loop/<timestamp>_analysis.md`:

```markdown
# Feedback Loop Analysis: YYYY-MM-DD

## Data Summary
- Forecasts analyzed: N
- Resolved forecasts: N
- Brier score: X.XX (if available)
- CP comparisons: N
- Average CP divergence: +/-X.X%

## CP Divergence Analysis
[For each large divergence, explain what it means]

## Patterns Identified
1. [Pattern] → [Root cause] → [Fix made]

## Changes Made
1. [File]: [Change] - [Rationale]

## Validation Plan
- [How will we know if fixes worked?]

## Next Steps
- [What to monitor]
```

Commit with: `meta(feedback): <brief summary of improvements>`

## Quick Reference: Diagnosis Guide

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| +ve CP divergence on definitional Qs | Criteria misinterpretation | Add definitional question guidance |
| +ve CP divergence on predictive Qs | Overconfidence | Strengthen "Nothing Ever Happens" |
| Zero subagent usage | Guidance too advisory | Make spawning MANDATORY for certain types |
| "Tool X failed" repeated | API/config issue | Fix tool or add fallback |
| Formulaic meta-reflections | Template fatigue | Simplify, focus on specifics |
| Missing 80% CIs | Not enforced | Add validation or stronger prompt language |

## Example Workflow

```bash
# 1. Collect data
uv run python .claude/scripts/feedback_collect.py --all-time

# 2. Read metrics
cat notes/feedback_loop/*_metrics.json | tail -1

# 3. Note large divergences, read their meta-reflections
# (Divergence >15pp needs investigation)

# 4. Identify pattern (e.g., "definitional questions have high divergence")

# 5. Make fix (e.g., add definitional question guidance to prompts.py)
# Edit src/aib/agent/prompts.py

# 6. Verify
uv run pyright src/aib/agent/prompts.py

# 7. Commit
git add src/aib/agent/prompts.py
git commit -m "meta(feedback): add definitional question criteria parsing guidance"

# 8. Document
# Write notes/feedback_loop/<timestamp>_analysis.md

# 9. Commit analysis
git add notes/feedback_loop/
git commit -m "meta(feedback): document analysis and changes"
```

## Guidelines

- **CP divergence is your best early signal** - Use it before resolutions
- **Definitional divergence is a red flag** - Usually means criteria misinterpretation
- **Fix problems, don't just document them** - This command should result in code changes
- **One fix per commit** - Track what helped
- **Subagents should be used** - Zero usage means the guidance isn't working

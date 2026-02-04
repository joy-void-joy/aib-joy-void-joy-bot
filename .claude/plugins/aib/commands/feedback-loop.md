---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, Task, WebSearch, AskUserQuestion
description: Analyze forecasts and improve agent based on calibration and process quality
---

# Feedback Loop: Three Levels of Analysis

The feedback loop operates at three levels. Spend real time on each:

1. **Object Level** - Improve tools, capabilities, data access
2. **Meta Level** - Improve the agent's self-assessment and tracking
3. **Meta-Meta Level** - Improve this feedback loop process itself

## Critical Constraint: What the Agent Can and Cannot See

**IMPORTANT**: The forecasting agent operates in the AIB tournament where:

- **Agent CAN see**: Prediction market prices (Polymarket, Manifold), underlying question CP (for meta-questions), news, APIs
- **Agent CANNOT see**: The CP of the question it is currently forecasting

This means:
- For meta-questions like "Will CP of Q be above X%?", the agent CAN see Q's current CP
- But the agent CANNOT see the meta-question's own CP

**Implication for feedback loop**: You can use CP divergence for post-hoc analysis to understand WHERE our reasoning differs from the crowd. But you CANNOT tell the agent to "adjust based on CP divergence" because it can't see that data during forecasting.

## Guiding Principle: The Bitter Lesson

Give the agent MORE capabilities and tools rather than MORE prescriptive rules.

| Prefer | Over |
|--------|------|
| Tools that provide data | Prompt rules that constrain behavior |
| General principles | Specific pattern patches |
| State/context via tools | F-string prompt engineering |
| Subagents for specialized work | Complex pipelines in main agent |

**The test**: Would this change still help if the question domain shifted completely? General principles yes, specific patches no.

## Phase 1: Ground Truth - What Actually Matters

The ONLY true ground truth is **resolution outcomes**. Everything else is proxy signal.

### 1a. Collect Resolution Data

```bash
uv run python .claude/scripts/feedback_collect.py --all-time
```

**If we have resolved forecasts**: Focus on Brier scores. This is the REAL signal.
- Which forecasts performed worst? Read their meta-reflections.
- Are there systematic patterns in errors?

**If we have NO resolved forecasts yet**: We're flying blind on accuracy. Focus on:
- Process quality (is the agent reasoning well?)
- Tool failures (what's blocking the agent?)
- Do NOT treat CP divergence as evidence of error

### 1b. Retrodict Missed Questions

If questions resolved before we forecast them, **retrodict** them to build calibration data:

```bash
# Check which questions we missed
uv run python .claude/scripts/forecast_queue.py missed aib --days 14

# Check their resolutions
uv run python .claude/scripts/check_resolved.py 41835 41521 41517

# Run retroactive forecasts (saves to notes/forecasts/, computes Brier scores)
uv run forecast retrodict 41835 41521 41517
```

The `retrodict` command:
- Runs the forecast agent on resolved questions
- Saves forecasts to `notes/forecasts/` just like normal
- Shows the actual resolution and final CP
- Computes Brier scores for binary questions
- Compares our performance to the final CP

**This is valuable calibration data** even though we can't submit. It tells us:
- What would we have forecast?
- Were we better or worse than CP?
- What reasoning did we use?

Run this on any missed questions to build up calibration data faster.

**If no missed AIB questions**: Search Metaculus for other resolved questions to retrodict:

```bash
# Search for recently resolved questions on any topic
# Then retrodict interesting ones for calibration practice
uv run forecast retrodict <question_id> <question_id> ...
```

This is useful for:
- Building calibration data when AIB is slow
- Testing the agent on different question types
- Practicing on domains where we're weak

### 1b. About Community Prediction

CP is just another forecaster. Diverging from CP is not inherently bad - we WANT an edge.

**Correct framing**:
- If our reasoning is sound and we have better information, divergence is GOOD
- If divergence correlates with poor Brier scores after resolution, THEN investigate
- Do NOT treat "matching CP" as a goal

**When CP divergence is useful**:
- Understanding WHERE our reasoning differs (not WHETHER we're wrong)
- After resolution, checking if divergence predicted error

**When CP divergence is misleading**:
- As a primary signal without resolution data
- When the agent has information CP lacks (breaking news, specific API data)

## Phase 2: Object Level - Read Traces Deeply

**This is the most important phase.** Do not skip to aggregate patterns.

### 2a. Read Full Reasoning Traces (logs/)

The `logs/` directory contains the ACTUAL reasoning traces from each forecast session. These are more detailed than meta-reflections and show exactly what the agent thought and did.

```bash
# List all logged forecasts
ls logs/

# Read the full trace for a specific question
cat logs/<question_id>/*.log
```

**For questions with large CP divergence, READ THE FULL LOG.** The meta-reflection is a summary; the log shows:
- The agent's raw thinking process
- Which searches and tools were called
- How evidence was interpreted
- Where reasoning may have gone wrong

### 2b. Read 5-10 Meta-Reflections

Pick a sample including:
- Questions with large CP divergence (if available)
- Questions where tools failed
- Questions across different types (binary, numeric, meta)

For each, ask:
1. **Is the reasoning sound?** Does the logic follow from the evidence?
2. **What tools worked?** What provided high-value information?
3. **What tools failed?** What blocked progress?
4. **What does the agent say it needs?** Explicit capability requests

**Cross-reference with logs**: If the meta-reflection says "I used 8 tool calls", check the log to see what actually happened.

### 2c. Extract Tool Failures

```bash
# Tool failures mentioned in meta-reflections
grep -rh "failed\|error\|Error\|didn't work\|couldn't\|blocked\|403\|404\|405" notes/meta/*.md | sort | uniq -c | sort -rn | head -20
```

Common patterns:
- WebFetch fails on JS-heavy sites → Add API-based tool
- Specific API returns errors → Fix or add fallback
- Tool exists but agent doesn't use it → Improve discoverability

### 2d. Extract Capability Requests

```bash
# What the agent explicitly says it needs
grep -rh "would be useful\|would have helped\|would benefit\|wish I had\|tool that\|specialized tool" notes/meta/*.md | head -20
```

**Trust these requests.** The agent knows what it needs. Build the tools it asks for.

### 2e. Evaluate Reasoning Quality

For forecasts with large CP divergence, ask:
1. Is the agent's evidence valid?
2. Is the logic sound?
3. Are there gaps in the analysis?
4. Would a different forecast be MORE justified by the evidence?

**If reasoning is sound**: Divergence may be an edge. Wait for resolution.
**If reasoning is flawed**: Identify the specific failure. Is it a capability gap or a reasoning error?

## Phase 3: Meta Level - Self-Assessment Quality

The meta-reflection template should help the agent identify its own weaknesses.

### 3a. Evaluate Meta-Reflection Usefulness

Read the meta-reflections and ask:
- Can I trace what actually happened?
- Are tool effectiveness notes accurate?
- Are capability gaps specific and actionable?
- Is self-critique genuine or formulaic?

### 3b. Tracking Quality

The meta-reflection says "Effort: ~N tool calls" but this is subjective.

**Better**: Link forecasts to actual tool traces programmatically.

```bash
# Check if we have programmatic tracking
grep -h "tool_calls\|duration_ms\|tokens\|cost" notes/meta/*.md | head -5
```

If tracking is subjective, consider:
- Adding actual tool call counts to forecast output
- Linking meta-reflection files to session logs
- Including timestamps and costs programmatically

### 3c. Template Improvements

If meta-reflections are formulaic or unhelpful:
- Simplify the template (fewer categories, more specifics)
- Request concrete examples instead of general assessments
- Remove sections that always produce boilerplate

## Phase 4: Implement Changes (Bitter Lesson Order)

### Priority 1: Fix Failing Tools

If a tool fails repeatedly, fix it or add an alternative.

```bash
# Example: Wikipedia 403 errors
# → Check if redirects param is set
# → Add error handling and fallback
```

### Priority 2: Build Requested Tools

What did the agent explicitly request?

| Agent Request | Action |
|--------------|--------|
| "CP history over time" | Build tool to fetch historical CP |
| "Prediction market aggregator" | Improve polymarket/manifold search |
| "Historical base rate database" | Build reference data tool |
| "WebFetch fails on X" | Add X-specific API tool |

### Priority 3: Improve Subagents

If subagents aren't used:
- Are they providing unique value?
- Are they too expensive (time/compute)?
- Should they be lighter/faster?

### Priority 4: Simplify Prompts (Not Add Rules)

Prompt changes should:
- ADD general principles that help across domains
- REMOVE prescriptive rules that add complexity
- PREFER "use tool X for Y" over "when pattern P, do Q"

**Do NOT add**:
- Specific rules for specific question types
- Numeric adjustments ("subtract 0.5 logits when...")
- Patches for observed patterns

## Phase 5: Meta-Meta Level - Improve This Process

After running the feedback loop, reflect:

### What data did you lack?

- Could you trace from forecast → reasoning → tools → outcome?
- Was programmatic tracking sufficient?
- What logs would have helped?

### What would make this easier next time?

Scripts to build:
- `trace_forecast.py` - Link forecast to full tool call trace
- `compare_to_resolution.py` - Show reasoning vs actual outcome
- `tool_failure_report.py` - Aggregate failures by tool and target

### Update this document

If you learned something about the feedback loop process:
- Add it to this document
- Add scripts that automate repetitive analysis
- Remove guidance that wasn't useful

## Anti-Patterns to Avoid

### DON'T: Patch prompts for observed patterns
❌ "When forecasting meta-predictions, subtract 0.5 logits"
❌ "For definitional questions, cap confidence at 70%"
✅ Build tool that provides historical calibration data
✅ Add general principle about interpretation uncertainty

### DON'T: Over-rely on CP divergence
❌ "Large CP divergence means we're wrong"
❌ "Tell agent to trust CP when divergence > 20pp"
✅ Wait for resolution data to know if divergence correlates with error
✅ Use CP divergence to understand WHERE reasoning differs, not WHETHER it's wrong

### DON'T: Add rules the agent can't act on
❌ "Adjust based on the meta-question's CP" (agent can't see this)
✅ Provide tools that give the agent actionable information

### DON'T: Skip reading traces
❌ Jump to aggregate statistics (average divergence)
✅ Read 5-10 meta-reflections deeply first
✅ Understand what actually happened in individual forecasts

## Documentation Template

Write to `notes/feedback_loop/<timestamp>_analysis.md`:

```markdown
# Feedback Loop Analysis: YYYY-MM-DD

## Ground Truth Status
- Resolved forecasts with our predictions: N
- Average Brier score: X.XX (or "none yet - process analysis only")

## Object-Level Findings

### Tool Failures
| Tool | Failure | Count | Fix |
|------|---------|-------|-----|
| WebFetch | 403 on site X | N | Add X API tool |

### Agent Capability Requests
- "Would benefit from X" → [action taken]
- "Tool Y failed" → [action taken]

### Reasoning Quality Assessment
- [For 3-5 forecasts, brief assessment of reasoning soundness]

## Meta-Level Findings

### Meta-Reflection Quality
- Are they useful for debugging? [yes/no + why]
- Is tracking programmatic? [yes/no + what's missing]

### Template Improvements Made
- [List any changes to meta-reflection prompt]

## Meta-Meta Findings

### What data did I lack?
- [Specific gaps]

### What scripts would help next time?
- [Specific scripts to build]

### How should this process change?
- [Updates to feedback-loop.md]

## Changes Made
| Level | Change | Rationale |
|-------|--------|-----------|
| Object | Added X tool | Agent requested it in N meta-reflections |
| Meta | Improved tracking | Subjective → programmatic |
| Process | Added script Y | Automate repetitive analysis |
```

## Scripts Available

```bash
# Collect feedback data
uv run python .claude/scripts/feedback_collect.py --all-time

# Collect from specific tournament
uv run python .claude/scripts/feedback_collect.py --tournament spring-aib-2026

# Check missed questions
uv run python .claude/scripts/forecast_queue.py missed aib --days 14

# Check resolutions for specific questions
uv run python .claude/scripts/check_resolved.py 41835 41521 41517

# Retrodict resolved questions (builds calibration data)
uv run forecast retrodict 41835 41521 41517

# Trace a forecast to its logs and metrics
uv run python .claude/scripts/trace_forecast.py show 41906

# Aggregate metrics across all forecasts
uv run python .claude/scripts/aggregate_metrics.py summary

# Calibration report (needs resolved forecasts)
uv run python .claude/scripts/calibration_report.py summary
```

## Key Questions to Answer Each Session

1. **Do we have resolution data?** If no, focus on process not accuracy.
2. **What's our Brier score?** This is the REAL metric (when available).
3. **What tools fail repeatedly?** Fix or replace them.
4. **What does the agent say it needs?** Trust and provide.
5. **Is the agent's reasoning sound?** Read traces deeply to find out.
6. **What would make this process better?** Update this document.

# Meta-Meta Analysis: Feedback Loop Process Reflection

**Date**: 2026-02-03
**Context**: After running the feedback loop and receiving user feedback about approach

## What I Did Wrong

### 1. Over-reliance on CP Comparison

I treated CP divergence as the primary signal and framed the goal as "reducing divergence." This is backwards.

**Correct framing**:
- CP is just another forecaster
- Divergence could mean we have an edge (good) or are miscalibrated (bad)
- Only RESOLUTION tells us which it is
- With no resolved forecasts, we're mostly guessing

### 2. Prescriptive Prompt Patches

I added specific rules like "subtract 0.5 logits for meta-predictions where you're >70%." This violates the bitter lesson.

**Better approach**: Build tools that give the agent relevant information:
- Historical meta-prediction accuracy database
- Resolution criteria parser that flags ambiguities
- Calibration tracker that shows the agent's own history

### 3. Not Reading Traces Deeply Enough

I focused on patterns across meta-reflections (CP divergence, subagent usage) rather than understanding individual forecasts deeply.

**What I should have done**:
- Pick 3-5 forecasts
- Read the full meta-reflection
- Understand what tools the agent used and why
- Identify what the agent said it NEEDED but couldn't get

## What the Agent Actually Needs (From Meta-Reflections)

### Tool Failures (Repeated)
- `WebFetch` fails on: TradingEconomics (405), Yahoo Finance (JS), Google Trends
- `get_coherence_links` returns 404s
- `polymarket_price` often finds no matching markets

### Capability Gaps (Agent's Own Words)
- "Template for FRED value on date X questions would be useful"
- "Real-time Metaculus CP tracker would be useful"
- "Wikipedia fetch failed (403 error)"
- "Can't download time series, only view current page"

### What This Implies

The agent needs BETTER DATA ACCESS, not more rules about how to think:

1. **FRED API tool** - Agent repeatedly tries to get economic data and fails
2. **Yahoo Finance API tool** - Stock price questions need reliable price data
3. **Google Trends API tool** - Multiple Trends questions, no good data access
4. **Better WebFetch** - Should handle JS-heavy sites or have specific fallbacks

## Tools That Should Be Built

| Priority | Tool | Rationale |
|----------|------|-----------|
| HIGH | `fred_data` | Repeatedly needed for economic questions |
| HIGH | `yahoo_finance` | Stock price questions need this |
| MEDIUM | `google_trends` | Several Trends-based questions |
| MEDIUM | `base_rate_lookup` | Agent often estimates from scratch |
| LOW | `criteria_analyzer` | Could flag ambiguous resolution criteria |

## Process Improvements for Next Time

### Scripts to Build

1. **`trace_forecast.py`** - Link a forecast to its full tool call trace
   - Input: post_id
   - Output: Timeline of tool calls, errors, key decisions

2. **`tool_failure_report.py`** - Aggregate tool failures
   - Count failures by tool and target
   - Identify patterns (e.g., "WebFetch fails on site X")

3. **`compare_resolution.py`** - After resolutions, show reasoning vs outcome
   - Input: post_id of resolved question
   - Output: Our forecast, our reasoning, actual resolution, what went wrong/right

### Tracking Improvements

The meta-reflection says "Effort: ~N tool calls" which is subjective. Should be:
- Actual tool call count (from logs)
- Actual time taken
- Token usage (if available)

This requires instrumenting the forecasting agent, not changing prompts.

## Changes Made This Session

### Good (Keep)
- Rewrote `.claude/commands/feedback-loop.md` to:
  - Emphasize capability improvement over prompt patching
  - Frame CP as weak signal, resolution as ground truth
  - Add three-level analysis (object/meta/meta-meta)
  - Include anti-patterns section

### Questionable (Revisit)
- Added prescriptive logit adjustments to prompts.py
- These are hole-patches, not principled improvements
- Should be replaced with tools when feasible

## Next Actions

1. **Build FRED API tool** - Highest priority based on agent needs
2. **Build Yahoo Finance tool** - For stock price questions
3. **Add tool call tracking** - Programmatic, not subjective
4. **Wait for resolutions** - Feb 15 has several questions resolving
5. **Re-evaluate prompt changes** - After we have Brier score data, see if they helped

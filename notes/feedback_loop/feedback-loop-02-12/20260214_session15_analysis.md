# Feedback Loop Analysis: 2026-02-14 Session 15 — Meta-Prediction Deep Dive

## Focus

Why is v0.10.0 meta (CP) reasoning so much worse than v0.3.1?

## Ground Truth Status

- Meta questions with both v0.3.1 and v0.10.0 retrodictions: 3 (39935, 41387, 41391)
- v0.3.1 meta average Brier (across all 11 meta Qs): 0.247
- v0.10.0 meta average Brier (3 Qs): 0.480
- Gap: 0.233 Brier — nearly 2x worse

## Head-to-Head Comparison

| Post | Question | Res. | v0.3.1 prob | v0.3 Brier | v0.10 prob | v0.10 Brier | CP data? (v0.10) |
|------|----------|------|-------------|------------|------------|-------------|-------------------|
| 39935 | Mamdani CP>91% | YES | 50% | 0.250 | 40% | 0.360 | YES (working) |
| 41387 | Dems House CP>9% | YES | 43% | 0.325 | 40% | 0.360 | YES (working) |
| 41391 | Shutdown CP>33% | NO | 70% | 0.490 | 85% | 0.722 | NO (100% failure) |

## Object-Level Findings

### Root Cause 1: `get_cp_history` Failure on 41391 (PRIMARY)

v0.10.0's catastrophic 41391 forecast (Brier 0.722) accounts for most of the gap.

**Tool metrics comparison:**
- v0.3.1: `get_cp_history` 4 calls, 2 errors (50%) — got enough data to see CP at 33.30%
- v0.10.0: `get_cp_history` 2 calls, 2 errors (100%) — got nothing

**Root cause:** The **negative caching bug in `_ensure_post_id`** (documented in session 14). When a transient 429 rate limit hit during post_id validation, `_ensure_post_id` returned None, and `get_cp_history` failed before attempting to fetch aggregation data. This was NOT a persistent Metaculus 429 problem — the tool calls took <2s total (instant failure from cached None), not the 30s+ you'd expect from rate-limit retries.

**Without CP data, the agent fell into event-level reasoning:**
- Agent reasoning: "CR expires Jan 30, 43-day shutdown precedent, partisan conflict → shutdown risk high → CP must be above 33%"
- Gave 85% (confident YES)
- Resolved NO — CP was near threshold and drifted below it

This is exactly the event-level fallacy the prompt warns against, but the agent overrode the guidance because the event-level signal was so strong. A warning alone is insufficient when the agent has rich event-level evidence and zero CP data.

**Fix applied in session 14:** `_ensure_post_id` now uses `MetaculusClient.fetch_post_json` (with built-in retry) and only caches successful resolutions.

### Root Cause 2: 40% Convergence on CP-Available Questions (SECONDARY)

When CP data WAS available (39935, 41387), v0.10.0 gave exactly 40% on both. Both resolved YES.

**39935 (Mamdani CP>91%):**
- v0.10.0 had working CP history, saw CP at 0.90 (below 0.91 threshold), 8-day downward trend
- Reasoned: "downward trend + stable below threshold → lean NO" → 40%
- Actually reasonable meta-prediction reasoning, just wrong in outcome (CP bounced back above 91%)

**v0.3.1 on the same question:**
- Also lacked CP trajectory data
- Reasoning: "CP is exactly at 91.00% threshold. Without trajectory data, this is a coin flip." → 50%
- Honest about its blindness, gave 50%

**Key insight:** v0.3.1's naive "I don't know, ~50%" outperformed v0.10.0's informed "I see a downward trend, 40%." Short-term CP trends are noisy — an 8-day decline doesn't reliably predict whether CP will still be below threshold 9 days later. The *level* (CP vs threshold) matters more than the *slope* (recent direction).

**41387 (Dems House CP>9%):**
- v0.10.0 had CP data, reasoned about stale predictions, small forecaster base → 40%
- v0.3.1 gave 43%
- Very similar. Both near the balanced prior. v0.3.1 slightly better simply by being closer to 50%.

**Pattern:** v0.10.0's prompt guidance ("start near 50% and adjust") created a systematic pull slightly below 50% (landing at 40%), possibly because the agent interpreted "adjust based on evidence" as needing to move away from 50% to show it was reasoning. v0.3.1 had no such guidance and defaulted to honest uncertainty.

### Summary of Failure Modes

1. **Without CP data (41391):** Event-level fallacy → catastrophic error (Brier 0.72). This is a DATA ACCESS problem. When the negative caching bug prevented CP access, the agent's reasoning quality collapsed.

2. **With CP data (39935, 41387):** Over-reading short-term trajectory → modest error (Brier ~0.36). The prompt's prescriptive ranges (40-60%, 35-65%) anchored the agent slightly below the balanced prior. v0.3.1's naive 50% was accidentally better.

3. **v0.3.1's advantage was partly luck:** Its "I don't know" approach (~50%) worked because meta-prediction thresholds are auto-generated near CP, making 50% a decent uninformed prior. It wasn't good reasoning — just honest uncertainty that happened to be well-calibrated.

## Changes Made

### Prompt (prompts.py) — Meta-Predictions Section Rewrite

| Change | Rationale |
|--------|-----------|
| Added "Why Thresholds Are Structurally Balanced" subsection | Explains the auto-generation mechanism and why the balanced prior exists. Agent needs to understand WHY 50% is reasonable, not just be told to stay near it. |
| Removed prescriptive numeric ranges (40-60%, 35-65%) | These anchored the agent at specific numbers instead of teaching principles. Agent would target 40% rather than reasoning about evidence quality. |
| Added "Trajectory skepticism" to Two Lenses section | Short-term CP trends are noisy. Level matters more than slope. Prevents over-reading recent directional movements. |
| Rewrote "When CP History Is Unavailable" as hard stop with case study | Added the 41391 example as a concrete cautionary tale. Changed from "don't do X" to explaining WHY event-level reasoning fails, with a real case where it produced catastrophic results. |
| Strengthened Common Mistakes entry for event-level fallacy | Added "the most destructive, producing our worst Brier scores by far" and note about the temptation being strongest when CP is missing. |
| Reframed buffer size as "most predictive variable" | CP level relative to threshold is the best predictor, more than any other variable. |

### Key Principles in New Prompt

1. **Burden of proof on directional evidence:** The balanced prior exists because thresholds are auto-generated near CP. Moving away requires evidence about forecaster behavior, not about the event.

2. **Level > slope:** How far CP is from threshold matters more than which direction it moved recently. Short-term trends are noise.

3. **CP-unavailable = hard stop:** When the most important input is missing, acknowledge blindness rather than substituting event reasoning. Only evidence about forecaster behavior itself (tiny forecaster base, major catalyst forcing updates) justifies departing from the balanced prior.

4. **No prescriptive numbers:** The prompt explains principles and reasoning rather than giving specific ranges. The agent should derive appropriate confidence from the evidence quality, not target a predetermined range.

## Meta-Level Findings

### The "More Data, Worse Forecast" Paradox

v0.10.0 had MORE information than v0.3.1 on 39935 (working CP trajectory data) and made a WORSE forecast. This is a known pattern in forecasting: additional noisy signals can degrade performance when they're over-weighted.

**Implication for the prompt:** The trajectory skepticism addition addresses this directly. The agent should weight the CP *level* heavily and treat short-term *direction* as weak signal.

### Prompt Compliance Problem

On 41391, v0.10.0 had explicit prompt guidance to stay moderate when CP data is unavailable — and ignored it, going to 85%. This means the old prompt's prescriptive rules were insufficient against strong event-level signals.

**The fix is narrative, not numeric:** The new prompt uses a concrete case study and explains the *mechanism* of failure (why event reasoning fails for meta-predictions) rather than just stating a range. Understanding why a constraint exists makes it harder to rationalize overriding it.

## Meta-Meta Findings

### This Session's Process

Focused analysis on a specific question (v0.10 vs v0.3 meta performance) was more productive than broad surveys. The three-question comparison revealed clear, actionable root causes.

### What's Still Missing

1. **v0.10.0 meta retrodictions with working CP data on questions that resolved NO** — both 39935 and 41387 resolved YES. We don't know how v0.10.0 performs on NO-resolving meta questions when CP data is available.

2. **Post-fix retrodictions** — the negative caching bug was fixed in session 14. We need retrodictions under the CURRENT code (with working `_ensure_post_id`) to validate that the data access problem is actually resolved.

3. **Testing the prompt changes** — this session's prompt rewrite needs retrodiction testing on meta questions to evaluate whether removing prescriptive ranges and adding trajectory skepticism actually improves calibration.

## Retrodiction Queue

Cannot run retrodictions due to Metaculus 429 rate limiting. When API is available:

```bash
# Find missed meta questions for retrodiction
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 21

# Priority: meta questions with confirmed resolution (R=Y)
# Need: mix of YES and NO resolving meta questions
# Goal: test both the _ensure_post_id fix AND the prompt changes
```

Testing priorities for next retrodiction batch:
- At least 3 meta-prediction questions (test prompt rewrite)
- Include both YES-resolving and NO-resolving meta questions if available
- Verify `get_cp_history` succeeds (validates session 14 bug fix)

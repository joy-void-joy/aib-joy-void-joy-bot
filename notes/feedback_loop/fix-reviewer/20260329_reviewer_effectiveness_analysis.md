# Reviewer Effectiveness Analysis — 2026-03-29

Agent versions analyzed: v3.5.0, v4.0.0, v4.0.1

## Question

Is the in-session reviewer shifting forecasts in the correct direction?

## Ground Truth

- Resolved forecasts with multi-reflection sessions: 22
- Actual revisions observed (estimate changed): 21
- Mostly v3.5.0 (reflection.yaml data), some v4.0.0

## In-Session Reviewer (Reflection Tool)

The reviewer gates forecast submission via approve/warn/fail verdicts. On fail, the agent must revise and call reflection() again.

### Direction accuracy

| Metric | Value |
|--------|-------|
| Revisions in correct direction | **67% (14/21)** |
| Mean improvement per revision | **+2.03pp** |
| Mean cumulative improvement per session | **+2.37pp** |
| Mean Brier improvement | **+0.0119 (5.7% relative)** |
| No-change revisions | 4/25 (16%) |

### After FAIL verdicts specifically

| Metric | Value |
|--------|-------|
| Correct direction | **62% (8/13)** |
| Mean improvement (beneficial) | **+6.12pp** |
| Mean worsening (harmful) | **-4.26pp** |

The asymmetry is favorable: when FAIL works, improvements are large (up to +12pp); when it backfires, damage is smaller.

### By question type

- Binary: **73% correct** direction
- Multiple choice: **50% correct** (coin flip — reviewer adds no value here)

### Failure patterns

- Stock price questions: reviewer pushed estimates wrong direction (e.g., post 42406: "60% is too low" → agent moved to 65% → resolved No)
- MC questions: reviewer frequently confused about which option to favor
- Best performance on meta-prediction questions (CP tracking) where reviewer correctly identified overconfidence

## Post-Session Opus Reviewer (reviewer_estimate)

Cannot evaluate yet. The `reviewer_estimate` field was added to ForecastSummary but no existing summary.json files have been regenerated with the new schema. All 87 summaries use the old format.

To populate: `uv run aib-devtools analysis review <post_id>` for individual posts.

## Bugs Found and Fixed

### 1. revision_history never persisted to disk (FIXED)

`core.py:1289` set `output.revision_history = review_state.history` AFTER `save_forecast()` at line 1280. Additionally, `save_forecast()` didn't accept `revision_history` as a parameter.

**Fix:** Moved assignment before save, added parameter to `save_forecast()` and `SavedForecast`.

### 2. Auto-approve threshold too aggressive (FIXED)

Threshold was 2 consecutive fails. Given the reviewer is correct 62% of the time on fails, this meant the strongest objections were most likely to be auto-approved.

**Fix:** Raised threshold from 2 to 3 consecutive fails. Updated prompt references.

## Recommendations (not yet implemented)

1. **Persist ReviewState.history to reflection.yaml** with explicit verdict labels (currently only critique text is saved, verdicts are reconstructed heuristically)
2. **Consider disabling reviewer for MC questions** where it's at coin-flip accuracy (or use a different prompt)
3. **Regenerate summary.json** for resolved forecasts to evaluate reviewer_estimate accuracy (deferred — expensive)

## Data Gaps

- `revision_history` field was never populated in stored JSONs (now fixed for future forecasts)
- `reviewer_estimate` not yet populated (summary.json regeneration deferred)
- Sample size modest (22 sessions) — mostly v3.5.0
- No v4.0.1 resolved forecasts yet for comparison

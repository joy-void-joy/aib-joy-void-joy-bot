# Feedback Loop Analysis: 2026-02-11 (Session 4)

## Ground Truth Status
- Live forecasts resolved: **0 of 92** (meta-prediction/stock batch resolves Feb 14-15)
- Retrodictions with resolution: **26** (16 binary, 10 numeric) — 12 new this session
- 22 resolved AIB questions still show R=- in API (no confirmed resolution data)
- No new resolved AIB/Cup/MiniBench questions available

## Object-Level Findings

### New Retrodiction Batch (12 questions, agent v0.3.1 with session 3 prompt fixes)

**Binary by Category:**

| Category | N | Avg Brier | Accuracy | Assessment |
|----------|---|-----------|----------|------------|
| Meta-prediction | 11 | 0.2561 | 6/11 (55%) | Near random (0.25 baseline) |
| Stock price | 4 | 0.2580 | 1/4 (25%) | Appropriately humble near 50% |
| Other | 1 | 0.2025 | 1/1 (100%) | Good |
| **All binary** | **16** | **0.2532** | **8/16 (50%)** | |

**Key misses:**
- **41391** (Brier 0.49): Predicted 70% YES on "Will shutdown CP rise above 33.30%?". Congress struck a deal in early January — genuine political surprise, not systematic error.
- **41387** (Brier 0.33): Predicted 43% YES on "Will Dems House CP rise above 9.00%?". Underweighted meta-effect (the meta-question itself attracts forecasters to the underlying question).

**Excluding the 41391 outlier, meta-prediction Brier = 0.233** (better than random).

**Numeric (10 forecasts):**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| 90% CI coverage | 90% | 90% | Perfect |
| 50% CI coverage | 90% | 50% | Still overdispersed |
| PIT K-S p-value | 0.036 | >0.05 | Marginally significant |
| Median bias | 8/10 above | 5/10 | Systematic low bias |

Stable quantities (SOFR, Treasury, OAS, revenue) are well-calibrated. Volatile quantities (BTC, VIX, spreads, EPS) have medians too low. PIT histogram concentrated at 0.4-0.8.

### Calibration Summary (All 26 forecasts)

| Metric | Session 3 | Session 4 | Delta |
|--------|-----------|-----------|-------|
| Binary ECE | 0.1375 | 0.1450 | +0.008 (slightly worse) |
| Binary Brier | 0.2180 | 0.2532 | +0.035 (worse, driven by 41391) |
| Binary bias | underconfident | overconfident (+0.055) | Flipped |
| Numeric 90% CI | 83% | 90% | +7pp (improved to target) |
| Numeric 50% CI | 83% | 90% | +7pp (still overdispersed) |
| PIT K-S p | 0.166 | 0.036 | Now significant |

### Tool Reliability (New Batch)

| Tool | Calls | Errors | Rate | Notes |
|------|-------|--------|------|-------|
| get_cp_history | 15 | 7 | **46.7%** | STILL BROKEN — see below |
| execute_code | 24 | 2 | 8.3% | Acceptable |
| get_metaculus_questions | 8 | 1 | 12.5% | Rate limits |
| fetch | 5 | 1 | 20.0% | Retrodict Wayback issues |
| search_exa | 40 | 0 | 0.0% | Excellent |
| web_search | 20 | 0 | 0.0% | Excellent |
| All others | 63 | 0 | 0.0% | Reliable |

### Critical Bug: get_cp_history Still Failing

Despite the session 2 fix (commit 22860ad), get_cp_history fails 47% of the time. Root cause: **each call makes 2 API requests** (ID verification + history fetch), doubling rate-limit exposure.

The `_ensure_post_id()` function always makes a verification API call, even when the agent passes a valid post_id. For 15 CP history calls across 12 retrodictions, that's 30 API requests — hitting Metaculus rate limits.

The 41391 meta-prediction (worst miss, Brier 0.49) had 2/4 CP history errors, meaning the agent had incomplete trajectory data for its most important tool.

**Fix needed**: Cache `_ensure_post_id()` results and/or skip verification when calling with known post_ids.

### Subagent Usage: Still Zero

Consistent pattern across all sessions. Not blocking performance (sessions 125-385s) but the agent may be under-utilizing parallel research on complex questions.

## Meta-Level Findings

### Binary Calibration Pattern

The reliability diagram shows:
- 40-50% bucket: 9 forecasts, actual 55.6% — slightly underconfident
- 50-60% bucket: 5 forecasts, actual 60.0% — slightly underconfident
- 70-80% bucket: 1 forecast, actual 0% — the 41391 outlier

Most binary predictions cluster near 50% (14/16 in the 40-60% range). This is correct for stock/meta questions that are near coin-flips. The agent is appropriately humble. The one time it deviated (70% on 41391), it was wrong — but that was a genuine surprise, not a systematic error.

### Numeric Overdispersion: Prompt Change Insufficient

Session 3 replaced "Set WIDE intervals" with evidence-quality guidance. The new batch (4 numeric forecasts, all with session 3 prompts) still shows all outcomes within the 50% CI. The evidence-quality guidance didn't produce measurably tighter CDFs.

This might be a fundamental issue with how LLMs estimate uncertainty — they may inherently set wide ranges when uncertain, regardless of prompt guidance.

**Not making further prompt changes**. With only 10 numeric data points, we can't reliably diagnose whether the overdispersion is getting better or worse. Wait for more data.

### No New Calibration Data Sources

- AIB: 22 resolved questions, all R=- (API doesn't populate resolution)
- Cup/MiniBench: API returns 400 for resolved queries
- The existing 14 original retrodictions have been analyzed 3 sessions running
- 12 new retrodictions added this session provide fresh signal

## Meta-Meta Findings

### Session Workflow Working Well

The feedback loop command structure is effective. Phase 0 (read previous analysis) prevents re-deriving. The categorization by question type (meta/stock/other/numeric) is essential and should be automated.

### Script Gap: No Category-Level Calibration

The calibration_analysis.py script reports overall metrics but not per-category (meta vs stock vs other). This matters because stock questions are inherently ~50/50 and shouldn't be averaged with meta-predictions that might show systematic bias.

### tmp/scripts/ Used for One-Off Analysis

Created `categorize_retrodictions.py` for category breakdown. Consider promoting to .claude/plugins/aib/scripts/ if pattern persists.

## Changes Made

| Level | Change | File(s) | Rationale |
|-------|--------|---------|-----------|
| Object | get_cp_history uses client library with HTML enrichment | forecasting.py | JSON API returns null aggregations; HTML has full data (275 CP history points recovered for post 40919) |
| Object | Cache _ensure_post_id results | forecasting.py | Avoid redundant API calls that trigger rate limits |
| Object | Add auth headers to HTML fallback | client.py | More robust against future auth changes |
| Object | forecast_queue.py uses AsyncMetaculusClient | forecast_queue.py | Individual post fetches now get HTML-enriched data |
| Object | check_cp.py single command uses client | check_cp.py | Gets full aggregation data via enrichment |
| Object | Handle "annulled" resolution type | resolution_update.py | Enriched data surfaces new resolution types that crashed the script |
| Meta-Meta | Session 4 analysis document | This file | Document findings |
| Meta-Meta | Created categorization script | tmp/scripts/categorize_retrodictions.py | Category-level calibration analysis |

## Key Discovery: JSON API Null Fields Are Pervasive

The Metaculus JSON API returns null for `aggregations`, `resolution`, `description`, and other fields. The DRF browsable HTML page (fetched with `Accept: text/html`) includes the full data. This was previously known for description fields but this session confirmed it also affects:
- **aggregations.recency_weighted.history** — CP trajectory data (critical for meta-predictions)
- **resolution** — actual resolution values (needed for calibration)

The `AsyncMetaculusClient._enrich_post_json()` method handles this automatically. All API calls should go through the client library to benefit from this enrichment.

## Still Proposed (Not Yet Implemented)

| Level | Change | Rationale | Priority |
|-------|--------|-----------|----------|
| Meta-Meta | Add category tagging to calibration_analysis.py | Need per-category Brier to distinguish stock noise from meta-prediction signal | Medium |
| Meta-Meta | Promote categorization script to aib/scripts/ | Reusable analysis | Low |

## Retrodiction Queue

### No New Candidates Available
- AIB: 22 resolved questions, all R=- (no confirmed resolution data in API)
- Cup/MiniBench: API returns 400 for resolved queries
- Existing questions have been thoroughly analyzed

### Recommendation: Fix get_cp_history, Then Wait for Feb 14-15

1. **Fix get_cp_history reliability** — this is the highest-priority action. The tool is critical for meta-predictions (the largest category of AIB questions) and fails half the time.
2. **Wait for Feb 14-15 live resolution batch** (28 meta-prediction/stock questions)
3. When batch resolves:
   - `resolution_update.py check` → update forecast files
   - `calibration_analysis.py summary` → first live calibration
   - Compare live vs retrodict patterns
   - Category-level analysis (meta vs stock vs other)

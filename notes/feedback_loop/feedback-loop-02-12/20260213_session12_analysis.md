# Feedback Loop Analysis: 2026-02-13 (Session 12)

## Ground Truth Status

- **Resolved forecasts with our predictions**: 0 with API-confirmed resolutions (406 still blocks)
- **Live forecasts**: 96 (0 resolved with Brier scores)
- **Retrodictions**: 56 total, 53 with resolutions
- **Binary retrodiction Brier**: 0.2825 (n=32)
- **Binary ECE**: 0.1594, MCE: 0.8200 (10%-20% bucket), Overconfidence: +0.0829
- **Numeric PIT**: borderline uniform (K-S p=0.059), 90% CI coverage: 90% (perfect)

### CP Fix Validation (v0.8.0 re-runs)

Session 11 recommended re-running 41387 and 39935 with the CP hiding fix. Results:

| ID | Question | v0.3.1 | v0.7.2 | v0.8.0* | Resolution |
|----|----------|--------|--------|---------|------------|
| 39935 | CP>91% (Mamdani) | 0.2809 | 0.5625 | **0.0484** | YES |
| 41387 | CP>9% (Dems House) | 0.3249 | 0.8100 | **0.6724** | YES |

*Labeled 0.7.3 due to uncommitted version file; actual code is v0.8.0 (CP fix committed).

**39935**: Dramatic improvement. Agent reasoned well from fundamentals (Wikipedia, polling data) despite having NO CP data at all (see root cause below).

**41387**: Marginal improvement over v0.7.2, still poor. Without CP data, agent estimated 18% (actual CP was >9%, resolved YES).

## Object-Level Findings

### 1. CRITICAL: CP History Aggregation Parsing Bug (Root Cause Found)

**Impact**: ALL `get_cp_history` calls returned 0 data points for ALL questions across ALL versions.

**Root cause**: Metaculus changed the `aggregation_explorer` API response structure. Data moved from `data["recency_weighted"]` to `data["aggregations"]["recency_weighted"]`. Our parser (`metaculus/client.py:186`) checked the old path only.

**Evidence**:
- Direct API test: 75 history points available for post 35760, 284 for 7452, 331 for 38665
- Our parser returned 0 for all three
- Meta-reflections across 10+ retrodictions report "CP history failed" or "returned 0 data points"

**Fix applied** (`metaculus/client.py:186`):
```python
# Before:
recency = data.get("recency_weighted")
# After:
recency = data.get("recency_weighted") or data.get("aggregations", {}).get("recency_weighted")
```

**Verified**: After fix, all three test questions return full CP history data.

**This is the highest-impact fix this session.** It restores the agent's ability to see CP trajectory for ALL questions, which is critical for meta-predictions and useful for calibration anchoring on all question types.

### 2. Inline CP Still Null (Different Issue)

`community_prediction_at_access_time` returns None from the JSON API (`/api/posts/{id}/`). This was previously populated via the HTML enrichment endpoint, which has returned 406 since Feb 12-13.

**Impact**: `get_metaculus_questions` returns `community_prediction: null` for binary questions.

**Mitigation**: With CP history now working, the agent can get CP trajectory via `get_cp_history`. This is actually MORE useful for meta-predictions than a single snapshot value.

**No fix needed**: The aggregation endpoint fix provides equivalent (better) data.

### 3. v0.3.1 vs v0.8.0 CP Data Access

| Version | CP Source | Status |
|---------|-----------|--------|
| v0.3.1 (Feb 11) | HTML enrichment → inline CP | Worked (pre-406 breakage) |
| v0.7.2 (Feb 11) | HTML enrichment → inline CP, but blanket CP hiding | Broke our own data |
| v0.8.0 (Feb 13) | HTML enrichment 406 + aggregation parsing bug | Both sources broken |
| v0.8.1 (this fix) | Aggregation endpoint (fixed parser) | **CP trajectory restored** |

v0.3.1 performed best (Brier 0.30) because it had inline CP data (API wasn't broken yet and no CP hiding bug). v0.8.1 should perform comparably or better — it has CP trajectory (richer than inline) plus all other improvements from 0.4.0-0.8.0.

### 4. Researcher Subagent Hallucination (39935)

The 39935 meta-reflection reports: "Researcher subagent: POOR - returned fabricated search results (fake candidates 'Tom Donovan', 'Jane Smith')."

The researcher subagent hallucinated fictional NYC mayoral candidates. This didn't affect the final forecast (agent compensated with Wikipedia), but is a reliability concern.

**Root cause**: Likely Wayback-restricted searches returned empty results, and the subagent filled the gap with confabulated content.

**Not fixing this session**: The agent correctly disregarded the fabricated results and found verified data through other tools. The subagent usage is rare (0% in live sessions). If subagent reliability becomes more important, we should add a disclaimer to the researcher prompt about not fabricating sources.

### 5. Tool Reliability Summary

| Tool | Status | Notes |
|------|--------|-------|
| **get_cp_history** | **FIXED** | Was returning 0 points for ALL questions; now works |
| Sandbox | 100% reliable | No issues |
| search_exa | ~94% | Occasional failures, acceptable |
| web_search | ~60% in retrodict | Often empty due to Wayback restrictions |
| fetch | ~70% | 403 on paywalled/JS sites |
| search_metaculus | Error on conditional type | Post 38676 crashes due to unhandled `conditional` type |

### 6. Calibration Analysis

Binary calibration (n=17 resolved binary retrodictions):
- ECE: 0.1594 (moderate — room for improvement)
- MCE: 0.8200 in 10-20% bucket (single forecast: 41387 at 18%, resolved YES)
- Overconfidence: +0.0829
- Brier: 0.2614 (slightly above random baseline of 0.25)
- Problem buckets: 10-20% (one forecast, fully wrong) and 80-90% (one forecast, fully wrong)

**Interpretation**: With only 17 data points and most in single-point buckets, the calibration numbers are noisy. The 40-60% range (12 forecasts, 50% resolution rate) is perfectly calibrated. The extreme buckets are unreliable with n=1 each.

## Meta-Level Findings

### Calibration Data Quality

With the CP history fix, future retrodictions should have significantly richer data. The v0.8.0 retrodictions were confounded by the parsing bug — they couldn't access CP even though the fix was supposed to make it available. v0.8.1 retrodictions will be the first clean test of the full system.

### Version Tracking

| Version | Changes | Retrodictions | Avg Brier |
|---------|---------|---------------|-----------|
| 0.3.1 | Baseline | 40 resolved | 0.2382 |
| 0.4.0 | Minor | 1 resolved | 0.2704 |
| 0.7.2 | Prompt rewrite + CP bug | 10 resolved | 0.4664 |
| 0.7.3/0.8.0 | CP hiding fix (but aggregation still broken) | 2 resolved | 0.3604 |
| 0.8.1 | **Aggregation parsing fix** | 0 (pending) | TBD |

## Meta-Meta Findings

### Aggregation API Schema Monitoring

The aggregation_explorer endpoint changed its response format without notice. This caused a silent failure — the parser returned empty results instead of erroring. Future-proofing: add a log warning when `recency_weighted` is not found at either path.

### Resolution Pipeline Still Blocked

HTML enrichment returns 406 (since Feb 12-13). All calibration data comes from retrodictions with manually-set resolutions. No new missed-question candidates are available because `forecast_queue.py missed` can't confirm resolutions.

### CP History Was the #1 Tool Failure

Scanning meta-reflections across 10+ retrodictions, "CP history failed/returned 0" is the single most common complaint. The fix addresses the root cause — this should dramatically improve agent capability, especially for meta-predictions.

## Changes Made

| Level | Change | File(s) | Rationale |
|-------|--------|---------|-----------|
| Object | Fix aggregation response parsing | metaculus/client.py:186 | API changed response structure; CP history returned 0 for ALL questions |
| Object | Version bump 0.7.3 → 0.8.1 | version.py | Aggregation fix changes agent behavior significantly |
| Meta-Meta | Analysis document | This file | Document findings |

### NOT Doing (Correctly)

- NOT fixing conditional question type in search (minor, agent works around it)
- NOT adding subagent hallucination guardrails (rare, agent self-corrects)
- NOT fixing inline CP null (aggregation endpoint provides better data)

## Future-Leak Detection Results

| Retrodict | Version | Result | Details |
|-----------|---------|--------|---------|
| 39935 | v0.8.0 | CLEAN | No future references; researcher hallucinated but from fabrication, not future data |
| 41387 | v0.8.0 | CLEAN | No future references; agent correctly limited to pre-Jan-5 data |

## Retrodiction Queue

### Priority 1: Validate CP History Fix (re-run meta-predictions with v0.8.1)

These meta-predictions were most affected by CP blindness. Re-running with v0.8.1 (working CP history) tests whether CP data access improves calibration.

```bash
# Re-run with working CP history
uv run forecast retrodict 41387  # CP>9%, Dems House — should anchor on actual CP now
uv run forecast retrodict 39935  # CP>91%, Mamdani — should confirm strong perf with CP data

# Apply known resolutions
uv run python .claude/plugins/aib/scripts/resolution_update.py set 41387 yes
uv run python .claude/plugins/aib/scripts/resolution_update.py set 39935 yes

# Rebuild scores and compare
uv run python .claude/plugins/aib/scripts/scores_table.py build
uv run python .claude/plugins/aib/scripts/scores_table.py compare 0.8.0 0.8.1
```

### Priority 2: New retrodiction candidates

The resolution pipeline is still blocked (406), so `forecast_queue.py missed` can't find new candidates. Re-use the remaining candidates from Session 10's queue that weren't yet run:

```bash
# Non-meta questions (unaffected by CP fix, but will benefit from CP anchoring)
uv run forecast retrodict 41414  # COF stock (binary)
uv run forecast retrodict 41388  # 30-Day SOFR (numeric)

# Apply resolutions
uv run python .claude/plugins/aib/scripts/resolution_update.py set 41414 no
uv run python .claude/plugins/aib/scripts/resolution_update.py set 41388 3.70668
```

### Priority 3: Meta-predictions from different eras

Once resolution pipeline is fixed, retrodict meta-predictions that resolved before the API breakage to validate CP history across different time periods.

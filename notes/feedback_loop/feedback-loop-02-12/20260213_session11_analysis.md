# Feedback Loop Analysis: 2026-02-13 (Session 11)

## Ground Truth Status

- **Resolved forecasts with our predictions**: 36 (API), 0 with populated resolution values
- **Live forecasts**: 96 (0 resolved with Brier scores)
- **Retrodictions**: 54 total, 51 with resolutions
- **Binary retrodiction Brier**: 0.2998 (30 resolved binary, near-random baseline 0.25)
- **Binary ECE**: 0.1953, MCE: 0.9000 (10-20% bucket), Overconfidence: +0.1447
- **Numeric PIT**: borderline uniform (K-S p=0.059), 90% CI coverage: 90% (perfect)

### Resolution Data Still Blocked

Metaculus API returns `resolution: null` for all resolved questions. HTML enrichment endpoint returns 406 since Feb 12-13. All calibration data comes exclusively from retrodictions with manually-set resolutions.

## Object-Level Findings

### 1. v0.7.2 Regression Confirmed (Root Cause Found)

**v0.7.2 avg Brier = 0.4664 vs v0.3.1 = 0.2382** on overlapping questions. 4 of 5 binary comparisons worse.

| ID | Question | v0.3.1 | v0.7.2 | Delta | Root Cause |
|----|----------|--------|--------|-------|------------|
| 41387 | CP>9% (Dems House) | 0.3249 | 0.8100 | +0.49 | **CP hiding bug** |
| 39935 | CP>91% (Mamdani) | 0.2809 | 0.5625 | +0.28 | **CP hiding bug** |
| 41391 | CP>33% (shutdown) | 0.4900 | 0.6724 | +0.18 | **Future-leak** + hedging backfire |
| 41417 | VICI stock | 0.2601 | 0.2809 | +0.02 | Minor |
| 41521 | UN Venezuela | 0.2025 | 0.0064 | **-0.20** | **Success** — precedent-skepticism fix |

### 2. Root Cause: Blanket CP Hiding in Retrodict Mode

In `forecasting.py:280`:
```python
hide_cp = retrodict_cutoff.get() is not None  # Hides ALL CPs
```

This hid CP for ALL questions in retrodict mode. But tournament rules say:
- Agent CAN see the underlying question's CP (for meta-predictions)
- Agent CANNOT see the meta-question's own CP

**Evidence of causation:**
- v0.3.1 (pre-fix): Agent saw CP=9.00% for underlying question → used as anchor → predicted 43%
- v0.7.2 (post-fix): CP null → built Monte Carlo model from scratch → predicted 10%
- Same question, same retrodict date — only difference was CP visibility

**Fix applied**: Added `forecasted_post_id` ContextVar. CP now only hidden for the question being forecasted. Version bumped to 0.8.0.

### 3. Future-Leak Through Question Fine Print (41391)

Agent accessed Q40971's fine print containing an OPM archive reference dated Jan 31, 2026, while retrodicting from Jan 5. The `get_metaculus_questions` tool returns full fine_print without temporal filtering.

**Impact**: 41391 v0.7.2 should be excluded from calibration (Brier 0.67 is tainted).

**Not fixed this session**: Filtering fine_print text for post-cutoff dates risks false positives and requires NLP-level date extraction. Documented as known gap.

### 4. 41521 Success: Precedent-Skepticism Works

v0.3.1: 85% YES → actual NO → Brier 0.7225
v0.7.2: 8% YES → actual NO → Brier 0.0064

The v0.6.0 prompt rewrite's precedent-skepticism guidance worked perfectly here. The agent properly assessed that the UNGA has almost never condemned US military operations.

### 5. Numeric Calibration Remains Strong

- 90% CI coverage: 90% (perfect target)
- PIT: borderline uniform (K-S p=0.059)
- One outlier: MSFT EPS ($3.85 median vs $5.16 actual) — extreme beat, outside 90% CI

### 6. Tool Reliability

| Tool | Status | Notes |
|------|--------|-------|
| Sandbox | 100% reliable | No issues across all sessions |
| get_cp_history | Fixed | aggregation_explorer works for open+resolved |
| search_exa | ~94% | Occasional failures, acceptable |
| WebFetch | Known 403s | Trading Economics, JS pages — expected |

### 7. Subagent Usage: Still 0% in Live Sessions

Only activation was 8901 retrodict (v0.6.0). The agent consistently finds questions "straightforward enough" for solo work. Not addressed this session — lower priority than the CP fix.

## Agent Capability Requests

No new capability requests surfaced in this session's retrodictions.

## Meta-Level Findings

### Calibration Data Quality

With the CP fix in v0.8.0, the next round of meta-prediction retrodictions should produce dramatically different results. The v0.7.2 data is confounded by the bug and shouldn't be used for calibration comparisons.

**Recommended**: Re-run 41387 and 39935 with v0.8.0, then compare to v0.3.1 to isolate the effect of the CP fix from other prompt changes.

### Version Tracking

| Version | Changes | Retrodictions | Avg Brier |
|---------|---------|---------------|-----------|
| 0.3.1 | Baseline | 40 resolved | 0.2382 |
| 0.4.0 | Minor | 1 resolved | 0.2704 |
| 0.7.2 | Prompt rewrite + CP bug | 10 resolved | 0.4664 |
| 0.8.0 | CP fix | 0 (pending) | TBD |

## Meta-Meta Findings

### Future-Leak Detection Gap

The feedback loop document discusses future-leak detection for WebSearch/WebFetch dates and agent reasoning text, but doesn't cover **Metaculus question fine print** as a leak vector. Added to known gaps.

### Airtightness Checklist Update Needed

The checklist in the feedback-loop command should include:
- [ ] No post-cutoff information in fetched question fine_print or resolution_criteria
- [ ] Related questions' fine print doesn't reference outcomes after cutoff

### feedback_collect.py Enhancement

The calibration numbers shifted between sessions (ECE 0.0875 → 0.1953, binary N dropped from 26 → 17). This is likely because different filtering is applied. Need to investigate why the count changed.

## Changes Made

| Level | Change | File(s) | Rationale |
|-------|--------|---------|-----------|
| Object | CP hiding: only for forecasted question | retrodict_context.py, forecasting.py, cli.py | Blanket hiding caused meta-prediction regression |
| Object | Version bump 0.7.2 → 0.8.0 | version.py | CP fix changes agent behavior |
| Meta-Meta | Analysis document | This file | Document findings |

### NOT Doing (Correctly)

- NOT adding prompt rules for meta-predictions
- NOT patching specific CP behavior with hardcoded thresholds
- NOT filtering fine_print text (too risky for false positives)

## Future-Leak Detection Results

| Retrodict | Version | Result | Details |
|-----------|---------|--------|---------|
| 41387 | v0.7.2 | CLEAN | No future references, just poor reasoning from missing CP |
| 39935 | v0.7.2 | CLEAN | Market anchoring, no future data |
| 41391 | v0.7.2 | LEAKED | Used OPM doc from Jan 31 in Q40971 fine print while retrodicting from Jan 5 |
| 41521 | v0.7.2 | CLEAN | Excellent reasoning, no future refs |

## Retrodiction Queue

### Priority 1: Validate CP Fix (re-run meta-predictions with v0.8.0)

These three meta-predictions were most affected by the CP hiding bug. Re-running with v0.8.0 tests whether the fix improves calibration.

```bash
# Re-run worst meta-prediction misses with v0.8.0 CP fix
uv run forecast retrodict 41387  # CP>9%, Dems House (was 0.81 Brier)
uv run forecast retrodict 39935  # CP>91%, Mamdani (was 0.56 Brier)

# Apply known resolutions
uv run python .claude/plugins/aib/scripts/resolution_update.py set 41387 yes
uv run python .claude/plugins/aib/scripts/resolution_update.py set 39935 yes

# Rebuild scores and compare
uv run python .claude/plugins/aib/scripts/scores_table.py build
uv run python .claude/plugins/aib/scripts/scores_table.py compare 0.7.2 0.8.0
```

### Priority 2: Run remaining queued retrodictions from Session 10

Several from the Session 10 queue haven't been run yet:

```bash
# Stock questions (non-meta, should be unaffected by CP fix)
uv run forecast retrodict 41414  # COF stock (binary)
uv run forecast retrodict 41388  # 30-Day SOFR (numeric)

# Apply resolutions
uv run python .claude/plugins/aib/scripts/resolution_update.py set 41414 no
uv run python .claude/plugins/aib/scripts/resolution_update.py set 41388 3.70668
```

### NOT Re-running (41391)

41391 (government shutdown) has a fine_print future-leak vector that hasn't been fixed. Re-running would produce another tainted result. Skip until fine_print filtering is addressed.

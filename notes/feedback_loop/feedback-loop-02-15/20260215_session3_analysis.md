# Feedback Loop Analysis: 2026-02-15 (Session 3 — Offline)

## Ground Truth Status
- Agent version analyzed: pre-version live + v1.1.0 retrodict (v1.2.0 has no data yet)
- Total forecasts: 228 (110 live, 118 retrodict)
- Resolved: 162 (46 live, 116 retrodict)
- Binary Brier (live, n=25): 0.176
- Binary Brier (retrodict v1.1.0, n=9): 0.199
- Binary ECE (live): 0.191, bias: underconfident (-0.19)
- Numeric: PIT uniform (K-S p=0.93), 100% within 90% CI, 50% within 50% CI

## Object-Level Findings

### Finding 1: Stock Direction Questions Are Correctly Handled

All 12 non-meta stock price binary questions predicted 47-55% (avg Brier 0.235). Expanded analysis (21 stock predictions with non-zero lean): 9 correct, 9 wrong — no better than chance. Agent correctly identifies these as near-coin-flips.

**However**: the agent over-researches stock questions. Example (RCL/41996): fetched stock_price, stock_history, 2 web searches for news/events, wrote detailed narrative analysis — producing 53% that's statistically indistinguishable from 50%. The prompt says "Simple stock direction questions need minimal research — fetch the data, run a simulation, output." The agent does narrative analysis instead of Monte Carlo.

**No change needed** — the output is correct (~50%), but process efficiency could improve. Not a priority since accuracy is already at the theoretical limit.

### Finding 2: Meta-Questions Show Genuine Skill

12 live meta-predictions averaged Brier 0.131 vs 0.25 random baseline. This is the agent's strongest category. Best: 41987 and 42014 (Brier 0.048 each).

### Finding 3: 42002 Meta Error — CP Data Failure

Worst meta question (Brier 0.302). Agent predicted 55% YES that CP would be above 47.00%, but CP stayed at/below threshold.

**Root cause: `get_cp_history` errored with 100% failure rate.** The agent only had a 4-day-stale CP snapshot ("47.00% as of 2026-02-01") from the question description — it could not see the actual CP trajectory.

**Evidence this was the critical gap (from trace explorer):**
- **42002 live** (no CP data): Brier **0.303** — agent reasoned from stale snapshot + underlying event fundamentals
- **42002 retrodict** (with CP data): Brier **0.144** — agent saw the downward trend and correctly forecast NO
- **41987 live** (with CP data): Brier **0.048** — agent discovered CP at 50% (above 46% threshold) via API
- **41998 live** (with CP data): Brier **0.073** — agent discovered CP at 26% (below 30% threshold) via API

When the agent has CP data, meta-predictions are excellent. When it doesn't, it falls back to event-level reasoning — exactly what the prompt warns against, but the agent had no alternative.

**Actionable**: Investigate why `get_cp_history` failed for question_id 41741. This is the highest-priority reliability fix.

### Finding 4: Resolution Criteria Pipeline — Not a Bug

Session 2 hypothesized the enrichment pipeline might have a bug preventing resolution_criteria from reaching Google Trends MC questions. **Investigation confirms**: resolution_criteria is `null` for ALL AutoQuestionsBot questions across both `/api/posts/` and `/api2/` endpoints, including the listing API. The data doesn't exist at source — AutoQuestionsBot generates questions programmatically without populating this field.

The v1.2.0 prompt-based approach (embedding DC semantics and change_stats in the tool output) is the correct mitigation. No pipeline fix possible.

### Finding 5: Google Trends MC — v1.2.0 Changes Untested

The worst-performing category (live MC log scores 0.92-1.61 for "Doesn't change" resolutions) was already addressed in v1.2.0 with:
- `change_stats` added to google_trends tool output
- MC guidance about DC resolution semantics and post-spike baseline behavior

No v1.2.0 forecasts exist yet. Need retrodictions to validate.

### Tool Failures
| Tool | Failure | Count | Fix |
|------|---------|-------|-----|
| resolution_criteria | Null for all AutoQuestionsBot Qs | All MC | Not fixable — data absent at source |
| get_cp_history | "Question not found" for meta Q | 1/1 in 42002 trace | Investigate: question_id vs post_id confusion? |
| meta-reflection | Missing for stock Qs | Multiple | Process gap (agent skips reflection on "simple" Qs) |

### Agent Capability Requests
- None explicit in the traces analyzed. The agent has the tools it needs; the issue was data absence (resolution_criteria) which v1.2.0 addresses through prompt guidance.

### Reasoning Quality Assessment
- **41996 (RCL, Brier 0.28)**: Sound reasoning, correct base rate, unnecessary narrative elaboration. Output correct.
- **42002 (DOJ meta, Brier 0.30)**: Good research, correct framework, wrong conclusion on a close call. CP stability at threshold wasn't weighted enough.
- **41987 (meta, Brier 0.048)**: Best meta question — had CP data, identified buffer size, made confident correct call.
- **Numeric forecasts**: Excellent across the board. No traces needed.

## Changes Made
| Level | Change | Rationale |
|-------|--------|-----------|
| None | No code/prompt changes this session | v1.2.0 changes haven't been tested yet; insufficient data for new interventions |
| Meta-meta | Confirmed resolution_criteria investigation | Closed the session 2 open question |

## Meta-Level Findings
- **Version tracking gap**: All live forecasts lack agent_version (generated before tracking was merged to main). Can't attribute live forecasts to specific versions. Retrodict forecasts have version correctly.
- **Missing meta-reflections**: Stock questions frequently skip the required meta-reflection. The agent treats them as too simple for the full process, but this means we can't track its self-assessment quality on these questions.

## Meta-Meta Findings
- **Trace explorer timeout**: The trace-explorer subagent ran 68 tool calls / 97K tokens but never produced a final report. Reading traces one-by-one exhausts context. Consider: have the trace explorer read tools-only summaries first, then deep-dive selectively.
- **Offline analysis is limited but viable**: With cached resolution data in `data/api_cache/`, calibration analysis works fully offline. The feedback loop command should document the `--offline` workflow.
- **Stock analysis yield**: Traces for stock questions confirmed the quantitative finding (random lean direction) but didn't reveal any new insights. Future sessions can skip stock traces unless calibration changes.

## Retrodiction Queue

v1.2.0 changes (change_stats + DC guidance) need testing. Queue Google Trends MC questions when online:

### Priority 1: Test v1.2.0 on Google Trends MC
```bash
# These resolved with "Doesn't change" — the category we're trying to improve
uv run forecast retrodict 42000 42005 42009
# These resolved with directional changes — verify we don't regress
uv run forecast retrodict 41992 42001 41965
```

### Priority 2: Non-meta binary diversity
Current binary calibration is dominated by stock questions (~50%) and meta questions. Need non-meta, non-stock binary retrodictions for better calibration assessment.
```bash
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 21
```

### Priority 3: Investigate get_cp_history failure
The 42002 trace showed `get_cp_history(question_id=41741)` returning no data for a question with 114 forecasters. This shouldn't happen. Test when API is available:
```bash
uv run python .claude/plugins/aib/scripts/debug.py metaculus --raw-only
```

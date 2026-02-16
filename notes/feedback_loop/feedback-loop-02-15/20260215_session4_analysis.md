# Feedback Loop Analysis: 2026-02-15 (Session 4 — Offline)

## Ground Truth Status
- Agent version analyzed: v1.1.0 retrodictions (v1.2.0 has 0 resolved forecasts)
- Total forecasts: 228 (110 live, 118 retrodict)
- Resolved: 162 (46 live, 116 retrodict)
- v1.1.0 resolved: 30 retrodictions (14 binary, 6 numeric, 10 MC)
- Binary Brier (v1.1.0, n=14): 0.186
- Numeric: 5/6 within 90% CI, avg norm_error=0.64
- Overall Binary ECE: 0.1533, underconfident (-0.15)

## Object-Level Findings

### Finding 1: MC "Doesn't Change" — Systematic Misunderstanding of Resolution Semantics

**This is the single most actionable finding across all four sessions.**

Three v1.1.0 "Doesn't change" retrodictions show the identical error pattern:

| Post | Topic | P(DC) | Log Score | Agent's Key Quote |
|------|-------|-------|-----------|-------------------|
| 41989 | thom tillis | 0.25 | 1.39 | "noise at low values makes exact stability unlikely" |
| 42006 | ilhan omar | 0.25 | 1.39 | "floor asymmetry makes Increases most likely" |
| 42009 | steve tisch | 0.20 | 1.61 | "Doesn't change is least likely since any small fluctuation registers" |

**Root cause (3 interacting errors):**

1. **Resolution semantics misunderstanding**: Agent treats "Doesn't change" as requiring exact integer equality. In reality, "Doesn't change" means ≤10% relative change — at low values (0-5), fluctuations of ±1 still qualify as "Doesn't change."

2. **Narrative construction overrides base rates**: Agent constructs catalyst stories (Super Bowl for tisch, court cases for omar, NC primary for tillis) that inflate P(Increases) at the expense of P(Doesn't change). These narratives sound compelling but represent low-probability events.

3. **Baseline persistence underweighted**: At values of 3-12 (post-spike baseline), the most likely outcome is staying at baseline — not continuing to decline or spiking again. Agent treats "near the floor" as evidence for directional movement when it's actually evidence for stability.

**v1.2.0 changes target exactly these errors:**
- `change_stats` in google_trends output provides empirical base rates
- Prompt guidance explains ≤10% relative change semantics
- "Post-spike baseline" guidance explains values at baseline stay at baseline

**Potential gap in change_stats**: The `_calculate_change_stats` function counts "no_change" as exact integer equality (point-to-point), but the resolution criterion compares values across the full period using a relative change threshold. These measure different things — point-to-point stability vs period-over-period stability. The `no_change_rate` from change_stats will undercount the true "Doesn't change" probability, especially at high values where ±10% covers multiple integers. If v1.2.0 retrodictions still underweight DC, consider computing a period-simulation metric instead.

**Key validation question**: Do v1.2.0 retrodictions on the same questions (queued in session 3) produce P(DC) > 0.40 instead of 0.20-0.25?

**Retrodict vs live comparison** shows data scarcity amplifies this error:
- 42005 (charles victor thompson): live log 0.14 vs retrodict log 0.97
- 42006 (ilhan omar): live log 0.60 vs retrodict log 1.39
- 42009 (steve tisch): live log 1.20 vs retrodict log 1.61

Live forecasts are consistently better on MC, likely because real-time web search provides richer context about baseline stability.

### Finding 2: MC "Directional Change" Retrodictions Show Genuine Skill

Counterpoint to Finding 1 — when the resolution IS a directional change, the agent performs well:

| Post | Topic | Resolution | Log Score |
|------|-------|------------|-----------|
| 41965 | gov't shutdown | Decreases | 0.20 |
| 41992 | helicopter | Increases | 0.43-0.84 |
| 42001 | ilhan omar net worth | Decreases | 0.69-0.80 |

The agent correctly identifies directional changes when they happen. The problem is specifically under-weighting "Doesn't change" — not poor directional reasoning.

### Finding 3: Worst Meta-Predictions Are Genuine Close Calls

Two worst v1.1.0 meta retrodictions were close-call questions where the agent was slightly on the wrong side:

- **41387** (Dems House, CP>9%): P(YES)=35%, resolved YES. CP was at exactly 9.00% — right at the threshold. Agent's reasoning was sound (downward trend, strict inequality), but CP crossed.
- **39935** (Mamdani, CP>91%): P(YES)=40%, resolved YES. CP at 0.90, just below 0.91 threshold. Agent ran Monte Carlo, got 38%, adjusted to 40%.

Both forecasts show correct meta-prediction methodology: CP-position-relative-to-threshold analysis, trajectory assessment, forecaster-count volatility. The errors are within the expected noise band — P(YES)=35-40% means you expect to be wrong 35-40% of the time. No systematic fix needed.

### Trace Explorer Findings (supplementary)

The trace explorer (57 tool calls, 317s, 7 traces read) confirmed all findings above and added:

- **Agent explicitly states it doesn't know the DC threshold**: "The critical question is how exactly resolution works. Without explicit resolution criteria, I need to think about what 'change' means in Google Trends context." — seen in all 5 MC traces.
- **41989 ran 4 times**: DC probability improved from 10% to 25% across attempts — agent learns from data but never reaches the right level without knowing the threshold.
- **42005 was best MC trace** (log=-0.97) because agent noticed integer granularity at near-zero: "at near-zero levels, Google Trends has coarse integer resolution." This naturally led to higher DC probability (38%).
- **Agent violates "Trust your computation" in 42006**: Simulation produced P(Increase)=57.6%, P(DC)=24.2%, P(Decrease)=18.2%, but agent manually adjusted to I:45%, DC:25%, D:30%.
- **All 7 traces CLEAN** — no future leaks detected. Retrodict infrastructure working correctly.
- **web_search returned zero results in every call across all 5 MC retrodict traces** (~30+ calls total). Blind mode is devastating for MC context.

### Tool Failures
| Tool | Failure | Count | Fix |
|------|---------|-------|-----|
| web_search (retrodict) | Empty results for all queries | All MC retrodict (30+ calls) | Expected — blind mode limits to pre-cutoff data |
| resolution_criteria | Null from Metaculus API | All MC | Not fixable — AutoQuestionsBot omits it |
| No new failures | — | — | — |

### Agent Capability Requests
- None identified in v1.1.0 traces. The agent has the tools it needs; the issue is resolution semantics understanding, which v1.2.0 addresses through prompt guidance + tool output.

### Reasoning Quality Assessment
- **MC "Doesn't change"**: Systematic error — agent consistently assigns 20-25% to the most likely outcome. v1.2.0 should fix this.
- **MC directional**: Good. Agent correctly identifies changes when they happen (log scores 0.20-0.84).
- **Meta-predictions**: Strong. Worst cases are close calls at thresholds, not reasoning failures.
- **Numeric**: Excellent. 5/6 within CI, near-zero errors on matched predictions.
- **Binary (non-meta, non-stock)**: Too few v1.1.0 samples (1: 41892, LDP Japan, Brier 0.16). Need more diversity.

## Prompt Health Audit

**Verdict: No rewrite needed. Prompt is structurally healthy.**

Assessed the 549-line `src/aib/agent/prompts.py`:
- No patchwork or addendum feel — reads as a coherent document
- v1.2.0 MC additions (MULTIPLE_CHOICE_GUIDANCE lines 456-478) are well-integrated
- Meta-Predictions section is long (45 lines) but justified by being the highest-error category
- Common Mistakes section has 2 intentional repetitions (status quo, meta event-reasoning) that serve as reminders
- `_RETRODICT_ADDENDUM` is empty — retrodict restrictions are tool-level, which is correct
- No contradictions between sections

**One structural observation**: Step 2 (Classification) doesn't list "Google Trends MC" as a question type. The agent classifies these ad-hoc. Not a functional problem because `MULTIPLE_CHOICE_GUIDANCE` is injected based on API question_type regardless of agent classification, but worth noting for a future rewrite.

**Patch count since last rewrite**: 1 (v1.2.0 MC guidance). Well below the >3 threshold that would trigger Priority 0 evaluation.

## Meta-Level Findings
- **Version tracking gap persists**: All 110 live forecasts have `agent_version: unknown`. Can't attribute live performance to specific versions. Only retrodict forecasts are versioned.
- **MC log scores not surfaced by extremes command**: `scores_table.py extremes --type multiple_choice` produces no output. The extremes command likely only supports binary/numeric. Need to add MC support or use csv directly.

## Meta-Meta Findings
- **Trace explorer still context-hungry**: The subagent is reading raw logs which are 60K+ tokens each. Session 3 noted the same issue. The forecast JSON files contain enough information for pattern analysis — the agent's reasoning, probabilities, and tool metrics are all there. Reading full logs should be reserved for investigating specific tool failures, not pattern recognition.
- **Session 3's retrodiction queue was completed**: All queued retrodictions (42000, 42005, 42009, 41992, 42001, 41965) were run as v1.1.0. But v1.2.0 retrodictions for the same questions haven't been run yet — that's the critical comparison.
- **Offline sessions have diminishing returns**: Sessions 3 and 4 analyzed the same data with similar findings. Without new retrodictions (especially v1.2.0), further offline sessions on this data won't yield new insights.

## Changes Made
| Level | Change | Rationale |
|-------|--------|-----------|
| None | No code/prompt changes this session | v1.2.0 changes must be validated with retrodictions before further modifications |
| Meta-meta | Deepened MC failure mode analysis | Confirmed the exact error pattern v1.2.0 targets |

## Retrodiction Queue

### Priority 1: v1.2.0 Validation on "Doesn't Change" (CRITICAL)

These are the same questions v1.1.0 scored worst on. Run with v1.2.0 to validate the change_stats + resolution semantics guidance:

```bash
# "Doesn't change" resolutions — must show P(DC) > 0.40 to validate v1.2.0
uv run forecast retrodict 41989 42005 42006 42009 42000
```

### Priority 2: v1.2.0 Directional Change Validation

Verify v1.2.0 doesn't regress on directional changes while improving DC:

```bash
# Directional resolutions — should maintain log scores < 1.0
uv run forecast retrodict 41992 42001 41965
```

### Priority 3: Non-Meta, Non-Stock Binary Questions

Current binary calibration is dominated by stock (~50%) and meta questions. Need diversity:

```bash
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 21
# Select 3-5 non-meta, non-stock binary questions with confirmed resolutions
```

### Priority 4: Investigate get_cp_history failure (from session 3)

Still unresolved — the 42002 trace showed `get_cp_history(question_id=41741)` returning no data for a question with 114 forecasters.

```bash
# When API is available:
uv run python .claude/plugins/aib/scripts/debug.py metaculus --raw-only
```

## Session Exit Criteria Assessment
1. [x] Calibration assessed for current version (v1.1.0 analyzed; v1.2.0 has no data)
2. [x] Trace analysis completed (direct reading of forecast JSONs + trace explorer for logs)
3. [ ] Changes made — none warranted; v1.2.0 validation pending
4. [x] Analysis document written
5. [x] Retrodictions queued

## Recommendation for Next Session

**Run v1.2.0 retrodictions before the next feedback loop session.** The highest-value action is validating whether `change_stats` + resolution semantics guidance fixes the MC "Doesn't change" error. Without this data, further analysis on existing v1.1.0 data is circular.

The next session should be **online** and focused on:
1. Running Priority 1-2 retrodictions
2. Comparing v1.1.0 vs v1.2.0 scores on the same questions
3. If v1.2.0 validates: queue broader retrodictions and consider merging to main
4. If v1.2.0 doesn't improve: investigate whether the agent ignores the guidance or the guidance is insufficient

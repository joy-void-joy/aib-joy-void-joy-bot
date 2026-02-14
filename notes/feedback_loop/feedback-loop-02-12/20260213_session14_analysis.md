# Feedback Loop Analysis: Session 14 — 2026-02-13

## Ground Truth Status
- 10 new retrodictions from v0.10.0 (binary + numeric)
- v0.10.0 binary Brier: avg 0.348 (n=5) — regression from v0.3.1's 0.238 (n=24)
- v0.10.0 numeric: 5/6 within CI, one major miss (MSFT EPS)
- Root cause identified: negative caching bug in CP history + catastrophic meta-prediction failure

## Object-Level Findings

### Bug Fix: Negative Caching in _ensure_post_id
**Impact:** Catastrophic for meta-predictions — single 429 rate limit cached None permanently, breaking all subsequent CP history calls for the entire session.

**Fix:** Only cache successful resolutions. Use MetaculusClient.fetch_post_json (has retry) for initial post_id validation instead of raw httpx.

### Regression Analysis: v0.10.0 vs v0.3.1

Cross-version comparison on same questions:
- v0.3.1: avg Brier 0.238 (n=24), range 0.122-0.49 — consistently moderate
- v0.10.0: avg Brier 0.348 (n=5), driven by 41391 (Brier 0.72)
- v0.10.0 non-meta binary: avg 0.149 (excellent)
- The regression is almost entirely from one catastrophic meta-prediction

### Key finding: v0.3.1's advantage was consistency, not brilliance
v0.3.1 never exceeded 0.49 Brier on any question. v0.10.0 has higher peaks but also a 0.72 disaster. The consistency principle was added to the prompt.

### Worst forecast: 41391 (shutdown meta, Brier 0.72)
- CP history tool failed (returned empty due to negative caching bug)
- Agent fell back to event-level reasoning: "shutdown risk is high → CP above 33.3%"
- Forecast 85% when resolution was NO
- v0.3.1 on same question: 0.70, Brier 0.49 (still worst, but less catastrophic)

### Best forecast: 41521 (UNGA Venezuela, Brier 0.048)
- Deep research: found precedents (Panama 1989, Grenada 1983) and counter-precedent (Iraq 2003)
- Identified absence of evidence (no draft resolution after 8 days)
- Confident directional call based on structural analysis

### MSFT EPS miss (all versions)
All versions forecast $3.85-3.91, resolution was $5.16. GAAP vs non-GAAP mismatch with one-time items. Prompt guidance strengthened for ambiguous metric definitions.

### Tool Failures
| Tool | Failure | Count | Fix |
|------|---------|-------|-----|
| get_cp_history | Empty due to negative caching | 2/10 | Fixed _ensure_post_id |
| Metaculus API | 429 rate limits | Frequent | Already has retry; caching fix prevents cascading |

### Reasoning Quality Assessment
- 41521 (Brier 0.048): Excellent — deep research, precedent + counter-precedent, structural analysis
- 41417 (Brier 0.25): Good — stock direction correctly defaults to 50%
- 41391 (Brier 0.72): Failed — event-level reasoning for meta-prediction, catastrophic
- 39935 (Brier 0.36): Moderate — correct direction but too confident without CP data

## Meta-Level Findings

### Prompt Rewrite from First Principles (v0.10.1 → v0.11.0)

Session 14's major contribution: full system prompt rewrite.

**Why a rewrite was needed:**
- Meta-prediction section had accumulated 3 patches (CP-unavailable, hedging exception, "50% is OK")
- These patches read as addendums, not integrated guidance
- The prompt's decision tree for meta-predictions didn't match the reasoning pattern that produced our best forecasts

**Key changes in the rewrite:**
1. Added "Consistency over brilliance" to Core Principles
2. Restructured Meta-Predictions as strongest section — "The Central Rule" + integrated CP handling
3. Added "When tools fail, deepen research" principle
4. Renamed "Nothing Ever Happens" → "Status Quo Persistence" (clearer)
5. Integrated hedging exception naturally (no "Exception:" patch)
6. Integrated CP-unavailable handling into meta-prediction section
7. Added "Event-level reasoning for meta-predictions" to Common Mistakes
8. Tightened NUMERIC_GUIDANCE EPS wording

**What the rewrite preserved:**
- All research phases (unchanged)
- Resolution criteria parsing (unchanged)
- Logit scale and factor system (unchanged)
- Meta-reflection structure (unchanged)
- All concrete examples (UNGA, product launches, etc.)

## Meta-Meta Findings (Feedback Loop Infrastructure)

### Updates to feedback-loop.md

Added **Priority 0: Evaluate Prompt Health** to Phase 4:
- When to rewrite vs patch (decision criteria)
- How to do a principled rewrite (5-step process)
- When NOT to rewrite

Added to Anti-Patterns: "Exception:" clauses and conditional patches as things to avoid.

Added Key Question #10: "Is the prompt accumulating patches?"

Added to Periodic Maintenance: "Prompt health audit" every 5-10 sessions.

Added "Track patch count" to Priority 4.

### Process Improvement
The prompt rewrite process itself should be documented as a reusable skill:
1. Study best traces → extract success patterns
2. Study worst traces → identify structural reasoning failures
3. Read full current prompt → identify patches and complexity
4. Rewrite from scratch → monolithic, coherent document
5. Test → 209/209 tests pass

## Changes Made
| Level | Change | Rationale |
|-------|--------|-----------|
| Object | Fixed negative caching bug in _ensure_post_id | CP history permanently broken by transient 429s |
| Object | Full prompt rewrite (v0.11.0) | Accumulated patches; meta-prediction section needed restructuring |
| Object | Added "consistency over brilliance" principle | v0.3.1 outperformed by never being catastrophically wrong |
| Object | Added "when tools fail, deepen research" | Best traces showed this pattern |
| Meta | Updated test for renamed section | "Apply Calibration" → "Calibration" |
| Meta-Meta | Added Priority 0 (Prompt Health) to feedback-loop.md | Rewrite process wasn't documented |
| Meta-Meta | Added patch tracking to feedback-loop.md | Prevent silent patch accumulation |
| Meta-Meta | Added prompt health to periodic maintenance | Regular structural review |

## Retrodiction Queue

Blocked by 429 rate limits during this session. The `forecast_queue.py missed` command
needs to run when Metaculus API is available.

```bash
# Run when rate limits clear:
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 14
# Then retrodict the resolved ones to test v0.11.0
```

The primary goal for next session's retrodictions: test v0.11.0's meta-prediction handling
on questions where v0.10.0 failed (especially meta-predictions where CP might be unavailable
or near the threshold).

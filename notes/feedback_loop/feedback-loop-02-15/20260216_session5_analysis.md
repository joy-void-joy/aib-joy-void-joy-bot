# Feedback Loop Analysis: 2026-02-16 (Session 5 — Offline)

## Focus: Unversioned Live vs v1.1.0 Retrodict on MiniBench Overlap

18 questions have both an unversioned live forecast (Feb 1-7) and a v1.1.0 retrodiction (Feb 15). This session compares reasoning, failure modes, and prompt differences.

## Ground Truth Status
- Unversioned live: 46 resolved forecasts (no version tag — made before versioning existed)
- v1.1.0 retrodictions: 30 resolved (14 binary, 6 numeric, 10 MC)
- Overlapping questions: 18 (7 MC, 6 binary, 5 numeric)

## Score Comparison on Overlapping Questions

### MC Questions (LogScore, lower = better)

| Post | Topic | Res | Live P(correct) | Live LogS | Retro P(correct) | Retro LogS | Winner |
|------|-------|-----|-----------------|-----------|-------------------|------------|--------|
| 41965 | gov shutdown | Decrease | 0.40 | 0.92 | 0.82 | 0.20 | **Retro** (4.6× better) |
| 41989 | thom tillis | DC | 0.30 | 1.20 | 0.15 | 1.90 | **Live** |
| 41992 | helicopter | Increase | 0.20 | 1.61 | 0.43 | 0.84 | **Retro** |
| 42001 | ilhan omar NW | Decrease | 0.20 | 1.61 | 0.50 | 0.69 | **Retro** |
| 42005 | CVT | DC | 0.87 | 0.14 | 0.38 | 0.97 | **Live** (6.9× better) |
| 42006 | ilhan omar | DC | 0.55 | 0.60 | 0.25 | 1.39 | **Live** |
| 42009 | steve tisch | DC | 0.30 | 1.20 | 0.20 | 1.61 | **Live** |

**MC subtotal: Live wins 3, Retro wins 3.** But the wins cluster by resolution type — live wins all "Doesn't change" resolutions, retro wins all directional resolutions.

### Binary Questions (Brier, lower = better)

| Post | Topic | Res | Live Brier | Retro Brier (best) | Winner |
|------|-------|-----|------------|---------------------|--------|
| 41987 | CP higher | yes | 0.048 | 0.160 | **Live** |
| 41994 | CP higher | no | 0.203 | 0.109 | **Retro** |
| 41999 | CP higher | yes | 0.102 | 0.144 | **Live** |
| 42002 | CP higher | no | 0.303 | 0.144 | **Retro** |
| 42011 | NVDA stock | yes | 0.270 | 0.250 | **Retro** (close) |
| 42014 | CP higher | yes | 0.048 | 0.029 | **Retro** |

**Binary subtotal: Live wins 2, Retro wins 4.**

### Overall: v1.1.0 retro scores better on 7/13, live better on 6/13. But the FAILURE MODES are completely different.

---

## Failure Mode Analysis

### Live (unversioned) failure mode: Hedging / flat distributions

The live agent spreads probability too evenly when evidence strongly points one direction.

**Example — 41965 (gov shutdown, resolved Decrease):**
- Live: {Increase: 0.25, DC: 0.35, Decrease: 0.40} — nearly flat
- Retro: {Increase: 0.08, DC: 0.10, Decrease: 0.82} — strong conviction
- Interest was AT ITS PEAK (100). Retro recognized decrease was nearly certain. Live hedged.

**Example — 42001 (ilhan omar net worth, resolved Decrease):**
- Live: {Increase: 0.35, DC: 0.45, Decrease: 0.20} — put MOST weight on wrong answer
- Retro: {Increase: 0.25, DC: 0.25, Decrease: 0.50} — correctly favored Decrease

The live agent's "Nothing Ever Happens" prior from the old prompt made it conservative on ALL MC options, including when strong decay signals said directional change was obvious.

### v1.1.0 failure mode: Systematically underweighting "Doesn't change"

The retro agent treats "Doesn't change" as requiring exact integer stability. At low Google Trends values (0-5), this is wrong — ±1 fluctuations at baseline still resolve as "Doesn't change."

**Example — 42005 (CVT, resolved DC):**
- Live: {Increase: 0.12, DC: **0.87**, Decrease: 0.01} — correctly maxed DC
- Retro: {Increase: 0.12, DC: 0.38, **Decrease: 0.50**} — saw 1→0 trajectory, bet on Decrease

Live reasoning: "current value ~1, already at baseline floor, minimal room to decrease further"
Retro reasoning: "clear exponential decay pattern from spike, trajectory predicts continued decline to 0"

Both saw the same data. Live correctly recognized that AT THE FLOOR, stability dominates. Retro saw the decay trend and projected it further, not realizing 1→0 still counts as "Doesn't change."

**Example — 42006 (ilhan omar, resolved DC):**
- Live: {Increase: 0.40, DC: **0.55**, Decrease: 0.05}
- Retro: {**Increase: 0.45**, DC: 0.25, Decrease: 0.30}

Live correctly identified: "Baseline value is ~3, making Decreases nearly impossible (would need negative values)." This threshold arithmetic is the key insight.

Retro constructed a narrative: "Floor effect creates upward asymmetry — much more room to increase than decrease." This narrative sounds smart but inflates P(Increase) at the expense of P(DC), which is the most common outcome at baseline.

---

## Prompt Comparison

### What the old prompt had that v1.1.0 lost

The old prompt (active during unversioned live forecasts) contained:

```
## Google Trends Questions
1. Anchor on the provided starting value
2. Search interest follows predictable patterns:
   - Peaks during active news events
   - Decays exponentially after peak (half-life ~3-7 days)
   - Rebounds before scheduled events
3. ±3 point thresholds are sensitive — current values matter enormously
4. Search for upcoming events in the forecasting window
5. Large forecaster bases create stability
```

The v1.1.0 prompt had NO Google Trends guidance — just a one-line tool listing:
```
- google_trends / google_trends_related: Search interest, public attention trends
```

The v1.1.0 MC guidance was minimal:
```
Before forecasting, consider:
(a) Time left until resolution
(b) Status quo outcome if nothing changes
(c) An unexpected scenario that could shift the outcome
Leave moderate probability on most options.
```

**Critical missing insight**: "±3 point thresholds are sensitive — current values matter enormously." This one line encodes the threshold arithmetic that makes the live agent so much better at DC. When value=3 and threshold=±3, "Decreases" requires <0 (impossible) and "Increases" requires >6 (unlikely without catalyst). DC has the widest possible range: [0,6]. The old prompt taught this; v1.1.0 didn't.

### What v1.1.0 gained

| Feature | Impact |
|---------|--------|
| "Trust your computation" principle | +++ (meta-predictions improved, Monte Carlo used correctly) |
| Explicit step-by-step framework (Parse → Classify → Research → Calibrate) | ++ (structured reasoning) |
| Phase-based tool guide | ++ (systematic research) |
| "Decompose across ambiguity" | + (numeric question improvement) |
| Meta-prediction section (50 lines, very detailed) | +++ (best category for v1.1.0) |
| Removed subagent overhead | + (simpler architecture) |

### Reasoning similarity

Both versions follow the same high-level pattern:
1. Check Google Trends data
2. Research the topic
3. Consider upcoming events / catalysts
4. Assess decay patterns
5. Forecast

The WEIGHTING is where they diverge:
- **Live agent** weights prompt heuristics heavily → better at pattern matching ("this looks like a baseline stability case")
- **Retro agent** weights research findings heavily → constructs narratives from news search → sometimes led astray by speculative catalysts

The live agent made 2-3 tool calls per MC question. The retro agent made 8-12. More research didn't help — it provided more narrative ammunition for speculative scenarios ("DOJ investigation could produce news," "Super Bowl could revive coverage") that inflated P(Increase) at the expense of P(DC).

---

## What v1.2.0 Already Addresses

The changes in commit 881473a directly target the MC DC failure:

1. **`change_stats` in google_trends output** — provides empirical base rates for Increase/Decrease/DC
2. **"Resolution semantics for Doesn't change"** — explains that low-value fluctuations resolve as DC
3. **"Post-spike decay" guidance** — values at baseline stay at baseline

These are good but may not be sufficient. See recommendations below.

## Recommendations

### 1. Add threshold arithmetic as an explicit step

Before any narrative reasoning on MC Google Trends questions, the agent should compute:
```
Current value: X
Threshold: ±3 (or ±10% relative)
P(Decrease) requires: end < X-3 → [compute if possible]
P(Increase) requires: end > X+3 → [compute what catalyst needed]
P(DC) covers: [X-3, X+3] → [compute width relative to plausible range]
```

This turns the old prompt's "thresholds are sensitive" intuition into a mechanical step that can't be overridden by narratives.

### 2. Add "compute first, narrate second" for MC

The v1.1.0 agent constructs catalyst narratives BEFORE checking if the quantitative base rates even support directional movement. Reorder: get `change_stats`, compute threshold arithmetic, THEN research catalysts only if the base rates suggest directional movement is plausible.

### 3. Don't regress on directional conviction

v1.1.0's best wins (gov shutdown: LogS=0.20, ilhan omar NW: LogS=0.69) come from having strong conviction when data clearly shows directional movement. v1.2.0 must keep this — "Trust your computation" is working for clear signals. The fix for DC underweighting should NOT create a new bias toward DC.

### 4. Keep research depth proportional to uncertainty

For Google Trends MC questions where threshold arithmetic clearly identifies one outcome (e.g., value=1 → DC near-certain), extensive web search adds noise, not signal. The `change_stats` should serve as a confidence check — if empirical DC rate is >50% AND threshold arithmetic favors DC, further research is low-value.

### 5. Validate with retrodiction

The critical test: run v1.2.0 on 42005, 42006, 42009, 41989 (DC resolutions) AND 41965, 42001, 41992 (directional resolutions). If v1.2.0 scores better on DC without regressing on directional, the changes are validated.

## Retrodiction Queue

Priority 1: v1.2.0 validation (same as session 4):
```bash
uv run forecast retrodict 41989 42005 42006 42009 42000 41992 42001 41965
```

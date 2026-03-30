# Audit Report: 7 Forecasts Across 2 Versions

**Post IDs**: 42701, 42303, 42710, 42726, 42693, 42707, 42700
**Versions**: v3.5.0 (1), v4.0.0 (6)
**Current version**: v4.1.0
**Date**: 2026-03-29

## Per-Question Overview

| Post ID | Version | Type | Forecast | Resolution | Brier/Score | Peer Score | Error Type |
|---------|---------|------|----------|------------|-------------|------------|------------|
| 42701 | 4.0.0 | MC | 80% Decreases | Doesn't change | LogS 2.12 | -96.8 | Overconfident |
| 42303 | 3.5.0 | discrete | median +8.5 | -1 (GS+1) | AbsErr 9.5 | -62.8 | Directionally wrong |
| 42710 | 4.0.0 | binary | 65% YES | NO | Brier 0.42 | -34.1 | Info already priced in |
| 42726 | 4.0.0 | binary | 34% YES | YES | Brier 0.44 | -22.4 | Momentum extrapolation |
| 42693 | 4.0.0 | binary | 46% YES | YES | Brier 0.29 | -9.6 | Good forecast |
| 42707 | 4.0.0 | binary | 40% YES | YES | Brier 0.36 | -2.5 | Good forecast |
| 42700 | 4.0.0 | binary | 53% YES | NO | Brier 0.28 | -1.0 | Good forecast |

## Post-Mortem (Resolved Questions)

### Post 42701: "Freeze Watch" Google Trends (v4.0.0, peer -96.8)

- **Forecast**: 80% Decreases, 12% Doesn't change, 8% Increases
- **Resolution**: Doesn't change
- **Error type**: Overconfident
- **What happened**: The agent observed a rapid spike decay (100→51→12 over 2 days from a "March megastorm") and predicted near-certain return to baseline (1-3) by March 27. A secondary freeze event hit on March 27 — freeze warnings and frost advisories were issued across 7 states (KS, MO, IL, KY, VA, WV, IN) with temperatures as low as 21°F. This pushed "freeze watch" search interest back to approximately 10-15, within ±3 of the March 17 value of 12.
- **Where reasoning diverged**: The agent correctly identified this tail risk ("weather unpredictability: another freeze event could occur within 10-day window") but assigned only 20% combined probability to non-Decreases outcomes. The key miscalibration: two separate freeze spikes had already occurred within 3 weeks (Feb 22 and Mar 15), demonstrating that late-season freeze events were more common than the agent's seasonality model assumed. The agent treated the per-day freeze probability as very low, but the cumulative probability over a 10-day window was materially higher.
- **What would have helped**: A medium-range weather forecast tool (10-day outlook) would have shown the incoming cold front. The `weather_forecast` tool (Open-Meteo) was added in v4.1.0 specifically for this type of question.
- **Google Trends normalization**: Confirmed NOT an artifact. The March 15 megastorm (~200M people affected) remained the scale anchor at 100. The March 27 event (~10-20M) produced a normalized value of ~10-15, consistent with its smaller scope.

### Post 42303: SDS vs GS Seat Difference — Slovenian Election (v3.5.0, peer -62.8)

- **Forecast**: Median +8.5 seats (SDS wins more), P10 = +1, P90 = +17
- **Resolution**: -1 (GS won 29 seats, SDS won 28)
- **Error type**: Directionally wrong — stale polling data
- **What happened**: The agent forecast on March 2, when all polls showed SDS leading by 3.5-11pp. Between March 2 and the election on March 22, the race shifted ~8 percentage points due to the **Black Cube scandal** — leaked recordings revealed that Israeli private intelligence firm Black Cube had met directly with Janša at SDS headquarters. Slovenia's intelligence agency (SOVA) confirmed foreign interference. This reframed leaked corruption allegations from damaging Golob to damaging Janša on sovereignty grounds. Final polls (Mar 16-20) showed GS leading or tied.
- **Where reasoning diverged**: The agent noted the 2022 polling miss for GS but dismissed it since "GS is now the incumbent, less likely to benefit from new-party effect." The reasoning was partially correct (GS didn't benefit from a new-party premium) but wrong about direction: GS still surged late, just from a different catalyst. The D'Hondt seat model was methodologically sound — the error was entirely in the vote share input.
- **What would have helped**: A wider polling uncertainty (5-6pp std instead of 3.5pp) would have captured this outcome more comfortably. The CDF contained the actual result at ~P5, so it wasn't impossible in the model — just heavily downweighted. Election-specific guidance requiring research of country polling accuracy history was added in v4.0.0+.

### Post 42710: CP > 30% for US Negative GDP (v4.0.0, peer -34.1)

- **Forecast**: 65% YES
- **Resolution**: NO (CP stayed ≤30%)
- **Error type**: Information already priced in
- **What happened**: The CP was exactly at 30.00% with +6pp momentum over 2 weeks, driven by the US-Iran conflict and oil shock. The agent ran weighted Monte Carlo simulations across drift scenarios, producing ~67% probability. But the CP stabilized at/below 30% — the sharp recent rise was itself evidence that the geopolitical shock was already incorporated into forecaster expectations.
- **Where reasoning diverged**: The agent correctly identified "information may already be priced in" as a factor (logit -0.5, confidence 0.6) but underweighted it. The summary noted this weakness: "Could have weighted the 'information already priced in' factor more heavily given the sharp recent CP move." The weighted Monte Carlo used 20% weight for "full momentum continuation" which was too optimistic.
- **What would have helped**: The v4.1.0 "CP Momentum and Mean-Reversion" prompt section explicitly warns: "Sharp recent momentum shows diminishing returns" and "Treat the most recent weekly change rate as an upper bound on future drift, not the expected rate."

### Post 42726: ERIE Stock Up (v4.0.0, peer -22.4)

- **Forecast**: 34% YES (price goes up)
- **Resolution**: YES (ERIE closed higher on March 27/28 than $240.37 on March 20)
- **Error type**: Momentum extrapolation at extremes
- **What happened**: ERIE was down 44.6% from its 52-week high, just 1.17% above its 52-week low. The agent used 30-day empirical drift of -0.62%/day in Monte Carlo simulations, producing P(higher) = 27-34%. The conditional base rate tool showed 65% positive at comparable drawdown levels, but the agent discounted this heavily for macro headwinds (Iran conflict, oil >$100, recession risk). The stock bounced from these oversold levels.
- **Where reasoning diverged**: The agent over-extrapolated recent negative momentum. At 1.17% above the 52-week low, mean reversion forces are empirically strong — the conditional base rate of 65% at this drawdown level was the more reliable signal. The 30-day drift parameter was contaminated by the very selloff that created the extreme positioning.
- **What would have helped**: Prompt guidance that conditional base rates at 52-week extremes should receive at least equal weight to recent drift parameters. The current HEAD adds bidirectional sensitivity testing but the momentum guidance ("over short horizons, trends persist") may reinforce the error.

### Post 42693: TEL Stock Up (v4.0.0, peer -9.6)

- **Forecast**: 46% YES
- **Resolution**: YES
- **Error type**: Good forecast (mildly underconfident)
- **What happened**: TEL was down ~19% from its 52-week high amid severe macro headwinds. The agent balanced a conditional base rate of 54.7% (at 15%+ drawdown) against Iran conflict, oil shock, and tariff headwinds, arriving at 46%. The stock recovered.
- **Where reasoning diverged**: N/A — well-calibrated. The 8pp gap between forecast (46%) and outcome (100% YES) is within normal calibration range for a ~50% prediction.
- **What would have helped**: N/A — the methodology was sound.

### Post 42707: CP > 61% for Fujimori Runoff (v4.0.0, peer -2.5)

- **Forecast**: 40% YES
- **Resolution**: YES (CP went above 61%)
- **Error type**: Good forecast (borderline)
- **What happened**: The CP had dropped from 67% to exactly 61% in one week. The agent correctly identified the threshold asymmetry (even staying flat = NO) and downward momentum. But Keiko's strong fundamentals (2nd place, 3/3 runoff track record) supported a CP in the 55-65% range, and the CP reversed its decline.
- **Where reasoning diverged**: Marginal. The 40% estimate was reasonable given the evidence. The Grozo scandal may have helped stabilize Keiko's positioning as the agent speculated.
- **What would have helped**: Better CP reversal base rates. The v4.1.0 mean-reversion guidance is minimally relevant here — the agent was already appropriately cautious.

### Post 42700: BR Stock Up (v4.0.0, peer -1.0)

- **Forecast**: 53% YES
- **Resolution**: NO (BR dropped to ~$157 by March 28, down from ~$179 on March 17)
- **Error type**: Good forecast
- **What happened**: BR was down 34% from its 52-week high. The agent balanced conditional base rates (65% positive at this drawdown) against severe macro headwinds, arriving at 53%. The macro headwinds won.
- **Where reasoning diverged**: Minimal. The 53% estimate correctly reflected near-maximum uncertainty about direction.
- **What would have helped**: N/A — this was well-calibrated.

## What Has Been Fixed

### Weather-Dependent Terms (fixes 42701)
- **Issue**: Agent had no weather forecast capability and couldn't assess probability of secondary weather events in the resolution window
- **Seen in**: post 42701 (v4.0.0), where a 7-state freeze event on March 27 invalidated the "Decreases" prediction
- **Fixed by**: `weather_forecast` tool added via Open-Meteo (no API key required). Prompt guidance for weather-dependent Google Trends questions: "A separate weather system can re-spike search interest days after a prior spike has decayed."
- **Diff**: `src/aib/agent/prompts.py` (weather-dependent terms guidance), `src/aib/agent/tool_policy.py` (weather_forecast tool registration)

### CP Momentum Mean-Reversion (fixes 42710)
- **Issue**: Agent extrapolated CP momentum linearly (+6pp/2wk → continued rise), over-weighting recent trend
- **Seen in**: post 42710 (v4.0.0), predicted 65% YES for CP crossing 30%, CP stayed ≤30%
- **Fixed by**: New "CP Momentum and Mean-Reversion" prompt section. Key guidance: "Sharp recent momentum shows diminishing returns — a +6pp movement in one week is more likely to produce +2pp the following week than another +6pp." Also: "Treat the most recent weekly change rate as an upper bound on future drift, not the expected rate."
- **Diff**: `src/aib/agent/prompts.py` (meta-prediction guidance subsection)

### Election Polling Error Guidance (fixes 42303)
- **Issue**: Agent used polling averages without researching country-specific polling accuracy
- **Seen in**: post 42303 (v3.5.0), where polls overestimated SDS lead by ~8pp
- **Fixed by**: Election-specific prompt guidance: "search for historical polling accuracy in the relevant country" and "your simulation's standard deviation must be at least as wide as the country's recent polling error magnitude." Also added prediction markets as contrarian check.
- **Diff**: `src/aib/agent/prompts.py` (election guidance section), added between v3.5.0 and v4.0.0, refined through v4.1.0

## What Remains Unaddressed

### Momentum Over-Extrapolation at 52-Week Extremes
- **Issue**: When stocks are near 52-week lows, the agent over-weights recent negative drift from Monte Carlo simulations and under-weights the conditional base rate from drawdown analysis. The 30-day drift parameter is contaminated by the very selloff that created the extreme positioning.
- **Seen in**: post 42726 (v4.0.0) — conditional base rate showed 65% positive but agent discounted to 34%
- **Partially addressed**: HEAD adds bidirectional sensitivity testing
- **Recommendation** (type: principle): Add prompt guidance for stocks within 5% of 52-week extremes. When the conditional base rate from drawdown analysis diverges significantly from Monte Carlo drift projections, the conditional base rate should receive at least equal weight. Rationale: mean reversion at extremes is well-documented across equity markets, and recent drift parameters at these levels systematically overstate continuation probability because they are measured during the selloff itself.

## Strengths to Preserve

### Conditional Base Rate Tool
- Provides essential quantitative anchoring that pure Monte Carlo misses
- **Seen in**: posts 42693 (54.7% at 15%+ drawdown, 137 episodes), 42700 (65% at 30%+ drawdown, n=20), 42726 (similar analysis)
- **Status in current**: Preserved — `stock_conditional_returns` tool unchanged in v4.1.0
- The best stock forecasts (42693, 42700) used this tool's output as a primary anchor. The worst (42726) had the right signal but over-discounted it.

### Factor Decomposition with Logit Weighting
- Every forecast has explicit factors with logit magnitude, confidence, and direction. Creates an auditable reasoning chain.
- **Seen in**: all 6 v4.0.0 forecasts — consistent structure, no double-counting detected in any trace
- **Status in current**: Preserved — factor model unchanged

### Multi-Source Research Strategy
- Agent consistently triangulates across multiple data sources: stock tools (price, history, conditional returns), news (AskNews), prediction markets (Polymarket, Manifold, Kalshi), economic data (FRED), and reference sources (Wikipedia)
- **Seen in**: 42710 (16 tools, 101 calls), 42726 (16 tools, 124 calls), 42707 (14 tools, 57 calls)
- **Status in current**: Preserved and enhanced (weather tools added)

### Monte Carlo Simulations with Multiple Drift Scenarios
- Rather than a single simulation, agent runs multiple scenarios (zero drift, recent drift, dampened drift, extreme regime) and weights them. Methodologically sound even when the result is wrong.
- **Seen in**: 42726 (27%/34%/28% across scenarios), 42693 (19%/42%/50%/55%), 42700 (35%/44%/50%/58%)
- **Status in current**: Preserved — sandbox execution unchanged

## Version Delta Summary

### v3.5.0 → v4.1.0 (1 forecast: 42303)

Large gap. Key changes:
- **Election guidance**: Polling error research requirement, simulation std floor, prediction market contrarian check (added in v4.0.0, refined through v4.1.0)
- **CDF construction**: Tail interpolation halfpoint change, PMF redistribution algorithm (numeric.py rewrite)
- **Reviewer restructuring**: From workflow/reasoning ratings to classification/risk_flags/reviewer_estimate
- **Impact on 42303**: HEAD would likely produce a wider CDF that captures the actual outcome, primarily from mandatory polling error research

### v4.0.0 → v4.1.0 (6 forecasts: 42701, 42710, 42726, 42693, 42707, 42700)

Medium gap. Key changes:
- **Weather tools**: `weather_forecast` added via Open-Meteo (directly fixes 42701)
- **CP mean-reversion**: New subsection warning against momentum extrapolation (directly fixes 42710)
- **Reviewer restructuring**: ForecastSummary model changed from workflow/reasoning ratings to classification/risk_flags/strengths/weaknesses
- **Metrics reset**: `reset_metrics()` called at session start
- **Impact**: Clear improvement for 42701 and 42710; no significant impact on 42693, 42707, 42700; partially addresses 42726

## Recommended Actions

1. **Prompt guidance for 52-week extreme stocks** — type: principle — evidence: 1/3 stock traces (42726)
   - When a stock is within 5% of its 52-week low/high and the conditional base rate diverges from Monte Carlo drift projections, add explicit prompt guidance requiring the conditional base rate to receive at least equal weight. The Monte Carlo drift at extremes is biased by the move that created the extreme.

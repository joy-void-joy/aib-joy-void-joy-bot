# Meta-Reflection: Netanyahu CP Meta-Prediction

**Post ID**: 40966 (underlying) / Meta-question about CP threshold
**Date**: 2026-02-04
**Final Forecast**: ~27% probability that CP > 30% on Feb 11

## Executive Summary

This is a meta-prediction asking whether the Metaculus community prediction for "Will Netanyahu cease to be PM in 2026?" will exceed 30% on Feb 11. The CP is currently at 26%, having dropped from 30% at question launch (Feb 1). With 787 forecasters and a downward trend, the CP would need to reverse course and gain 4+ percentage points in 7 days.

## Research Audit

### Searches Performed
1. **get_metaculus_questions** - Got current CP (26%) and forecaster count (787)
2. **get_cp_history** - Failed (wrong ID format - needs question_id not post_id)
3. **polymarket_price** - No relevant markets found
4. **manifold_price** - Found several markets at 39-44%
5. **WebSearch x3** - Got coalition status, election timing, recent news

### Most Informative Sources
- Metaculus API: Current CP at 26% (crucial - below threshold)
- Manifold Markets: ACX 2026 question at 39% (significant gap with Metaculus)
- Times of Israel liveblog: Phase 2 negotiations starting Feb 4

## Reasoning Quality Check

### Strongest Evidence FOR my forecast (CP stays below 30%)
1. CP has already dropped from 30% → 26% (4pp decline in 3 days)
2. 787 forecasters creates significant inertia
3. No immediate coalition-breaking catalyst despite fragility

### Strongest Evidence AGAINST my forecast
- Manifold markets are 13-18pp higher than Metaculus CP
- Phase 2 ceasefire negotiations starting today could create news
- Smotrich threatening to leave if ceasefire continues
- Cross-platform arbitrage could pull Metaculus CP upward

### What a smart disagreer would say
"The gap between Manifold (39-44%) and Metaculus (26%) is huge. As sophisticated forecasters notice this discrepancy, they'll update toward market prices. Plus, phase 2 negotiations starting today create immediate news risk that could stress the coalition."

### Calibration Check
- **Question type**: Meta-prediction (forecasting forecaster behavior)
- **Skepticism applied**: Yes - I'm skeptical of dramatic CP swings in short timeframes
- **Uncertainty calibrated**: Moderate uncertainty; the Manifold gap is a real factor but recent CP decline argues against reversal

## Subagent Decision

Did not use subagents. This is a short-horizon meta-prediction where:
- The key data (current CP, forecaster count, market prices) is quickly obtainable
- Research findings inform each other (current CP level → determines what news would matter)
- No complex calculations needed

Subagents would add overhead without proportional benefit.

## Tool Effectiveness

- **get_metaculus_questions**: Provided critical current CP (26%)
- **get_cp_history**: Failed - needed question_id (40674) not post_id (40966). Documentation unclear.
- **polymarket_price**: No relevant markets (expected - Netanyahu PM isn't a typical Polymarket topic)
- **manifold_price**: Very useful - showed 13-18pp gap with Metaculus
- **WebSearch**: Effective for current news context

## Process Feedback

### Guidance that matched well
- "Meta-prediction: Model the forecasters, not the underlying event"
- Focus on current CP, forecaster count, and catalysts

### Missing guidance
- Better documentation for question_id vs post_id distinction in get_cp_history
- Would benefit from guidance on typical CP drift rates for different forecaster counts

## Calibration Tracking

- **80% CI**: CP on Feb 11 will be between 22% and 35%
- **Update triggers**:
  - +10% if coalition collapses this week
  - +5% if Smotrich formally leaves coalition
  - -5% if phase 2 negotiations proceed smoothly

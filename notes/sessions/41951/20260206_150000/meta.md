# Meta-Reflection: Gorton and Denton By-Election Forecast

**Post ID:** 41951
**Question:** Which Party will win the 2026 Gorton and Denton by-election?
**Date:** 2026-02-06
**Election Date:** 2026-02-26 (20 days away)

## Executive Summary

Final forecast: Green Party 50%, Reform UK 32%, Labour 15%, Other 3%

This is a three-way race with significant uncertainty. The Green Party has emerged as the betting market favorite after initially trailing Reform. The race is notable for Labour's self-inflicted damage in blocking Andy Burnham from standing, combined with their historic national unpopularity.

## Research Audit

### Searches Performed
1. **Web search for polls and candidates** - Very useful, found poll numbers and candidate list
2. **Polymarket search** - Found link but no direct market on this specific election
3. **Manifold search** - Found market showing Greens favored over Labour (70% probability Greens beat Labour)
4. **Betting odds search** - MOST useful source, found current exchange and bookmaker prices
5. **Candidate background search** - Useful for understanding Reform's Matt Goodwin selection

### Most Informative Sources
- OLBG betting odds article: Gave clear odds table (Green 8/11, Reform 6/4, Labour 11/2)
- Betfair Exchange prices: Green 1.88, Reform 3.0, Labour 6.4
- Search result snippets with polling data (Reform 30%, Labour 27%, Greens 17% in one poll)

### Data Gaps
- Wikipedia article blocked (403 error)
- Couldn't access detailed Electoral Calculus projections
- No direct Polymarket market found for this specific election

## Reasoning Quality Check

### Strongest Evidence FOR my forecast (Green favored):
1. **Betting markets consensus** - Multiple bookmakers and Betfair Exchange all have Greens as clear favorites (~50-57% implied)
2. **Vote splitting dynamics** - In a three-way race, Greens can win with ~30% if Labour and Reform split the rest
3. **Burnham blocking** - Massive self-own by Labour that depressed their chances significantly

### Strongest Evidence AGAINST my forecast:
1. **Raw polling shows Reform leading** - One poll: Reform 30%, Labour 27%, Greens 17%
2. **Greens have never held this seat** - Winning a "safe Labour" seat would be historic
3. **Matt Goodwin is high-profile** - His media presence could drive turnout for Reform

### What would a smart disagreer say?
"The betting markets are overreacting to recent trends. Labour has deep roots in Manchester, the polling shows Reform actually leading, and by-election surprises often favor the opposition party with the most momentum - which is Reform, not Greens."

### What evidence would change my mind?
- New poll showing Reform with clear lead (35%+)
- High-profile endorsement of Reform candidate
- Labour internal polling showing recovery
- Green ground game problems emerging

### Calibration Check
- **Question type:** Predictive (which party will win future election)
- **"Nothing Ever Happens" applicable?** Partially - Labour holding would be the "status quo" outcome
- **Am I overconfident in Greens?** Possibly - markets might be overreacting to trends

I've adjusted slightly toward Labour (15%) from pure market-implied (13-14%) to account for incumbency and "nothing ever happens" bias.

## Subagent Decision

Did not use subagents. This question is:
- Time-sensitive (closes today at 17:00 UTC)
- Primarily requires market/polling research, not complex analysis
- Well-served by web searches and market price lookups

Subagents would add latency without significant benefit.

## Tool Effectiveness

**Worked well:**
- WebSearch: Found comprehensive polling and betting data in snippets
- Manifold price lookup: Found relevant market
- OLBG WebFetch: Successfully extracted odds table

**Tool limitations (not failures):**
- Wikipedia WebFetch: 403 error (access blocked)
- Several news site WebFetch: 403 errors
- Polymarket: No specific market for this UK by-election

**Actual capability gap:**
- No direct API access to UK betting exchanges for real-time prices

## Process Feedback

**Prompt guidance that worked:**
- "Prefer programmatic access over page parsing" - markets gave cleaner data than trying to scrape news
- Market price integration guidance was helpful

**Would do differently:**
- Could have searched more specifically for "Electoral Calculus Gorton" or "YouGov MRP" for model-based projections

## Calibration Tracking

**Confidence:** 70% confident my forecast is within 10pp of true probabilities for each option

**80% CI for Green Party win probability:** [40%, 60%]

**Update triggers:**
- New constituency poll: would update ±5-10pp depending on results
- Major campaign news/scandal: ±5-10pp
- Endorsement from Burnham: would significantly boost whoever he endorses

# Meta Reflection: Ground Transportation CO2 Emissions Change 2020-2025

**Post ID**: 5680 (original) / 41843 (AIB tournament)
**Question**: By how much will carbon dioxide emissions change from ground transportation globally between 2020 and 2025?
**Final Forecast**: Median ~+17%, with 80% CI of +10% to +24%
**Confidence Level**: Medium-high - good data trail but final 2025 numbers not yet published

## Executive Summary

This question asks for the percentage change in global ground transportation CO2 emissions from 2020 (the COVID low) to 2025. My analysis indicates a likely increase of 15-20%, driven by post-COVID recovery that brought emissions back to near-2019 levels by 2022, followed by slower growth through 2025 as EV adoption accelerates.

## Research Audit

### Searches Run (Value Assessment)
1. **Carbon Monitor website** - Low value (interactive data not extractable via WebFetch)
2. **IEA transport data** - Medium value (confirmed 2022 transport ~8 Gt, recovery trends)
3. **Web searches on transport emissions** - High value (found year-over-year growth rates)
4. **PMC paper on Carbon Monitor 2022** - High value (found ground transport growth: +8.8% 2021, +2.5% 2022)
5. **ICCT/energynews forecasts** - Medium value (2025 expected to peak at ~9 Gt)
6. **Metaculus search** - Low value (found original question but no CP available)

### Most Informative Sources
- Carbon Monitor scientific paper (PMC10010646): Ground transport growth rates +8.8% (2020→2021), +2.5% (2021→2022)
- IEA transport data: 2024 road emissions ~6 Gt, 8% above 2015, growth averaged 0.2% annually 2019-2024
- Climate TRACE: Jan 2025 transport -1.57% vs Jan 2024, indicating slowdown/peaking

## Reasoning Quality Check

### Strongest Evidence FOR my forecast (+15-20%)
1. Carbon Monitor's published year-over-year data shows +8.8% and +2.5% growth in 2021-2022
2. IEA confirms transport emissions nearly returned to 2019 levels by 2022
3. ICCT projects 2025 as the peak year for road transport emissions
4. 2020 was an anomalous COVID low point - any reasonable recovery implies double-digit percentage increase

### Strongest Argument AGAINST my forecast
- A smart disagreer might argue: "EV adoption accelerated faster than expected in 2023-2025, especially in China. This could have dampened recovery more than historical trends suggest."
- Evidence that would change my mind: If Carbon Monitor data shows 2024-2025 ground transport declining year-over-year (not just slowing growth), I would revise down to +10-15%.

### Calibration Check
- **Question type**: Measurement (definitional at resolution - "what value will Carbon Monitor report?")
- **Skepticism applied**: This is a measurement question about a near-certain recovery scenario. "Nothing Ever Happens" doesn't apply - COVID disruption was real and recovery is well-documented.
- **Uncertainty calibration**: Main uncertainty is in extrapolating 2023-2025 without exact Carbon Monitor data. I've widened my interval to account for methodological variations and final revisions.

## Subagent Decision

I did NOT use subagents for this forecast.

**Justification**: The research was relatively straightforward - sequential searching to find growth rates and trends. Each finding informed the next search (e.g., finding Carbon Monitor paper led to searching for 2023-2025 data). Parallelization would not have helped since I needed to understand the baseline methodology before searching for specific years.

For a more complex question (e.g., multiple independent factors), I would have spawned deep-researcher and link-explorer in parallel.

## Tool Effectiveness

### Tools that worked well
- **WebSearch**: Found multiple sources with year-over-year data
- **get_metaculus_questions**: Confirmed original question details
- **mcp__forecasting__search_metaculus**: Found related questions

### Actual tool failures
- None - all tools returned results or empty results as expected

### Tools with empty results (expected behavior)
- **WebFetch** on carbonmonitor.org: Site uses interactive JavaScript, so CSS/structure returned without actual data values
- **WebFetch** on energynews.pro: 403 Forbidden (site blocks bots)
- **Statista**: Paywall blocked exact figures

### Capability gaps
- No direct API access to Carbon Monitor's downloadable data files
- Would be useful to have a tool that can execute JavaScript-rendered pages

## Process Feedback

### Prompt guidance that matched well
- Resolution criteria parsing was critical - understanding "January 2020 to December 2025" meant full-year comparison
- The recommendation to check prediction markets was helpful (though none found for this specific question)

### What I'd do differently
- Start by searching for academic papers using Carbon Monitor data rather than trying to fetch the website directly
- The scientific papers (PMC) had the most precise year-over-year figures

## Calibration Tracking

- **80% CI**: +10% to +24%
- **Comparable past forecasts**: Similar to other post-COVID recovery measurement questions
- **Update triggers**:
  - +5%: If Carbon Monitor shows 2024-2025 growth stronger than 1%
  - -5%: If Carbon Monitor shows 2024-2025 decline or EV impact was substantial

## Key Calculation Summary

Starting from 2020 baseline = 100:
- 2021: 100 × 1.088 = 108.8 (Carbon Monitor data)
- 2022: 108.8 × 1.025 = 111.5 (Carbon Monitor data)
- 2023: 111.5 × 1.025 = 114.3 (estimated, based on overall transport +4%)
- 2024: 114.3 × 1.015 = 116.0 (estimated, based on transport +1.2%)
- 2025: 116.0 × 1.01 = 117.2 (estimated, emissions peaking)

**Central estimate: +17%**

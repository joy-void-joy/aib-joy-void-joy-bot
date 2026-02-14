# Meta-Reflection: US Inflation 2022 (Post 8901)

## Executive Summary
Post 8901 asks for US inflation in 2022. No explicit resolution criteria given, but likely annual average CPI-U YoY. Published Dec 11, 2021, just after Nov CPI showed 6.8% YoY. My forecast: median ~6.7%, with P10=4.8% and P90=8.8%.

## Evidence Assessment
**Strongest FOR higher inflation (>6%):**
- Mechanical carryover: even zero monthly inflation yields 3.6% annual average
- Q4 2021 MoM running at 0.83% — extraordinary momentum
- Shelter inflation lag: market rents surged 15-20% in 2021, OER/rent CPI lags 12-18 months
- Tight labor market driving wage pressures
- Consensus had systematically underestimated inflation throughout 2021

**Strongest AGAINST (for lower inflation):**
- Fed was pivoting hawkish (taper acceleration, rate hikes planned)
- Used car prices expected to normalize
- Supply chains expected to heal
- Fiscal stimulus winding down
- Historical mean reversion of inflation

**What a smart disagreer would say:** The consensus of professional forecasters (~4-5% CPI) reflected genuine structural analysis. Supply bottlenecks WOULD ease, used cars WOULD normalize, and the Fed tightening cycle would bite. My estimate is anchored too much on momentum and not enough on mean reversion.

**My counter:** The consensus was consistently wrong throughout 2021. Shelter catch-up alone (a mechanical, lagging process) virtually guaranteed elevated readings. The high MoM base entering 2022 creates a very high floor.

## Tool Audit
- FRED data worked well — got actual CPI index values for 2020-2021
- Metaculus search found the question successfully
- search_exa and web_search returned empty results (retrodict mode limitations)
- Monte Carlo simulation in sandbox worked smoothly
- The analyst subagent produced good analysis but couldn't access tools; the researcher subagent was similarly limited

## Subagent Decision
Used both researcher and analyst subagents. The researcher couldn't access search tools effectively in retrodict mode. The analyst produced useful qualitative analysis from training knowledge but couldn't use FRED tools. In hindsight, doing the FRED queries directly was more effective. The subagents were somewhat redundant here.

## Calibration
- Question type: Measurement/numeric forecast
- Am I hedging? My median of 6.7% is notably above the Dec 2021 consensus (~4-5%) but below what actually happened (~8.0%). This seems reasonably calibrated for the information available.
- The 80% CI of [4.8, 8.8] seems appropriate — wide enough to capture both aggressive deceleration and persistence scenarios.
- I'm NOT hedging toward 50th percentile in a binary sense; I'm taking a directional position that inflation would be higher than consensus expected.
- What would move my forecast: specific supply shock information (e.g., geopolitical events), Fed meeting outcomes, monthly CPI releases in early 2022.

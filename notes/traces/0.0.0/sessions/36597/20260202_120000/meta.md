# Meta Reflection: Mounjaro Q1 2026 Revenue Forecast

## Executive Summary
- **Question**: What will be the reported Q1 2026 global revenue for Mounjaro?
- **Final Forecast**: Central estimate ~$7.0B, with 80% CI roughly $5.8B-$8.3B
- **Confidence**: Medium - Strong historical data trajectory, but Q4 2025 not yet reported

## Research Process

### Strategy
1. Started by gathering historical quarterly revenue data for Mounjaro
2. Calculated YoY and sequential growth rates to understand trajectory
3. Searched for analyst consensus estimates for 2026
4. Checked prediction markets (none found)
5. Looked for recent news affecting supply/demand

### Most Valuable Sources
- Eli Lilly's official investor relations releases (Q1, Q2, Q3 2025 earnings)
- CNBC and Fierce Pharma coverage of earnings
- JP Morgan Healthcare Conference coverage (Jan 2026)

### Key Data Points Found
| Quarter | Revenue | YoY Growth |
|---------|---------|------------|
| Q1 2024 | $1.81B | - |
| Q3 2024 | $3.11B | - |
| Q4 2024 | $3.50B | - |
| Q1 2025 | $3.84B | +112% |
| Q2 2025 | $5.20B | +68% |
| Q3 2025 | $6.52B | +109% |
| Q4 2025 | ~$7.5B est | TBD (Feb 4) |

### Searches That Didn't Help
- No specific Q1 2026 analyst estimates found
- No relevant prediction markets on Polymarket or Manifold

## Tool Effectiveness

### High Value
- **WebSearch**: Excellent for gathering historical earnings data and analyst commentary
- **execute_code**: Useful for calculating growth rates and projections systematically

### Moderate Value
- **WebFetch**: Some pages returned only JavaScript/structure, not article content

### Not Helpful
- **Prediction markets**: No relevant markets for this specific question

## Reasoning Quality

### Strongest Evidence
1. Consistent ~100-110% YoY growth in recent quarters
2. Supply constraints have eased, enabling continued growth
3. Q1 2025 showed no seasonal dip from Q4 2024
4. Tirzepatide became world's best-selling drug franchise

### Key Uncertainties
1. Q4 2025 not yet reported (Feb 4, 2026)
2. Degree of growth rate moderation as base gets larger
3. Exact impact of international expansion timing
4. Competition dynamics with Novo Nordisk

### "Nothing Ever Happens" Application
- This doesn't strongly apply here - Mounjaro's growth trajectory is well-established with concrete evidence
- However, I'm moderating growth rate expectations from ~109% to ~75% as the base gets larger
- Maintained wide confidence intervals given the timing uncertainty

## Calibration Notes

### Confidence Level
Medium-high confidence in the central estimate, but appropriately wide intervals because:
- Q4 2025 earnings (Feb 4) will provide crucial information
- Growth rate moderation magnitude is uncertain
- The question closes the same day as today

### What Would Change My Forecast
- Q4 2025 earnings (if available before close) showing unexpected acceleration or deceleration
- Any supply disruption news
- Major pricing/reimbursement changes

## System Design Reflection

### Tool Gaps
- Would benefit from a dedicated financial data tool (FactSet, Bloomberg terminal access) for consensus estimates
- Real-time SEC filing parser would help for investor relations content

### Subagent Friction
- For this relatively straightforward financial forecasting question, didn't need subagents
- Direct research was sufficient given clear data sources

### Prompt Assumptions
- The guidance worked well for this type of question
- Financial/earnings forecasts have a clear research path

### What Should Exist
- Integrated financial data feeds for company earnings/guidance
- Automatic detection of related Metaculus questions on same company/product

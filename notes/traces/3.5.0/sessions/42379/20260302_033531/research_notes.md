# Q42379: Russia Google Trends Interest Change (Mar 2 - Mar 14)

## Key Data Points

### Resolution Window (Feb 12 - Mar 14, tz=0, geo=US)
- Mar 2 value: 95 (near ceiling of 100)
- Peak: 100 (Feb 13, Feb 15)
- Min: 62 (Feb 25-27)
- Volatility: daily std ~14 points, trailing ~10.5

### Threshold
- ±3 for "Doesn't change" → need end value in [92, 98]
- "Increases": > 98
- "Decreases": < 92

### Empirical 12-day Changes (Resolution Window, n=7)
- From high starts (95-100): ALL decreased (-25 to -38)
- From low starts (76-78): ALL increased (+9 to +19)
- No "Doesn't change" outcomes

### Conditional Base Rates (Longer Series, High Starts ≥59, n=12-13)
- Decreases: 83-85%
- Doesn't change: 8%
- Increases: 8%

### Monte Carlo Results
- Mean-reverting MC: Dec 76%, DC 12%, Inc 11%
- Bootstrap MC: Dec 47-50%, DC 7-8%, Inc 43-46%
- Strong negative autocorrelation (-0.459) → mean reversion

### News Context
- Abu Dhabi peace talks scheduled early March (likely Mar 3-7)
- Russia may walk away if Ukraine doesn't cede territory
- Olympics queries fading (Winter Olympics ended ~Feb 22)
- Active war coverage ongoing
- 4th anniversary of invasion just passed (Feb 24)

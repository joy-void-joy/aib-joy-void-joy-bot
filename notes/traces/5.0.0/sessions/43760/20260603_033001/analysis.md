# MSTR mNAV Analysis - June 3, 2026

## Current State
- MSTR closing price (June 2): $136.08 (down 9.15% on day)
- BTC price: ~$66,070-$69,800 (crashed from $74K)
- Market cap: ~$48.7B
- Fixed EV component (debt+preferred-cash): ~$21.35B (from strategy.com May 29 data)
- Current mNAV estimate: 1.19-1.25 (depends on exact BTC price at MSTR close)

## Key Structural Insight
mNAV = (MC + Fixed) / (BTC_Holdings × BTC_Price)

The fixed debt/preferred component (~$21B) means:
- When both BTC and MSTR drop together, mNAV INCREASES
- mNAV only drops when MSTR underperforms BTC significantly
- For mNAV < 1.0: Need MSTR 25%+ decline from current if BTC flat

## Monte Carlo Results (500K sims, fat-tailed, bearish drift)
- rho=0.75: P(mNAV < 1.0) = 0.32%
- rho=0.50: P(mNAV < 1.0) = 2.35%
- rho=0.90: P(mNAV < 1.0) = 0.01%

## Threshold Analysis
- MSTR needs to drop to ~$102 (-25%) with BTC flat for mNAV < 1.0
- Or MSTR -15% + BTC +10% -> mNAV = 0.97
- Both scenarios require significant MSTR/BTC decorrelation

## Estimate: ~3% probability

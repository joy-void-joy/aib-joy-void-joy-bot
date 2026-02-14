# Feedback Loop Analysis: Session 13 (2026-02-13)

## Ground Truth Status
- Binary Brier: 0.2600 (17 forecasts), ECE 0.1076, MCE 0.2650
- Numeric PIT: 50% CI coverage 89% (target: 50%) — distributions systematically too wide
- Version comparison: v0.3.1 (0.2382, n=40) > v0.9.1 (0.3313, n=10) > v0.8.1 (0.4048, n=8)

## Object-Level Findings

### Critical Discovery: CP Over-Anchoring
When the agent retrieves CP history for meta-predictions, performance is **3x WORSE**
(Brier 0.534 with CP data vs 0.181 without). Root cause: the v0.9.1 prompt said "CP
trajectory is far more informative than reasoning about the event itself," causing agents
to build Markov chain models from small CP samples (~20-40 data points). These models
create false precision.

### Tool Failures / Bugs Fixed
| Tool | Issue | Fix |
|------|-------|-----|
| FRED (fred_series) | User-provided observation_end bypassed retrodict cutoff via `or`-fallback | Enforce cutoff unconditionally when set |
| search_news | No retrodict cutoff enforcement (AskNews API lacks date filtering) | Exclude from retrodict mode entirely |
| fetch (retrodict) | 77% failure rate in retrodict mode | Known issue — Wayback Machine coverage gaps |

### Future Leak Found
- **Question 41419**: FRED tool returned Jan 14 data despite Jan 6 retrodict cutoff
- Agent explicitly passed `observation_end: "2026-01-14"` which bypassed the cutoff
- Root cause: `end_date = validated.observation_end or reference_date.isoformat()` — the
  `or` let user-provided dates override cutoff

### Reasoning Quality
- Best v0.3.1 patterns: "50% base + directional adjustment" for meta-predictions,
  Monte Carlo from empirical volatility for stocks, confidence-weighted factor system
- Worst v0.3.1 patterns: narrative-driven reasoning on stock questions, anchoring on
  stale analyst consensus with too-narrow distributions

## Meta-Level Findings

### Prompt Rewrite
Complete rewrite from first principles based on v0.3.1 analysis. Key additions:
- Detailed resolution criteria parsing (1a-1d) with edge case identification
- Nothing Ever Happens with concrete domain examples (products, geopolitics, personnel)
- Precedent Skepticism four-step check with counter-precedent search
- Meta-prediction guidance warning against quantitative models from small CP samples
- Numeric calibration section addressing over-wide distributions
- Comprehensive meta-reflection template

### Tool Schema Standardization
Replaced plain dict schemas (`{"query": str}`) with `Model.model_json_schema()` across
all 25 tools. Added usage examples to tool descriptions for spawn_subagents (6 patterns),
search_exa, wikipedia, get_cp_history, fred_series, fred_search, company_financials,
stock_price, stock_history, polymarket_price, search_arxiv, execute_code.

### SubagentOutput Refactor
Replaced manual field-by-field copying from ForecastOutput to SubagentOutput with direct
embedding of ForecastOutput. The main agent now gets full reasoning traces from subquestions
instead of just summary + numbers.

## Meta-Meta Findings

### Analysis Process
- Reading v0.3.1 traces was the highest-value activity — identified specific patterns
  that produced good calibration (Monte Carlo, 50% base for meta)
- CP over-anchoring discovery came from version-stratified Brier analysis, not from
  reading individual traces — aggregate analysis has unique value

### Updates Made
- Tool descriptions now include usage examples (in code, not prompt)
- spawn_subagents examples show multi-subquestion decomposition patterns
- All tool input schemas use proper Pydantic model_json_schema()

## Changes Made
| Level | Change | Rationale |
|-------|--------|-----------|
| Object | FRED cutoff enforcement | Future leak in retrodict (41419) |
| Object | search_news retrodict exclusion | No date filtering available |
| Object | System prompt full rewrite | v0.3.1 had best Brier; detailed prompts work better |
| Object | Meta-prediction guidance rewrite | CP over-anchoring 3x worse |
| Object | Numeric calibration guidance | PIT shows 89% coverage at 50% CI |
| Object | SubagentOutput → embed ForecastOutput | Main agent lost reasoning/factors for subquestions |
| Meta | Tool schemas → model_json_schema() | Agent gets proper field descriptions and constraints |
| Meta | Tool description examples | Agent learns calling patterns from examples |
| Meta-Meta | This analysis document | Documents findings for next session |

## Retrodiction Queue

See below — queued for next session to validate v0.9.2 changes.

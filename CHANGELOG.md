# Changelog

Agent version history. Each version tracks a behavioral change in the forecasting agent.

## v3.6.0 (2026-03-11)

Unified market search; reflection and prompt quality improvements; reviewer adversarial check
- prompts: reframe factors as scaffolding — agent owns its probability, factors organize evidence
- prompts: rewrite reflection guidance as prose (adversarial reasoning, calibration check, tool audit, update triggers)
- prompts: add Threshold Questions guidance (model continuous quantity first, derive crossing probability)
- prompts: add sensitivity testing guidance for numeric questions
- prompts: soften "trust your computation" to encourage distributional variants via additional simulations
- prompts: add small-CP-sample warning to meta-predictions section
- tools: add unified prediction market search across Polymarket, Manifold, and Kalshi with relevance filtering
- tools: fix Wikipedia URL-encoding bug in direct article handler (unquote titles)
- reviewer: add adversarial reasoning check (warn when assessment lacks counterarguments)
- MC question reflection with softmax gap metrics
- file-based trace reading for reasoning condensation
- CDF + numeric bounds + score fields in forecast output
- baseline score computation
- reviewer verdict recovery and already-happened hardening

## v3.5.1 (2026-03-06)

Fix "already happened" trap: reviewer verdict recovery, pre-publication enforcement, prompt hardening
- reflection: recover reviewer verdict from ToolUseBlock fallback when StructuredOutput fails
- reflection: add logging at silent auto-approve and escape-hatch decision points
- reflection: strengthen reviewer pre-publication guidance — discard pre-pub factors, enumerate non-exceptions
- prompts: harden "already happened" rule — "absolute rule", enumerate known rationalizations

## v3.5.0 (2026-03-02)

Reviewer independently assesses probability and flags disagreements; CLI supports question metadata overrides
- reviewer probability assessment with WebSearch access
- CLI --description/--resolution-criteria/--fine-print overrides
- trace output line wrapping

## v3.4.0 (2026-02-27)

conditional MC guidance with directional-change-specific Google Trends instructions and resolution mechanism uncertainty
- directional-change guidance only injected when MC options match
- Google Trends tz=0 and date-range matching instructions
- SerpAPI vs pytrends measurement uncertainty guidance
- improved post-spike decay model for active topics
- small-sample-size base-rate caveat

## v3.3.0 (2026-02-27)

regime detection, rate futures enrichment, and reviewer distribution checks
- fred_series: adds `regime_stats` via backward-expansion regime detection on all series
- fred_series: adds `rate_futures` with market-implied rate path from Fed Funds futures for known interest rate series (DTB4WK, FEDFUNDS, SOFR, etc.)
- reflection: adds `precision` metric (range/|center|) to NumericDistributionMetrics
- reviewer: adds regime-spanning data window check for numeric/discrete forecasts
- prompts: adds regime-aware data window guidance and rate futures centering for short-horizon interest rate questions

## v3.2.0 (2026-02-24)

structured reviewer gate; enhanced fetch_url with data extraction; stock and Trends analysis tools
- reviewer: structured verdicts (approve/warn/fail) with gate that blocks StructuredOutput until approved
- fetch_url: extracts embedded page data (Next.js state, JSON script tags, global state) from JS pages
- stock_price: adds summary_stats (drawdown, trailing returns, volatility, recent low/high)
- stock_conditional_returns: empirical forward return distributions conditioned on drawdown magnitude
- google_trends: adds tail_stats for regime detection (stable tail, peak/trough, trailing volatility)
- removes standalone Playwright browser tools and TodoWrite in favor of data-focused tooling

## v3.0.0 (2026-02-19)

structured reflection with reviewer sub-agent; type-specific forecast models; enhanced trace output
- reflection tool: per-outcome breakdown, trace-as-file, focused reviewer sub-agent
- type-specific forecast model factories with supports/conditional fields on Factor
- enhanced build_trace and create_forecast_model wiring in core agent
- pretty-print JSON tool results with field truncation
- source tracking extracted to dedicated module
- google_trends gains tz and custom date ranges
- fetch pipeline returns page titles and relevant links
- submission formats supports field and prepends reasoning to comments

## v2.1.0 (2026-02-18)

fetch pipeline returns page titles and relevant links; source extraction handles augmented web search; first-person condensed reasoning
- fetch_url extracts titles via trafilatura metadata and surfaces follow-up links
- source extraction distinguishes augmented vs plain tool results
- condensed reasoning uses first-person voice with variable length
- reasoning comment includes last agent text block
- loop interval reduced to 10min

## v2.0.0 (2026-02-18)

Unified fetch/search pipeline, versioned trace storage, World Bank tools
- Devtools: deleted 9 obsolete one-off scripts
- added migration commands

## v1.3.0 (2026-02-18)

rewrite meta-prediction prompt to reduce 50% anchoring
- remove hedging check carve-out for meta-predictions
- replace structurally-balanced framing with CP-data-drives-the-forecast
- add retry on CP history failure
- add with_retry to _fetch_aggregation

## v1.2.0 (2026-02-15)

Google Trends tool: add change_stats to output; MC prompt: resolution semantics for directional questions
- google_trends now includes period-over-period change statistics (increase/decrease/no_change counts and rates)
- MC guidance explains Doesn't change resolution semantics at low values

## v1.1.0 (2026-02-14)

Remove subagent infrastructure, keep only spawn_subquestions
- delete spawn_subagents tool and all subagent types (researcher
- analyst
- premortem)
- remove subagents.py module
- remove 15 dead Pydantic output models from models.py
- simplify prompts and composition server

## v1.0.0 (2026-02-14)

feedback loop: prompt rewrite, subagent fixes, scoring improvements
- principle-based prompt rewrite
- fine_print redaction
- norm_error metric
- subagent stream fixes
- aggregation API fix

## v0.11.0 (2026-02-14)

Rewrite meta-prediction prompt: principle-based guidance, trajectory skepticism, event-level fallacy hard stop
- remove prescriptive ranges
- add structural balance principle
- add case study

## v0.10.0 (2026-02-14)

Reverted to stable version with user-controlled version bumps.
- Added "trust your computation" principle
- Added momentum vs mean-reversion guidance
- Required user approval for version bumps

## v0.9.2 (2026-02-13)

Full system prompt rewrite from first principles.
- Restructured meta-prediction section
- Added "consistency over brilliance" principle
- Added "when tools fail, deepen research" principle
- Renamed "Nothing Ever Happens" to "Status Quo Persistence"

## v0.8.1 (2026-02-13)

Bug fixes for v0.8.0.

## v0.8.0 (2026-02-13)

Prompt refinements and calibration improvements.

## v0.7.1 (2026-02-13)

Minor version bump for calibration tweaks.

## v0.6.0 (2026-02-13)

System prompt and subagent ontology rewrite.
- New subagent structure (researcher, analyst, premortem, subquestion)
- Hedging reduction guidance
- Meta-prediction improvements

## v0.5.0 (2026-02-12)

Sandbox architecture change: replaced one-shot exec with persistent REPL.

## v0.4.0 (2026-02-11)

Documentation update and tool improvements.

## v0.3.1 (2026-02-09)

Baseline version with calibration data. Most retrodiction data comes from this version.

## v0.3.0 (2026-02-09)

First version with AGENT_VERSION tracking in forecasts.

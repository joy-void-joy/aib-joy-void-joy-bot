# Changelog

Agent version history. Each version tracks a behavioral change in the forecasting agent.

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

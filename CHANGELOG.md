# Changelog

Agent version history. Each version tracks a behavioral change in the forecasting agent.

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

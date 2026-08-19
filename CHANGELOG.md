# Changelog

Agent version history. Each version tracks a behavioral change in the forecasting agent.

## v7.2.0 (2026-08-18)

Govern each session by the fields that actually bound it
- agent: every session states its own autonomy instead of all eight opening at `bypassPermissions`. Six read and answer at `ask`; the worldview fixer mutates its store at `accept_edits`; the forecaster keeps `unattended` for the Docker sandbox and its own notes
- agent: the tool roster moves to `tools` — the field that bounds a session — from `allowed_tools`, which the SDK documents as auto-approval that explicitly does not restrict. Measured against a live session: a roster of `Read` at `bypassPermissions` cannot reach the shell
- agent: the hand-built PreToolUse allowlist hook is gone. It stood in for the roster field this project was not using. MCP tools needed no field either — every server here is built carrying exactly the tools its session may call, so wiring already bounded them
- agent: a session naming no built-in is now given none, rather than Claude Code's entire default set. The two worldview sessions work solely through their own servers and had been getting the lot
- agent: `plan` is used nowhere, against the shape this change was sketched with. Measured to complete a turn without ever submitting its output, which would have cost six sub-agents their structured answer
- agent: `ENABLE_TOOL_SEARCH` moves onto the Claude-only transform, since a Codex session would otherwise have run with schema deferral on and nothing saying so

## v7.1.0 (2026-08-18)

Open every agent session through the portable runtime seam
- agent: the Claude-only settings — the bash sandbox
- the roots read outside cwd
- the transport ceiling — ride a ConfigTransform stacked after rendering
- so the portable request stays one both runtimes accept

## v7.0.0 (2026-08-17)

Replace the hand-copied lup with a real lup dependency — a new framework under the agent
- major, by aib's own rule ("architecture changes: new LLM, new framework"): the Claude Agent SDK went 0.1.26 → 0.2.139, every tool crosses a new boundary, and a content-safety guard now rewrites every tool result
- deps: lup is a git dependency with the [claude,codex,docker] extras. `aib.tools.{decorator,mcp_server,responses}` are deleted, as are the mechanisms behind `metrics`/`retry`/`throttle` and ~80 lines of `paths.py`
- tools: all 40 tools moved from `@mcp_tool` to `lup.mcp.lup_tool` and declare an output model instead of returning a bare dict. Three that genuinely answer two ways — `wikipedia`, `get_cp_history`, `wv_read_entry` — declare a union, which keeps each arm's wire format exact instead of flattening both into one envelope
- tools: every tool result now passes `guard_result`, which writes an oversized declared string field to disk and leaves a path and a preview in its place. Only fields a model declares as `str` are affected, so an oversized page, arXiv paper, Wikipedia article or Wayback snapshot no longer reaches the provider's truncation
- tools: `TailStats` became a model with optional fields, so absent Google Trends statistics serialize as `null` rather than as missing keys
- tools: URL routing moved to `lup.tool_routes`. A redirection now matches on the parsed host, so a registration for `bls.gov` no longer also answers for `bls.gov.evil.example`
- paths: the session kernel — project root, notes/traces/feedback directories, the timestamp format, versioned sessions and logs — is `lup.workspace.paths`. Both layouts are already `notes/traces/<version>/…`, so no data moves
- version: AGENT_VERSION moved from `src/aib/version.py` to `[tool.lup] agent_version` in pyproject.toml, which is what lup reads to key `notes/traces/<version>/`. The re-exec trick that defeated the import cache is gone — reading a value out of a manifest needs no such thing
- policy: `ToolPolicy` subclasses `lup.tool_policy.BaseToolPolicy`, and each exclusion now carries its reason, so availability can answer *why* a tool is missing rather than only that it is
- devtools: `py`, `sync`, `report` and `harness` sub-apps composed from lup; `dev worktree` installs `aib-workflow@aib` rather than a marketplace name that never existed
- plugin: the permission policy is a declaration compiled into `.claude/plugins/lup/`, and the regex scripts under `.claude/plugins/aib/hooks/` are deleted. They judged the raw command *string* with unanchored patterns and last-match-wins, so `rm -rf x && git status` matched the `git status` allow and was auto-approved; the policy now parses a command into segments and joins them deny > ask > defer > allow. Refusing a forecast becomes a gate rather than a norm — `uv run forecast` and the three `lup-devtools` verbs that open the same agent are declared refused, each carrying the instruction to print the command instead
- plugin: editing anything under `tests/` is an approval question, and a refusal for the resolver's implementer — the first time that contract is enforced rather than stated in a prompt
- plugin: `.claude/CLAUDE.md` and `.claude/settings.json` are generated from `src/aib/devtools/harness/`. The guidance was 2858 bytes past the size at which a runtime silently truncates it, so its reference sections moved to `docs/devtools.md`
- gates: the pre-push quality check moved from a PreToolUse hook into the tracked `.githooks/pre-push`, where it covers human pushes too, has no 30-second ceiling, and cannot race a second hook engine for the same decision
- tools: the research sub-agent's allowlist is derived from the servers it is actually given rather than from a union of seventeen named groups. Measured before and after — the two lists are identical, so nothing the agent may call changes
- fix: `ForecastMeta.tools_used_count` was always 0 — it read `total_calls`, a key no metrics summary has ever carried

## v6.4.0 (2026-07-24)

Restore tool visibility and forecast on Opus 5
- agent: ENABLE_TOOL_SEARCH=false on every SDK session — schemas were deferred past 10% of the context window, so the research sub-agent saw ~35 tool names without schemas and reported served capabilities (options_iv, twice) as missing. v6.2.0 allowed ToolSearch, which let the agent load a schema but still left it guessing the right search terms
- tools: research() accepts a bare query alongside the questions list — the nested field is itself named query, and 14 of 70 v6.3.0 sessions burned a call on the validation error before retrying
- tools: wayback_snapshot() exposes the Internet Archive to the orchestrator and the research sub-agent, clamped to the retrodict cutoff; the Wayback code existed but served only retrodict plumbing for search and exa
- tools: mcp_tool resolves parameter annotations via get_type_hints, so a module using deferred annotations can register a tool
- config: orchestrator and every nested agent forecast on claude-opus-5[1m]; tool-free one_shot helpers stay on haiku/sonnet

## v6.3.0 (2026-07-01)

Embed nested sub-agent reasoning traces inline in the reviewed forecast trace
- agent: research/subforecast/premortem sub-agents now capture their own SDK message stream and register a sub-trace on the session, keyed by query/question/ordinal
- agent: ReasoningLogger expands each nested sub-trace inline beneath the tool result that produced it, so build_trace no longer shows nested agents as opaque tool results
- agent: the post-session reviewer (condensed_reasoning) and the premortem gate now see the full nested reasoning — closing blind spots in retrodict future-leak detection, tool auditing of the ~35 research-side data tools, and reasoning-level risk flags
- nested traces are hand-carried via NestedAgentReport.trace and a transient (non-persisted) ForecastOutput.trace field; nothing extra is written to disk or shown to the live forecasting agent

## v6.2.0 (2026-06-30)

Lock the agent out of the host shell; isolate the SDK spawn cwd from the worktree
- agent: Bash removed from the built-in toolset (orchestrator + research sub-agent) — code execution runs only in the Docker-isolated mcp__sandbox__execute_code tool, eliminating the silent host-shell fallback that engaged when the sandbox was unavailable
- paths: AGENT_CWD moved from notes/agent-cwd into the system temp dir so the SDK subprocess working directory never lands in (or gets committed to) the git tree; the legacy in-tree path is gitignored
- tools: reflection() accepts `factors` passed as a JSON string (coerced like `tentative_estimate` already was), fixing a list_type validation crash when the agent serializes the field
- agent: ToolSearch added to the allow-list — it was being denied by the tool whitelist, which blocked the agent from loading deferred tool schemas (e.g. mcp__sandbox__execute_code) and forced the Bash fallback
- agent: native WebSearch/WebFetch allowed for live forecasts but denied during retrodict (added to retrodict's denied-tools set) so they can't bypass the cutoff that mcp__search__* enforce
- agent: forecasting session no longer inherits the user's account MCP connectors (Gmail/Drive/Calendar/Remote) — `--strict-mcp-config` loads only the bot's own MCP servers
- agent: setting_sources pinned to [] and ~/.claude/projects dropped from add_dirs, so a forecast can't load the user's settings or read their other Claude Code projects

## v6.1.0 (2026-06-29)

Worldview store becomes a self-maintaining, coherent world model, and the forecast store is activated
- worldview: top-level forecasts now register as depth-0 entries (notes/worldview/forecasts/), feeding the maintenance sweep's resolution, scoring, and research-linking — previously only subforecasts populated the store, so it stayed empty
- worldview: `aib-devtools worldview loop` surveys the whole store for issues (contradictions, outdated entries, duplicates, missing links, resolvable forecasts) and fans out a fix agent per issue in parallel — independent of forecasting
- worldview: a read-only survey agent registers issues via an `add_issue` tool in one pass; a fix agent then resolves each issue via research + structural ops
- tools: wv_reconcile re-researches a disputed claim and supersedes the conflicting entries with one authoritative note; wv_refresh re-researches a stale entry in place
- worldview: research overwrites preserve the prior snapshot, building a per-fact trajectory (time series)
- worldview: contradictions are reconciled and uncertain forecast resolutions retried — never deferred to human review
- agent: worldview_manager removed from the forecaster's toolset; maintenance runs only via the standalone loop
- agent: get_research_mcp_servers is sandbox-optional so maintenance can research outside a forecast
- prompts: tool docs present the exact callable name (e.g. mcp__research__research) instead of the bare name, eliminating "No such tool available: research" retries
- prompts: subforecast decomposition is now directive — binary-threshold-on-a-quantity questions default to a numeric subforecast + CDF threshold, rather than permissive guidance the agent never acted on

## v6.0.0 (2026-06-29)

Default forecasting model upgraded to Claude Opus 4.8
- config: default model claude-opus-4-6 → claude-opus-4-8
- config: add summer-futureeval-2026 tournament (alias: futureeval) as default loop target alongside minibench

## v5.0.0 (2026-04-08)

Hierarchical sub-agent architecture with persistent worldview store
- agent: flat ~50-tool surface restructured into orchestrator (~10 tools) + research/subforecast sub-agents
- tools: research() — Opus sub-agent with ~35 data-gathering tools, parallel execution, resumable sessions
- tools: subforecast() — replaces spawn_subquestions, worldview persistence, bounded recursion (max_depth)
- tools: worldview_manager() — dedicated maintenance agent (dedup, cleanup, linking, contradictions, resolution)
- worldview: persistent store (notes/worldview/) with research and forecast entries, version-independent
- worldview: entry lifecycle (fresh/stale/superseded/resolved), TTL-based staleness, amend with revision history
- reviewer: worldview consistency checks (binary/numeric CDF threshold, cross-question, research contradictions)
- devtools: worldview CLI (list, show, maintain, resolve) and resolution sync integration
- agent: reflection() is now a fast, cheap checkpoint — factor-consistency metrics and YAML logging only, no reviewer call
- agent: new premortem() tool runs the Opus reviewer sub-agent with adversarial gate (counterargument, what_would_change_my_mind, confidence_in_estimate)
- gate: StructuredOutput requires both reflection() and premortem() approval (auto-approve after 3 consecutive fails)
- session: ReviewState moved to session.py, shared between reflection, premortem, and StructuredOutput hook
- reviewer: weak-counterargument and overconfident-self-assessment checks for adversarial fields
- agent: Forecast requires anchor_logit; probability_from_factors uses it as prior instead of implicit 50/50 midpoint

## v4.2.0 (2026-03-30)

Anchor-first reasoning, weather tools, and meta-prediction guidance
- agent: anchor field in all forecast models — structured base-rate before factor analysis
- prompts: anchor-first reasoning framework — factors push against reference class gravity
- prompts: CP mean-reversion prior — sharp momentum shows diminishing returns
- prompts: election polling error guidance — simulation width must reflect historical polling error
- prompts: weather awareness for Google Trends questions
- tools: Open-Meteo weather forecast tool (excluded in retrodict)

## v4.1.0 (2026-03-29)

Feedback loop session 8: numeric calibration fixes, meta-prediction improvements, options IV tool
- prompts: symmetric distribution width guidance — equal emphasis on too-narrow and too-wide (fixes 50% CI coverage)
- prompts: width sanity check — P5-P95 must span ≥2× implied random-walk range
- prompts: regime-conditional volatility — crisis premium (1.5-2× vol) for active geopolitical events
- prompts: scenario weight uncertainty — run mixtures with alternative weights
- prompts: meta-prediction threshold asymmetry — strict inequality means status quo = NO
- prompts: momentum trap warning — CP trend toward threshold is already priced in
- prompts: correlated evidence stacking — factors from same event count once
- tools: new options_iv tool — ATM implied volatility, put-call skew, volatility smile for CDF cross-validation

## v4.0.1 (2026-03-24)

Fix CDF sharpness: outward PMF redistribution and reduced tail mass

## v4.0.0 (2026-03-16)

Unified @mcp_tool decorator; session-scoped state; Opus reviewer with ForecastSummary; feedback loop decomposition
- tools: @mcp_tool decorator unifies @tool + @tracked + validation + error handling + url_route registration
- tools: all 30+ tools migrated from manual MCP response handling to @mcp_tool
- tools: new search_markets unifies Polymarket/Manifold/Kalshi search with LLM relevance filtering
- agent: ForecastSession replaces module-level globals with ContextVar-based session state
- agent: Opus reviewer replaces Sonnet condenser — produces structured ForecastSummary (tool audit, workflow assessment, reasoning review, pipeline health)
- agent: partial forecast recovery saves reasoning on agent crash
- agent: question-type conditional prompts (numeric/discrete skip meta-prediction sections)
- models: flexible percentile_values dict replaces fixed percentile_10..percentile_90 fields
- prompts: Threshold Questions subsection, sensitivity testing, factor-as-scaffolding reframe
- prompts: reflection restructured — tool_audit and process_reflection moved to Opus reviewer
- devtools: analysis.py replaces feedback.py + metrics.py + track_record.py (dashboard, tool-health, tool-needs, prompt-health, review)
- devtools: resolution commands renamed (check→sync, resolve→tentative, +set)
- commands: monolithic feedback-loop.md decomposed into fb-status, fb-investigate, fb-analyze, fb-reflect, fb-implement, fb-retrodict

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

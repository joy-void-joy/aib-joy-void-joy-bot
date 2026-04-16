# Hierarchical Sub-Agent Architecture (v5.0.0)

> Restructure the forecasting agent from a flat ~50-tool surface into a hierarchical sub-agent architecture with a persistent worldview store. Solves binary/numeric inconsistency and enables cross-session knowledge reuse.
>
> Design document: `design.md`

## Implementation Phases

### Phase 0: Worldview Store Infrastructure
- [x] `src/aib/worldview/__init__.py` — package init
- [x] `src/aib/worldview/models.py` — entry schemas
  - WorldviewResearchEntry, WorldviewForecastEntry, Revision, Source, DataPoint
  - `stale_after` + `resolvable_after` as separate fields
  - `state`: fresh / stale / superseded / resolved (EntryState StrEnum)
  - `superseded_by`: slug pointer
  - `revision_history`: amend audit trail
  - Slug generation: 8-char hash with collision detection (no python-slugify dep)
  - `from_forecast_output()` / `to_forecast_output()` conversion helpers
- [x] `src/aib/worldview/lookup.py` — CRUD, staleness checking, state transitions, amend
  - save/load for both entry types
  - Iteration with computed staleness (fresh → stale on read when past stale_after)
  - `amend_research_entry()` / `amend_forecast_entry()` with revision tracking
  - `supersede_entry()`, `resolve_forecast_entry()`, `archive_entry()`
  - `commit_worldview()` git integration
  - `all_slugs()` for collision detection
- [x] `src/aib/paths.py` — add WORLDVIEW_PATH constants + iteration helpers

### Phase 1: research() Tool
- [x] `src/aib/tools/research.py` — Opus sub-agent with built-in SDK tools
  - List input → parallel execution (asyncio.gather)
  - Pre-write dedup check (keyword search on worldview store filenames)
  - Pass existing entries as context so Opus can update/supersede/ignore
  - Resumable sessions via SDK session IDs + `cwd=notes/worldview/`
  - Amend mode (patch fields without re-running Opus)
  - Follow-up mode (resume prior SDK session)
  - Worldview persistence (save_research_entry + commit)
- [x] `src/aib/agent/tool_policy.py` — RESEARCH_TOOLS set, research MCP server, tool surface split
  - get_allowed_tools() → ~10 orchestrator tools (BUILTIN, METACULUS, SANDBOX, NOTES, RESEARCH, COMPOSITION)
  - get_mcp_servers() → orchestrator servers only (sandbox, composition, research, metaculus, notes)
  - New get_research_mcp_servers() → data servers (financial, government, search, trends, markets, weather, reddit, asknews)
  - "markets" server split into "metaculus" (main) + "markets" (research sub-agent)
- [x] `src/aib/agent/prompts.py` — STEP 3 rewritten for research() delegation with fallback to direct tools
- [x] `src/aib/agent/core.py` — nudge hooks removed, research MCP servers wired to ForecastSession
- [x] `src/aib/agent/session.py` — research_mcp_servers field added to ForecastSession
- [x] `src/aib/agent/sources.py` — updated for mcp__metaculus__ prefix

### Phase 2: subforecast() Tool
- [x] `src/aib/tools/subforecast.py` — replaces spawn_subquestions
  - List input → parallel execution (asyncio.gather)
  - Bounded recursion (max_depth default 1, cap 3)
  - Worldview persistence (from_forecast_output conversion)
  - Amend mode (patch probability/CDF/factors, logged in revision_history)
  - CDF threshold extraction for binary derivation
- [x] Delete `src/aib/tools/composition.py`

### Phase 3: worldview_manager() Agent
- [x] `src/aib/tools/worldview_manager.py` — dedicated maintenance agent
  - Cleanup: archive resolved subforecasts, prune entries past 2×TTL
  - Dedup: keyword overlap detection (Jaccard >0.6), auto-supersede older duplicates
  - Link: connect research ↔ subforecast entries via keyword tags (Jaccard >0.25)
  - Contradictions: flag research entries with conflicting data points (>30% deviation)
  - Resolve: sweep subforecasts where `resolvable_after < now`, AI resolve via resolver.py, score
  - MCP tool registered on main agent (`mcp__worldview__worldview_manager`)
  - `run_maintenance()` function for CLI/tournament-run integration
  - dry_run + skip_resolve flags for cost control
- [x] `src/aib/agent/tool_policy.py` — WORLDVIEW_MANAGER_TOOLS, MCP server, allowed tools
- [x] `tests/unit/test_worldview_manager.py` — 17 tests (scoring, keywords, cleanup, dedup, contradictions, resolvable, linking)

### Phase 4: Premortem Expansion
- [x] `src/aib/tools/reflection.py` — reviewer expanded with worldview access
  - Reviewer already uses Opus (since Phase 1)
  - Added WORLDVIEW_PATH to reviewer's allowed directories (Read/Glob/Grep)
  - Binary vs numeric consistency check (CDF-implied threshold vs binary probability)
  - Cross-question consistency check (keyword overlap in worldview forecasts)
  - Research contradiction check (worldview research key_facts vs factor claims)

### Phase 5: Resolution & CLI
- [x] AI resolution sweep in `resolution sync` — sweep where `resolvable_after < now`
- [x] `src/aib/devtools/worldview.py` — CLI commands (list, show, maintain, resolve)
- [x] `src/aib/devtools/main.py` — register worldview subcommand
- [x] Archive management (resolved → archive/) — handled by worldview_manager cleanup + resolve commands

### Phase 6: Integration Testing & Release
- [ ] Test binary threshold → subforecast spawned, CDF extracted, probability derived (requires live agent)
- [ ] Test numeric question → worldview entry written (requires live agent)
- [ ] Test related topic → agent discovers existing worldview entry via Grep (requires live agent)
- [x] Test amend mode → revision_history populated correctly (`test_worldview_lookup.py`)
- [x] Test resolution sweep → AI resolution triggers for `resolvable_after < now` (`test_worldview_manager.py`)
- [x] Test worldview manager → dedup works on overlapping entries (`test_worldview_manager.py`)
- [x] `uv run pytest` — 412 tests pass (14 new worldview lookup tests)
- [x] `uv run pyright` — 0 errors
- [x] Version bump to v5.0.0

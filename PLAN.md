# Feedback Loop & Devtools Architecture

## Current Status

The feedback loop is decomposed into 6 focused subcommands (`/fb-status`, `/fb-investigate`, `/fb-analyze`, `/fb-reflect`, `/fb-implement`, `/fb-retrodict`), orchestrated by `/feedback-loop`. Each subcommand is independently invocable and backed by purpose-built devtools in `src/aib/devtools/analysis.py`.

A post-session Opus reviewer produces structured `summary.json` files alongside each forecast trace. These are the central data source for downstream analysis — devtools aggregate them rather than re-interpreting traces with LLMs.

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Subcommand structure | Separate .md files | Each invocable independently; orchestrator calls in sequence |
| Post-session reviewer | Opus, combined with condensation | Replaces trace-explorer + Sonnet condensation in one pass |
| Summary storage | `summary.json` in session directory | Easy iteration for devtools; separate from forecast data |
| Tool audit structure | `by_tool: dict[str, str]` (compact one-line format) | Structured PerToolReview was too complex for LLM output; one-line format with consistent keywords enables grep-based aggregation |
| Trace-explorer | Removed | summary.json + devtools aggregation replaces it |
| Version-explorer | Kept | Code diffs still need LLM; CHANGELOG handles the overview |
| Resolution naming | `sync` + `tentative` | `check`/`resolve` were near-synonymous |
| Dashboard | Fast by default, `--refresh` flag | Don't block on API calls; opt-in sync |
| Done marking | Orchestrator-level, after full session | Subcommands don't mark; orchestrator marks at the end |
| Condensed reasoning | Separate field in summary.json | Short `summary` for review; longer `condensed_reasoning` for Metaculus comments |

## Architecture

```
/feedback-loop (orchestrator)
  ├── /fb-status        → analysis dashboard, analysis status, scores show
  ├── /fb-investigate   → scores show, summary.json, web search, error classification
  ├── /fb-analyze       → analysis tool-health, analysis tool-needs, version-diff
  ├── /fb-reflect       → analysis tracking-gaps, prompt-health, process assessment
  ├── /fb-implement     → code changes, version bump, commit
  └── /fb-retrodict     → queue missed, candidate selection

Post-session reviewer (core.py:review_forecast_trace)
  → ForecastSummary structured output → summary.json

Analysis devtools (analysis.py)
  dashboard, tool-health, tool-needs, tracking-gaps, prompt-health,
  version-diff, mark/unmark, status, review
```

## Data Flow

```
Forecast run
  → trace_for_condensation.md (session dir)
  → Opus reviewer → summary.json (session dir)
  → condensed_reasoning → ForecastOutput → Metaculus comment

Feedback loop
  → analysis devtools read summary.json files
  → aggregate tool health, capability gaps, reasoning patterns
  → inform implementation priorities
```

## Remaining Work

- [ ] Validate by running `/feedback-loop` end-to-end with the new subcommands
- [ ] After first session: assess whether `by_tool` one-line format is aggregatable enough
- [ ] After first session: assess whether subcommand gates and scoped `allowed-tools` work well in practice
=======
**Phase**: Feedback Loop & Devtools Overhaul (Phase 8)

---

## Important Distinction

**.claude/ directory** is for **Claude Code** (the development assistant working on this codebase). It contains settings, plugins, and instructions for the IDE-based Claude.

**The forecaster agent** (built with Claude Agent SDK) is a separate runtime that will have its own tools configured via `allowed_tools` and `mcp_servers` in `ClaudeAgentOptions`. It does NOT use `.claude/` settings.

---

## Phase 8: Feedback Loop & Devtools Overhaul

> Goal: Decompose the monolithic `/feedback-loop` (850 lines) into focused subcommands, each backed by purpose-built devtools. Kill overlapping devtools (`feedback collect`, `metrics`). Preserve every concern from the original without dropping any.

### Problem

1. `/feedback-loop` is 850 lines mixing workflow, reference material, and process guidance
2. `/audit` duplicates 40% of feedback-loop (resolution investigation, trace-explorer launch, error classification)
3. `feedback collect` mashes resolution matching, CP comparison, retrodict collection, and state tracking into one blob
4. `metrics` group overlaps with `scores` and has no tool-error focus
5. Tool errors, capability requests, and tracking quality have no dedicated devtools — they require launching the trace-explorer (expensive) or manual reading
6. No way to mark forecasts as "analyzed" outside of the now-deprecated `feedback collect`
7. Changes get written but never committed (noted as #1 process failure across 4 sessions)

### Concern Inventory

Every concern from the original `/feedback-loop` command, mapped to where it lives in the new design:

| # | Concern | Current Location | New Location |
|---|---------|-----------------|--------------|
| 1 | Three-level framework (object/meta/meta-meta) | Preamble | Orchestrator preamble + `/fb-reflect` |
| 2 | Input handling (post IDs or auto-discover) | Input section | Orchestrator |
| 3 | CP visibility constraint | Preamble | CLAUDE.md (already partially there) |
| 4 | Bitter Lesson guiding principle | Preamble | CLAUDE.md |
| 5 | Offline mode handling | Preamble | Devtools handle gracefully; orchestrator note |
| 6 | Previous session continuity | Phase 0 | `/fb-status` |
| 7 | "Done" marking / analyzed items | Phase 0 | `analysis mark/unmark/status` |
| 8 | Current version identification | Phase 1a | `analysis dashboard` |
| 9 | Resolution checking/updating | Phase 1a | `resolution check` (exists) |
| 10 | Tentative AI resolutions | Phase 1a | `resolution resolve` (exists) |
| 11 | Scores collection | Phase 1a | `scores show` (exists) |
| 12 | Version/type/resolution grouping | Phase 1a | `analysis dashboard` |
| 13 | Per-forecast resolution investigation | Phase 1b | `/fb-investigate` |
| 14 | Error classification (9 types) | Phase 1b | `/fb-investigate` |
| 15 | Counterfactual analysis | Phase 1b | `/fb-investigate` |
| 16 | Calibration aggregate view | Phase 1c | `calibration summary` (exists) |
| 17 | Pattern verification vs individual cases | Phase 1c | `/fb-investigate` |
| 18 | Missed question identification | Phase 1d | `queue missed` (exists) |
| 19 | Retrodiction execution | Phase 1d | `/fb-retrodict` |
| 20 | Blind mode documentation | Phase 1d | `/fb-retrodict` (condensed) |
| 21 | Future-leak detection (tool-level) | Phase 1d | trace-explorer (exists) |
| 22 | Future-leak detection (LLM training) | Phase 1d | trace-explorer (exists) |
| 23 | Known leak vectors | Phase 1d | `/fb-retrodict` reference |
| 24 | Retrodiction result collection | Phase 1e | `scores show --source retrodict` |
| 25 | Retrodiction accuracy evaluation | Phase 1e | `/fb-investigate` |
| 26 | Retrodiction airtightness evaluation | Phase 1e | trace-explorer (exists) |
| 27 | Tool effectiveness under blind mode | Phase 1e | `/fb-traces` |
| 28 | CP divergence interpretation | Phase 1f | CLAUDE.md |
| 29 | Gate: post-mortem presentation | Phase 1 gate | `/fb-investigate` gate |
| 30 | Version scoping (auto-scope) | Phase 2 | CLAUDE.md devtools section |
| 31 | Trace-explorer launch | Phase 2a | `/fb-traces` |
| 32 | Version reviewer usage | Phase 2a | `/fb-traces` |
| 33 | Version explorer usage | Phase 2a | `/fb-traces` |
| 34 | Deep-dive on flagged traces | Phase 2b | `/fb-traces` |
| 35 | Tool failure evaluation | Phase 2c | `analysis tool-health` + `/fb-traces` |
| 36 | Capability request evaluation | Phase 2c | `analysis tool-needs` + `/fb-traces` |
| 37 | Reasoning quality evaluation | Phase 2c | `/fb-traces` |
| 38 | Tool value assessment | Phase 2c | `analysis tool-health` |
| 39 | Meta: actionable insight self-check | Phase 3a | `/fb-reflect` |
| 40 | Meta: tracking data quality | Phase 3b | `analysis tracking-gaps` + `/fb-reflect` |
| 41 | Meta: missing data identification | Phase 3c | `/fb-reflect` |
| 42 | Gate: approved priority list | Phase 2+3 gate | `/fb-implement` gate |
| 43 | Prompt health (rewrite vs patch) | Phase 4 P0 | `analysis prompt-health` + `/fb-implement` |
| 44 | Fix failing tools | Phase 4 P1 | `/fb-implement` |
| 45 | Build requested tools | Phase 4 P2 | `/fb-implement` |
| 46 | Improve subagents | Phase 4 P3 | `/fb-implement` |
| 47 | Simplify prompts | Phase 4 P4 | `/fb-implement` |
| 48 | Patch count tracking | Phase 4 | `analysis prompt-health` |
| 49 | Version bumps | Phase 4 | `/fb-implement` |
| 50 | Change verification (git diff) | Phase 4 | `/fb-implement` |
| 51 | Change logging in analysis doc | Phase 4 | `/fb-implement` |
| 52 | Meta-meta: document self-evaluation | Phase 5a | `/fb-reflect` |
| 53 | Meta-meta: build missing scripts | Phase 5b | `/fb-reflect` |
| 54 | Meta-meta: improve data collection | Phase 5c | `/fb-reflect` |
| 55 | Meta-meta: update this document | Phase 5d | `/fb-reflect` |
| 56-59 | Anti-patterns (4 types) | Anti-patterns | CLAUDE.md |
| 60 | Analysis document template | Template section | Orchestrator |
| 61 | Command reference | Commands Available | CLAUDE.md devtools section |
| 62-66 | Periodic maintenance (5 items) | Periodic section | `/fb-reflect` |
| 67 | Key questions checklist (11 items) | Key Questions | Distributed across subcommands |
| 68 | Retrodiction queue selection | Phase 6 | `/fb-retrodict` |
| 69 | Selection criteria | Phase 6 | `/fb-retrodict` |
| 70 | Output format | Phase 6 | `/fb-retrodict` |
| 71 | Feedback cycle description | Phase 6 | `/fb-retrodict` |
| 72 | Completion checklist | Checklist | Orchestrator |
| 73 | Anti-skip guards | Checklist | Orchestrator |

### Step 1: New Devtools — `analysis` Group

Create `src/aib/devtools/analysis.py` with these commands:

#### `analysis dashboard`

One-screen health check replacing the first 30% of every feedback session.

```
=== Feedback Dashboard (v3.6.0) ===

Resolution Pipeline:
  Last scrape: 2026-03-15 16:21:36
  Resolved (all): 121 binary, 63 numeric
  Resolved (v3.6.0): 1
  Unanalyzed: 14 forecasts

Calibration (all-versions):
  Binary: Brier 0.200, ECE 0.13 (n=121)
  Numeric: 79% CI coverage (n=63)

Tool Health (v3.6.0, 15 forecasts):
  ⚠ search_exa:      7/7 errors (100%)
  ⚠ get_cp_history:   6/6 errors (100%)
  ⚠ polymarket_price: 6/6 junk (100%)
  ⚠ fetch_url:        11/78 errors (14.1%)
    reflection:       3/18 errors (16.7%)
    web_search:       6/86 errors (7.0%)

Uncommitted Changes: 14 files modified (git diff --stat)

Previous Session: 20260316_analysis.md
  Key finding: CDF pipeline tail distortion
  Changes: 1 committed (cdf-fix), 14 still uncommitted
```

Data sources:
- `tool_metrics.by_tool` from all forecast JSONs
- `scores show --resolved` summary
- `calibration summary` headline
- `git diff --stat` for uncommitted changes
- Most recent `*_analysis.md` for previous session
- `analysis status` for unanalyzed count

Flags: `--version V`, `--all-versions`

#### `analysis tool-health`

Replaces `metrics tools` + `metrics errors`. Focused on actionable tool health.

```
=== Tool Health (v3.6.0, 15 forecasts) ===

Tool               Calls  Errors  Rate    Avg ms  Status
─────────────────────────────────────────────────────────
web_search           86       6   7.0%    15056   OK
fetch_url            78      11  14.1%    11025   ⚠ FAILING
wikipedia            45       0   0.0%      216   OK
reflection           18       3  16.7%   140165   ⚠ FAILING
get_metaculus_q       8       0   0.0%      431   OK
search_exa            7       7 100.0%     5098   ✗ BROKEN
get_cp_history        6       6 100.0%      312   ✗ BROKEN (by design)
polymarket_price      6       0   0.0%     2341   OK (but 6 junk results)

⚠ Flagged tools (>10% error rate):
  search_exa: 400 Bad Request (all 7 calls) — posts: 42510-42516
  fetch_url: 403 on congress.gov(3), bls.gov(4), oscars.org(2), hockey-reference(2)
  reflection: StructuredOutput parse failures — posts: 42513, 42514, 42632
```

Data sources: `tool_metrics.by_tool` from forecast JSONs
Flags: `--version V`, `--since TIMESTAMP`, `--threshold N` (error rate threshold, default 10%)

#### `analysis tool-needs`

Extracts capability requests from `reflection.yaml` files.

```
=== Agent Capability Requests (v3.6.0, 15 reflections) ===

Frequency  Request                                    Posts
─────────────────────────────────────────────────────────────
  3/15     Sports/standings API for structured data   42562, 42510, 42511
  2/15     Wayback Machine page revision history      42511, 42636
  1/15     MarketWatch data format verification       42561

Source fields: tool_audit, process_reflection
```

Data sources: `reflection.yaml` files under `sessions/*/`
Parses `tool_audit` and `process_reflection` for capability request patterns
Flags: `--version V`

#### `analysis tracking-gaps`

Meta-level: is the agent emitting enough data for analysis?

```
=== Tracking Gaps (v3.6.0) ===

Forecasts: 15 total
  With tool_metrics: 15/15 ✓
  With reflection.yaml: 15/15 ✓
  With trace.md: 15/15 ✓
  With token_usage: 15/15 ✓
  With sources_consulted: 15/15 ✓
  With factors: 14/15 (missing: 42512 — event already happened, no factors needed)

Field Coverage:
  resolution: 1/15 (14 pending)
  peer_score: 1/15
  submitted_at: 15/15
```

Data sources: forecast JSONs + session directories
Flags: `--version V`

#### `analysis prompt-health`

Automated prompt health check.

```
=== Prompt Health ===

File: src/aib/agent/prompts.py
  Total lines: 426
  Sections: 11
  Growth since v3.4.0: +43 lines (+11.2%)

Patch indicators:
  "if ... fails" clauses: 2
  "Exception:" patterns: 0
  "Note:" annotations: 3
  Conditional rules: 4

Patches since last rewrite (v3.0.0):
  v3.4.0: "already happened" trap hardening
  v3.5.0: MC reflection metrics
  v3.6.0: macro context principle, breaking news guidance, reviewer escape hatch

Patch count: 5 (threshold: 3)
⚠ Consider structural rewrite evaluation
```

Data sources: `src/aib/agent/prompts.py`, git log for version tags
Flags: `--since-version V` (count patches since that version)

#### `analysis mark` / `analysis unmark` / `analysis status`

"Done" marking for feedback loop.

```bash
# Mark forecasts as analyzed
uv run aib-devtools analysis mark 42510 42511 42512

# Unmark
uv run aib-devtools analysis unmark 42510

# Show status
uv run aib-devtools analysis status
# Analyzed: 42 forecasts
# Unanalyzed: 14 forecasts (v3.6.0: 14)
# Last marked: 2026-03-16 (session: 20260316_analysis.md)
```

State stored in `notes/feedback_loop/analyzed.json`:
```json
{
  "analyzed": {
    "42510": {"session": "20260316_analysis.md", "marked_at": "2026-03-16T12:00:00"},
    "42511": {"session": "20260316_analysis.md", "marked_at": "2026-03-16T12:00:00"}
  }
}
```

- [x] Design complete
- [ ] Implement `analysis.py` with all 7 commands
- [ ] Register in `main.py`
- [ ] Add to CLAUDE.md devtools section

### Step 2: Kill/Merge Existing Devtools

#### Kill `feedback collect`

`feedback.py` currently does:
1. Fetch resolved questions from API → already done by `resolution check`
2. Match forecasts to resolutions → already done by `scores show`
3. CP comparison → move to `scores cp`
4. Retrodict collection → move to `scores show --source retrodict`
5. State tracking → replaced by `analysis mark/status`

Actions:
- [ ] Move CP comparison logic to `scores cp` command
- [ ] Delete `feedback.py`
- [ ] Remove from `main.py`
- [ ] Update CLAUDE.md

#### Kill `metrics` group

| metrics command | Replacement |
|----------------|-------------|
| `metrics summary` | `analysis dashboard` |
| `metrics tools` | `analysis tool-health` |
| `metrics by-type` | `scores summary --by-type` |
| `metrics errors` | `analysis tool-health` |

Actions:
- [ ] Add `--by-type` flag to `scores summary` (port `metrics by-type` logic)
- [ ] Port cost/token summary from `metrics summary` into `analysis dashboard`
- [ ] Delete `metrics.py`
- [ ] Remove from `main.py`
- [ ] Update CLAUDE.md

### Step 3: Command Decomposition — `/feedback-loop`

Split into 6 focused subcommand files + 1 thin orchestrator.

#### `/fb-status` (~60 lines)

**Replaces**: Phase 0 + Phase 1a
**Concerns covered**: 6, 7, 8, 9, 10, 11, 12

```
1. Run `analysis dashboard` — see current state at a glance
2. Run `analysis status` — how many unanalyzed forecasts?
3. Read most recent *_analysis.md — what was done last time?
4. Run `resolution check` + `resolution resolve --all` — update resolution data
5. If post IDs provided, use them; otherwise use unanalyzed forecasts
6. Present: status summary + target forecasts
   Gate: "These N forecasts are the targets. Proceed?"
```

#### `/fb-investigate` (~80 lines)

**Replaces**: Phase 1b + 1c + 1e
**Concerns covered**: 13, 14, 15, 16, 17, 24, 25, 26, 27, 28, 29

```
1. For each resolved target forecast:
   a. Run `scores show <id>` — get score, resolution
   b. Investigate the real-world outcome (web search, data sources)
   c. Classify error (9-type table)
   d. Build counterfactual
2. For retrodictions: evaluate accuracy + note airtightness (trace-explorer handles later)
3. Run `calibration summary` — check aggregate patterns
4. Cross-reference: does calibration confirm or contradict individual findings?
   Gate: present post-mortem table + error summary + calibration headline + counterfactuals
```

The error classification table and CP divergence guidance live in this file as compact reference (not the 60-line treatise from the original).

#### `/fb-traces` (~50 lines)

**Replaces**: Phase 2
**Concerns covered**: 31, 32, 33, 34, 35, 36, 37, 38

```
1. Run `analysis tool-health` — quick pre-check before launching subagent
2. Run `analysis tool-needs` — quick pre-check
3. Launch trace-explorer with:
   - Target post IDs
   - Resolution context from /fb-investigate
   - Calibration patterns
   - Tool health flags
4. Optionally launch version-reviewer or version-explorer
5. Evaluate: tool failures, capability requests, reasoning quality, tool value
```

#### `/fb-reflect` (~70 lines)

**Replaces**: Phase 3 + Phase 5 + Periodic Maintenance
**Concerns covered**: 1, 39, 40, 41, 52, 53, 54, 55, 62-66

```
Meta level:
1. Run `analysis tracking-gaps` — is the agent emitting enough data?
2. Did this session surface actionable insights? If not, why?
3. Can we correlate tool usage with forecast quality? What data is missing?

Meta-meta level:
4. Run `analysis prompt-health` — is the prompt accumulating patches?
5. Were the subcommands helpful? Anything confusing or missing?
6. Any repetitive manual analysis that should be a devtools command?
7. Any fields missing from forecast JSON or reflection.yaml?
8. Update subcommand files with what was learned

Periodic (every 3rd session):
9. Reread all subcommand files — still accurate?
10. Prompt health audit — read full prompts.py with fresh eyes
11. Clean up notes/ — archive old analysis files
12. Sync learnings to CLAUDE.md
```

#### `/fb-implement` (~80 lines)

**Replaces**: Phase 4
**Concerns covered**: 42, 43, 44, 45, 46, 47, 48, 49, 50, 51

```
Gate (entry): Present prioritized changes list with Bitter Lesson classification.
  User must approve before implementation.

Priority order:
  P0: Prompt health evaluation (rewrite vs patch) — use `analysis prompt-health`
  P1: Fix failing tools — from `analysis tool-health` flags
  P2: Build requested tools — from `analysis tool-needs`, discuss with user
  P3: Improve subagents — from trace-explorer findings
  P4: Simplify prompts — remove rules, add principles

After implementation:
  1. Version bump: `uv run aib-devtools version bump <level> "<summary>"`
  2. Commit changes (the missing step!)
  3. Verify: `git diff --stat` confirms each change exists
  4. Log changes in analysis document with COMMITTED/PROPOSED/DEFERRED status
  5. Mark analyzed forecasts: `uv run aib-devtools analysis mark <ids>`
```

#### `/fb-retrodict` (~50 lines)

**Replaces**: Phase 1d + Phase 6
**Concerns covered**: 18, 19, 20, 23, 68, 69, 70, 71

```
1. Find candidates: `uv run aib-devtools queue missed aib --days 14`
2. Only suggest R=Y questions
3. Prefer: diverse types, challenging topics, sufficient pre-resolution time
4. Output ready-to-use retrodict command

Reference (condensed):
- Blind mode restricts to historical data
- Known leak vectors
- Retrodict → calibration feedback cycle
```

Future-leak detection stays in trace-explorer (concerns 21, 22, 26) — it's already there and works well.

#### `/feedback-loop` — Orchestrator (~60 lines)

**Replaces**: The 850-line monolith
**Concerns covered**: 1, 2, 5, 29, 42, 60, 72, 73

```
# Feedback Loop: Orchestrator

Calls subcommands in sequence with gates between them.

## Sequence

1. /fb-status          → State + targets
   Gate: confirm targets
2. /fb-investigate     → Resolution investigation (skip if no resolved forecasts)
   Gate: confirm post-mortem
3. /fb-traces          → Trace analysis
4. /fb-reflect         → Meta + meta-meta reflection
   Gate: confirm priority list
5. /fb-implement       → Make changes, commit, bump version
6. /fb-retrodict       → Queue next retrodictions

## Analysis Document

Write to notes/feedback_loop/<branch>/<timestamp>_analysis.md
using the standard template (sections contributed by each subcommand).

## Completion Checklist
[Condensed from the original — one line per subcommand]

## Offline Mode
If API rate-limited, skip steps that hit the API.
All analysis commands work offline.
```

### Step 4: Move Reference Material

These sections from the original feedback-loop.md move to CLAUDE.md (or are already there):

| Section | Destination |
|---------|-------------|
| CP visibility constraint | CLAUDE.md (already present) |
| Bitter Lesson philosophy | CLAUDE.md (new section under Development Workflow) |
| Anti-patterns (4 types) | CLAUDE.md (new section under Development Workflow) |
| CP divergence interpretation | CLAUDE.md |
| Version scoping (auto-scope) | CLAUDE.md devtools section |
| Commands Available reference | CLAUDE.md devtools section (already there) |

### Step 5: Update `/audit`

Keep audit's structure (it works) but use new devtools:

- [ ] Phase 1a: use `analysis dashboard` instead of manual `grep AGENT_VERSION` + `scores show`
- [ ] Phase 1a: use `analysis status` for "done" marking context
- [ ] Phase 2: reference `analysis tool-health` and `analysis tool-needs` in the synthesis phase
- [ ] After audit: `analysis mark <ids>` to mark audited forecasts

### Step 6: Update CLAUDE.md Devtools Section

Reflect the new devtools structure:

```
aib-devtools
├── analysis           Cross-forecast pattern extraction
│   ├── dashboard      One-screen health check
│   ├── tool-health    Tool error rates and usage patterns
│   ├── tool-needs     Agent capability requests from reflections
│   ├── tracking-gaps  Check data completeness across forecasts
│   ├── prompt-health  Prompt patch count and growth metrics
│   ├── mark           Mark forecasts as feedback-loop-analyzed
│   ├── unmark         Remove analyzed mark
│   └── status         Show analyzed vs unanalyzed counts
│
├── scores             Unified scores table (unchanged + additions)
│   ├── show           Show scores table
│   ├── summary        Aggregate statistics (+ --by-type from metrics)
│   ├── compare        Compare two agent versions
│   ├── regression     Regression suite results
│   ├── extremes       Best/worst forecasts
│   └── cp             Community prediction comparison (from feedback collect)
│
├── calibration        (unchanged)
├── queue              (unchanged)
├── resolution         (unchanged)
├── trace              (unchanged)
├── api                (unchanged)
├── dev                (unchanged)
├── version            (unchanged)
├── git                (unchanged)
└── health             (unchanged)

REMOVED:
├── feedback           → replaced by analysis group
└── metrics            → merged into analysis + scores
```

### Implementation Order

1. **Create `analysis.py`** with all 7 commands — this is the foundation everything else depends on
2. **Move CP comparison** to `scores cp` — preserves the feature before killing feedback.py
3. **Add `--by-type`** to `scores summary` — preserves metrics by-type before killing metrics.py
4. **Kill `feedback.py` and `metrics.py`** — remove from main.py, delete files
5. **Write subcommand files** — `/fb-status`, `/fb-investigate`, `/fb-traces`, `/fb-reflect`, `/fb-implement`, `/fb-retrodict`
6. **Rewrite `/feedback-loop`** as thin orchestrator
7. **Update `/audit`** to use new devtools
8. **Move reference material** to CLAUDE.md
9. **Update CLAUDE.md** devtools section

### Files Modified

| File | Action |
|------|--------|
| `src/aib/devtools/analysis.py` | CREATE — new analysis group |
| `src/aib/devtools/main.py` | EDIT — add analysis, remove feedback + metrics |
| `src/aib/devtools/scores.py` | EDIT — add `cp` command, `--by-type` to summary |
| `src/aib/devtools/feedback.py` | DELETE |
| `src/aib/devtools/metrics.py` | DELETE |
| `.claude/plugins/aib/commands/fb-status.md` | CREATE |
| `.claude/plugins/aib/commands/fb-investigate.md` | CREATE |
| `.claude/plugins/aib/commands/fb-traces.md` | CREATE |
| `.claude/plugins/aib/commands/fb-reflect.md` | CREATE |
| `.claude/plugins/aib/commands/fb-implement.md` | CREATE |
| `.claude/plugins/aib/commands/fb-retrodict.md` | CREATE |
| `.claude/plugins/aib/commands/feedback-loop.md` | REWRITE — thin orchestrator |
| `.claude/plugins/aib/commands/audit.md` | EDIT — use new devtools |
| `.claude/CLAUDE.md` | EDIT — update devtools section, add reference material |

---

## Completed Phases (1-7)

### Phase 1: Foundation [x]
### Phase 2: Metaculus Integration [x]
### Phase 3: MCP Servers [x]
### Phase 4: Agent Setup [x]
### Phase 5: CLI & Submission [x]
### Phase 6: Robustness (partial)
### Phase 7: Feedback Loop [x] (being overhauled in Phase 8)

---

## Project Structure

```
src/
└── aib/
    ├── __init__.py
    ├── cli.py                    # Typer CLI entry point
    ├── agent/
    │   ├── __init__.py
    │   ├── core.py               # Claude Agent SDK + MCP config
    │   ├── models.py             # Forecast + subagent output models
    │   ├── prompts.py            # System prompts (lighter workflow)
    │   └── subagents.py          # Subagent definitions
    ├── tools/
    │   ├── __init__.py
    │   ├── forecasting.py        # In-process MCP: forecasting-tools
    │   ├── sandbox.py            # In-process MCP: Docker sandbox
    │   ├── composition.py        # In-process MCP: parallel_research, spawn_subquestions
    │   └── markets.py            # In-process MCP: Polymarket, Manifold
    └── devtools/
        ├── __init__.py
        ├── main.py               # Root CLI app composing all sub-apps
        ├── analysis.py           # NEW: cross-forecast pattern extraction
        ├── scores.py             # Unified scores table
        ├── calibration.py        # Calibration analysis
        ├── queue.py              # Forecasting queue
        ├── resolution.py         # Resolution updates
        ├── trace.py              # Forecast tracing
        ├── api.py                # API inspection
        ├── dev.py                # Development tools
        ├── version.py            # Version management
        ├── git.py                # Git operations
        └── health.py             # Service health checks

notes/
├── traces/<version>/
│   ├── forecasts/<post_id>/      # Forecast JSONs
│   ├── sessions/<post_id>/<ts>/  # Session working notes + reflection.yaml
│   ├── retrodict/<post_id>/      # Retrodict forecast JSONs
│   └── logs/<post_id>_<ts>.md    # Agent reasoning logs
├── feedback_loop/                # Analysis outputs
│   ├── <branch>/                 # Per-worktree analysis
│   │   ├── <timestamp>_analysis.md
│   │   └── ...
│   └── analyzed.json             # "Done" marking state
└── regression_suite.json
```

---

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Package layout | src/ layout | Standard Python packaging |
| MCP integration | `ClaudeAgentOptions.mcp_servers` | Direct SDK integration, no separate processes |
| Subagent structure | 5 flexible agents | Fewer agents, more autonomy |
| Notes structure | Timestamped folders | RW for current session, RO for history |
| Market tools | Real API calls | Polymarket + Manifold provide market signals |
| Feedback loop | Decomposed subcommands | Each concern gets focused attention |
| Devtools | Concern-based extraction | Data one command away, not buried in LLM analysis |
| "Done" marking | Simple JSON state file | Replaces feedback_state.json's overloaded tracking |
>>>>>>> feedback-loop-03-16

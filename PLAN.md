# Implementation Plan: Feedback Loop & Devtools Overhaul

## Overview

Decompose the monolithic `/feedback-loop` (850 lines) into focused subcommands, each backed by purpose-built devtools. Add a post-session Opus reviewer that produces structured `summary.json` files alongside each forecast, replacing the trace-explorer subagent and Sonnet condensation step. Kill overlapping devtools (`feedback collect`, `metrics`). Rename confusing commands (`resolution check` → `resolution sync`, `resolution resolve` → `resolution tentative`).

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Subcommand structure | Separate .md files | Each invocable independently; orchestrator calls in sequence |
| Post-session reviewer | Opus, combined with condensation | Replaces trace-explorer + Sonnet condensation in one pass |
| Summary storage | `summary.json` alongside forecast JSON | Easy iteration for devtools; separate from forecast data |
| Tool audit structure | `by_tool: dict[str, PerToolReview]` | Mirrors tool_metrics; trivial to aggregate across forecasts |
| Trace-explorer | Removed | summary.json + devtools aggregation replaces it |
| Version-explorer | Kept, available to both audit and feedback-loop | Code diffs still need LLM; CHANGELOG handles the overview |
| Resolution naming | `sync` + `tentative` | `check`/`resolve` were near-synonymous |
| Dashboard | Fast by default, `--refresh` flag | Don't block on API calls; opt-in sync |
| Feedback-loop principles | Stay in `feedback-loop.md` | In scope when running full loop; subcommands are standalone |
| Analysis doc template | Orchestrator prescribes structure | Ensures consistency; each subcommand fills its section |
| Done marking | Orchestrator-level, after full session | Subcommands don't mark; orchestrator marks at the end |
| CP comparison | Move to `scores cp` | Low priority; peer_score already embeds CP performance |
| Condensed reasoning | Separate field in summary.json | Short `summary` for review; longer `condensed_reasoning` for Metaculus comments |

---

## Step 1: Post-Session Opus Reviewer

> Central to the entire design. Without summary.json, the devtools have nothing to aggregate.

### 1a. ForecastSummary Pydantic Model

Create in `src/aib/agent/models.py`:

```python
class PerToolReview(BaseModel):
    calls: int
    errors: int
    error_messages: list[str]
    impact: str                     # "none" / "minor" / "significant"
    recovery: str | None
    value: str                      # "high" / "medium" / "low" / "wasted"
    missing_calls: str | None       # should have been called but wasn't
    notes: str

class ToolAudit(BaseModel):
    total_calls: int
    total_errors: int
    by_tool: dict[str, PerToolReview]
    capability_gaps: list[str]
    subtle_bugs: list[str]

class WorkflowAssessment(BaseModel):
    info_gathering: str
    structured_reasoning: str
    self_correction: str
    efficiency: str

class ReasoningReview(BaseModel):
    evidence_quality: int           # 1-5
    evidence_notes: str
    logical_coherence: int          # 1-5
    logical_notes: str
    calibration_sense: int          # 1-5
    calibration_notes: str
    strengths: list[str]
    weaknesses: list[str]

class PipelineHealth(BaseModel):
    issues: list[str]
    clean: bool

class FutureLeak(BaseModel):
    verdict: str                    # "CLEAN" / "SUSPECT" / "LEAKED"
    evidence: list[str]

class ForecastSummary(BaseModel):
    """Post-session structured review of a forecast trace."""
    summary: str                    # 2-3 sentence review summary
    condensed_reasoning: str        # Full narrative for Metaculus comments
    tool_audit: ToolAudit
    workflow: WorkflowAssessment
    reasoning: ReasoningReview
    pipeline: PipelineHealth
    future_leak: FutureLeak | None  # only for retrodict traces
    notable_observations: list[str]
    actionable_improvements: list[str]
```

### 1b. Replace `condense_reasoning()` in core.py

Replace the Sonnet `condense_reasoning()` function with an Opus reviewer that:
1. Writes trace to `trace_for_condensation.md` (same as current)
2. Runs Opus with `Read` tool access + `ForecastSummary` StructuredOutput
3. Saves output to `summary.json` alongside the forecast JSON
4. Returns `condensed_reasoning` string for `ForecastOutput`

Location: `src/aib/agent/core.py` lines 644-709 (replace `condense_reasoning`) and line 1007 (call site)

Output path: `notes/traces/<version>/forecasts/<post_id>/<timestamp>_summary.json`

The Opus reviewer prompt should cover everything from `/review`:
- Tool use audit (errors, recovery, subtle bugs, missing calls)
- Workflow assessment (info gathering, structure, self-correction, efficiency)
- Reasoning quality (evidence, logic, calibration)
- Pipeline health (MCP, sandbox, tokens, prompt issues)
- Future-leak detection (for retrodict traces — check retrodict_date)
- Condensed reasoning narrative (first-person, markdown, matches the forecast)

### 1c. CLI Backfill Command

Add `analysis review` command to `src/aib/devtools/analysis.py`:

```bash
# Review a specific forecast (reads saved trace)
uv run aib-devtools analysis review 42510

# Review all forecasts missing summary.json
uv run aib-devtools analysis review --backfill

# Review with a specific version filter
uv run aib-devtools analysis review --version 3.6.0 --backfill
```

Reads `trace_for_condensation.md` from `sessions/<post_id>/<timestamp>/`.

### 1d. Update submission.py

Change `submission.py` to read `condensed_reasoning` from:
1. `ForecastOutput.condensed_reasoning` (same field name, now produced by Opus)
2. No structural change needed — just the source of the data changes

### 1e. Trim reflection.py

Drop these fields from the reflection prompt and schema:
- `tool_audit` — now in summary.json
- `process_reflection` — now in summary.json

Reflection keeps: factors, tentative_estimate, assessment, calibration_notes, key_uncertainties, update_triggers, reviewer_critique.

**Files modified:**
- `src/aib/agent/models.py` — add ForecastSummary and related models
- `src/aib/agent/core.py` — replace condense_reasoning with Opus reviewer
- `src/aib/agent/reflection.py` — drop tool_audit and process_reflection
- `src/aib/submission.py` — no change needed (reads same field)

---

## Step 2: New Devtools — `analysis` Group

Create `src/aib/devtools/analysis.py`.

### `analysis dashboard [--refresh]`

One-screen health check. Fast by default (reads local data only). `--refresh` runs `resolution sync` + `resolution tentative --all` first.

Shows:
- Current agent version
- Resolution pipeline: last sync, resolved counts (all vs current version)
- Unanalyzed forecast count (from `analyzed.json`)
- Calibration headline (Brier, ECE, CI coverage)
- Tool health summary (flagged tools from summary.json aggregation)
- Uncommitted changes (`git diff --stat`)
- Previous session summary (last `*_analysis.md`)

Data sources: forecast JSONs, summary.json files, `analyzed.json`, `git diff`, `calibration summary`

### `analysis tool-health [--version V] [--since T] [--threshold N]`

Aggregates `tool_audit.by_tool` from all summary.json files.

Shows per-tool: calls, errors, error rate, avg time, common error messages, affected posts. Flags tools above threshold (default 10%). Shows capability gaps aggregated across all summaries.

### `analysis tool-needs [--version V]`

Aggregates `tool_audit.capability_gaps` from all summary.json files. Groups by similarity, counts frequency, lists affected posts.

### `analysis tracking-gaps [--version V]`

Checks data completeness: which forecasts have summary.json, reflection.yaml, trace.md, tool_metrics, token_usage, factors, resolution, peer_score.

### `analysis prompt-health [--since-version V]`

Reads `src/aib/agent/prompts.py`. Counts lines, sections, growth since specified version. Scans for patch indicators ("if...fails", "Exception:", "Note:"). Counts patches since last rewrite from CHANGELOG.md.

### `analysis version-diff <v1> <v2>`

Reads CHANGELOG.md entries between two versions. Shows compact delta without needing LLM or git diffs. For code-level diffs, use version-explorer subagent.

### `analysis mark <post_id>...` / `analysis unmark <post_id>...` / `analysis status`

"Done" marking for feedback loop. State stored in `notes/feedback_loop/analyzed.json`.

### `analysis review <post_id> [--backfill] [--version V]`

CLI backfill: reads saved trace, runs Opus reviewer, writes summary.json. See Step 1c.

---

## Step 3: Kill/Merge Existing Devtools

### Rename resolution commands

- `resolution check` → `resolution sync` (scrapes Metaculus profile via Playwright)
- `resolution resolve` → `resolution tentative` (AI-powered early resolution)

Update: `src/aib/devtools/resolution.py` command names, `/resolve` slash command references, `feedback-loop.md`, CLAUDE.md.

### Kill `feedback collect`

Its functionality is split:
- Resolution matching → `scores show` (exists)
- CP comparison → `scores cp` (new, see below)
- Retrodict collection → `scores show --source retrodict` (exists or add flag)
- State tracking → `analysis mark/status` (new)

Delete `src/aib/devtools/feedback.py`. Remove from `main.py`.

### Kill `metrics` group

| metrics command | Replacement |
|----------------|-------------|
| `summary` | `analysis dashboard` (cost/token summary) |
| `tools` | `analysis tool-health` (reads summary.json, richer) |
| `by-type` | `scores summary --by-type` (add flag) |
| `errors` | `analysis tool-health` |

Delete `src/aib/devtools/metrics.py`. Remove from `main.py`.

### Add `scores cp`

Move CP comparison logic from `feedback.py` to `scores.py`. Shows our forecast vs community prediction for all binary forecasts, sorted by divergence.

### Add `--by-type` to `scores summary`

Port the question-type grouping from `metrics by-type`.

### Merge `track_record` into `scores`

Move `track_record show` → `scores track-record` (or merge into `scores show` display).
Move `track_record backfill-cdf` → `scores backfill-cdf`.
Delete `src/aib/devtools/track_record.py`. Remove from `main.py`.

### Update `/resolve` command

Update to call `resolution tentative` instead of `resolution resolve`.

---

## Step 4: Command Decomposition — `/feedback-loop`

### `/fb-status` (~60 lines)

**Replaces**: Phase 0 + Phase 1a

```
1. Run `analysis dashboard` — one-screen health check
2. Run `analysis status` — unanalyzed forecast count
3. Read most recent *_analysis.md — what was done last time?
4. If --refresh: run `resolution sync` + `resolution tentative --all`
5. If post IDs provided, use them; otherwise use unanalyzed forecasts
6. Run `scores show <target_ids>` — scores for targets
   Gate: present status + targets, ask what to focus on
```

### `/fb-investigate` (~80 lines)

**Replaces**: Phase 1b + 1c + 1e

```
For each resolved target forecast:
  1. Run `scores show <id>` — score, resolution value
  2. Read summary.json — tool audit, reasoning review, workflow assessment
  3. Investigate real-world outcome (web search, data APIs)
  4. Classify error (9-type table, included as compact reference)
  5. Build counterfactual

For retrodictions: note airtightness from summary.json future_leak field

Cross-reference with calibration:
  Run `calibration summary` — aggregate patterns
  Verify: does calibration confirm or contradict individual findings?

Gate: present post-mortem table + error summary + calibration headline + counterfactuals
```

### `/fb-analyze` (~50 lines)

**Replaces**: Phase 2 (trace analysis via trace-explorer)

```
1. Run `analysis tool-health` — aggregated tool errors from summary.json
2. Run `analysis tool-needs` — capability gaps from summary.json
3. Summarize: which tools fail, what the agent needs, reasoning quality patterns
4. For version comparison context: run `analysis version-diff`
5. For code-level diffs (if needed): launch version-explorer subagent
6. Flag 1-2 worst forecasts for manual trace reading if summary.json raises questions
```

No subagent required in the standard flow. If deeper trace reading needed, use `trace log <id>`.

### `/fb-reflect` (~50 lines, guided reflection)

**Replaces**: Phase 3 (meta) + Phase 5 (meta-meta)

```
Meta level:
  1. Run `analysis tracking-gaps` — is the agent emitting enough data?
  2. Review summary.json schema — is it capturing what we need?
  3. Did this session surface actionable insights? If circular → schema or reviewer prompt needs improvement

Meta-meta level:
  4. Run `analysis prompt-health` — is the prompt accumulating patches?
  5. Were the subcommands helpful? Anything confusing or missing?
  6. Any repetitive analysis that should be a devtools command?
  7. Any fields missing from summary.json or reflection.yaml?
  8. Update subcommand files with learnings

Periodic (every 3rd session):
  9. Reread all subcommand files
  10. Prompt health audit — read full prompts.py
  11. Clean up notes/
  12. Sync learnings to CLAUDE.md
```

### `/fb-implement` (~80 lines)

**Replaces**: Phase 4

```
Gate (entry): Present prioritized changes with Bitter Lesson classification.
  User must approve before implementation.

Priority order:
  P0: Prompt health (rewrite vs patch — use analysis prompt-health data)
  P1: Fix failing tools (from analysis tool-health flags)
  P2: Build requested tools (from analysis tool-needs, discuss with user)
  P3: Improve subagents (from summary.json workflow assessments)
  P4: Simplify prompts (remove rules, add principles)

After implementation:
  1. Version bump: `uv run aib-devtools version bump <level> "<summary>"`
  2. Commit changes
  3. Verify: `git diff --stat` confirms each change
  4. Log changes in analysis doc (COMMITTED / PROPOSED / DEFERRED)
```

### `/fb-retrodict` (~50 lines)

**Replaces**: Phase 1d + Phase 6

```
1. Find candidates: `uv run aib-devtools queue missed aib --days 14`
2. Only suggest R=Y questions
3. Prefer: diverse types, challenging topics, sufficient pre-resolution time
4. Output ready-to-use retrodict command

Reference (condensed):
- Blind mode restricts to historical data
- Known leak vectors
- Future-leak detection now handled by post-session reviewer (summary.json)
- Retrodict → calibration feedback cycle
```

### `/feedback-loop` — Orchestrator (~150 lines)

```
Orchestrator (~60 lines):
  1. /fb-status          → State + targets
     Gate: confirm targets
  2. /fb-investigate     → Resolution investigation (skip if no resolved)
     Gate: confirm post-mortem
  3. /fb-analyze         → Tool health + capability gaps + patterns
  4. /fb-reflect         → Meta + meta-meta reflection
     Gate: confirm priority list
  5. /fb-implement       → Make changes, commit, bump version
  6. /fb-retrodict       → Queue next retrodictions
  7. Mark analyzed forecasts: `uv run aib-devtools analysis mark <ids>`
  8. Write analysis doc to notes/feedback_loop/<branch>/<timestamp>_analysis.md

Analysis doc template (~20 lines)
Principles section (~70 lines): Bitter Lesson, anti-patterns, CP guidance, offline mode
```

---

## Step 5: Update `/audit`

Keep audit's structure (it works). Update to use new devtools:

- Phase 1a: use `analysis dashboard` instead of manual metadata collection
- Phase 1a: `analysis version-diff` for quick CHANGELOG delta between versions
- Phase 2: reference summary.json for resolution investigation context
- Phase 3: read summary.json files instead of launching trace-explorer
  - For version comparison: version-explorer subagent stays (code diffs)
- Phase 4: synthesis maps findings to version changes (audit's unique value)
- After audit: `analysis mark <ids>`
- Update `/resolve` to call `resolution tentative`

---

## Step 6: Delete/Update Supporting Files

- [ ] Delete `.claude/plugins/aib/agents/trace-explorer.md`
- [ ] Update CLAUDE.md: devtools section, add Bitter Lesson reference, remove trace-explorer references
- [ ] Update `feedback-loop.md` references in CLAUDE.md
- [ ] Update any commands that reference `resolution check` or `resolution resolve`

---

## Concern Inventory

Every concern from the original 850-line `/feedback-loop`, mapped to its new home:

| # | Concern | New Location |
|---|---------|-------------|
| 1 | Three-level framework | Orchestrator preamble + `/fb-reflect` |
| 2 | Input handling | Orchestrator |
| 3 | CP visibility constraint | Orchestrator principles |
| 4 | Bitter Lesson | Orchestrator principles |
| 5 | Offline mode | Orchestrator principles + devtools handle gracefully |
| 6 | Previous session continuity | `/fb-status` |
| 7 | Done marking | `analysis mark/status` (orchestrator-level) |
| 8 | Version identification | `analysis dashboard` |
| 9 | Resolution updating | `resolution sync` (renamed) |
| 10 | Tentative AI resolutions | `resolution tentative` (renamed) |
| 11 | Scores | `scores show` (exists) |
| 12 | Grouping by version/type | `analysis dashboard` |
| 13 | Per-forecast investigation | `/fb-investigate` |
| 14 | Error classification | `/fb-investigate` |
| 15 | Counterfactual analysis | `/fb-investigate` |
| 16 | Calibration aggregate | `calibration summary` (exists) |
| 17 | Pattern verification | `/fb-investigate` |
| 18 | Missed questions | `queue missed` (exists) |
| 19 | Retrodiction execution | `/fb-retrodict` |
| 20 | Blind mode docs | `/fb-retrodict` (condensed) |
| 21 | Future-leak (tool) | Post-session reviewer → summary.json |
| 22 | Future-leak (LLM) | Post-session reviewer → summary.json |
| 23 | Known leak vectors | `/fb-retrodict` reference |
| 24 | Retrodict collection | `scores show --source retrodict` |
| 25 | Retrodict accuracy | `/fb-investigate` |
| 26 | Retrodict airtightness | summary.json `future_leak` field |
| 27 | Tool effectiveness (blind) | `/fb-analyze` via summary.json |
| 28 | CP divergence guidance | Orchestrator principles |
| 29 | Gate: post-mortem | `/fb-investigate` gate |
| 30 | Version scoping | CLAUDE.md |
| 31 | Trace-explorer launch | Removed — replaced by summary.json + devtools |
| 32 | Version reviewer | Available to both `/fb-analyze` and `/audit` |
| 33 | Version explorer | Available to both `/fb-analyze` and `/audit` |
| 34 | Deep-dive on flagged traces | Manual `trace log <id>` for 1-2 worst |
| 35 | Tool failure evaluation | `analysis tool-health` |
| 36 | Capability requests | `analysis tool-needs` |
| 37 | Reasoning quality | summary.json `reasoning` field |
| 38 | Tool value assessment | `analysis tool-health` |
| 39 | Meta: actionable insight check | `/fb-reflect` |
| 40 | Meta: tracking data quality | `analysis tracking-gaps` + `/fb-reflect` |
| 41 | Meta: missing data | `/fb-reflect` |
| 42 | Gate: priority list | `/fb-implement` gate |
| 43 | Prompt health | `analysis prompt-health` + `/fb-implement` |
| 44 | Fix failing tools | `/fb-implement` P1 |
| 45 | Build requested tools | `/fb-implement` P2 |
| 46 | Improve subagents | `/fb-implement` P3 |
| 47 | Simplify prompts | `/fb-implement` P4 |
| 48 | Patch count tracking | `analysis prompt-health` |
| 49 | Version bumps | `/fb-implement` |
| 50 | Change verification | `/fb-implement` (git diff) |
| 51 | Change logging | `/fb-implement` (analysis doc) |
| 52 | Meta-meta: document eval | `/fb-reflect` |
| 53 | Meta-meta: build scripts | `/fb-reflect` |
| 54 | Meta-meta: improve data | `/fb-reflect` |
| 55 | Meta-meta: update docs | `/fb-reflect` |
| 56-59 | Anti-patterns | Orchestrator principles |
| 60 | Analysis doc template | Orchestrator |
| 61 | Command reference | CLAUDE.md |
| 62-66 | Periodic maintenance | `/fb-reflect` (every 3rd session) |
| 67 | Key questions checklist | Distributed across subcommands |
| 68 | Retrodict queue | `/fb-retrodict` |
| 69 | Selection criteria | `/fb-retrodict` |
| 70 | Output format | `/fb-retrodict` |
| 71 | Feedback cycle | `/fb-retrodict` |
| 72 | Completion checklist | Orchestrator |
| 73 | Anti-skip guards | Orchestrator |

---

## Implementation Order

| Step | Description | Files | Depends On |
|------|-------------|-------|------------|
| 1a | ForecastSummary Pydantic model | `models.py` | — |
| 1b | Opus reviewer (replace condense_reasoning) | `core.py` | 1a |
| 1e | Trim reflection (drop tool_audit, process_reflection) | `reflection.py` | 1b |
| 2 | New `analysis.py` devtools (dashboard, tool-health, tool-needs, tracking-gaps, prompt-health, version-diff, mark/unmark/status, review) | `analysis.py`, `main.py` | 1a (reads summary.json) |
| 3a | Rename resolution commands | `resolution.py` | — |
| 3b | Move CP comparison to `scores cp` | `scores.py` | — |
| 3c | Add `--by-type` to `scores summary` | `scores.py` | — |
| 3d | Merge `track_record` into `scores` | `scores.py`, `track_record.py` | — |
| 3e | Kill `feedback.py` and `metrics.py` | `feedback.py`, `metrics.py`, `main.py` | 2, 3b |
| 4 | Write subcommand files | `commands/fb-*.md` | 2 |
| 4o | Rewrite `/feedback-loop` orchestrator | `commands/feedback-loop.md` | 4 |
| 5 | Update `/audit` to use new devtools | `commands/audit.md` | 2 |
| 5b | Update `/resolve` to use `resolution tentative` | `commands/resolve.md` | 3a |
| 6a | Delete trace-explorer | `agents/trace-explorer.md` | 4 |
| 6b | Update CLAUDE.md | `.claude/CLAUDE.md` | all |

---

## Files Modified

| File | Action |
|------|--------|
| `src/aib/agent/models.py` | EDIT — add ForecastSummary + related models |
| `src/aib/agent/core.py` | EDIT — replace condense_reasoning with Opus reviewer |
| `src/aib/agent/reflection.py` | EDIT — drop tool_audit and process_reflection |
| `src/aib/devtools/analysis.py` | CREATE — new analysis group (8 commands) |
| `src/aib/devtools/main.py` | EDIT — add analysis, remove feedback + metrics + track_record |
| `src/aib/devtools/resolution.py` | EDIT — rename check→sync, resolve→tentative |
| `src/aib/devtools/scores.py` | EDIT — add `cp` command, `--by-type`, merge track_record |
| `src/aib/devtools/feedback.py` | DELETE |
| `src/aib/devtools/metrics.py` | DELETE |
| `src/aib/devtools/track_record.py` | DELETE |
| `.claude/plugins/aib/commands/fb-status.md` | CREATE |
| `.claude/plugins/aib/commands/fb-investigate.md` | CREATE |
| `.claude/plugins/aib/commands/fb-analyze.md` | CREATE |
| `.claude/plugins/aib/commands/fb-reflect.md` | CREATE |
| `.claude/plugins/aib/commands/fb-implement.md` | CREATE |
| `.claude/plugins/aib/commands/fb-retrodict.md` | CREATE |
| `.claude/plugins/aib/commands/feedback-loop.md` | REWRITE — thin orchestrator + principles |
| `.claude/plugins/aib/commands/audit.md` | EDIT — use new devtools |
| `.claude/plugins/aib/commands/resolve.md` | EDIT — resolution tentative |
| `.claude/plugins/aib/agents/trace-explorer.md` | DELETE |
| `.claude/CLAUDE.md` | EDIT — update devtools section, add references |

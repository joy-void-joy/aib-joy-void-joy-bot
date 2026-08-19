<!-- Generated from aib.devtools.harness.content.docs.devtools by `uv run lup-devtools harness generate all` — edit the source, not this file. See docs/harness.md. -->

# Development CLI

`lup-devtools` is this repository's development tooling, composed in
`src/aib/devtools/main.py` from two halves: what only this project has —
forecasting analysis, calibration, scoring, the worldview store — and what
the library ships for any project built on it.

**Always use `lup-devtools` instead of ad-hoc commands.** If you find
yourself running the same thing repeatedly, add a command: to
`src/aib/devtools/` when only this project wants it, and upstream to `lup`
when another project built on it would.

```
lup-devtools
├── agent              Agent tool serving for an interactive session
│   └── serve-tools    Serve the research tools over MCP stdio (--list, --server)
│
├── claude             Run the runtime wired for this project
│   ├── (default/run)  Launch with research tools, local plugin, profile
│   └── usage          API usage and rate limit display
│
├── calibration        Calibration analysis and diagnostics
│   ├── binary         Binary forecast calibration (ECE/MCE, reliability diagrams)
│   ├── numeric        Numeric/discrete calibration via PIT analysis
│   ├── summary        Combined calibration summary for feedback loop
│   ├── export         Export calibration data to JSON
│   ├── report         Basic Brier/log scores and bucket table
│   ├── detail         Forecast-by-forecast results
│   └── cdf            CDF sharpness analysis
│
├── scores             Unified scores table (wraps aib.scoring)
│   ├── scrape         Scrape track record, update forecast JSONs with peer scores
│   ├── show           Scores table (--post-id, --version, --min-version, --source)
│   ├── summary        Aggregate by type, source, version (--min-version)
│   ├── compare        Compare two agent versions on overlapping questions
│   ├── regression     Regression suite results
│   ├── extremes       Best/worst forecasts (--non-meta, --min-version, --type, -n)
│   ├── strip          Strip plot by agent version (--min-version, watch mode)
│   ├── trend          Peer scores over time (--min-version, watch mode)
│   ├── track-record   Peer and baseline scores from forecast JSONs (--min-version)
│   └── backfill-cdf   Backfill CDF/numeric_bounds via Metaculus API
│
├── queue              Forecasting queue and priorities
│   ├── status         Tournament status overview
│   ├── upcoming       Questions closing soon (--days N, --all)
│   ├── missed         Recently closed without forecast (--days N)
│   └── search         Search questions (--type, --limit, --resolved/--open)
│
├── analysis           Forecast analysis and feedback loop
│   ├── dashboard      One-screen health check (--refresh)
│   ├── tool-health    Aggregate tool errors from forecasts + summary.json
│   ├── tool-needs     Capability gaps from summary.json reviews
│   ├── tracking-gaps  Data completeness check
│   ├── prompt-health  Prompt size and patch accumulation
│   ├── version-diff   CHANGELOG entries between two versions
│   ├── mark/unmark    Mark forecasts as analyzed
│   ├── status         Show analysis state
│   └── review         Run the reviewer on a trace (--backfill) — spawns an agent
│
├── resolution         Resolution updates
│   ├── sync           Scrape profile page for resolutions and scores (--backfill, --dry-run)
│   ├── tentative      AI-powered early resolution — spawns an agent
│   ├── status         Show resolution status of all forecasts
│   └── set            Manually set resolution for a post
│
├── worldview          Worldview store management
│   └── loop           Refresh the worldview — spawns an agent
│
├── trace              Forecast tracing and log analysis
│   ├── show           Show forecast trace for a post ID (--verbose)
│   ├── list           List all traced forecasts
│   ├── errors         Show forecasts with errors
│   ├── log            Extract agent reasoning from forecast log
│   └── logs           List available forecast logs
│
├── api                API inspection and debugging
│   ├── inspect        Explore package APIs
│   ├── module-path    Get filesystem path for a module
│   ├── module-source  Get source code for a module
│   ├── post           Inspect a Metaculus post's API data
│   ├── cp             Check community predictions for all forecasts
│   ├── cp-single      Check community prediction for a single post
│   ├── debug          Debug Metaculus API parsing (--tournament, --raw-only)
│   ├── mcp-error      Debug MCP error propagation
│   ├── websearch      Debug web search tool
│   └── earnings       Check earnings dates for a ticker
│
├── dev                Worktrees, branches, and pre-flight checks (the library's,
│   │                  wired over this project's declarations)
│   ├── worktree       create / list / remove
│   ├── check          ruff format, ruff check, pyright, pytest
│   ├── comments       Open `# lup:` feedback, and the pass that retires a claim
│   ├── issues         The open issues a resolver run would take as evidence
│   ├── pr             PR lifecycle (status, merge, push, checks)
│   ├── conflict       Merge/rebase conflict resolution
│   ├── rules          Generate the Lup rule and typed-suppression reference
│   ├── policy         What the declared permission policy decides, and why
│   ├── report-friction File or correct workflow friction in this checkout
│   ├── git-hooks      Write the declared guards into the tracked .githooks/
│   ├── setup-hooks    Point git at them (core.hooksPath -> .githooks)
│   ├── data-split     Refuse a commit mixing forecast data with code
│   ├── pr-base        Refuse a push whose PR would carry inherited data
│   └── gate           The checks a branch is held to before it leaves
│
├── version            Agent version management
│   ├── show           Display the current agent version
│   ├── bump           Bump version, update changelog, and create git tag
│   └── list           List all versions from git history
│
├── git                Git operations for forecasts
│   ├── commit-forecasts Commit uncommitted forecast files (one per question)
│   ├── local          Check local submission status
│   ├── mark           Mark forecast as submitted
│   ├── backfill       Backfill submitted_at from API
│   └── check          Check API forecast status
│
├── migration          One-time data migrations
│   ├── traces         Migrate flat notes/ to notes/traces/<version>/
│   └── retrodict      Migrate notes/retrodict/ to versioned layout
│
├── health             Service health checks
│   └── check          Ping Metaculus, Exa, FRED, Docker
│
│  — from here down, the library's, composed rather than written —
│
├── py                 Python module introspection (info, source, search, eval)
├── sync               Track sync.json repos and review their commits
├── harness            Generate and check the native harness tree
└── report             Everything left to implement, across every surface
```

Tournaments: `aib` (AIB Spring 2026), `minibench` (MiniBench), `cup`
(Metaculus Cup), `all` (cross-tournament).

## Worktrees rather than branches

`git switch -c` creates a branch and stays where it is, so switching changes
every file in place. `git worktree add` creates a directory with its own
working copy, so several branches are open at once in separate directories —
which is why this repository develops in worktrees, and why `dev worktree
create` makes them siblings under `tree/` rather than nested inside another
checkout.

## Commit types

| Type | For |
|---|---|
| `feat` | A new feature or capability |
| `fix` | A bug fix |
| `refactor` | A change that neither fixes a bug nor adds a feature |
| `docs` | Documentation only |
| `test` | Adding or updating tests |
| `chore` | Maintenance — dependencies, build config |
| `meta` | The harness declarations and the trees they generate |
| `data` | Generated data and output — forecasts, metrics, logs |

```
feat(agent): add permission handler for read-only directories
fix(tools): handle missing API key gracefully
refactor(sandbox): extract Docker client initialization
meta(harness): declare the fetch scope for a new data source
data(forecasts): add Feb 4 2026 forecast batch
```

## What an unpublished `main` does to a pull request

A feature branch is cut from local `main`, inheriting its unpushed data
commits. When the PR is opened, GitHub computes the merge base against
`origin/main` — which has never seen them — and folds every inherited
`notes/` file into the merge as a fresh addition with no shared ancestry.
Local `main` still holds those files as real commits, so the next `git pull`
collides add/add on every one of them.

That is what put 506 data files into PR #55. The push guard refuses at the
moment it would happen again; publishing `main` first is what settles it.

## The version floor

The views that pool several versions into one picture start at
`aib.paths.MIN_CHART_VERSION`, currently v7.0.0. Below it the scores measure
an agent on a different framework and a different SDK, so a chart carrying
both reads as a trend where there is only a change of subject. Pass
`--min-version 0.0.0` for the whole history, or any other release to move the
floor. An A/B arm is scoped by the release in its `<version>+<name>` label,
so an experiment charts alongside the version it branched from.

The floor bounds the unbounded case only. `--version 6.3.0` names what it
wants and is served, and so is a post named by `scores show --post-id`:
asking for a post asks for that post, whichever version forecast it.

## Resolution versus grep

| Task | Use resolution | Use grep/Edit |
|---|---|---|
| Find where a function is defined | `go-to-definition` | |
| Find all callers of a function | `find-references` | |
| Rename a variable/function/class | `rename-symbol` | |
| Search for a string literal | | `Grep` |
| Search across non-Python files | | `Grep` |
| Change logic within a function | | `Edit` |
| Add new code | | `Edit` / `Write` |

## When a forecast fails

**Common issues:**

- `METACULUS_TOKEN` not set → Startup fails (required)
- `EXA_API_KEY` not set → Web search fails
- `FRED_API_KEY` not set → FRED economic data tools fail
- Docker not running → Sandbox code execution fails

**Inspecting tool outputs:**

- Tool results are JSON-encoded; parse with `json.loads()` if debugging
- Check `src/aib/tools/*.py` for expected input/output schemas

## A/B testing

Variants are named agent configurations registered in `notes/variants.json`:

```json
{
  "variants": [
    {"name": "baseline", "note": "current defaults"},
    {"name": "sonnet-max", "model": "sonnet", "effort": "max", "profile": "alt"}
  ]
}
```

`uv run forecast ab -v baseline -v sonnet-max` runs every question (the
regression suite by default) under each variant. Each arm is a separate
process — `settings.model` is a process global read from many modules, so
arms sharing an interpreter would fight over it. Give each arm its own
`profile` so they don't share one account's rate limit.

Traces land in `notes/traces/<version>+<variant>/`, which keeps arms from
overwriting each other and keeps an in-flight experiment out of the released
version's calibration numbers (`parse_semver` rejects the suffixed name).
Compare arms with `lup-devtools scores compare <version>+a <version>+b`.

Valid `effort` values are `low`, `medium`, `high`, `xhigh`, `max`.

## The three verbs that spawn an agent

`analysis review`, `resolution tentative`, and `worldview loop` each open a
forecasting agent against paid APIs, exactly as `uv run forecast` does. All
three are refused by the shell policy, which names them one by one in
`harness/content/shell_vocabulary.py`. The rest of the CLI is blessed with
the toolchain, so the refusal sits on the verbs rather than on the tool.

Print the command for the user and say what to look for in its output.

## Code change reports

After completing code modifications, provide an extensive report:

1. **Summary** — One paragraph explaining the overall change and its purpose
2. **Files Modified** — Each file with path, nature of change, and a brief description
3. **Detailed Changes** — For each significant change: surrounding context (10-20 lines), before/after if modifying existing code, and the rationale for the approach
4. **Architectural Considerations** — Did you consider unifying with existing patterns? Are there similar functions that could be consolidated?
5. **Testing** — What tests were added or modified?

Code blocks carry their location, so a reader can find what is being
described:

```python
# src/aib/tools/example.py (lines 45-67)

def existing_function():
    # ... existing code ...
    new_behavior = do_something_different()
    # ... more existing code ...
    return result
```

A worked example:

```markdown
## Summary

Refactored URL handling to use standard library instead of manual string manipulation.

## Files Modified

- `src/aib/agent/retrodict.py` — Simplified Wayback URL construction
- `tests/unit/test_retrodict.py` — Updated test expectations

## Detailed Changes

### 1. Wayback URL Construction (retrodict.py:83-97)

**Before:**
[code block showing old implementation]

**After:**
[code block showing new implementation]

**Rationale:** The Wayback Machine accepts raw URLs directly—no encoding needed.
The previous `quote()` call was breaking query parameters.

## Architectural Considerations

- Checked `src/aib/tools/` for similar URL handling patterns—none found
- This is the only place we construct Wayback URLs

## Testing

- Updated `test_url_with_query_params` to verify query strings are preserved
- All 6 Wayback-related tests pass
```

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Note:** Modifying `CLAUDE.md` or `AGENTS.md` means modifying `.claude/CLAUDE.md` (this file).

## Project Overview

A forecasting bot for the [Metaculus AI Benchmarking Tournament](https://www.metaculus.com/aib/). Uses Claude Code with extended capabilities (web search, Python execution, etc.) to generate accurate predictions on forecasting questions.

Built with Python 3.13+ and the Claude Agent SDK. Uses `uv` as the package manager.

### Important Context

- **Submission is handled separately** — This codebase generates forecasts; a separate system handles submission to Metaculus
- **No community predictions available** — The AIB tournament does not expose community predictions, so we cannot use them for sanity-checking
- **CDF required for numeric questions** — Numeric and discrete questions require a 201-point CDF (cumulative distribution function), not just point estimates

## Reference Files

- **src/aib/cli.py**: CLI entry point (`uv run forecast test <question_id>`)
- **src/aib/agent/core.py**: Main forecasting agent orchestration using Claude Agent SDK
- **src/aib/agent/subagents.py**: Subagent definitions (deep-researcher, estimator, etc.)
- **src/aib/agent/numeric.py**: CDF generation for numeric/discrete questions
- **src/aib/submission.py**: Metaculus API submission functions
- **src/aib/tools/**: MCP tool implementations (forecasting, sandbox, composition, markets)

## Commands

```bash
# Install dependencies
uv sync

# Run a test forecast (does not submit to Metaculus)
uv run forecast test <question_id>

# Forecast and submit to Metaculus
uv run forecast submit <question_id>

# Forecast, submit, and post reasoning as a private comment
uv run forecast submit <question_id> --comment

# Forecast all open questions in a tournament (skips already forecast)
uv run forecast tournament aib       # AIB Spring 2026
uv run forecast tournament minibench # MiniBench
uv run forecast tournament cup       # Metaculus Cup

# Add a new dependency (DO NOT modify pyproject.toml directly)
uv add <package-name>

# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Type check
uv run pyright
```

## Testing

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_tools.py

# Run tests matching a pattern
uv run pytest -k "test_forecast"
```

**Test organization:**
- `tests/unit/` - Unit tests (mock external APIs)
- `tests/integration/` - Integration tests (require API keys, use `@pytest.mark.integration`)

## Debugging

**When a forecast fails:**
1. Check the notes folder (`notes/sessions/<session_id>/`) for intermediate reasoning
2. Run with `--verbose` flag for detailed tool call logging
3. Check API key configuration: missing keys log warnings at startup

**Common issues:**
- `METACULUS_TOKEN` not set → Startup fails (required)
- `EXA_API_KEY` not set → Web search fails
- Docker not running → Sandbox code execution fails

**Inspecting tool outputs:**
- Tool results are JSON-encoded; parse with `json.loads()` if debugging
- Check `src/aib/tools/*.py` for expected input/output schemas

## Git Workflow

This project uses **git worktrees** (not regular branches) to develop multiple features in parallel.

**IMPORTANT:** Never commit directly to `main`. Always work in a worktree.

### Worktrees vs Branches

- **`git checkout -b`**: Creates a branch but stays in the same directory. Switching branches changes all files in place.
- **`git worktree add`**: Creates a new directory with its own working copy. Multiple branches can be worked on simultaneously in separate directories.

### If already in a worktree:

**You are typically already in a worktree subbranch.** Check with `git worktree list` to confirm. If you're in a feature worktree, just work directly—no need to create another worktree or branch out.

### When implementing a feature:

1. **Create a worktree** (if the user hasn't already created one):
   ```bash
   git worktree add ./worktrees/feat-name -b feat/feature-name
   cd ./worktrees/feat-name
   ```
2. **Commit regularly and atomically** — Each commit should represent a single logical change. Don't bundle unrelated changes together. This creates a clear history that will be rebased before merging.
3. Push the branch when the feature is complete (or periodically for backup)
4. **Rebase before merging** — Once the feature is complete, rebase to create semantically meaningful commits. Squash fixups, reorder for clarity, and write descriptive commit messages.
5. Create a PR for review
6. **Clean up worktree** after merge:
   ```bash
   git worktree remove ./worktrees/feat-name
   ```

### Commit Best Practices

- **Commit before responding** — Always commit your work before responding to the user. This ensures progress is saved and creates natural checkpoints. Don't accumulate multiple changes across responses.
- **Commit early, commit often** — Don't wait until a feature is "done" to commit. Frequent commits provide checkpoints and make rebasing easier.
- **Keep commits atomic** — Each commit should do one thing. If you need to describe your commit with "and", it should probably be two commits.
- **History will be rebased** — Don't worry about perfect commit messages during development. The history will be cleaned up via interactive rebase before the PR is merged.
- **Meaningful final commits** — After rebasing, each commit should tell a story: what changed and why. The final history should be easy to read and bisect.

### Commit Message Format

Use conventional commit syntax: `type(scope): description`

**Types:**
- `feat` — New feature or capability
- `fix` — Bug fix
- `refactor` — Code change that neither fixes a bug nor adds a feature
- `docs` — Documentation only
- `test` — Adding or updating tests
- `chore` — Maintenance (dependencies, build config, etc.)
- `meta` — Changes to `.claude/` files (CLAUDE.md, settings, scripts, commands)

**Examples:**
```
feat(agent): add permission handler for read-only directories
fix(tools): handle missing API key gracefully
refactor(sandbox): extract Docker client initialization
docs(readme): add installation instructions
meta(claude): update commit message guidelines
```

**Note:** The `worktrees/` directory is gitignored.

## Code Style & Dependencies

### Primary Libraries
- **claude-agent-sdk**: Primary framework for building agents
- **pydantic**: For data validation and settings
- **pydantic-ai**: Use when calling Claude outside of Agent SDK (never manually parse LLM output)
- **pydantic-settings**: For configuration (not dotenv)

### forecasting-tools Library Notes

The `forecasting-tools` library has some type annotation limitations to be aware of:

1. **Question type polymorphism**: `MetaculusApi.get_question_by_post_id()` and `get_questions_matching_filter()` return `MetaculusQuestion`, but the actual runtime objects are subclasses (`BinaryQuestion`, `NumericQuestion`, `MultipleChoiceQuestion`, etc.). Use `isinstance()` checks when accessing subclass-specific attributes.

2. **`community_prediction_at_access_time`**: This attribute only exists on `BinaryQuestion`, not on the base `MetaculusQuestion`. Always check `isinstance(q, BinaryQuestion)` before accessing it.

3. **API method names**: Use `MetaculusClient.get_links_for_question()` for coherence links (not `get_coherence_links_for_question`). Check method names with the `inspect_api.py` script.

### Type Safety Requirements
- **No bare `except Exception`** — always catch specific exceptions
- **Every function must specify input and output types**
- **Use Python 3.12+ generics syntax**: `class A[T]`, not `Generic[T]`
- Use `TypedDict` and Pydantic models for structured data
- Never manually parse Claude/agent output — use structured outputs via pydantic
- **Never use `# type: ignore`** — Ask the user how to properly fix type errors instead of suppressing them

### Code as Documentation

The codebase should read as a **monolithic source of truth**—understandable without any knowledge of its history.

**The test:** Before adding a comment, ask: "Would this comment exist if the code had always been written this way?" If the answer is no—if you're only adding it because you modified the line—don't add it.

**Do not:**
- Add comments to explain modifications you made
- Reference what code used to do (e.g., "Previously this returned None")
- Add inline comments when changing a line (this is almost always explaining the change, not the code)
- Use phrases like "now", "new", "updated", "fixed", or "changed" in comments

**Do:**
- Write comments that would make sense to someone who never saw previous versions
- Use commit messages for change history, not code comments
- Only add comments that document genuinely non-obvious behavior

**Example — Bad:**
```python
env_file=(".env", ".env.local"),  # .env.local overrides .env
```
This comment was added because the line was changed. If the code had always supported multiple env files, no one would bother commenting that the second one overrides the first—that's standard behavior.

**Example — Good:**
```python
env_file=(".env", ".env.local"),
```
No comment needed. The behavior is self-evident to anyone familiar with config file precedence.

### Error Handling Philosophy

**MCP tools should:**
- Return `{"content": [...], "is_error": True}` for recoverable errors (let agent retry/adapt)
- Log exceptions with `logger.exception()` for debugging
- Include actionable error messages (what failed, why, what to try)

**Agent code should:**
- Raise exceptions for unrecoverable errors (missing config, invalid state)
- Use the `with_retry` decorator for transient failures (HTTP timeouts, rate limits)
- Validate inputs early with Pydantic models

**Never silently swallow errors** — either handle them meaningfully or let them propagate.

### Tools
- **uv**: Package manager. Use `uv add <package>` to install packages (never edit pyproject.toml directly)
- **ruff**: Formatting and linting
- **pyright**: Type checking

## Helper Scripts

The `.claude/scripts/` directory contains reusable scripts for common tasks. **Always use these scripts instead of ad-hoc commands.** Never use `uv run python -c "..."` or bare `python`/`python3` — these are denied in settings.json. Always use `uv run` to ensure the correct virtualenv. If the existing scripts don't cover your use case, create a new script.

If you find yourself running the same kind of command repeatedly—whether it's a Python snippet, a bash pipeline, an API call, a data transformation, or any other programmatic operation—**stop and create a script** in `.claude/scripts/` instead. Then update this section of CLAUDE.md to document it.

**Write scripts in Python using [typer](https://typer.tiangolo.com/)** for consistent CLI interfaces with automatic help text and argument parsing. Use **[sh](https://sh.readthedocs.io/)** for shell commands instead of `subprocess`.

This applies to any repetitive programmatic call, not just Python functions.

### inspect_api.py

Explore package APIs—never use `python -c "import ..."` or ad-hoc REPL commands.

```bash
# Show summary of a class (methods, properties, constants)
uv run python .claude/scripts/inspect_api.py <module.Class>

# Show signature of a specific method
uv run python .claude/scripts/inspect_api.py <module.Class.method>

# Show full help() output
uv run python .claude/scripts/inspect_api.py <module.Class> --help-full
```

Examples:
```bash
uv run python .claude/scripts/inspect_api.py forecasting_tools.SmartSearcher
uv run python .claude/scripts/inspect_api.py forecasting_tools.MetaculusApi.get_question_by_post_id
uv run python .claude/scripts/inspect_api.py mcp.server.fastmcp.FastMCP --help-full
```

### module_info.py

Get paths and source code for installed Python modules. Use this instead of `uv run python -c "import x; print(x.__file__)"`.

```bash
# Get the file path of a module
uv run python .claude/scripts/module_info.py path forecasting_tools.helpers.asknews_searcher

# View module source code (first 100 lines by default)
uv run python .claude/scripts/module_info.py source forecasting_tools.helpers.asknews_searcher

# View more lines
uv run python .claude/scripts/module_info.py source forecasting_tools.helpers.asknews_searcher --lines 200
```

### new_worktree.py

Create a new git worktree with Claude session migration. Use this instead of manually running `git worktree add` when you want to preserve Claude Code context in the new worktree.

```bash
# Create new worktree branching from current branch
uv run python .claude/scripts/new_worktree.py <worktree-name>

# Migrate a specific session instead of most recent
uv run python .claude/scripts/new_worktree.py <worktree-name> --session-id <uuid>

# Skip uv sync (if you'll do it manually)
uv run python .claude/scripts/new_worktree.py <worktree-name> --no-sync

# Skip copying logs/ directory
uv run python .claude/scripts/new_worktree.py <worktree-name> --no-copy-data
```

The script:
1. Creates a new worktree in the `tree/` directory with a new branch
2. Copies `.env.local` and `logs/` directory (notes/ is tracked in git)
3. Runs `uv sync --all-groups --all-extras`
4. Migrates the most recent Claude session to the new worktree

After running, `cd` to the new worktree and run `claude --resume` to continue the session.

### feedback_collect.py

Collect calibration data from resolved forecasts. Used by the `/feedback-loop` command to gather metrics before analysis.

```bash
# Collect from default tournament (AIB Spring 2026)
uv run python .claude/scripts/feedback_collect.py

# Collect from specific tournament
uv run python .claude/scripts/feedback_collect.py --tournament spring-aib-2026

# Collect all resolved questions (ignore last run timestamp)
uv run python .claude/scripts/feedback_collect.py --all-time

# Collect only questions resolved after a date
uv run python .claude/scripts/feedback_collect.py --since 2026-01-01
```

The script:
1. Fetches resolved questions from Metaculus
2. Matches them to forecasts in `notes/forecasts/`
3. Computes Brier scores, log scores, and calibration buckets
4. Saves metrics to `notes/feedback_loop/<timestamp>_metrics.json`

### trace_forecast.py

Link forecasts to their logs and metrics. Useful for debugging and feedback loop analysis.

```bash
# Show details for a specific forecast
uv run python .claude/scripts/trace_forecast.py show 41906

# Show with full tool-by-tool metrics
uv run python .claude/scripts/trace_forecast.py show 41906 --verbose

# List recent forecasts with metrics summary
uv run python .claude/scripts/trace_forecast.py list

# Show forecasts with tool errors
uv run python .claude/scripts/trace_forecast.py errors
```

The script displays:
- Forecast details (probability, logit, timestamp)
- Tool metrics (call counts, error rates, durations)
- Log file paths and sizes
- Error breakdowns by tool

### debug.py

Debug tools for Metaculus API parsing and MCP error propagation.

```bash
# Test Metaculus API parsing
uv run python .claude/scripts/debug.py metaculus --tournament spring-aib-2026

# Test only raw API parsing (no client)
uv run python .claude/scripts/debug.py metaculus --raw-only

# Test MCP error flag propagation (SDK workaround verification)
uv run python .claude/scripts/debug.py mcp-error
```

### aggregate_metrics.py

Aggregate metrics across all forecasts for analysis.

```bash
# Show summary (counts, costs, tokens)
uv run python .claude/scripts/aggregate_metrics.py summary

# Show tool usage aggregates
uv run python .claude/scripts/aggregate_metrics.py tools

# Show metrics by question type
uv run python .claude/scripts/aggregate_metrics.py by-type

# Show forecasts with high error rates
uv run python .claude/scripts/aggregate_metrics.py errors
```

### resolution_update.py

Fetch resolutions from Metaculus and update saved forecasts.

```bash
# Check for and apply resolution updates
uv run python .claude/scripts/resolution_update.py check

# Dry run (don't modify files)
uv run python .claude/scripts/resolution_update.py check --dry-run

# Show resolution status of all forecasts
uv run python .claude/scripts/resolution_update.py status

# Manually set resolution for a forecast
uv run python .claude/scripts/resolution_update.py set 12345 yes
```

### calibration_report.py

Generate calibration reports from resolved forecasts.

```bash
# Show calibration summary (Brier scores, buckets)
uv run python .claude/scripts/calibration_report.py summary

# Show detailed forecast-by-forecast results
uv run python .claude/scripts/calibration_report.py detail

# Export calibration data to JSON
uv run python .claude/scripts/calibration_report.py export
uv run python .claude/scripts/calibration_report.py export -o custom_path.json
```

### forecast_queue.py

Manage forecasting queue and priorities. Shows questions that need forecasting, sorted by urgency.

```bash
# Show forecasting status for a tournament
uv run python .claude/scripts/forecast_queue.py status aib

# Show questions closing soon that haven't been forecast
uv run python .claude/scripts/forecast_queue.py upcoming aib --days 7

# Include already-forecasted questions in the list
uv run python .claude/scripts/forecast_queue.py upcoming aib --all

# Show recently resolved questions that we missed
uv run python .claude/scripts/forecast_queue.py missed aib --days 14
```

Tournaments: `aib` (AIB Spring 2026), `minibench` (MiniBench), `cup` (Metaculus Cup)

## Settings & Configuration

All Claude Code settings modifications should be **project-level** (in `.claude/settings.json`), not user-level, so they're shared with the team.

### Merging Local Settings

**Every time you ask for permissions or respond to the user**, check if `.claude/settings.local.json` exists. If it does, review it for sensible defaults that should be merged into `.claude/settings.json`. This ensures useful permission patterns discovered during development get committed to the shared config.

`.claude/settings.local.json` is gitignored and contains user-specific or experimental settings. When a pattern proves useful, merge it to `.claude/settings.json` so the whole team benefits.

## Planning & Documentation

**PLAN.md** is the source of truth for what has been built and what remains. Keep it synchronized with reality:
- **Reflect actual state**: PLAN.md must accurately describe what exists in the codebase, not aspirational designs
- Mark completed items when finishing work (`[x]`)
- Update architecture decisions as they evolve
- Add new tasks discovered during implementation
- Keep status indicators current (`[ ]` pending, `[x]` done, `[~]` in progress)
- **No speculative code**: Don't include code snippets for unimplemented features—describe what to build, not how

## Asking Questions

**Always use the `AskUserQuestion` tool** instead of asking questions in plain text. This applies to:
- Clarifying requirements or ambiguous instructions
- Offering choices between implementation approaches
- Confirming before destructive or irreversible actions
- Any situation where you need user input before proceeding

Even if the question is open-ended and just needs a text response, use `AskUserQuestion` with options that include a blank/custom input option. This allows the user to parse responses as structured notifications rather than scanning through conversation summaries.

**Do not** embed questions in regular text responses—always route them through the tool.

## When in Doubt

Err on the side of asking questions (using `AskUserQuestion`) rather than making assumptions.

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

---

# Getting Started

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
- `FRED_API_KEY` not set → FRED economic data tools fail
- Docker not running → Sandbox code execution fails

**Inspecting tool outputs:**

- Tool results are JSON-encoded; parse with `json.loads()` if debugging
- Check `src/aib/tools/*.py` for expected input/output schemas

---

# Development Workflow

## Git Workflow

This project uses **git worktrees** (not regular branches) to develop multiple features in parallel.

**IMPORTANT:** Never commit _code_ directly to `main`. Always work in a worktree for code changes.

**Exception:** Data commits (`data(forecasts):`) can go directly to main—forecast outputs don't need review.

### Worktrees vs Branches

- **`git checkout -b`**: Creates a branch but stays in the same directory. Switching branches changes all files in place.
- **`git worktree add`**: Creates a new directory with its own working copy. Multiple branches can be worked on simultaneously in separate directories.

### If already in a worktree

**You are typically already in a worktree subbranch.** Check with `git worktree list` to confirm. If you're in a feature worktree, just work directly—no need to create another worktree or branch out.

### When implementing a feature

1. **Create a worktree** (if the user hasn't already created one):
   ```bash
   git worktree add ./worktrees/feat-name -b feat/feature-name
   cd ./worktrees/feat-name
   ```
2. **Commit regularly and atomically** — Each commit should represent a single logical change. Don't bundle unrelated changes together.
3. Push the branch when the feature is complete (or periodically for backup)
4. **Rebase before merging** — Once complete, rebase to create semantically meaningful commits. Squash fixups, reorder for clarity.
5. Create a PR for review
6. **Clean up worktree** after merge:
   ```bash
   git worktree remove ./worktrees/feat-name
   ```

### Commit Guidelines

- **Commit before responding** — Always commit your work before responding to the user. Don't accumulate multiple changes across responses.
- **Commit early, commit often** — Frequent commits provide checkpoints and make rebasing easier.
- **Keep commits atomic** — Each commit should do one thing. If you need "and" in your message, it should be two commits.
- **History will be rebased** — Don't worry about perfect messages during development. The history will be cleaned up before merge.
- **Meaningful final commits** — After rebasing, each commit should tell a story: what changed and why. The final history should be easy to read and bisect.

### Commit Message Format

Use conventional commit syntax: `type(scope): description`

**Types:**

- `feat` — New feature or capability
- `fix` — Bug fix
- `refactor` — Code change that neither fixes a bug nor adds a feature
- `docs` — Documentation only (README, standalone docs)
- `test` — Adding or updating tests
- `chore` — Maintenance (dependencies, build config, etc.)
- `meta` — Changes to `.claude/` files (CLAUDE.md, settings, scripts, commands)
- `data` — Generated data and outputs (forecasts, metrics, logs)

**Examples:**

```
feat(agent): add permission handler for read-only directories
fix(tools): handle missing API key gracefully
refactor(sandbox): extract Docker client initialization
meta(claude): update commit message guidelines
data(forecasts): add Feb 4 2026 forecast batch
```

### Forecast Commits

Forecast outputs use `data(forecasts):` and can be committed directly to main (no worktree needed).

**What goes in a forecast commit:**

- Forecast markdown files (`notes/forecasts/<question_id>/`)
- Meta-analysis notes (`notes/meta/`) — commit alongside the forecasts they relate to, not separately
- Resolution updates when questions resolve

**What does NOT go in a forecast commit:**

- Code changes (use worktree + PR)

**Note:** The `worktrees/` directory is gitignored.

## Editing Style

**Prefer small, atomic edits.** A PreToolUse hook auto-allows edits that match safe patterns (≤3 lines, pure deletions, import changes, adding comments/docstrings, whitespace-only). Larger edits require manual approval.

- **Split large changes into multiple small edits** — each Edit call should change ≤3 lines when possible
- **Separate concerns** — move imports in one edit, change logic in another
- **Delete separately** — remove old code in one edit, add new code in another

This makes reviews faster and keeps the workflow smooth.

## Code Style & Dependencies

### Primary Libraries

- **claude-agent-sdk**: Primary framework for building agents (use `query()` for one-shot LLM calls with structured output)
- **pydantic**: For data validation and settings
- **pydantic-settings**: For configuration (not dotenv)

### forecasting-tools Library Notes

The `forecasting-tools` library has some type annotation limitations:

1. **Question type polymorphism**: `MetaculusApi.get_question_by_post_id()` returns `MetaculusQuestion`, but actual objects are subclasses (`BinaryQuestion`, `NumericQuestion`, etc.). Use `isinstance()` checks.

2. **`community_prediction_at_access_time`**: Only exists on `BinaryQuestion`. Always check `isinstance(q, BinaryQuestion)` first.

3. **API method names**: Use `MetaculusClient.get_links_for_question()` for coherence links. Check method names with `inspect_api.py`.

### Type Safety Requirements

- **No bare `except Exception`** — always catch specific exceptions
- **Every function must specify input and output types**
- **Use Python 3.12+ generics syntax**: `class A[T]`, not `Generic[T]`
- Use `TypedDict` and Pydantic models for structured data
- Never manually parse Claude/agent output — use structured outputs via pydantic
- **Never use `# type: ignore`** — Ask the user how to properly fix type errors

### Use Standard Libraries

When integrating with external services (APIs, data sources, etc.):

- **Use existing Python libraries first** — Check PyPI for official or well-maintained client libraries before writing raw HTTP requests
- **Examples**: Use `arxiv` for arXiv search, `yfinance` for stock data, `fredapi` for FRED economic data
- **Don't rebuild the wheel** — If a library exists with good documentation and maintenance, use it

### Code as Documentation

The codebase should read as a **monolithic source of truth**—understandable without any knowledge of its history.

**The test:** Before adding a comment, ask: "Would this comment exist if the code had always been written this way?" If no—don't add it.

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

Why this is bad: The comment only exists because the line was *changed*. If the code had always supported multiple env files, no developer would comment that later files override earlier ones—that's how all config file systems work. The comment explains the modification, not the code.

**Example — Good:**

```python
env_file=(".env", ".env.local"),
```

Why this is good: The behavior is self-evident to anyone familiar with configuration precedence. No comment needed. The git history explains *when* and *why* multiple env files were added.

**The underlying principle:** Comments that explain *what you changed* create noise for future readers who don't care about the change—they just need to understand the current code. Those explanations belong in commit messages, where they're preserved but don't clutter the codebase.

### Error Handling Philosophy

**MCP tools should:**

- Return `{"content": [...], "is_error": True}` for recoverable errors
- Log exceptions with `logger.exception()` for debugging
- Include actionable error messages (what failed, why, what to try)

**Agent code should:**

- Raise exceptions for unrecoverable errors (missing config, invalid state)
- Use the `with_retry` decorator for transient failures (HTTP timeouts, rate limits)
- Validate inputs early with Pydantic models

**Never silently swallow errors** — either handle them meaningfully or let them propagate.

### Tools

- **uv**: Package manager. Use `uv add <package>` (never edit pyproject.toml directly)
- **ruff**: Formatting and linting
- **pyright**: Type checking

---

# Tooling

## Helper Scripts

The `.claude/plugins/aib/scripts/` directory contains reusable scripts. **Always use these scripts instead of ad-hoc commands.** Never use `uv run python -c "..."` or bare `python`/`python3` — these are denied in settings.json.

If you find yourself running the same command repeatedly, **create a script** in `.claude/plugins/aib/scripts/` and document it here.

**Write scripts in Python using [typer](https://typer.tiangolo.com/)** for CLI interfaces. Use **[sh](https://sh.readthedocs.io/)** for shell commands instead of `subprocess`.

### inspect_api.py

Explore package APIs—never use `python -c "import ..."` or ad-hoc REPL commands.

```bash
uv run python .claude/plugins/aib/scripts/inspect_api.py <module.Class>
uv run python .claude/plugins/aib/scripts/inspect_api.py <module.Class.method>
uv run python .claude/plugins/aib/scripts/inspect_api.py <module.Class> --help-full
```

### module_info.py

Get paths and source code for installed Python modules.

```bash
uv run python .claude/plugins/aib/scripts/module_info.py path <module>
uv run python .claude/plugins/aib/scripts/module_info.py source <module> [--lines N]
```

### new_worktree.py

Create a new git worktree with Claude session migration.

```bash
uv run python .claude/plugins/aib/scripts/new_worktree.py <name> [--session-id UUID] [--no-sync] [--no-copy-data]
```

Creates worktree in `tree/`, copies `.env.local` and `logs/`, runs `uv sync`, migrates Claude session. After running, `cd` to the worktree and run `claude --resume`.

### feedback_collect.py

Collect calibration data from resolved forecasts.

```bash
uv run python .claude/plugins/aib/scripts/feedback_collect.py [--tournament X] [--all-time] [--since DATE]
```

### trace_forecast.py

Link forecasts to their logs and metrics.

```bash
uv run python .claude/plugins/aib/scripts/trace_forecast.py show <id> [--verbose]
uv run python .claude/plugins/aib/scripts/trace_forecast.py list
uv run python .claude/plugins/aib/scripts/trace_forecast.py errors
```

### debug.py

Debug tools for Metaculus API parsing and MCP error propagation.

```bash
uv run python .claude/plugins/aib/scripts/debug.py metaculus [--tournament X] [--raw-only]
uv run python .claude/plugins/aib/scripts/debug.py mcp-error
```

### aggregate_metrics.py

Aggregate metrics across all forecasts.

```bash
uv run python .claude/plugins/aib/scripts/aggregate_metrics.py summary|tools|by-type|errors
```

### resolution_update.py

Fetch resolutions from Metaculus and update saved forecasts.

```bash
uv run python .claude/plugins/aib/scripts/resolution_update.py check [--dry-run]
uv run python .claude/plugins/aib/scripts/resolution_update.py status
uv run python .claude/plugins/aib/scripts/resolution_update.py set <id> <yes|no>
```

### calibration_report.py

Generate calibration reports from resolved forecasts.

```bash
uv run python .claude/plugins/aib/scripts/calibration_report.py summary|detail
uv run python .claude/plugins/aib/scripts/calibration_report.py export [-o FILE]
```

### forecast_queue.py

Manage forecasting queue and priorities.

```bash
uv run python .claude/plugins/aib/scripts/forecast_queue.py status <tournament>
uv run python .claude/plugins/aib/scripts/forecast_queue.py upcoming <tournament> [--days N] [--all]
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed <tournament> [--days N]
```

Tournaments: `aib` (AIB Spring 2026), `minibench` (MiniBench), `cup` (Metaculus Cup)

## Settings & Configuration

All Claude Code settings modifications should be **project-level** (in `.claude/settings.json`), not user-level.

### Merging Local Settings

**Every time you respond to the user**, check if `.claude/settings.local.json` exists. If it does, review it for sensible defaults to merge into `.claude/settings.json`. This ensures useful permission patterns get committed to the shared config.

---

# Process & Communication

## Asking Questions

**Always use the `AskUserQuestion` tool** instead of asking questions in plain text. This applies to:

- Clarifying requirements or ambiguous instructions
- Offering choices between implementation approaches
- Confirming before destructive or irreversible actions
- Proposing changes or improvements
- Any situation where you need user input before proceeding

Even for open-ended questions, use `AskUserQuestion` with options that include a custom input option. This allows structured notification parsing.

**When proposing changes:**

- **Propose, don't assume**: Use AskUserQuestion before making changes
- **Show context**: Show relevant current state before proposing
- **Explain rationale**: Every suggestion should include why it would help
- **Offer alternatives**: Present options when multiple valid approaches exist

**When in doubt, ask.** Err on the side of asking questions rather than making assumptions.

## Planning & Documentation

**PLAN.md** is the source of truth for what has been built and what remains. Keep it synchronized with reality:

- **Reflect actual state**: PLAN.md must describe what exists, not aspirational designs
- Mark completed items when finishing work (`[x]`)
- Update architecture decisions as they evolve
- Add new tasks discovered during implementation
- Keep status indicators current (`[ ]` pending, `[x]` done, `[~]` in progress)
- **No speculative code**: Describe what to build, not how

## Code Change Reports

After completing code modifications, provide an **extensive report** including:

1. **Summary** — One paragraph explaining the overall change and its purpose

2. **Files Modified** — List each file with path, nature of change, and brief description

3. **Detailed Changes** — For each significant change:
   - **Context**: Show surrounding code (10-20 lines)
   - **Before/After**: If modifying existing code, show both versions
   - **Rationale**: Why this approach was chosen

4. **Architectural Considerations** — Did you consider unifying with existing patterns? Are there similar functions that could be consolidated?

5. **Testing** — What tests were added/modified?

**Code block format:**

```python
# src/aib/tools/example.py (lines 45-67)

def existing_function():
    """Show enough context to understand the change."""
    # ... existing code ...
    new_behavior = do_something_different()
    # ... more existing code ...
    return result
```

**Example report:**

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

## Slash Commands & Skills

**After every command invocation**, reflect on how it was actually used vs. documented:

1. **Compare intent vs usage**: Did the command serve its documented purpose, or was it adapted?
2. **Notice patterns**: When the user corrects your approach or redirects focus, that's a signal the command should evolve.
3. **Proactively propose updates**: Use AskUserQuestion to suggest command improvements.

**Evolution signals:**

- User provides external docs → Add doc-fetching or reference to command
- User corrects your approach → Update command to prevent future errors
- User asks for something the command should cover → Expand scope
- User ignores sections → Consider simplifying

## External Resources

When questions involve Claude Code, Agent SDK, or Claude API:

1. **Use the claude-code-guide subagent**:
   ```
   Task(subagent_type="claude-code-guide", prompt="<specific question>")
   ```

2. **Fetch docs directly** for specific pages:
   - `WebFetch(url="https://docs.claude.com/en/agent-sdk/<topic>")`
   - `WebFetch(url="https://docs.claude.com/en/claude-code/<topic>")`

When the user provides documentation links, incorporate that knowledge into CLAUDE.md or relevant commands.

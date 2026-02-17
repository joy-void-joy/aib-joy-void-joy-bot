# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Note:** Modifying `CLAUDE.md` or `AGENTS.md` means modifying `.claude/CLAUDE.md` (this file).

## Project Overview

A forecasting bot for the [Metaculus AI Benchmarking Tournament](https://www.metaculus.com/aib/). Uses Claude Code with extended capabilities (web search, Python execution, etc.) to generate accurate predictions on forecasting questions.

Built with Python 3.13+ and the Claude Agent SDK. Uses `uv` as the package manager.

### Important Context

- **Submission is handled separately** — This codebase generates forecasts; a separate system handles submission to Metaculus
- **No CP during live forecasting** — The agent cannot see the community prediction for the question it is currently forecasting (tournament rule). CP data is available post-hoc via individual API fetches for calibration analysis.
- **CDF required for numeric questions** — Numeric and discrete questions require a 201-point CDF (cumulative distribution function), not just point estimates

---

# Getting Started

## Reference Files

- **src/aib/cli.py**: CLI entry point (`uv run forecast test <question_id>`)
- **src/aib/agent/core.py**: Main forecasting agent orchestration using Claude Agent SDK
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

**Do not hypothesize — trace.** When debugging errors, find the actual logs and read the exact exception. Do not list "likely causes" or suggest the user check things. Open the log files yourself, grep for the error, read the traceback, and report what actually happened. If the logs don't contain enough information, say exactly what logging to add and where, so the error is captured next time.

Use `/debug <error message>` to trace an error through the logs automatically.

**When a forecast fails:**

1. Search `logs/<question_id>/` for the error text and grep for ERROR/exception — read the full traceback, don't stop at the catch-all error message
2. Check `notes/sessions/<session_id>/` for the agent's intermediate reasoning and meta-reflection
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
4. **Bump AGENT_VERSION** if the branch changes agent behavior (prompts, tools, subagents, scoring). See `src/aib/version.py` for bump rules. Data-only or infrastructure changes don't need a bump.
5. **`/rebase`** — Pushes the branch, opens a PR, then cleans up the commit history with `git reset --soft main` and force-pushes.
6. **Review the PR** — If changes are needed, fix them on the feature branch and re-run `/rebase` (it rebuilds the history and force-pushes, updating the PR).
7. **`/close`** — Once the PR is approved, merges it and cleans up the branch.

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
- Session notes (`notes/sessions/`) — commit alongside the forecasts they relate to, not separately
- Resolution updates when questions resolve

**What does NOT go in a forecast commit:**

- Code changes (use worktree + PR)

**Note:** The `worktrees/` directory is gitignored.

## Editing Style

**Prefer small, atomic edits.** A PreToolUse hook counts "real" changed lines (ignoring imports, comments, whitespace, blank lines, docstrings) and auto-allows edits with ≤3 real changes. Pure deletions, TypedDict/BaseModel definitions, and single-line `replace_all` renames are always auto-allowed.

- **Split large changes into multiple small edits** — keep real (non-trivial) line changes to ≤3 per Edit call
- **Separate concerns** — move imports in one edit, change logic in another (import changes are trivial and don't count)
- **Use `rename-symbol`** for identifier renames instead of `Edit` with `replace_all`

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

3. **API method names**: Use `MetaculusClient.get_links_for_question()` for coherence links. Check method names with `uv run aib-devtools api inspect`.

### Type Safety Requirements

- **No bare `except Exception`** — always catch specific exceptions
- **Every function must specify input and output types**
- **Never use `Any`** — Use `TypedDict` for dict-like data, `BaseModel` for validated models, or specific types. `Any` hides type errors and defeats static analysis.
- **Use Python 3.12+ generics syntax**: `class A[T]`, not `Generic[T]`
- Use `TypedDict` and Pydantic models for structured data
- Never manually parse Claude/agent output — use structured outputs via pydantic
- **Never use `# type: ignore`** — Ask the user how to properly fix type errors

### No Regex/String Parsing for Structured Data

Never use regex or string substitution to parse HTML, XML, JSON, or other structured formats. Use proper parsing libraries:

- **Web page text extraction**: Use `trafilatura` — it handles boilerplate removal, content extraction, and metadata
- **HTML DOM manipulation**: Use `beautifulsoup4` when you need to navigate/query the DOM tree
- **XML**: Use `xml.etree.ElementTree` or `lxml`
- **JSON embedded in HTML**: Parse the HTML with BeautifulSoup first, then `json.loads()`

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

### Pyright LSP

The `pyright-lsp` plugin is enabled and provides code intelligence tools. **Use these actively** — they are faster and more accurate than grep-based searches for code understanding and refactoring.

**Navigation (use before editing unfamiliar code):**

- **go-to-definition** — Jump to where a symbol is defined. Use this instead of grepping for `def foo` or `class Foo`.
- **find-references** — Find all usages of a symbol. Use this instead of grepping for a symbol name.
- **hover-documentation** — Get type info and docs for a symbol at a position.
- **list-symbols** — List all symbols in a file. Use this instead of grepping for `def ` or `class `.
- **find-implementations** — Find implementations of an interface or abstract method.
- **trace-call-hierarchy** — Understand call chains. Use this instead of manually tracing function calls.

**Refactoring:**

- **rename-symbol** — Rename a symbol across the workspace. **Always prefer this over `Edit` with `replace_all`** for identifier renames — it understands scope and won't rename unrelated identifiers that happen to share the same name.
- **rename-symbol-strict** — Same as above but with explicit position for disambiguation when multiple candidates exist at the same location.

**Diagnostics:**

- After every file edit, pyright automatically analyzes changes and reports type errors. Pay attention to these — they catch issues immediately.

**When to use LSP vs grep/Edit:**

| Task | Use LSP | Use grep/Edit |
|---|---|---|
| Find where a function is defined | `go-to-definition` | |
| Find all callers of a function | `find-references` | |
| Rename a variable/function/class | `rename-symbol` | |
| Search for a string literal | | `Grep` |
| Search across non-Python files | | `Grep` |
| Change logic within a function | | `Edit` |
| Add new code | | `Edit` / `Write` |


---

# Tooling

## Running Python

Bare `python`/`python3` and `uv run python -c "..."` are denied by the Bash permission hook. When you need to run Python:

1. **Prefer `aib-devtools`** — Use existing commands (`uv run aib-devtools <group> <command>`), or add new functionality to `src/aib/devtools/` if a capability is missing.
2. **Use `tmp/*.py` only as a stepping stone** — Write a throwaway script in `tmp/` and run it with `uv run python tmp/my_script.py`. **Once it works, always promote it to `aib-devtools`** — don't just copy it verbatim; generalize the functionality with proper CLI arguments, help text, and error handling so it's reusable beyond the immediate task. Extract the logic into the appropriate sub-group in `src/aib/devtools/`, register the command, and delete the tmp script. Tmp scripts are prototypes, not permanent tools.

## aib-devtools CLI

Source: `src/aib/devtools/`

```
aib-devtools
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
│   ├── build          Rebuild scores CSV from all forecast JSONs
│   ├── show           Show scores table (--post-id, --version, --source, --resolved)
│   ├── summary        Aggregate statistics by type, source, version
│   ├── compare        Compare two agent versions on overlapping questions
│   ├── regression     Regression suite results
│   └── extremes       Best/worst forecasts (--non-meta, --version, --type, -n)
│
├── queue              Forecasting queue and priorities
│   ├── status         Tournament status overview
│   ├── upcoming       Questions closing soon (--days N, --all)
│   ├── missed         Recently closed without forecast (--days N)
│   └── search         Search questions (--type, --limit, --resolved/--open)
│
├── resolution         Resolution updates
│   ├── check          Fetch and apply resolutions from Metaculus (--dry-run)
│   ├── status         Show resolution status of all forecasts
│   └── set            Manually set resolution for a post
│
├── feedback           Feedback collection
│   └── collect        Collect metrics from resolved forecasts
│
├── trace              Forecast tracing and log analysis
│   ├── show           Show forecast trace for a post ID (--verbose)
│   ├── list           List all traced forecasts
│   ├── errors         Show forecasts with errors
│   ├── log            Extract agent reasoning from forecast log
│   └── logs           List available forecast logs
│
├── metrics            Aggregate metrics
│   ├── summary        Overall metrics summary
│   ├── tools          Tool usage statistics
│   ├── by-type        Metrics by question type
│   └── errors         Error summary
│
├── api                API inspection and debugging
│   ├── inspect        Explore package APIs (replaces python -c "import ...")
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
├── dev                Development tools
│   └── worktree       Create a new worktree with plugin refresh
│
├── version            Agent version management
│   ├── show           Display current AGENT_VERSION
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
└── health             Service health checks
    └── check          Ping Metaculus, Exa, FRED, Docker
```

Tournaments: `aib` (AIB Spring 2026), `minibench` (MiniBench), `cup` (Metaculus Cup), `all` (cross-tournament)

## Permission Hooks

Permissions are managed by **PreToolUse hook scripts** in `.claude/plugins/aib/hooks/scripts/` rather than glob patterns in `settings.json`. Each hook uses regex patterns for precise control.

| Hook | Tool | Config |
|---|---|---|
| `auto_allow_fetch.py` | WebFetch | `ALLOW_PATTERNS` (regex), `DENY_PATTERNS` (regex + reason) |
| `auto_allow_bash.py` | Bash | `RULES` list (gitignore-style: last match wins) |
| `auto_allow_edits.py` | Edit | Trivial-line counting, protected file list |

**To add a new allowed URL or command**, edit the pattern list at the top of the corresponding hook script. Non-matching inputs fall through to the user prompt (ask).

`settings.json` only contains rules that don't need regex: `WebSearch` (allow), `Read(.local)` (deny), `Edit(pyproject.toml)` (ask).

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

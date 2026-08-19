<!-- Generated from aib.devtools.harness.content.guidance by `uv run lup-devtools harness generate all` — edit the source, not this file. See docs/harness.md. Deliberately rendered as .claude/CLAUDE.md under Claude Code, AGENTS.md under Codex. -->

# Repository guidance

This file is what an agent working in this repository is given before it reads anything else.

**Note:** It is generated. The source is `src/aib/devtools/harness/content/guidance.py`; edit that and run `uv run lup-devtools harness generate all`.

## Project Overview

A forecasting bot for the [Metaculus AI Benchmarking Tournament](https://www.metaculus.com/aib/). Uses the Claude Agent SDK with extended capabilities (web search, Python execution, etc.) to generate accurate predictions on forecasting questions.

Built with Python 3.14+ and the Claude Agent SDK. Uses `uv` as the package manager, and `lup` as the agent framework beneath it.

### Important Context

- **Submission is handled separately** — This codebase generates forecasts; a separate system handles submission to Metaculus
- **No CP during live forecasting** — The agent cannot see the community prediction for the question it is currently forecasting (tournament rule). CP data is available post-hoc via individual API fetches for calibration analysis.
- **CDF required for numeric questions** — Numeric and discrete questions require a 201-point CDF (cumulative distribution function), not just point estimates
- **Version scope** — When analyzing forecasts, traces, or calibration data, determine which versions are relevant from context (user's question, current version, task at hand). Don't default to scanning all versions — earlier versions had different architectures and their data is rarely comparable. When in doubt, ask.

---

# Getting Started

## Reference Files

- **src/aib/cli.py**: CLI entry point (`uv run forecast test <question_id>`)
- **src/aib/agent/core.py**: Main forecasting agent orchestration using Claude Agent SDK
- **src/aib/agent/numeric.py**: CDF generation for numeric/discrete questions
- **src/aib/submission.py**: Metaculus API submission functions
- **src/aib/tools/**: MCP tool implementations (forecasting, sandbox, composition, markets)

## Never run a forecast yourself

**`uv run forecast ...` is the user's command to run, never yours.** This covers
`test`, `submit`, `tournament`, `loop`, `retrodict`, and `backfill-comments` —
whether or not the variant submits to Metaculus. The same applies to any
`lup-devtools` command that spawns a forecasting agent (`worldview loop`,
`resolution tentative`, `analysis review`).

A forecast burns real credits, takes tens of minutes, and writes to `notes/`.
The user decides when to spend that, and watches it live.

This is a gate rather than a norm: every one of those spellings is declared
refused in `harness/content/shell_vocabulary.py`, and the refusal carries the
instruction below. What makes it a declaration rather than a warning is that
the policy judges a parsed command, so putting the forecast behind something
else on the same line does not get it through.

When a change needs a forecast to verify, finish everything you *can* verify —
tests, `ruff`, `pyright`, `lup-devtools health check`, targeted probes of the
changed code — then **print the exact command for the user to run** and say what
to look for in the output:

> Ready to verify. Run:
> ```bash
> uv run forecast test 44798
> ```
> Watch for: `mcp__research__research` succeeding on the first call (no pydantic
> validation retry), and the reflection `tool_audit` listing no missing
> capabilities.

Do not launch it in the background, and do not offer to run it "just this once".

## Commands

```bash
uv sync
uv add <package-name>     # never edit pyproject.toml directly
uv run ruff format .
uv run ruff check .
uv run pyright
```

The forecasting commands are the user's to run and yours to print:

```bash
uv run forecast test <question_id>              # no submission
uv run forecast submit <question_id> [--comment]
uv run forecast tournament <aib|minibench|cup>  # skips already forecast
uv run forecast ab --list | -v <variant> -v <variant>
```

Any of them takes `--profile <name>` to run on a registered Claude account.
`docs/devtools.md` carries the tournament names and the rest.

## A/B Testing

Variants are named agent configurations registered in `notes/variants.json`,
run side by side with `uv run forecast ab`. Each arm is a separate process
and wants its own `profile`, and traces land under `<version>+<variant>` so
an in-flight experiment stays out of the released version's calibration
numbers. `docs/devtools.md` carries the registry format and the rest.

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

**A test is edited like any other file** — the ordinary lattice judges it, with
no gate of its own. What the gate protected still holds as a norm: a test states
the behaviour production owes, so changing one to match an implementation is
backwards. Change the implementation, and edit the test only when it genuinely
encodes the wrong behaviour — saying, in the commit, which it was.

## Debugging

**Do not hypothesize — trace.** When debugging errors, find the actual logs and read the exact exception. Do not list "likely causes" or suggest the user check things. Open the log files yourself, grep for the error, read the traceback, and report what actually happened. If the logs don't contain enough information, say exactly what logging to add and where, so the error is captured next time.

Use /lup:debug to trace an error through the logs automatically.

**When a forecast fails:**

1. Search `logs/<question_id>/` for the error text and grep for ERROR/exception — read the full traceback, don't stop at the catch-all error message
2. Check `notes/traces/<version>/sessions/<session_id>/` for the agent's intermediate reasoning and meta-reflection
3. Check API key configuration: missing keys log warnings at startup

`docs/devtools.md` lists the common startup failures and what each missing
key breaks.

---

# Development Workflow

## Git Workflow

This project uses **git worktrees** (not regular branches) to develop multiple features in parallel.

**IMPORTANT:** Never commit _code_ directly to `main`. Always work in a worktree for code changes.

**Exception:** Data commits (`data(forecasts):`) can go directly to main—forecast outputs don't need review.

### If already in a worktree

**You are typically already in a worktree subbranch.** Check with `git worktree list` to confirm. If you're in a feature worktree, just work directly—no need to create another worktree or branch out.

### When implementing a feature

1. **Create a worktree** (if the user hasn't already created one):
   ```bash
   uv run lup-devtools dev worktree create feat-name
   ```
   This creates the worktree as a sibling under `tree/` (e.g., `tree/feat-name` alongside `tree/main`), syncs dependencies, and refreshes plugins. **Never** use `git worktree add ./worktrees/...` — worktrees must be siblings, not nested inside another checkout.
2. **Commit regularly and atomically** — Each commit should represent a single logical change. Don't bundle unrelated changes together.
3. Push the branch when the feature is complete (or periodically for backup)
4. **Bump AGENT_VERSION** if the branch changes agent behavior (prompts, tools, subagents, scoring). `[tool.lup] agent_version` in `pyproject.toml` is where it lives. Data-only or infrastructure changes don't need a bump. **Every version bump must include a corresponding `CHANGELOG.md` entry** — use `uv run lup-devtools version bump` or manually add an entry following the existing format.
5. **/lup:rebase** — Pushes the branch, opens a PR, then cleans up the commit history with `git reset --soft main` and force-pushes.
6. **Review the PR** — If changes are needed, fix them on the feature branch and re-run the rebase skill (it rebuilds the history and force-pushes, updating the PR).
7. **/lup:close** — Once the PR is approved, merges it and cleans up the branch.

The plugin needs no version bump of its own: it is generated, so its version is
the harness generator's and moves when the declaration does.

It is not installed through a marketplace. `harness claude` launches the
generated tree of whichever checkout it is run from, naming it with
`--plugin-dir`, so a worktree carries its plugin by existing and a change on a
feature branch takes effect there immediately.

### Commit Guidelines

- **Commit before responding** — Always commit your work before responding to the user. Don't accumulate multiple changes across responses.
- **Commit early, commit often** — Frequent commits provide checkpoints and make rebasing easier.
- **Keep commits atomic** — Each commit should do one thing. If you need "and" in your message, it should be two commits.
- **History will be rebased** — Don't worry about perfect messages during development. The history will be cleaned up before merge.
- **Meaningful final commits** — After rebasing, each commit should tell a story: what changed and why. The final history should be easy to read and bisect.

### Commit Message Format

Conventional commits, `type(scope): description`. Two types are this
repository's own: `meta` for the harness declarations and the trees they
generate, and `data` for generated output. `docs/devtools.md` lists every
type with an example.

### Forecast Commits

Forecast outputs use `data(forecasts):` and can be committed directly to main (no worktree needed).

**What goes in a forecast commit:**

- Forecast markdown files (`notes/traces/<version>/forecasts/<question_id>/`)
- Session notes (`notes/traces/<version>/sessions/`) — commit alongside the forecasts they relate to, not separately
- Resolution updates when questions resolve

**What does NOT go in a forecast commit:**

- Code changes (use worktree + PR)

**Note:** The `worktrees/` directory is gitignored.

### Keep `main` published

**Push `main` after committing data.** The forecast loop commits `notes/` to local
`main`, so `main` drifts ahead of `origin/main` unless you push. A feature branch
cut from that `main` inherits the unpushed commits, and the PR folds every one of
their `notes/` files in as a fresh addition. `docs/devtools.md` carries how that
happens and what it cost.

```bash
git log --oneline origin/main..main   # should be empty before you open a PR
git push origin main
```

### Git Hooks

Four guards over two moments, declared in `src/aib/devtools/dev.py` and written
by `uv run lup-devtools dev git-hooks install`. Each moment runs its guards in
declaration order and stops at the first refusal, so the nearly-free check goes
first.

| Moment | Refuses |
|---|---|
| `pre-commit` | A generated artifact behind its source. Then a commit mixing `notes/` data with code — data goes to `main`, code through a worktree and a PR. |
| `pre-push` | A branch whose PR would carry `notes/` files, i.e. `main` is unpushed and the base is stale. Then `dev gate`: `ruff`, `pyright`, the non-integration tests, and `harness check all`. |

Both push guards read git's ref list, which git delivers once, so the hook
captures it and replays it to each.

The bodies are tracked, and `core.hooksPath` is what points git at them — one
setting per clone, which every worktree cut from it inherits. `dev setup-hooks`
writes that setting; `dev git-hooks install` writes the bodies. Bypass either
moment with `--no-verify` when a branch deliberately reshapes `notes/`.

## Editing Style

**Prefer small, atomic edits.** The edit gate counts "real" changed lines (ignoring imports, comments, whitespace, blank lines, docstrings) and auto-allows edits with ≤3 real changes. Pure deletions, TypedDict/BaseModel definitions, and single-line `replace_all` renames are always auto-allowed.

- **Split large changes into multiple small edits** — keep real (non-trivial) line changes to ≤3 per Edit call
- **Separate concerns** — move imports in one edit, change logic in another (import changes are trivial and don't count)
- **Use the codeintel rename tool** for identifier renames instead of `Edit` with `replace_all`

This makes reviews faster and keeps the workflow smooth.

## Code Style & Dependencies

### Primary Libraries

- **claude-agent-sdk**: Primary framework for building agents (use `query()` for one-shot LLM calls with structured output)
- **lup**: The agent framework this project is built on — tools, tracing, paths, hooks, and the permission policy
- **pydantic**: For data validation and settings
- **pydantic-settings**: For configuration (not dotenv)

### forecasting-tools Library Notes

The `forecasting-tools` library has some type annotation limitations:

1. **Question type polymorphism**: `MetaculusApi.get_question_by_post_id()` returns `MetaculusQuestion`, but actual objects are subclasses (`BinaryQuestion`, `NumericQuestion`, etc.). Use `isinstance()` checks.

2. **`community_prediction_at_access_time`**: Only exists on `BinaryQuestion`. Always check `isinstance(q, BinaryQuestion)` first.

3. **API method names**: Use `MetaculusClient.get_links_for_question()` for coherence links. Check method names with `uv run lup-devtools api inspect`.

### Type Safety Requirements

- **No bare `except Exception`** — always catch specific exceptions
- **Every function must specify input and output types**
- **Never use `Any`** — Use `TypedDict` for dict-like data, `BaseModel` for validated models, or specific types. `Any` hides type errors and defeats static analysis.
- **Use Python 3.12+ generics syntax**: `class A[T]`, not `Generic[T]`
- Use `TypedDict` and Pydantic models for structured data
- Never manually parse Claude/agent output — use structured outputs via pydantic
- **Never use `# type: ignore`** — Ask the user how to properly fix type errors

### No Private Functions or Variables

Don't use leading underscores on functions, constants, or variables. Everything should be public. If a utility might be reusable, it will be — and private names discourage reuse. Before writing a new helper, check if one already exists in the codebase that can be made public or is already public.

### No String Manipulation on Structured Data

If you're reaching for `re`, `.replace()`, `.split()`, string slicing, or any string operation to extract, transform, or filter structured data, something is wrong. Operate on the structure directly.

- **Web pages**: Use `trafilatura` for text extraction, `beautifulsoup4` for DOM queries
- **XML**: Use `xml.etree.ElementTree` or `lxml`
- **JSON**: `json.loads()`, not regex
- **SDK objects**: Filter `ContentBlock` lists by type and attribute (e.g. `ToolUseBlock.name`, `ToolResultBlock.tool_use_id`) — see `sources.py` for the pattern
- **Dates/timestamps**: Parse to `datetime`, don't compare strings — see `aib.paths.parse_timestamp()`
- **URLs**: Use `urllib.parse`, not string splitting
- **File paths**: Use `pathlib.Path`, not string concatenation

String operations are for formatting output. If you're using them to understand or transform data, you're working at the wrong abstraction level. `import re` in particular is a code smell — if you find yourself writing a regex, stop and look for the structured API.

### Timestamp Comparisons

Never compare timestamp strings lexicographically (`ts_a > ts_b`). Always parse to `datetime` first using `aib.paths.parse_timestamp()`. This function handles both forecast filenames (`YYYYMMDD_HHMMSS.json`) and retrodict filenames (`YYYY-MM-DD_YYYYMMDD_HHMMSS.json`).

### Use Standard Libraries

When integrating with external services (APIs, data sources, etc.):

- **Use existing Python libraries first** — Check PyPI for official or well-maintained client libraries before writing raw HTTP requests
- **Examples**: Use `arxiv` for arXiv search, `yfinance` for stock data, `fredapi` for FRED economic data
- **Don't rebuild the wheel** — If a library exists with good documentation and maintenance, use it

### Tool Design: Data Over Interaction

When a tool fails or isn't delivering value, don't just remove it — ask what the agent actually needed. The right abstraction is usually "get the data", not "here's a browser/API/interface, figure it out."

- **Design tools around what the agent needs**, not what the underlying technology exposes
- **Automate data extraction** rather than giving the agent interactive tools to fish for it
- **Follow the data augmentation pattern**: `web_search` doesn't just return raw search results — it automatically enriches them with structured API data from recognized domains. `fetch_url` doesn't just return page text — it extracts embedded data (Next.js state, JSON script tags, global state) from JS-rendered pages. New tools should follow this pattern: do the enrichment inside the tool, not in the agent's reasoning loop

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

- Take a validated input model and return one; raise `ToolError` to send a recoverable failure back as an MCP error
- Log exceptions with `logger.exception()` for debugging
- Include actionable error messages (what failed, why, what to try)

The `is_error` envelope and the input-validation reply belong to the `@lup_tool`
decorator, not to the handler.

**Agent code should:**

- Raise exceptions for unrecoverable errors (missing config, invalid state)
- Use the `with_retry` decorator for transient failures (HTTP timeouts, rate limits)
- Validate inputs early with Pydantic models

**Never silently swallow errors** — either handle them meaningfully or let them propagate.

**Retrodict transparency:** The forecasting agent must never know it's in retrodict mode. Everything it sees — tool results, error messages, available tools, data ranges — should be indistinguishable from a live forecast. Never mention retrodict, cutoff dates, time constraints, or historical mode in any agent-visible surface (tool responses, error messages, tool descriptions). When data is filtered or a tool is gated by `retrodict_cutoff`, present the result as if that's simply how the world is: "not found", "no data available", "currently unavailable".

### Tools

- **uv**: Package manager. Use `uv add <package>` (never edit pyproject.toml directly)
- **ruff**: Formatting and linting
- **pyright**: Type checking

### Code Intelligence

Code intelligence tools answer questions about code by *resolving* it, through
a language server. **Use these actively** — they are faster and more accurate
than grep-based searches for code understanding and refactoring.

**Navigation (use before editing unfamiliar code):**

- **go-to-definition** — Jump to where a symbol is defined. Use this instead of grepping for `def foo` or `class Foo`.
- **find-references** — Find all usages of a symbol. Use this instead of grepping for a symbol name.
- **hover-documentation** — Get type info and docs for a symbol at a position.
- **list-symbols** — List all symbols in a file. Use this instead of grepping for `def ` or `class `.
- **find-implementations** — Find implementations of an interface or abstract method.
- **trace-call-hierarchy** — Understand call chains. Use this instead of manually tracing function calls.

**Refactoring:**

- **rename-symbol** — Rename a symbol across the workspace. **Always prefer this over `Edit` with `replace_all`** for identifier renames — it understands scope and won't rename unrelated identifiers that happen to share the same name. Where the tool reports the edits rather than applying them, apply them yourself.

**Diagnostics:**

- After every file edit, the type checker analyzes the change and reports errors. Pay attention to these — they catch issues immediately.

`grep` stays right for what is genuinely characters: a string literal, a
comment, a non-Python file. Anything about a *name* — where it is defined,
who calls it, what it is called now — goes through resolution.

---

# Tooling

## Running Python

Bare `python`/`python3` and `uv run python -c "..."` are denied by the shell
policy. Match the rung to the question:

1. **To read code** — `lup-devtools py info`, `py source`, `py search`, `py imports`, and the codeintel tools answer without running anything.
2. **To compute something** — `uv run lup-devtools py eval '<expression>'` auto-imports and evaluates.
3. **To do it again** — add a command under `src/aib/devtools/`, which is reviewable, testable, and reachable next time.

`tmp/` is gitignored, so a script there reaches no diff, no reviewer, and no
later session — which is why it is not a rung. The argument is reviewability
rather than power: an agent may already edit `devtools/` and run it.

## lup-devtools CLI

Source: `src/aib/devtools/`. Two halves: what only this project has —
forecasting analysis, calibration, scoring, the worldview store — and what
the library ships for any project built on it.

**Always use `lup-devtools` instead of ad-hoc commands.** If you find
yourself running the same thing repeatedly, add a command: to
`src/aib/devtools/` when only this project wants it, and upstream to `lup`
when another project built on it would.

`docs/devtools.md` carries the whole command tree, the tournament names, and
the three verbs that spawn a forecasting agent and are therefore refused.

## The Gates You Will Meet

You are not expected to hold this repository's conventions in memory. The
permission policy is a declaration compiled into the plugin that enforces it,
and every refusal names what it caught and how to answer.

Every shell command, URL scope, and edit is classified. Segments join
deny > ask > defer > allow, and malformed input fails conservatively. Two
refusals are worth knowing before you meet them:

- **A forecast, in any spelling.** Refused, with the instruction to print the command instead.
- **A hand edit to a generated tree.** The harness tree is compiled from the declarations under `src/aib/devtools/harness/`; edit those and regenerate.

`# lup: escalate: <why>` as the leading line of a shell command promotes a
classified deny or ask into an approval question carrying that reason.

Change the policy with /lup:hooks, which edits the canonical inputs and regenerates the plugin.

## Settings & Configuration

Settings are project-level, in the tree the harness owns (.claude/settings.json), never user-level — and generated, so the source to edit is `harness/content/settings.py`.

### Merging Local Settings

**Every time you respond to the user**, check whether a local settings file
sits beside the generated one. If it does, review it for sensible defaults
worth keeping. The merge target is the declaration in
`harness/content/settings.py` rather than the generated file — a permission
added to the artifact is reverted by the next generation, and one added to the
declaration is what every later tree carries.

### Environment

`.env` holds defaults; `.env.local` holds secrets, is gitignored, and overrides them. Configuration is loaded through pydantic-settings in `src/aib/config.py`, which is the only module that reads the environment.

---

# Process & Communication

## Asking Questions

**Always surface a question as a question**, through the structured question
facility, rather than as narration the user has to notice. This applies to:

- Clarifying requirements or ambiguous instructions
- Offering choices between implementation approaches
- Confirming before destructive or irreversible actions
- Proposing changes or improvements
- Any situation where you need user input before proceeding

Even for open-ended questions, attach concrete options plus a free-form one — structured answers are what downstream notification parsing reads.

**When proposing changes:**

- **Propose, don't assume**: Ask before making changes
- **Show context**: Show relevant current state before proposing
- **Explain rationale**: Every suggestion should include why it would help
- **Offer alternatives**: Present options when multiple valid approaches exist

**When in doubt, ask.** Err on the side of asking questions rather than making assumptions.

## Deferred Work

**Never create tracking files.** A `TODO.md`, backlog, or roadmap file parks a
decision where no workflow will surface it again — deferral by tracking file is
delegation to nobody. Work that is not being done now lives in one of three
places, chosen by what it is attached to:

- **A `# lup: defer: <text>` note**, when the work belongs to a site in this code, where `lup-devtools report` keeps it visible until somebody wakes it.
- **A GitHub issue**, when the subject is the tooling misbehaving rather than the code.
- **A question to the user**, when whether to defer at all is itself the open question.

`uv run lup-devtools report` answers what is left across every surface: open
notes, unverified claims, stale generated artifacts, and unlanded branches.

This replaces the rule that `PLAN.md` is the source of truth for what has been
built and what remains. The root `PLAN.md` is not deleted — it holds real
history — but it is no longer maintained as a tracking file, and work still
live in it belongs in a `# lup: defer:` note at the site it concerns, where
`report` will keep surfacing it.

## Code Change Reports

After completing code modifications, provide an **extensive report**: a
one-paragraph summary, the files modified, the detailed changes with
surrounding context and a rationale for each, the architectural
considerations, and what was tested.

`docs/devtools.md` carries the section-by-section format and a worked
example.

## Slash Commands & Skills

This repository carries one plugin, generated, under the `lup` prefix. Most of
its roster is the library's — the git and review loop, the resolver, code work,
harness authoring, and the feedback loop. Four are this repository's own, and
they are the forecasting ones: `audit`, `design`, `fb-retrodict`, and `leak`.

A skill that only looked like this repository's own is not among them.
Clearing branches and worktrees is `land`, resolving a conflicted tree is
`merge`, and the feedback-loop phases are the library's. Each was maintained
twice under a second, hand-written plugin until the declaration replaced it —
so when a workflow here seems to want a new skill, look for the library's word
for it first.

**After every command invocation**, reflect on how it was actually used vs. documented:

1. **Compare intent vs usage**: Did the command serve its documented purpose, or was it adapted?
2. **Notice patterns**: When the user corrects your approach or redirects focus, that's a signal the command should evolve.
3. **Proactively propose updates**: Surface the suggested improvement as a question.

**Evolution signals:**

- User provides external docs → Add doc-fetching or reference to command
- User corrects your approach → Update command to prevent future errors
- User asks for something the command should cover → Expand scope
- User ignores sections → Consider simplifying

Every skill is generated, so none is edited in place — the markdown each
harness tree carries is output. A library skill's source is a declaration under
`packages/lup`, so improving one is a change to send upstream; this
repository's four are declared under
`src/aib/devtools/harness/content/skills/`, and change here.

## Reporting Friction

When the tooling fights you, **open a GitHub issue** rather than only working
around it and moving on. A workaround that lives in one session's narration
teaches nobody; the issue is what survives the session. File one whenever a
command half-completes and leaves inconsistent state, a classifier reports a
failed probe as though it were a fact, or a permission boundary blocks an
operation the documented workflow prescribes.

Record what you observed rather than what you concluded: the exact command,
the exact error, the state it left behind, and what the recovery cost. Name
the component that owns the fix — which for anything about the harness, the
policy, or the devtools skeleton is `lup` rather than this repository, so the
issue is filed against `joy-void-joy/lup` and not here.

This repository's `dev` sub-app is its own four commands rather than the
library's tree, so it has no `report-friction` yet. Write the issue by hand
with those five fields.

## External Resources

When a question is about the harness you are running under, its agent SDK, or its model API, read
that runtime's own documentation rather than answering from memory: delegate
to the documentation subagent where one is available, or fetch the Claude Code and Agent SDK documentation at https://docs.claude.com/ and https://code.claude.com/ directly. The fetch scopes the permission policy admits are declared in `harness/catalog.py`. When the user provides documentation links, incorporate that knowledge into the guidance source or the relevant skill declaration.

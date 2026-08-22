<!-- Generated from aib.devtools.harness.content.guidance by `uv run lup-devtools harness generate all` — edit the source, not this file. See docs/harness.md. Deliberately rendered as .claude/CLAUDE.md under Claude Code, AGENTS.md under Codex. -->

# Repository guidance

What an agent working in this repository is given before it reads anything else.

**It is generated.** The source is `src/aib/devtools/harness/content/guidance.py`; edit that and run `uv run lup-devtools harness generate all`.

## What this is

A forecasting bot for the [Metaculus AI Benchmarking Tournament](https://www.metaculus.com/aib/). It opens a Claude Agent SDK session with research tools — web search, page fetch, markets, financial and government data, a Python sandbox — and produces a calibrated prediction. Python 3.14+, `uv` for packages, `lup` as the agent framework beneath it.

Four facts about the tournament shape the code, and every one of them is a constraint rather than a preference:

- **Submission is separate.** This codebase generates forecasts; another system submits them.
- **No community prediction during a live forecast.** The agent cannot see the CP for the question it is forecasting — a tournament rule. CP is fetched post-hoc, per question, for calibration analysis only.
- **Numeric and discrete questions need a 201-point CDF**, not a point estimate. `src/aib/agent/numeric.py` builds it.
- **Version scope.** Traces, forecasts and calibration data are keyed by agent version, and earlier versions had different architectures. Work out which versions the question is about rather than scanning all of them; when in doubt, ask.

## Never run a forecast yourself

**`uv run forecast ...` is the user's command to run, never yours.** That covers `test`, `submit`, `tournament`, `loop`, `retrodict` and `backfill-comments`, whether or not the variant submits — and equally the `lup-devtools` verbs that open the same agent: `worldview loop`, `resolution tentative`, `analysis review`.

A forecast burns real credits, takes tens of minutes, and writes to `notes/`. The user decides when to spend that, and watches it live.

This is a gate rather than a norm. Every spelling is declared refused in `harness/content/shell_vocabulary.py`, and because the policy judges a *parsed* command, hiding the forecast behind something else on the same line does not get it through.

When a change needs a forecast to verify, finish everything you *can* verify — tests, `ruff`, `pyright`, `lup-devtools health check`, targeted probes of the changed code — then **print the exact command and say what to look for**:

> Ready to verify. Run:
> ```bash
> uv run forecast test 44798
> ```
> Watch for: `mcp__research__research` succeeding on the first call (no pydantic
> validation retry), and the reflection `tool_audit` listing no missing
> capabilities.

Do not launch it in the background, and do not offer to run it "just this once".

## Where things are

| Path | What it holds |
|---|---|
| `src/aib/cli.py` | The `forecast` entry point |
| `src/aib/agent/core.py` | Forecasting agent orchestration |
| `src/aib/agent/numeric.py` | CDF generation for numeric and discrete questions |
| `src/aib/agent/prompts.py` | The forecasting system prompt, assembled from sections |
| `src/aib/tools/` | MCP tools: research, sandbox, markets, composition |
| `src/aib/submission.py` | Metaculus API submission |
| `src/aib/devtools/` | The `lup-devtools` CLI |
| `notes/traces/<version>/` | Forecasts and session notes, per agent version |
| `logs/<question_id>/` | Raw run logs |

## Commands

```bash
uv sync
uv add <package>          # never edit pyproject.toml directly
uv run ruff format . && uv run ruff check .
uv run pyright
uv run pytest             # -v, -k <pattern>, or a path
```

Yours to print, never to run — each takes `--profile <name>` to pick a registered Claude account:

```bash
uv run forecast test <question_id>              # no submission
uv run forecast submit <question_id> [--comment]
uv run forecast tournament <aib|minibench|cup>  # skips already forecast
uv run forecast ab --list | -v <variant> -v <variant>
```

## A/B testing

Variants are named agent configurations in `notes/variants.json`, run side by side with `uv run forecast ab`. Each arm is its own process and wants its own `profile`. Traces land under `<version>+<variant>`, so an experiment in flight stays out of the released version's calibration numbers. `docs/devtools.md` carries the registry format.

## Testing

`tests/unit/` mocks external APIs; `tests/integration/` needs API keys and is marked `@pytest.mark.integration`.

A test is edited like any other file — the ordinary lattice judges it, with no gate of its own. That makes the norm yours to keep: a test states the behaviour production owes, so editing one to match an implementation is backwards. Change the implementation, and touch the test only when it genuinely encodes the wrong behaviour — saying which, in the commit.

## Debugging

**Do not hypothesize — trace.** Find the actual logs and read the exact exception. Do not list likely causes or ask the user to check things. Open the files, grep for the error, read the traceback, report what happened. If the logs do not say enough, say exactly what logging to add and where.

Use $lup:debug to trace an error through the logs automatically.

**When a forecast fails:** search `logs/<question_id>/` for the error text and for ERROR or exception, and read the *full* traceback rather than stopping at the catch-all. Then read `notes/traces/<version>/sessions/<session_id>/` for the agent's own reasoning and meta-reflection. Missing API keys log warnings at startup; `docs/devtools.md` says what each one breaks.

---

# Working on it

## Worktrees, not branches

Code changes never land on `main` directly. Data does — forecast output needs no review.

You are usually in a worktree already; `git worktree list` confirms it. If you are, work where you are. If not:

```bash
uv run lup-devtools dev worktree create feat-name
```

That makes a sibling under `tree/`, syncs dependencies, and refreshes plugins. Never `git worktree add ./worktrees/...` — worktrees are siblings, not nested checkouts. The generated plugin travels with the worktree, so a harness change on a feature branch takes effect there immediately.

Then: commit atomically as you go, push when the feature is done, and $lup:rebase to clean the history and open a PR. Fixes go on the branch and re-run it. $lup:close merges once approved and clears the branch.

**Bump the agent version** if the branch changes what the forecasting agent *does* — prompts, tools, subagents, scoring. It lives at `[tool.lup] agent_version` in `pyproject.toml`, and every bump needs a `CHANGELOG.md` entry: `uv run lup-devtools version bump` writes both. Infrastructure and data changes need no bump.

## Commits

Commit before responding, early and often, and keep each one to a single thing — if the message needs "and", it is two commits. Messages are cleaned up before merge, so during development they only have to be true.

Conventional commits, `type(scope): description`. Two types are this repository's own: `meta` for harness declarations and the trees they generate, and `data` for generated output. `docs/devtools.md` lists them all.

**Forecast commits** use `data(forecasts):` and go straight to `main`: the forecast markdown under `notes/traces/<version>/forecasts/<question_id>/`, the session notes beside them, and resolution updates as questions resolve. Never code.

**Push `main` after committing data.** The forecast loop commits `notes/` to local `main`, which then drifts ahead of `origin/main`. A branch cut from that `main` inherits the unpushed commits, and its PR folds every one of their `notes/` files in as a fresh addition.

```bash
git log --oneline origin/main..main   # empty before you open a PR
git push origin main
```

Two git hooks enforce both, declared in `src/aib/devtools/dev.py` and installed by `dev git-hooks install`. `pre-commit` refuses a generated artifact behind its source, then a commit mixing `notes/` data with code. `pre-push` refuses a branch whose PR would carry `notes/` files, then runs `dev gate` — ruff, pyright, the non-integration tests, and `harness check all`. `--no-verify` bypasses a moment when a branch deliberately reshapes `notes/`.

## Editing style

**Prefer small, atomic edits.** The edit gate counts real changed lines — imports, comments, whitespace, blank lines and docstrings do not count — and auto-allows three or fewer. Pure deletions, TypedDict and BaseModel definitions, and single-line `replace_all` renames are always allowed.

Split a large change into several edits, and separate concerns: move imports in one, change logic in another.

---

# Code

## Types

- Every function annotates its inputs and its return.
- **Never `Any`.** `TypedDict` for dict-shaped data, `BaseModel` for validated models, a concrete type otherwise.
- **Never `# type: ignore`.** Ask how to fix the error properly.
- No bare `except Exception` — catch what you mean, except at a boundary that logs or re-raises.
- Python 3.12+ generics: `class A[T]`, not `Generic[T]`.
- Never hand-parse agent output. Take a structured output through a Pydantic model.

## No private names

Nothing here is private, so no leading underscore on a function, class, constant or variable. A helper that genuinely should not pollute the namespace nests inside its only caller. Before writing a new helper, look for one that already exists — private names are how a reusable thing stays unreused. An unused parameter (`_context`) is exempt; that is a linting convention, not a privacy one.

## No string manipulation on structured data

Reaching for `re`, `.replace()`, `.split()` or slicing to extract, transform or filter structured data means a parser was missed. Operate on the structure:

| Data | Reach for |
|---|---|
| Web pages | `trafilatura` for text, `beautifulsoup4` for the DOM |
| XML | `xml.etree.ElementTree` or `lxml` |
| JSON | `json.loads()` |
| SDK content | Filter `ContentBlock` lists by type and attribute — `sources.py` has the pattern |
| Dates | `aib.paths.parse_timestamp()` |
| URLs | `urllib.parse` |
| Paths | `pathlib.Path` |

String operations are for formatting output. `import re` in particular is a smell: stop and find the structured API.

**Timestamps especially.** Never compare timestamp strings lexicographically. `aib.paths.parse_timestamp()` handles both forecast filenames (`YYYYMMDD_HHMMSS.json`) and retrodict filenames (`YYYY-MM-DD_YYYYMMDD_HHMMSS.json`).

## Use the library that exists

Check PyPI for an official or well-maintained client before writing raw HTTP — `arxiv`, `yfinance`, `fredapi` are all here for that reason.

`forecasting-tools` has three annotation gaps worth knowing: `MetaculusApi.get_question_by_post_id()` is typed as returning `MetaculusQuestion` but hands back subclasses, so use `isinstance()`; `community_prediction_at_access_time` exists only on `BinaryQuestion`; and coherence links come from `MetaculusClient.get_links_for_question()`. `uv run lup-devtools api inspect` settles a method name rather than guessing at it.

## Tool design: data over interaction

When a tool fails or is not earning its place, ask what the agent actually needed. The right abstraction is almost always "get me the data", not "here is a browser, go fish".

- **Automate the extraction** rather than handing the agent an interactive surface.
- **Enrich inside the tool, not in the reasoning loop.** `search` asks nine sources at once and enriches each hit with structured API data from recognized domains, carrying the page's own text so a match needs no second call. `fetch` pulls embedded state out of JS-rendered pages and hands a URL to whichever tool knows it better.
- **A choice the tool can make is not the agent's to make.** Sixteen tools once took free text and returned ranked hits; picking between them was mechanical, and a source the agent had no reason to ask went unasked — so a capability it could not know was relevant was unreachable in practice. When several tools share a signature, the thing that varies is a parameter: fan out over it and report what each source said.

## Error handling

An MCP tool takes a validated input model and returns one, raising `ToolError` to send a recoverable failure back as an MCP error with a message saying what to try. The `is_error` envelope and the input-validation reply belong to the `@lup_tool` decorator, not the handler. Log with `logger.exception()`.

Elsewhere: raise for unrecoverable errors, wrap transient ones in `with_retry`, validate inputs early. Never swallow an error silently.

**Retrodict transparency.** The forecasting agent must never learn it is in retrodict mode. Tool results, error messages, available tools and data ranges all have to be indistinguishable from a live run. Never mention retrodict, cutoff dates, time constraints or historical mode in anything the agent can see. Where `retrodict_cutoff` filters data or gates a tool, present the result as simply how the world is: "not found", "no data available", "currently unavailable".

## Code as documentation

The codebase should read as though it had always been written this way. Before adding a comment, ask whether it would exist if the code had always looked like this. If not, it belongs in the commit message.

So: never explain a modification, never say what the code used to do, and never write "now", "new", "updated", "fixed" or "changed" in a comment. `env_file=(".env", ".env.local")` needs no note that the later file wins — that is how configuration precedence works everywhere. Comment only genuinely non-obvious behaviour.

---

# Tooling

## Running Python

Bare `python`, `python3` and `uv run python -c "..."` are denied. Match the rung to the question:

1. **To read code** — `lup-devtools py info`, `py source`, `py search`, `py imports`, and the codeintel tools answer without running anything.
2. **To compute something** — `uv run lup-devtools py eval '<expression>'` auto-imports and evaluates.
3. **To do it again** — add a command under `src/aib/devtools/`, which is reviewable, testable, and there next time.

`tmp/` is gitignored, so a script written there reaches no diff, no reviewer and no later session — which is why it is not a rung. The argument is reviewability, not power: you may already edit `devtools/` and run it.

## Code intelligence

Resolve, do not grep. Navigate with **go-to-definition**, **find-references**, **hover-documentation**, **list-symbols**, **find-implementations** and **trace-call-hierarchy** before editing unfamiliar code, and rename with **rename-symbol** rather than `Edit` with `replace_all` — it understands scope and will not touch unrelated identifiers sharing a name.

`grep` stays right for what is genuinely characters: a string literal, a comment, a non-Python file. Anything about a *name* goes through resolution. `docs/devtools.md` has the task-by-task table where the line is not obvious.

## lup-devtools

Source: `src/aib/devtools/`. **Use it instead of ad-hoc commands.** If you run the same thing twice, add a command — to `src/aib/devtools/` when only this project wants it, upstream to `lup` when any project built on it would.

`docs/commands.md` is every command the CLI serves with a line on each, walked from the wired app at generation time rather than listed by hand — so a command is there by existing, and reading it is how you find one you did not know to look for. `uv run lup-devtools <command> --help` gives its arguments. `docs/devtools.md` carries what a walk cannot reach: the tournament names, the commit types, and why three verbs are refused.

## The gates you will meet

You are not expected to hold these conventions in memory. The permission policy is a declaration compiled into the plugin that enforces it, and every refusal names what it caught and what to do instead. Shell commands, fetch scopes and edits are all classified; segments join deny > ask > defer > allow, and malformed input fails conservatively.

Two refusals are worth knowing before you meet them:

- **A forecast, in any spelling** — print the command instead.
- **A hand edit to a generated tree** — the trees compile from declarations under `src/aib/devtools/harness/`. Edit those and regenerate.

`# lup: escalate: <why>` as the leading line of a shell command turns a classified deny or ask into an approval question carrying that reason.

A gate that feels wrong is usually a **seam** — an opinion the library holds that this repository is meant to overrule. `dev seams` prints each one, what it holds, and the line of `harness/catalog.py` it is written on; the same command settles one (`--own`/`--disown` a file, `--retire`/`--keep` a scan rule). Reach for it before working around a verdict: a decision written into the declaration is one the next session meets too.

Change the policy with $lup:hooks, which edits the canonical inputs and regenerates the plugin.

## Settings and environment

Settings are project-level, in the tree the harness owns (.codex/config.toml), never user-level — and generated, so the source to edit is `harness/content/settings.py`.

**Every time you respond**, check whether a local settings file sits beside the generated one, and review it for defaults worth keeping. Merge them into the declaration, not the artifact: a permission added to the generated file is reverted by the next generation.

`.env` holds defaults; `.env.local` holds secrets, is gitignored, and overrides them. `src/aib/config.py` is the only module that reads the environment.

---

# Process

## Ask as a question

**Surface a question as a question**, through the structured facility, rather than as narration the user has to notice — when requirements are ambiguous, when several approaches are valid, before anything destructive, and whenever you would otherwise assume. Even open-ended questions get concrete options plus a free-form one, because structured answers are what downstream notification parsing reads.

Propose rather than assume: show the current state, say why the change would help, and offer the alternatives you considered.

## Deferred work

**Never create a tracking file.** A `TODO.md`, backlog or roadmap parks a decision where no workflow will surface it again — deferral by tracking file is delegation to nobody. Work not being done now lives in one of three places, chosen by what it is attached to:

- **A `# lup: defer: <text>` note**, when the work belongs to a site in this code. Default to the bare `defer:`; a bracketed `defer[<gate>]:` states a real, externally-checkable gate, never that this code might change again. Two spellings are resolved rather than printed, and `dev check` fails the run either comes true: `defer[gone:<path>]` wakes once that path stops existing, and `defer[branch:<name>]` wakes for whoever is standing on that branch — read off `main`, so it reaches them without their having merged it. Write a branch note where you are and aim it at the branch that has to act. Any other gate stays prose, and prose stays advisory.
- **A GitHub issue**, when the subject is the tooling misbehaving rather than the code.
- **A question to the user**, when whether to defer at all is the open question.

`uv run lup-devtools report` answers what is left across every surface: open notes, unverified claims, stale generated artifacts, unlanded branches. The root `PLAN.md` holds real history but is not maintained; work still live in it belongs in a note at the site it concerns.

## Report what you changed

After code modifications, give an **extensive report**: a one-paragraph summary, the files modified, the detailed changes with surrounding context and a rationale for each, the architectural considerations, and what was tested. `docs/devtools.md` carries the format and a worked example.

## Skills

One generated plugin, under the `lup` prefix. Most of the roster is the library's — the git and review loop, the resolver, code work, harness authoring, the feedback loop. Four are this repository's own, and they are the forecasting ones: `audit`, `design`, `fb-retrodict`, and `leak`. Clearing branches is `land`, resolving a conflicted tree is `merge`, and the feedback-loop phases are the library's — so when a workflow here seems to want a new skill, look for the library's word for it first.

Every skill is generated, so none is edited in place. This repository's four are declared under `src/aib/devtools/harness/content/skills/`; a library skill's source is upstream, so improving one is a change to send there.

**After invoking a command**, notice how it was actually used against how it is documented. When the user corrects your approach, redirects focus, or asks for something the command should have covered, that is the command asking to evolve — surface the improvement as a question.

## Report friction

When the tooling fights you, **file it** rather than only working around it: a workaround that lives in one session's narration teaches nobody. `uv run lup-devtools dev report-friction` writes the issue with the fields that make it actionable — what you ran, the exact error, the state it left behind, what recovery cost, and which component owns the fix. File whenever a command half-completes and leaves inconsistent state, a classifier reports a failed probe as fact, or a permission boundary blocks something the documented workflow prescribes.

Record what you observed, not what you concluded. Anything about the harness, the policy, or the devtools skeleton is `lup`'s rather than this repository's, and the command routes it there.

## External resources

When the question is about the runtime you are running under, its agent SDK, or its model API, read that runtime's own documentation rather than answering from memory — delegate to a documentation subagent where there is one, or fetch the Codex documentation at https://developers.openai.com/codex/ and https://learn.chatgpt.com/ directly. The fetch scopes the policy admits are declared in `harness/catalog.py`. When the user gives you a documentation link, fold what it taught into this guidance or the relevant skill declaration.

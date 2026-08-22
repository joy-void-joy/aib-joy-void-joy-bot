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

`docs/commands.md` is the tree itself: every command the CLI serves with a
line on what each does, walked from the wired app at generation time. It is
not repeated here, because a second copy is one that falls behind — and a
copy that has fallen behind looks exactly like one that has not. What
follows is what the walk cannot reach: what the names mean, which verbs are
refused, and the decisions behind the workflow.

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

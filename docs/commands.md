<!-- Generated from lup.devtools.dev.commands by `uv run lup-devtools harness generate all` — edit the source, not this file. See docs/harness.md. -->

# Command reference

Every command `lup-devtools` serves, walked from the composed CLI at generation time. A command reaches this page by existing, so nothing is left out for want of being remembered — including the ones a session rarely runs directly, which are exactly the ones a hand-written list loses first.

Run any of them with `uv run lup-devtools <command>`, and add `--help` for its arguments and options: the summary here is the first line of each command's own documentation, not a substitute for reading it.

## `agent`

| Command | What it does |
| --- | --- |
| `agent serve-tools` | Serve the session-free research tools over MCP stdio. |

## `analysis`

| Command | What it does |
| --- | --- |
| `analysis dashboard` | One-screen health check for the feedback loop. |
| `analysis tool-health` | Aggregate tool usage and errors from forecasts and summary.json reviews. |
| `analysis tool-needs` | Aggregate capability gaps from summary.json reviews. |
| `analysis flags` | Aggregate risk flags from summary.json reviews. |
| `analysis tracking-gaps` | Check data completeness across forecasts. |
| `analysis prompt-health` | Analyze the forecasting prompt for size and patch accumulation. |
| `analysis version-diff` | Show CHANGELOG entries between two versions. |
| `analysis mark` | Mark forecasts as analyzed. |
| `analysis unmark` | Remove analysis marks from forecasts. |
| `analysis status` | Show analysis state: which forecasts have been analyzed. |
| `analysis review` | Run the Opus reviewer on a forecast trace, producing summary.json. |

## `api`

| Command | What it does |
| --- | --- |
| `api inspect` | Inspect a Python module, class, or method. |
| `api module-path` | Print the file path of a Python module. |
| `api module-source` | Print the source code of a Python module. |
| `api post` | Inspect raw Metaculus API response for a post. |
| `api cp` | Inspect aggregation data in resolved question API responses. |
| `api cp-single` | Inspect a single question&#x27;s aggregation data via direct fetch. |
| `api debug` | Debug Metaculus API parsing and client. |
| `api mcp-error` | Test if is_error property works on lup&#x27;s CallToolResult subclass. |
| `api websearch` | Test the retrodict web search (Exa-based). |
| `api earnings` | Check what yfinance earnings_dates provides for a ticker. |
| `api trends` | Fetch Google Trends data for a keyword and optionally compare two dates. |

## `calibration`

| Command | What it does |
| --- | --- |
| `calibration binary` | Binary forecast calibration analysis. |
| `calibration numeric` | Numeric/discrete forecast calibration via PIT analysis. |
| `calibration summary` | Combined calibration summary for feedback loop sessions. |
| `calibration export` | Export calibration data to JSON. |
| `calibration report` | Basic calibration report: Brier/log scores and bucket table. |
| `calibration detail` | Show detailed forecast-by-forecast results. |
| `calibration cdf` | Analyze CDF sharpness across numeric forecasts. |

## `claude`

| Command | What it does |
| --- | --- |
| `claude run` | Launch Claude Code with the project&#x27;s tools, local plugin, and profile. |

## `dev`

| Command | What it does |
| --- | --- |
| `dev branches` | Analyze branch containment, PR status, and worktree info. |
| `dev base-branch` | Detect the base branch for the current (or specified) branch. |
| `dev freshness` | Report how far this checkout sits behind its own remote and its base. |
| `dev pr-body` | Generate a PR body (summary, commits, test plan) from branch commits. |
| `dev survey` | Full branch inventory: containment, PRs, unique commits, diff sizes. |
| `dev merge-driver` | Register the ownership-manifest merge driver `.gitattributes` names. |
| `dev delete` | Delete a branch and its worktree, and origin&#x27;s copy if it is spent. |
| `dev retire` | Retire a branch through a pull request, so its commits outlive it. |
| `dev archive-traces` | Copy a worktree&#x27;s session traces into the archive beside the repository. |
| `dev resolve-branch` | Create + switch to the resolve/&lt;id&gt; branch (a resolve editor&#x27;s first step). |
| `dev resolve-review` | Render a resolve manifest and its branch diffs into one static HTML review. |
| `dev resolve-summary` | Print per-concern verdicts from a resolve manifest. |
| `dev check` | Run ruff format, ruff check, pyright, and pytest. Read-only by default. |
| `dev comments` | List unresolved `# lup:` feedback comments, or act on specific ones. |
| `dev todos` | List `# lup: template:` markers — a scaffold&#x27;s open decisions. |
| `dev seams` | Show what this project settled about itself, or settle one of them. |
| `dev refutations` | Resolve one file&#x27;s proposed content and report what it refutes. |
| `dev directives` | Measure every `# lup: ignore` against the canonical inline placement. |
| `dev report-friction` | File or correct workflow friction in this checkout&#x27;s repository. |
| `dev issues` | List the open issues a resolver run would take as evidence. |
| `dev rules` | Generate the Lup rule and typed-suppression reference. |
| `dev relocate` | Repoint every import of a module that moved between the two halves. |
| `dev policy` | Show what the declared permission policy decides about an input, and why. |
| `dev vocabulary` | Show every shell form the declared vocabulary judges, and how. |
| `dev setup-hooks` | Point git at the tracked hooks (core.hooksPath -&gt; .githooks). |
| `dev data-split` | Refuse a commit carrying both forecast data and code. |
| `dev pr-base` | Refuse a push whose PR would carry data an unpublished main holds. |
| `dev gate` | Run the checks this repository holds a branch to before it leaves. |
| `dev worktree create` | Create or re-attach a git worktree. |
| `dev worktree list` | List all git worktrees with branch and status info. |
| `dev worktree remove` | Remove a git worktree. |
| `dev pr status` | Fetch PR review status, checks, and comments for a branch. |
| `dev pr merge` | Merge a PR and pull changes into the integration branch. |
| `dev pr sync-base` | Sync the base branch and merge it into the current feature branch. |
| `dev pr push` | Push the current branch and report any existing PR. |
| `dev pr create` | Create a new PR. |
| `dev pr update` | Update a PR body. |
| `dev conflict list` | Show conflicted files with scope classification (in-scope vs out-of-scope). |
| `dev conflict status` | Detect conflict state, list files, and show both sides&#x27; history. |
| `dev conflict audit` | Post-resolution deletion audit: check for accidentally dropped code. |
| `dev conflict complete` | Finalize the merge/rebase/cherry-pick after all conflicts are resolved. |
| `dev plugin name` | Name this repo&#x27;s plugin marketplace uniquely (the plugin entry is kept). |
| `dev git-hooks install` | Install every git hook this repository declares. |
| `dev git-hooks status` | Report what this clone refuses, at every moment a hook sits at. |
| `dev git-hooks uninstall` | Remove them, leaving hooks written elsewhere alone. |
| `dev model-config census` | Enumerate every `model_config` declaration by right-hand-side shape. |
| `dev model-config aliases` | List every shared configuration alias, and who imports each one. |
| `dev model-config convert` | Rewrite every assigned `model_config` as class keywords, in place. |
| `dev model-config declared` | Record every class&#x27;s declared configuration, without importing it. |
| `dev model-config declared-at` | Record what every class declared as of a git revision. |
| `dev model-config snapshot` | Record the configuration pydantic resolved onto every model. |
| `dev model-config snapshot-at` | Record the configuration pydantic resolved at a git revision. |
| `dev model-config compare` | Diff two snapshots; exit non-zero when any model&#x27;s config moved. |

## `git`

| Command | What it does |
| --- | --- |
| `git commit-forecasts` | Commit all uncommitted forecast files, one commit per question. |
| `git local` | Check local submission status for a question. |
| `git mark` | Mark a forecast as submitted (using API timestamp if available). |
| `git backfill` | Backfill submitted_at for forecasts confirmed by the Metaculus API. |
| `git check` | Check if a question shows as already forecast in the API. |

## `harness`

| Command | What it does |
| --- | --- |
| `harness generate` | Deterministically generate owned native artifacts without launching. |
| `harness check` | Read-only ownership and generated-artifact drift check for CI. |
| `harness reconcile` | Classify local differences without rewriting canonical Python source. |
| `harness apply-reconciliation` | Apply a stale-base-checked source patch, then regenerate every target. |
| `harness propose-reconciliation` | Persist a source patch for separate review and stale-base-checked apply. |
| `harness doctor` | Report installed native runtime evidence without updating either CLI. |
| `harness serve-resolver-tools` | Serve one worker&#x27;s question tools over stdio, for out-of-process runtimes. |
| `harness claude` | Generate/reconcile Claude artifacts and launch the verified plugin. |
| `harness codex` | Generate/reconcile Codex artifacts and launch without updating the CLI. |
| `harness resolve status` | Say whether a run is alive, where it stands, and what it last did. |
| `harness resolve supervise` | Answer any run under ``.lup/resolve``, live or parked. |
| `harness resolve questions` | List a run&#x27;s questions and what each one has been answered. |
| `harness resolve answer` | Offer an answer to one or more of a run&#x27;s questions. |
| `harness resolve actors` | List every actor this run has recorded, and what each has not read yet. |
| `harness resolve say` | Tell an actor something. It reads this and keeps going. |
| `harness resolve accept` | Accept one concern over one failing verification, on the human&#x27;s word. |
| `harness resolve retire` | Retire one concern whose work was settled somewhere other than this run. |
| `harness resolve redirect` | Stop an actor and put it on something else. |
| `harness resolve park` | Ask every open wait in this run to give up now. |
| `harness resolve drain` | Ask a busy run to finish what is in flight and stop, resumably. |
| `harness resolve refresh` | Bring a run&#x27;s base, and the leases holding work, up to its branch. |
| `harness resolve intake` | Print what a run started now would plan from, without starting one. |
| `harness profile list` | Show every profile, and which one a launch selects by default. |
| `harness profile add` | Register a runtime configuration home under a name. |
| `harness profile use` | Select the profile a launch uses when none is named. |
| `harness profile remove` | Forget a profile, leaving its configuration home on disk. |

## `health`

| Command | What it does |
| --- | --- |
| `health check` | Ping each external dependency and report status. |

## `hooks`

| Command | What it does |
| --- | --- |
| `hooks classify` | Say what the policy decides about one shell command, and why. |
| `hooks classify-fetch` | Say whether a URL is inside this project&#x27;s declared fetch scopes. |
| `hooks sweep` | Classify a list of commands at once, and exit non-zero if any is not allowed. |
| `hooks roots` | List the path roles and protected roots the declaration carries. |

## `migration`

| Command | What it does |
| --- | --- |
| `migration traces` | Migrate flat notes/{forecasts,sessions,logs} to notes/traces/&lt;version&gt;/. |
| `migration retrodict` | Migrate notes/retrodict/ into notes/traces/&lt;version&gt;/retrodict/. |
| `migration archive` | Migrate notes/archive/ into notes/traces/&lt;version&gt;/. |

## `py`

| Command | What it does |
| --- | --- |
| `py info` | Inspect a Python object — adapts to modules, classes, functions, values. |
| `py source` | View source code for a Python object, or a package file tree with --tree. |
| `py eval` | Evaluate a Python expression in the sandbox, with modules auto-imported. |
| `py imports` | Show what a module imports, or what imports it (--reverse). |
| `py search` | Search for symbols across installed packages by name (case-insensitive). |

## `queue`

| Command | What it does |
| --- | --- |
| `queue upcoming` | Show questions closing soon that need forecasting. |
| `queue status` | Show forecasting status for a tournament. |
| `queue missed` | Show recently resolved questions suitable for retrodiction. |
| `queue search` | Search Metaculus for questions suitable for retrodiction. |

## `resolution`

| Command | What it does |
| --- | --- |
| `resolution sync` | Check for and apply resolution updates via profile page scrape. |
| `resolution status` | Show resolution status of all forecasts (live + retrodict). |
| `resolution set` | Manually set resolution for a forecast. |
| `resolution tentative` | Attempt early resolution using AI agents to check criteria. |
| `resolution backfill-criteria` | Backfill missing fields from session traces into forecast JSONs. |

## `scores`

| Command | What it does |
| --- | --- |
| `scores scrape` | Scrape track record and update forecast JSONs with peer scores. |
| `scores show` | Show the scores table (formatted). |
| `scores summary` | Aggregate statistics by type, source, and version. |
| `scores compare` | Compare scores between two agent versions on overlapping questions. |
| `scores regression` | Show latest scores for curated regression suite questions. |
| `scores extremes` | Show best and worst forecasts. |
| `scores strip` | Strip plot of scores by agent version (from track record). |
| `scores trend` | Scatter plot of peer scores over time, colored by agent version. |
| `scores track-record` | Display peer and baseline scores from forecast JSONs. |
| `scores backfill-scores` | Fetch community predictions and compute peer+baseline scores for resolved forecasts. |
| `scores backfill-cdf` | Backfill CDF and numeric_bounds into forecast JSONs via Metaculus API. |

## `sync`

| Command | What it does |
| --- | --- |
| `sync status` | Show tracked projects and their sync status (read-only). |
| `sync fetch` | Clone missing repos and fetch/reset cached ones (network + writes). |
| `sync log` | List commits to review: everything upstream added since the last sync. |
| `sync diff` | Show full diff for a specific commit. |
| `sync mark-synced` | Advance the sync checkpoint to the upstream&#x27;s current HEAD. |
| `sync setup` | Set the local path for a project (writes to sync.json.local). |

## `trace`

| Command | What it does |
| --- | --- |
| `trace show` | Show forecast trace for a post ID. |
| `trace list` | List recent forecasts with their metrics summary. |
| `trace errors` | Show forecasts with tool errors. |
| `trace log` | Show filtered reasoning trace from forecast log. |
| `trace logs` | List all available log directories. |

## `version`

| Command | What it does |
| --- | --- |
| `version changelog` | Show changes since a version tag, classified by type. |
| `version bump` | Bump agent version, record the release, and create a git tag. |
| `version list` | List all agent versions from git history. |

## `worldview`

| Command | What it does |
| --- | --- |
| `worldview list` | Show all worldview entries with state and staleness. |
| `worldview show` | Display a single worldview entry. |
| `worldview maintain` | Run one worldview survey + fix sweep. |
| `worldview loop` | Run the always-on worldview loop: survey the store, then fix each issue. |
| `worldview resolve` | Check sub-forecasts for AI resolution where resolvable_after &lt; now. |

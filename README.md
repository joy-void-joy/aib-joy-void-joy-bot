# AIB Forecasting Bot

An experiment in vibecoding a tournament entry for the [Metaculus AI Benchmarking Tournament](https://www.metaculus.com/aib/).

Rather than carefully engineering a forecasting system, this project uses Claude Code to iteratively build, run, and improve itself. The human provides direction and runs the feedback loop; the agent does the forecasting and suggests its own improvements.

## The Approach

This bot is built on the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk), which lets us give Claude access to tools (web search, code execution, prediction markets, economic data) and let it figure out how to use them.

We're applying the [Bitter Lesson](http://www.incompleteideas.net/IncsIdeas/BitterLesson.html) in the sense that we:

- **Don't decompose the problem** — Give the agent all the tools and let it decide what's relevant
- **Don't engineer the pipeline** — Let search, reasoning, and synthesis happen in one connected system
- **Build tools over system-prompt patches** — Adding more capabilities trump patching the system prompt
 
The agent has access to web search, news APIs, prediction markets (Polymarket, Manifold), economic data (FRED), Google Trends, Wikipedia, sandboxed Python execution, and the ability to spawn sub-forecasts. It uses whatever combination makes sense for each question.

### Available Tools

The forecasting agent can use:

- **Research**: Exa web search, AskNews for recent events, Wikipedia, Metaculus question search
- **Markets**: Polymarket and Manifold prices, stock data and history
- **Economic data**: FRED time series (interest rates, inflation, employment, etc.)
- **Trends**: Google Trends interest over time, comparisons, related queries
- **Computation**: Sandboxed Python execution in Docker for Monte Carlo simulations, statistical analysis
- **Decomposition**: Spawn parallel sub-forecasts for complex questions

In addition, its reasoning trace is reviewed by another agent before submitting to ensure no hallucination/over-hedging has been produced.

## The Feedback Loop

We're continuously updating the bot through the /feedback-loop command and /audit command, that review past forecasts after resolution, review the reasoning, and see what tools failed or would have been helpful and what guidance to tweak.

## Everything is Documented
We're also comiting .claude as part of the project itself, since it is the very scaffolding that helps me build the tool and improve on itself.
The forecast reasoning trace and submissions are comitted as well for reviewing purpose.

## Setup

Requires Python 3.13+, [uv](https://docs.astral.sh/uv/), and Docker (for sandboxed code execution).

```bash
git clone <repo-url>
cd aib
uv sync
cp .env .env.local
# Add your API keys to .env.local
```

### API Keys

Copy `.env` to `.env.local` and fill in your keys there. `.env.local` is gitignored and overrides `.env`.

**Required:**

| Variable | Where to get it |
|---|---|
| `METACULUS_TOKEN` | [metaculus.com/accounts/settings](https://www.metaculus.com/accounts/settings/) — under "API Access" |

**Search (recommended — enables web research):**

| Variable | Where to get it |
|---|---|
| `EXA_API_KEY` | [dashboard.exa.ai](https://dashboard.exa.ai/) |
| `ASKNEWS_API_KEY` | [my.asknews.app](https://my.asknews.app/) |
| `PERPLEXITY_API_KEY` | [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api) |

**Economic & government data (optional):**

| Variable | Where to get it |
|---|---|
| `FRED_API_KEY` | [fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html) |
| `BLS_API_KEY` | [registrationapps.bls.gov/bls_registration/registration.aspx](https://registrationapps.bls.gov/bls_registration/registration.aspx) |
| `CENSUS_API_KEY` | [api.census.gov/data/key_signup.html](https://api.census.gov/data/key_signup.html) |

**Social media (optional):**

| Variable | Where to get it |
|---|---|
| `REDDIT_CLIENT_ID` | [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) — click "create another app", choose "script", set redirect URI to `http://localhost:8080`. The ID is shown under the app name. **Note:** Reddit now requires API approval via their Data API Terms; creating the app alone isn't enough. Expect a few days wait for personal projects. |
| `REDDIT_CLIENT_SECRET` | Shown as "secret" on the same app page |

**LLM routing (optional):**

| Variable | Where to get it |
|---|---|
| `OPENROUTER_API_KEY` | [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys) |

You can also override agent settings in `.env.local`:

```bash
AIB_MODEL=claude-opus-4-5-20251101  # Model to use
AIB_MAX_BUDGET_USD=5.0              # Per-forecast budget cap
AIB_MAX_TURNS=50                    # Max agent turns per forecast
```

## Usage

```bash
# Test a forecast without submitting
uv run forecast test <question_id>

# Forecast and submit to Metaculus
uv run forecast submit <question_id>

# Forecast all open questions in a tournament
uv run forecast tournament aib
```

## Development

```bash
uv run ruff format .   # Format
uv run ruff check .    # Lint
uv run pyright         # Type check
uv run pytest          # Test
```

Run `/feedback-loop` in Claude Code to analyze recent forecasts and identify improvements.

## License
MIT

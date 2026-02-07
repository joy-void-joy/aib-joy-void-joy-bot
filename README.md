# AIB Forecasting Bot

An experiment in vibecoding a tournament entry for the [Metaculus AI Benchmarking Tournament](https://www.metaculus.com/aib/).

Rather than carefully engineering a forecasting system, this project uses Claude Code to iteratively build, run, and improve itself. The human provides direction and runs the feedback loop; the agent does the forecasting and suggests its own improvements.

## The Approach

This bot is built on the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk), which lets us give Claude access to tools (web search, code execution, prediction markets, economic data) and let it figure out how to use them.

The core idea comes from Richard Sutton's [Bitter Lesson](http://www.incompleteideas.net/IncsIdeas/BitterLesson.html): general methods that scale with computation beat hand-crafted solutions. Applied here, that means:

- **Don't decompose the problem** — Give the agent all the tools and let it decide what's relevant
- **Don't engineer the pipeline** — Let search, reasoning, and synthesis happen in one connected system
- **Don't patch observed failures** — When something goes wrong, add capability rather than rules

The agent has access to web search, news APIs, prediction markets (Polymarket, Manifold), economic data (FRED), Google Trends, Wikipedia, sandboxed Python execution, and the ability to spawn sub-forecasts. It uses whatever combination makes sense for each question.

### Available Tools

The forecasting agent can use:

- **Research**: Exa web search, AskNews for recent events, Wikipedia, Metaculus question search
- **Markets**: Polymarket and Manifold prices, stock data and history
- **Economic data**: FRED time series (interest rates, inflation, employment, etc.)
- **Trends**: Google Trends interest over time, comparisons, related queries
- **Computation**: Sandboxed Python execution in Docker for Monte Carlo simulations, statistical analysis
- **Decomposition**: Spawn parallel sub-forecasts for complex questions

It also has five specialized subagents it can delegate to: deep-researcher, estimator, quick-researcher, link-explorer, and fact-checker. Each runs with its own tool access and returns structured results.

## The Feedback Loop

The interesting part isn't the forecasting agent itself — it's the process of improving it.

After running forecasts, we analyze the reasoning traces at three levels:

**Object level**: What tools failed? What data was missing? What did the agent explicitly ask for? This drives new tool development.

**Meta level**: Is the agent's self-assessment useful? Can we trace from forecast to reasoning to outcome? This improves observability.

**Meta-meta level**: Is this feedback process itself working? What would make it easier? This improves the loop.

The `/feedback-loop` command in Claude Code runs this analysis. Over time, the agent accumulates capabilities based on what it actually needs, not what we guessed it would need.

## Everything is Documented

This repo commits things you wouldn't normally commit: the `.claude/` directory with its settings, commands, and helper scripts; the `notes/` directory with research, forecasts, and meta-reflections from every run.

The idea is that the development process itself is the product. By tracking:

- **`.claude/CLAUDE.md`** — Instructions for Claude Code when working on this repo
- **`.claude/commands/`** — Slash commands like `/feedback-loop` that encode workflows
- **`.claude/scripts/`** — Helper scripts for analysis, built as the feedback loop identified needs
- **`notes/forecasts/`** — Every forecast with its reasoning, factors, and confidence
- **`notes/sessions/`** — Agent self-reflections and session data organized by post ID
- **`notes/research/`** — Research notes organized by question

...we create a record of how the system evolved. When Claude Code runs the feedback loop, it can read its own past reasoning and identify patterns. The meta-reflections explicitly ask: what tools helped? what was missing? what would I do differently?

This is the "vibecoding" part: instead of designing upfront, we let the system tell us what it needs through its own documentation.

## Project Structure

```
src/aib/
├── agent/
│   ├── core.py         # Main forecasting orchestration
│   ├── subagents.py    # Specialized sub-agent definitions
│   ├── numeric.py      # CDF generation for numeric questions
│   └── prompts.py      # System prompts
└── tools/
    ├── forecasting.py  # Metaculus API + web search
    ├── markets.py      # Prediction market data
    ├── financial.py    # FRED economic data
    ├── trends.py       # Google Trends
    ├── sandbox.py      # Docker code execution
    └── composition.py  # Sub-forecast spawning

.claude/
├── CLAUDE.md           # Instructions for Claude Code
├── commands/
│   └── feedback-loop.md  # The improvement workflow
└── scripts/
    ├── feedback_collect.py   # Gather resolution data
    ├── trace_forecast.py     # Link forecasts to logs
    └── calibration_report.py # Analyze accuracy

notes/
├── forecasts/    # Saved forecasts with full reasoning
├── meta/         # Agent self-reflections
├── research/     # Research notes by question
└── feedback_loop/# Analysis results
```

## Setup

Requires Python 3.13+, [uv](https://docs.astral.sh/uv/), and Docker (for sandboxed code execution).

```bash
git clone <repo-url>
cd aib
uv sync
cp .env .env.local
# Add your API keys to .env.local
```

Required: `METACULUS_TOKEN`, `ANTHROPIC_API_KEY`

Optional (enable additional tools): `EXA_API_KEY`, `ASKNEWS_CLIENT_ID`/`ASKNEWS_SECRET`, `FRED_API_KEY`

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

[Add license information]

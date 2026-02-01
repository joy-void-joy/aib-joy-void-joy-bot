# Implementation Plan: Metaculus Forecasting Bot

## Current Status

**Phase**: Agent Architecture Refactored

MCP tools are integrated directly into `ClaudeAgentOptions`:
- **forecasting**: In-process SDK server wrapping forecasting-tools
- **sandbox**: In-process SDK server using docker-py
- **composition**: In-process SDK server for parallel research and subquestions
- **markets**: In-process SDK server for Polymarket and Manifold

---

## Important Distinction

**.claude/ directory** is for **Claude Code** (the development assistant working on this codebase). It contains settings, plugins, and instructions for the IDE-based Claude.

**The forecaster agent** (built with Claude Agent SDK) is a separate runtime that will have its own tools configured via `allowed_tools` and `mcp_servers` in `ClaudeAgentOptions`. It does NOT use `.claude/` settings.

---

## Project Structure

```
src/
└── aib/
    ├── __init__.py
    ├── cli.py                    # Typer CLI entry point
    ├── agent/
    │   ├── __init__.py
    │   ├── core.py               # Claude Agent SDK + MCP config
    │   ├── models.py             # Forecast + subagent output models
    │   ├── prompts.py            # System prompts (lighter workflow)
    │   └── subagents.py          # Subagent definitions
    └── tools/
        ├── __init__.py
        ├── forecasting.py        # In-process MCP: forecasting-tools
        ├── sandbox.py            # In-process MCP: Docker sandbox
        ├── composition.py        # In-process MCP: parallel_research, spawn_subquestions
        └── markets.py            # In-process MCP: Polymarket, Manifold

notes/
├── sessions/<session_id>/        # RW - current session working notes
├── research/                     # RO - all historical research
│   └── <timestamp>/              # RW - this session's research
├── forecasts/                    # RO - all historical forecasts
│   └── <question_id>/            # RW - forecasts for this question
└── feedback_loop/                # Calibration metrics and analysis
    ├── <timestamp>_metrics.json  # Output from feedback_collect.py
    ├── <timestamp>_analysis.md   # Analysis notes from /feedback-loop
    └── last_run.json             # Tracks last collection timestamp
```

---

## CLI Commands

```bash
# Test a single question without submitting
uv run forecast test <question_id>

# Forecast and submit to Metaculus
uv run forecast submit <question_id>

# Forecast, submit, and post reasoning as a private comment
uv run forecast submit <question_id> --comment
```

---

## Subagents

| Agent | Model | Purpose |
|-------|-------|---------|
| `deep-researcher` | Sonnet | Flexible research: base rates, key factors, enumeration |
| `estimator` | Sonnet | Fermi estimation with code execution |
| `precedent-finder` | Sonnet | Find similar historical events |
| `resolution-analyst` | Sonnet | Parse resolution criteria for edge cases |
| `market-researcher` | Haiku | Fast search for related questions/markets across platforms (Metaculus, Manifold, Polymarket) |

---

## MCP Tools

### forecasting (in-process)
- `get_metaculus_question(post_id)` - Full question details
- `list_tournament_questions(tournament_id)` - Open questions
- `search_metaculus(query)` - Search by text
- `get_community_prediction(post_id)` - Community forecast (NOT available in AIB tournament)
- `get_coherence_links(post_id)` - Related questions
- `search_exa(query)` - Web search
- `search_news(query)` - News search
- `search_wikipedia(query)` - Wikipedia search for base rates and reference classes

### sandbox (in-process)
- `execute_code(code)` - Run Python in Docker
- `install_package(packages)` - Install PyPI packages

### composition (in-process)
- `parallel_research(tasks)` - Batch web/news search queries concurrently
- `parallel_market_search(tasks)` - Batch market searches (Polymarket/Manifold) concurrently
- `spawn_subquestions(subquestions)` - Decompose and forecast in parallel

### markets (in-process)
- `polymarket_price(query)` - Search Polymarket markets
- `manifold_price(query)` - Search Manifold markets

---

## Phases

### Phase 1: Foundation
> Goal: Basic project structure and configuration

- [x] Create src/aib/ package with src layout
- [x] Create `agent/` subpackage with core, models, prompts
- [x] Create `tools/` subpackage for MCP tools
- [x] Add dependencies
- [x] Create `config.py` with `Settings` class (pydantic-settings)

### Phase 2: Metaculus Integration
> Goal: Communicate with Metaculus API

- [x] Use forecasting-tools' `MetaculusApi` via MCP tools
- [x] Port `NumericDistribution` for 201-point CDF generation

**CDF Generation**: Numeric and discrete questions require a 201-point CDF (or fewer based on `inbound_outcome_count`). Implemented in `src/aib/agent/numeric.py`:
- `NumericDistribution` class: Converts sparse percentiles to full CDF
- `percentiles_to_cdf()`: Convenience function for common use
- Agent outputs 6 percentiles (10, 20, 40, 60, 80, 90) which are interpolated to 201 points
- Handles open/closed bounds, log-scaled questions, and discrete question sizing

### Phase 3: MCP Servers
> Goal: Set up tool infrastructure for agent

- [x] forecasting.py: Metaculus API + search tools
- [x] sandbox.py: Docker-based code execution
- [x] composition.py: parallel_research, spawn_subquestions
- [x] markets.py: Polymarket, Manifold API

### Phase 4: Agent Setup
> Goal: Claude with persistent context, MCP tools, and subagent delegation

- [x] `agent/prompts.py`: Lighter workflow system prompt
- [x] `agent/core.py`: Claude Agent SDK with all MCP servers
- [x] `agent/subagents.py`: 5 specialized subagents
- [x] `agent/models.py`: Output models for all subagents
- [x] Notes folder with timestamped sessions, research, and forecasts

### Phase 5: CLI & Submission
> Goal: Working commands with full logging and Metaculus submission

- [x] `cli.py`: Typer CLI with `test` and `submit` commands
- [x] `submission.py`: Metaculus API submission (forecasts + comments)
- [ ] Logging all agent interactions to `logs/<timestamp>_<question_id>.json`
- [x] Console output: probability + reasoning summary

### Phase 6: Robustness
> Goal: Production-ready reliability

- [ ] Error handling with retries and fallback predictions
- [ ] Rate limiting for API calls
- [ ] Tests for critical paths

### Phase 7: Feedback Loop
> Goal: Learn from resolved forecasts to improve calibration

- [x] `feedback_collect.py`: Fetch resolved questions, match to forecasts, compute Brier/log scores
- [x] `/feedback-loop` command: Orchestrate collection, analysis, and code improvements
- [ ] Calibration analysis: Identify systematic biases (overconfidence, domain blindspots)
- [ ] Prompt refinement: Automatically adjust prompts based on calibration data
- [ ] Experiment tracking: Version prompts and compare performance across runs

**Data flow:**
```
Metaculus (resolved questions) → feedback_collect.py → notes/feedback_loop/
                                                              ↓
                                              /feedback-loop command
                                                              ↓
                                        Analyze patterns → Edit agent code
```

---

## MCP Configuration

```python
mcp_servers={
    "forecasting": forecasting_server,
    "sandbox": sandbox.create_mcp_server(),
    "composition": composition_server,
    "markets": markets_server,
}
```

### Prerequisites

1. **forecasting-tools**: Installed via `uv add forecasting-tools`
   - Requires `METACULUS_TOKEN` env var
   - Requires OpenRouter/OpenAI API key for SmartSearcher

2. **Docker**: Must be running for sandbox
   - Uses `ghcr.io/astral-sh/uv:python3.12-bookworm-slim` image
   - Container created fresh per question, destroyed after

---

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Package layout | src/ layout | Standard Python packaging |
| MCP integration | `ClaudeAgentOptions.mcp_servers` | Direct SDK integration, no separate processes |
| Subagent structure | 5 flexible agents | Fewer agents, more autonomy |
| Notes structure | Timestamped folders | RW for current session, RO for history |
| Market tools | Real API calls | Polymarket + Manifold provide market signals |
| Market researcher | Haiku model | Fast, cheap for cross-platform market/question search |
| Parallel tools | Batched execution | parallel_research + parallel_market_search for efficiency |
| Workflow | Guidance over rigid steps | Agent decides research depth |

---

## Dependencies

```bash
uv add forecasting-tools pydantic pydantic-settings docker httpx
```

**External:**
- Docker (must be running for sandbox)

Already installed: `claude-agent-sdk`, `typer`

---

## Reference

See `to_port/` directory for original reference implementations:
- Metaculus API endpoints and authentication patterns
- Question type structures and payloads
- CDF generation logic for numeric questions
- System prompt examples

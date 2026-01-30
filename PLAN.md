# Implementation Plan: Metaculus Forecasting Bot

## Current Status

**Phase**: Foundation (not started)

The codebase currently has a stub `main.py` with no real implementation. `main_with_no_framework.py` serves as a reference for Metaculus API patterns.

---

## Project Structure

```
aib/
├── main.py                      # Typer CLI entry point
├── main_with_no_framework.py    # Reference implementation (read-only)
├── config.py                    # Settings via pydantic-settings
├── metaculus/
│   ├── __init__.py
│   ├── client.py                # Metaculus API client (httpx async)
│   ├── models.py                # Question and prediction Pydantic models
│   └── cdf.py                   # CDF generation for numeric questions
├── forecaster/
│   ├── __init__.py
│   ├── agent.py                 # Claude Agent SDK with persistent context
│   ├── tools.py                 # SpawnSubquestions custom tool
│   ├── prompts.py               # System prompts for forecasting
│   └── handlers.py              # Question-type-specific logic
├── mcp_servers/
│   ├── __init__.py
│   └── forecasting_tools_mcp.py # MCP wrapper for forecasting-tools library
├── logs/                        # Run logs (gitignored)
└── tests/
    └── ...
```

---

## CLI Commands

```bash
# Test a single question without submitting
uv run python main.py test <question_id>

# (Future) Run full forecasting loop
uv run python main.py run

# (Future) Sync questions to Metaculus
uv run python main.py sync
```

---

## Phases

### Phase 1: Foundation
> Goal: Basic project structure and configuration

- [ ] Create `config.py` with `Settings` class (pydantic-settings)
- [ ] Create `metaculus/` package structure
- [ ] Create `forecaster/` package structure
- [ ] Create `mcp_servers/` package structure
- [ ] Add dependencies: `typer`, `pydantic`, `pydantic-settings`, `httpx`, `forecasting-tools`, `mcp`

### Phase 2: Metaculus Integration
> Goal: Communicate with Metaculus API

- [ ] `metaculus/models.py`: Pydantic models for questions (Binary, Numeric, MultipleChoice, Date)
- [ ] `metaculus/models.py`: Pydantic models for predictions/payloads
- [ ] `metaculus/client.py`: Async client with `list_open_questions()`, `get_question()`, `submit_prediction()`, `post_comment()`
- [ ] `metaculus/cdf.py`: Port `NumericDistribution` from reference impl for 201-point CDF generation

### Phase 3: MCP Servers
> Goal: Set up tool infrastructure for agent

- [ ] `mcp_servers/forecasting_tools_mcp.py`: Wrap forecasting-tools library as MCP server
  - `smart_search(query)` → SmartSearcher
  - `key_factors_research(question)` → KeyFactorsResearcher
  - `base_rate_research(event)` → BaseRateResearcher
  - `fermi_estimate(question)` → FermiEstimator
  - `metaculus_search(query)` → Search existing questions
- [ ] Configure `code-sandbox-mcp` for Python execution (Docker-based)

### Phase 4: Agent Setup
> Goal: Claude with persistent context, MCP tools, and subquestion spawning

- [ ] `forecaster/prompts.py`: System prompts adapted from reference impl
- [ ] `forecaster/agent.py`: Claude Agent SDK with persistent context + MCP config
- [ ] `forecaster/tools.py`: `SpawnSubquestions` tool
  - Takes list of subquestions
  - Spawns parallel sub-agents (same model, same tools except SpawnSubquestions)
  - Aggregates and returns results
- [ ] `forecaster/handlers.py`: Per-question-type handlers

### Phase 5: CLI & Logging
> Goal: Working test command with full logging

- [ ] `main.py`: Typer CLI with `test` command
- [ ] Logging all agent interactions to `logs/<timestamp>_<question_id>.json`
- [ ] Console output: probability + reasoning summary

### Phase 6: Robustness
> Goal: Production-ready reliability

- [ ] Error handling with retries and fallback predictions
- [ ] Rate limiting for API calls
- [ ] Tests for critical paths
- [ ] (Future) `run` and `sync` commands

---

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| CLI | Typer | Modern, type-safe, good UX |
| HTTP client | `httpx` (async) | Native async, modern API |
| Config | `pydantic-settings` | Type-safe, validation, .env support |
| Python MCP | `code-sandbox-mcp` (Docker) | Container isolation, local execution |
| Research tools | Wrap `forecasting-tools` as MCP | Claude can use research tools directly |
| Agent context | Persistent (not `query()`) | Maintain state across session |
| Subquestion spawning | `SpawnSubquestions` tool | Claude controls decomposition, parallel execution |
| Sub-agent model | Same as parent | Consistent quality |
| Failure mode | Always submit (fallback to uniform) | Tournament requires predictions |

---

## Dependencies

```bash
uv add typer pydantic pydantic-settings httpx forecasting-tools mcp
```

**External:**
- Docker (must be running for code-sandbox-mcp)
- `code-sandbox-mcp` MCP server

Already installed: `claude-agent-sdk`

---

## Reference

See `main_with_no_framework.py` for:
- Metaculus API endpoints and authentication patterns
- Question type structures and payloads
- CDF generation logic for numeric questions
- System prompt examples

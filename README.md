# AIB Forecasting Bot

A forecasting bot for the [Metaculus AI Benchmarking Tournament](https://www.metaculus.com/aib/). Uses Claude with extended capabilities (web search, code execution, etc.) to generate predictions on forecasting questions.

Built with Python 3.13+ and the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk).

## Features

- **Multi-tool forecasting**: Web search (Exa), news search (AskNews), prediction market data
- **Sandboxed code execution**: Run Python analysis in isolated Docker containers
- **Question decomposition**: Break complex questions into sub-forecasts
- **Structured output**: Produces probability estimates, CDFs for numeric questions, confidence intervals, and reasoning factors

## Setup

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- Docker (for sandboxed code execution)

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd aib
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Configure environment variables:
   ```bash
   cp .env .env.local
   # Edit .env.local with your actual API keys
   ```

4. (Optional) Pull the sandbox Docker image:
   ```bash
   docker pull ghcr.io/astral-sh/uv:python3.12-bookworm-slim
   ```

### Required API Keys

| Variable | Description | Required |
|----------|-------------|----------|
| `METACULUS_TOKEN` | Metaculus API token | Yes |
| `ANTHROPIC_API_KEY` | Anthropic API key (for Claude) | Yes |

### Optional API Keys

| Variable | Description |
|----------|-------------|
| `EXA_API_KEY` | Exa search API |
| `ASKNEWS_CLIENT_ID` / `ASKNEWS_SECRET` | AskNews API |
| `OPENAI_API_KEY` | OpenAI API (for embeddings) |
| `PERPLEXITY_API_KEY` | Perplexity search |
| `OPENROUTER_API_KEY` | OpenRouter API |

## Usage

### Test a Forecast

Run a forecast on a single question without submitting to Metaculus:

```bash
uv run forecast test <question_id>
```

Options:
- `-v, --verbose`: Show detailed logging and full reasoning
- `-s, --stream`: Stream thinking blocks as they arrive

Example:
```bash
uv run forecast test 12345 --verbose
```

### Output

The bot outputs:
- **Probability** (for binary questions)
- **Probabilities** (for multiple choice questions)
- **Median + 90% CI** (for numeric questions)
- **Factors**: Key considerations with their impact on the forecast
- **Sources**: Number of sources consulted

## Configuration

All settings can be configured via environment variables with the `AIB_` prefix:

| Variable | Default | Description |
|----------|---------|-------------|
| `AIB_MODEL` | `claude-opus-4-5-20251101` | Claude model to use |
| `AIB_MAX_BUDGET_USD` | unlimited | Max cost per forecast |
| `AIB_MAX_TURNS` | unlimited | Max agent turns per forecast |
| `AIB_SANDBOX_TIMEOUT_SECONDS` | 30 | Code execution timeout |

See `src/aib/config.py` for all available settings.

## Development

```bash
# Format code
uv run ruff format .

# Lint
uv run ruff check .

# Type check
uv run pyright

# Run tests
uv run pytest
```

## Architecture

```
src/aib/
├── cli.py          # CLI entry point
├── config.py       # Settings management
├── agent/
│   ├── core.py     # Main forecasting agent
│   └── subagents.py # Specialized sub-agents
└── tools/          # MCP tool implementations
    ├── forecasting.py  # Metaculus API tools
    ├── sandbox.py      # Docker code execution
    ├── composition.py  # Sub-forecast orchestration
    └── markets.py      # Prediction market data
```

## License

[Add license information]

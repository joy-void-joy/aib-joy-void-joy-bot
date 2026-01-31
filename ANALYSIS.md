# AIB Forecasting Bot - Architecture Analysis

## Overview

This document provides a comprehensive analysis of the MCP servers, tools, prompts, and subagents in the AIB Forecasting Bot codebase, along with identified issues and improvement recommendations.

## Current Architecture

### MCP Servers (4 total, 15 tools)

#### 1. Forecasting Server (`src/aib/tools/forecasting.py`)
| Tool | Description | Rate Limited |
|------|-------------|--------------|
| `get_metaculus_question` | Fetch question details (title, background, resolution criteria) | Yes (5 concurrent) |
| `list_tournament_questions` | List open questions from a tournament | Yes (5 concurrent) ✅ |
| `search_metaculus` | Text search across Metaculus questions | Yes (5 concurrent) |
| `get_community_prediction` | Fetch community forecast (N/A in AIB tournament) | Yes (5 concurrent) ✅ |
| `get_coherence_links` | Get related questions via coherence links | Yes (5 concurrent) ✅ |
| `search_exa` | AI-powered web search via Exa | Yes (3 concurrent) |
| `search_news` | Recent news via AskNews API | Yes (3 concurrent) |
| `search_wikipedia` | Wikipedia article search | Yes (3 concurrent) |
| `get_wikipedia_article` | Fetch full Wikipedia article content | Yes (3 concurrent) ✅ NEW |

#### 2. Sandbox Server (`src/aib/tools/sandbox.py`)
| Tool | Description |
|------|-------------|
| `execute_code` | Run Python code in isolated Docker container (1GB RAM, network enabled, 30s timeout ✅) |
| `install_package` | Install PyPI packages via `uv pip install` |

#### 3. Composition Server (`src/aib/tools/composition.py`)
| Tool | Description |
|------|-------------|
| `parallel_research` | Batch multiple web/news searches concurrently |
| `parallel_market_search` | Batch Polymarket/Manifold searches concurrently |
| `spawn_subquestions` | Recursively forecast sub-questions (prevents infinite recursion) |

#### 4. Markets Server (`src/aib/tools/markets.py`)
| Tool | Description |
|------|-------------|
| `polymarket_price` | Search Polymarket for current market prices |
| `manifold_price` | Search Manifold Markets for current prices |

### Shared Utilities

#### Response Helpers (`src/aib/tools/responses.py`) ✅ NEW
- `mcp_success(result)` - Unified successful MCP response
- `mcp_error(message)` - Unified error MCP response

### Subagents (5 total)

| Name | Model | Purpose | Tools |
|------|-------|---------|-------|
| `deep-researcher` | Sonnet | Flexible research (base rates, key factors, enumeration) | search_exa, search_news, search_wikipedia, get_wikipedia_article, metaculus tools, file I/O |
| `estimator` | Sonnet | Fermi estimation with code execution | search_exa, search_news, sandbox tools, file I/O |
| `precedent-finder` | Sonnet | Find historical precedents and calculate base rates | same as deep-researcher |
| `resolution-analyst` | Sonnet | Parse resolution criteria for edge cases | same as deep-researcher |
| `market-researcher` | Haiku | Fast cross-platform market/question search | metaculus tools, market tools, parallel_market_search, file I/O |

### System Prompts

1. **Main Forecasting Prompt** (`FORECASTING_SYSTEM_PROMPT`):
   - Tool reference guide (updated with Wikipedia tools ✅)
   - Subagent descriptions
   - Output format (factors with logit values)
   - Logit scale reference table
   - Calibration guidance ("Nothing Ever Happens" principle)
   - Notes folder structure

2. **Type-Specific Guidance**:
   - Binary: Probability-focused, 0.01-0.99 range
   - Numeric: Percentile estimation with fat-tail guidance
   - Multiple Choice: Probability distribution summing to 1.0

3. **Subagent Prompts**: Detailed task-specific prompts for each subagent

---

## Issues Identified & Status

### Critical Issues

| # | Issue | Status |
|---|-------|--------|
| 1 | Missing Rate Limiting on Several Tools | ✅ FIXED |
| 2 | `search_news` Ignores `num_results` Parameter | ✅ DOCUMENTED |
| 3 | Inconsistent Error Response Patterns | ✅ FIXED |
| 4 | Missing Timeout Configuration in Sandbox | ✅ FIXED |

### Moderate Issues

| # | Issue | Status |
|---|-------|--------|
| 5 | Duplicate Code for Market Parsing | ✅ FIXED |
| 6 | `QuestionLinkerOutput` Should be `MarketResearcherOutput` | ✅ FIXED |
| 7 | `spawn_subquestions` only supports binary | ✅ FIXED (now supports numeric/multiple_choice) |
| 8 | Hardcoded Model Names | ✅ FIXED |
| 9 | Wikipedia Search Doesn't Fetch Article Content | ✅ FIXED |
| 10 | No Caching for Repeated API Calls | ✅ FIXED |

### Minor Issues

| # | Issue | Status |
|---|-------|--------|
| 11 | Inconsistent Tool Naming Convention | ⏳ PENDING |
| 12 | Missing Docstrings on Some Helper Functions | ✅ FIXED |
| 13 | `get_community_prediction` Returns None for Non-Binary | ✅ DOCUMENTED |
| 14 | No Tool for Getting Multiple Questions at Once | ✅ FIXED |
| 15 | Subagent JSON Output Not Validated | ⏳ PENDING |
| 16 | No Tool Metrics/Observability | ✅ FIXED |
| 17 | `@tracked` decorator not applied to tools | ✅ FIXED |
| 18 | Hardcoded HTTP timeouts | ✅ FIXED |
| 19 | Frozen date in system prompt | ✅ FIXED |
| 20 | Incomplete tools/__init__.py | ✅ FIXED |

---

## Fixes Implemented (This Iteration)

### 1. Rate Limiting Added to All Metaculus API Tools
- `list_tournament_questions` now uses `_metaculus_semaphore`
- `get_community_prediction` now uses `_metaculus_semaphore`
- `get_coherence_links` now uses `_metaculus_semaphore`

### 2. Unified Error Response Pattern
- Created new `src/aib/tools/responses.py` with `mcp_success()` and `mcp_error()`
- Updated all tool files to use shared helpers
- Removed duplicate `_success`, `_error`, `_error_response` functions

### 3. Model Name Now Configurable
- `core.py` now uses `settings.model` instead of hardcoded string

### 4. Sandbox Timeout Implementation
- Added `CodeExecutionTimeoutError` exception
- `run_code()` now uses threading for timeout support
- Respects `settings.sandbox_timeout_seconds` (default: 30s)
- Tool description updated to show timeout

### 5. Market Parsing Refactored
- Added `parse_polymarket_event()` and `parse_manifold_market()` helpers in `markets.py`
- Updated `composition.py` to use shared parsers
- Eliminated duplicate parsing logic

### 6. Renamed Output Model
- `QuestionLinkerOutput` → `MarketResearcherOutput` in `models.py`

### 7. Wikipedia Article Fetching Tool
- Added `get_wikipedia_article` tool to fetch full article content
- Includes truncation for very long articles (>50k chars)
- Added to forecasting server, core.py allowed_tools, and subagent tools

### 8. Documentation Updates
- `search_news` tool description now documents that `num_results` is ignored
- `get_community_prediction` description clarifies non-binary limitation
- System prompt updated with Wikipedia tools

### 9. In-Memory Caching (Iteration 2)
- Created `src/aib/tools/cache.py` with `TTLCache` class
- Added `@cached(ttl=...)` decorator for async functions
- Applied to `_fetch_metaculus_question` and `_exa_search` (5-minute TTL)
- Cache stats available via `get_cache_stats()`

### 10. Batch Question Fetching (Iteration 2)
- Added `get_metaculus_questions_batch` tool to fetch up to 20 questions in parallel
- Leverages caching and rate limiting

### 11. Missing Docstrings (Iteration 2)
- Added comprehensive docstrings to `_run_exa_search` and `_run_news_search`

### 12. Tool Metrics/Observability (Iteration 2)
- Created `src/aib/tools/metrics.py` with `MetricsCollector` and `ToolMetrics`
- Added `@tracked(tool_name)` decorator for async tool functions
- Tracks call count, error count, min/max/avg duration
- Metrics logged at end of each forecast run
- Added `tool_metrics` field to `ForecastOutput` model

### 13. Non-binary Sub-forecasts (Iteration 3)
- Extended `SubQuestion` TypedDict with `type`, `options`, and `numeric_bounds` fields
- Updated `spawn_subquestions` to handle binary, numeric, and multiple_choice types
- Binary sub-questions are aggregated; other types return individual results
- Weight validation only applies to binary sub-questions

### 14. @tracked Decorator Applied (Iteration 3)
- Added `@tracked` decorator to all MCP tools in:
  - `forecasting.py` (10 tools)
  - `markets.py` (2 tools)
  - `composition.py` (3 tools)
  - `sandbox.py` (2 tools)
- Every tool call now records metrics automatically

### 15. HTTP Timeout Consistency (Iteration 4)
- Replaced hardcoded `timeout=30.0` with `settings.http_timeout_seconds`
- Updated in markets.py and forecasting.py (Wikipedia tools)

### 16. Dynamic Date in System Prompt (Iteration 4)
- Fixed frozen date issue: `FORECASTING_SYSTEM_PROMPT` was using `datetime.now()` at module import
- Created `get_forecasting_system_prompt()` function to generate prompt with current date at runtime
- Updated core.py to use the function

### 17. Updated tools/__init__.py (Iteration 4)
- Added exports for cache, metrics, and responses modules
- Organized exports into logical groups (servers, decorators, helpers, metrics)

### 18. CLI Tool Metrics Display (Iteration 4)
- Added tool call count and error count to CLI forecast output

---

## Remaining Improvements (Future Work)

### Medium Priority
- [ ] Standardize tool naming convention

### Low Priority
- [ ] Enforce structured output validation for subagents

---

## Rewrite Considerations

If rewriting from scratch, the key architectural decisions I would keep:

1. **In-process MCP servers** - Good choice for SDK integration, no RPC overhead
2. **Separate composition layer** - Parallel execution abstraction is valuable
3. **Subagent specialization** - Different tools/models for different tasks
4. **Notes folder persistence** - Enables session continuity
5. **Logit-based reasoning** - Good scaffolding for interpretability

What I would change:

1. **Tool registry pattern** - Single place to define all tools with consistent metadata
2. **Unified response format** - All tools return same structure ✅ (partially done)
3. **Centralized caching layer** - Transparent caching for all API calls
4. **Plugin architecture for search providers** - Easy to add Perplexity, Tavily, etc.
5. **Validation middleware** - Automatic input/output validation
6. **Observability hooks** - Built-in logging, metrics, cost tracking per tool

---

## Files Reference

| File | Purpose | Changes |
|------|---------|---------|
| `src/aib/tools/forecasting.py` | Forecasting MCP server | Rate limiting, Wikipedia tool, batch tool, caching |
| `src/aib/tools/sandbox.py` | Docker sandbox MCP server | Timeout implementation |
| `src/aib/tools/composition.py` | Composition MCP server | Uses shared response helpers, market parsers, docstrings |
| `src/aib/tools/markets.py` | Markets MCP server | Added parse helpers, shared responses |
| `src/aib/tools/responses.py` | Shared MCP response utilities | NEW FILE (iteration 1) |
| `src/aib/tools/cache.py` | TTL-based API caching | NEW FILE (iteration 2) |
| `src/aib/tools/metrics.py` | Tool call metrics/observability | NEW FILE (iteration 2) |
| `src/aib/tools/retry.py` | Retry utilities | No changes |
| `src/aib/agent/core.py` | Main forecasting agent | Uses settings.model, Wikipedia tool, metrics integration |
| `src/aib/agent/prompts.py` | System prompts | Updated tool documentation |
| `src/aib/agent/subagents.py` | Subagent definitions | Added Wikipedia tool to research tools |
| `src/aib/agent/models.py` | Pydantic models | Renamed QuestionLinkerOutput, added tool_metrics field |
| `src/aib/agent/numeric.py` | CDF generation | No changes |
| `src/aib/config.py` | Configuration | No changes |
| `src/aib/cli.py` | CLI entry point | No changes |

## Summary of Changes

### Iteration 1 (8 fixes)
1. Rate limiting on Metaculus API tools
2. Unified error response pattern (responses.py)
3. Configurable model name
4. Sandbox timeout implementation
5. Market parsing refactoring
6. Model renaming (QuestionLinkerOutput → MarketResearcherOutput)
7. Wikipedia article fetching tool
8. Documentation improvements

### Iteration 2 (4 fixes)
1. In-memory caching (cache.py)
2. Batch question fetching tool
3. Missing docstrings
4. Tool metrics/observability (metrics.py)

### Iteration 3 (2 fixes)
1. Non-binary sub-forecasts in spawn_subquestions
2. @tracked decorator on all MCP tools (17 tools total)

### Iteration 4 (4 fixes)
1. HTTP timeout consistency (settings.http_timeout_seconds)
2. Dynamic date in system prompt
3. Updated tools/__init__.py exports
4. CLI tool metrics display

**Total: 18 improvements implemented across 4 iterations.**

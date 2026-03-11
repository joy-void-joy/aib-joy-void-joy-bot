# MCP Tool Overhaul: Design Document

**Status:** Proposed
**Version:** v3.5.1 baseline
**Date:** 2026-03-11

---

## Problem Statement

The forecasting agent sees a flat list of **48 tools** and must choose among them on every turn. Trace data from the 20 most recent forecasts shows:

- **6 tools** handle 90%+ of all calls (`web_search`, `execute_code`, `wikipedia`, `fetch_url`, `get_metaculus_questions`, `reflection`)
- **30+ tools** have zero calls across all 20 forecasts
- **2 tools** are actively broken (`search_exa` at 80% error rate, `get_cp_history` at 71% error rate)
- The agent routinely faces "which tool?" confusion between overlapping tools (`web_search` vs `WebSearch` vs `search_exa`; `fetch_url` vs `WebFetch`; `fred_series` vs `bls_series`)

The tool surface is too wide, too flat, and too redundant. The agent wastes reasoning cycles choosing between tools that differ only in implementation detail.

---

## Design Principles

### 1. One Tool Per Intent

The agent thinks in intents: "I need market data", "I need economic indicators", "I need news." Each intent should map to exactly one tool. Internal fan-out across APIs, platforms, and fallbacks happens inside the tool — invisible to the agent.

### 2. Hide Implementation Details

`WebSearch` is an implementation detail of `web_search`. `WebFetch` is an implementation detail of `fetch_url`. The agent should never see these — they're internal plumbing. Wrapped tools strictly dominate their raw counterparts (augmentation, domain dispatch, retrodict safety).

### 3. Zero-Call Tools Earn Their Way Back

A tool that has never been called across 20 forecasts doesn't belong in the agent's flat list. It can still exist as infrastructure (called internally by other tools, or via domain dispatch) — but it shouldn't consume space in the tool list or reasoning budget.

### 4. Parameters Over Proliferation

`stock_price`, `stock_history`, and `stock_conditional_returns` are the same tool with different parameters. `polymarket_price` and `polymarket_history` differ only in `history_days`. Use parameters to express variation, not separate tool registrations.

### 5. Fix Before Refactor

Broken tools are bugs, not design problems. Fix `search_exa` and `get_cp_history` before restructuring anything.

---

## Current State: Tool Inventory

### Active Bugs

| Tool | Error Rate | Root Cause | Impact |
|------|-----------|------------|--------|
| `search_exa` | 80% (4/5 calls) | `startPublishedDate` parameter causes 400 Bad Request from Exa API. Introduced in commit 285f964 (Feb 26). | Agent loses AI-powered semantic search; falls back to slower `web_search` |
| `get_cp_history` | 71% (5/7 calls) | `aggregation_explorer` endpoint returns 403 Forbidden (Cloudflare block). Introduced when switching from `api2/questions/` endpoint in commit 8474912 (Feb 11). | Meta-prediction questions are blind to CP trajectories — the system prompt calls this "the most important tool for meta-predictions" |

### Usage Tiers (20 most recent forecasts)

**Workhorse (reliable, high volume):**

| Tool | Calls | Errors | Notes |
|------|-------|--------|-------|
| `web_search` | 61 | 0 | ~3 calls/forecast. Primary research tool. |
| `wikipedia` | 45 | 3 | Background facts, context |
| `execute_code` | 42 | 0 | Monte Carlo, stats, data processing |
| `fetch_url` | 41 | 3 | URL content extraction |
| `get_metaculus_questions` | 20 | 0 | Exactly 1/forecast (question retrieval) |
| `reflection` | 20 | 7 | 1/forecast. "Errors" are reviewer `fail` verdicts (by design). |

**Occasional (domain-specific, reliable):**

| Tool | Calls | Errors | Notes |
|------|-------|--------|-------|
| `polymarket_price` | 8 | 0 | |
| `stock_history` | 8 | 0 | |
| `fred_series` | 8 | 0 | |
| `stock_price` | 6 | 0 | |
| `manifold_price` | 5 | 0 | |
| `kalshi_price` | 5 | 0 | |
| `google_trends` | 2 | 0 | Only for Trends-specific questions |
| `stock_conditional_returns` | 2 | 0 | |

**Never called (0 calls across 20 forecasts):**

- Search: `search_arxiv`, `fetch_arxiv`
- Financial: `fred_search`, `company_financials`, `world_bank_indicator`, `world_bank_search`
- Government: `bls_series`, `census_data`
- Markets: `polymarket_history`, `manifold_history`, `kalshi_history`, `kalshi_event`, `list_tournament_questions`, `search_metaculus`, `get_coherence_links`
- Trends: `google_trends_compare`
- Social: `reddit_search`, `reddit_hot`
- Composition: `spawn_subquestions`
- Sandbox: `install_package`
- AskNews: `search_news`, `search_google`, `search_x_twitter`, `do_news_research`
- SDK: `Write`, `Bash`, `Glob`, `Grep`, `Task` (used by reviewer sub-agent, not main agent)

### Server Inventory

| Server | Type | Tools | Notes |
|--------|------|-------|-------|
| `search` | In-process SDK | 6 | web_search, search_exa, wikipedia, fetch_url, search_arxiv, fetch_arxiv |
| `financial` | In-process SDK | 8 | FRED (2), yfinance (4), World Bank (2) |
| `markets` | In-process SDK | 12 | Metaculus (5), Polymarket (2), Manifold (2), Kalshi (3) |
| `government` | In-process SDK | 2 | BLS, Census |
| `trends` | In-process SDK | 2 | Google Trends (single + compare) |
| `reddit` | In-process SDK | 2 | Search + hot posts |
| `sandbox` | In-process SDK | 2 | execute_code + install_package |
| `composition` | In-process SDK | 1 | spawn_subquestions |
| `notes` | In-process SDK | 1 | reflection (triggers Sonnet reviewer) |
| `asknews` | Remote HTTP | 4 | search_news, search_google, search_x_twitter, do_news_research |
| SDK built-in | — | 8 | WebSearch, WebFetch, Read, Write, Glob, Grep, Bash, Task |

**Total: 48 tools across 11 servers.**

---

## Proposed Design: 48 → ~20 Tools

### Target Tool List

```
Server: search (3 tools)
  search        — Unified web search (web + Exa + AskNews, merged & deduped)
  fetch         — Unified URL fetcher (domain dispatch, Playwright, extraction)
  wikipedia     — Wikipedia search/summary/full (unchanged, well-designed)

Server: academic (1 tool)
  arxiv         — Search + fetch in one tool (search by default, fetch when paper_id given)

Server: data (3 tools)
  economic_data — FRED + BLS + World Bank unified by indicator/search/source
  stock         — Price + history + conditional returns by parameter
  company_data  — Company financials (earnings, income, balance sheet)

Server: markets (3 tools)
  market_prices — Polymarket + Manifold + Kalshi in one call
  metaculus     — Question fetch + search + tournament + coherence by action
  cp_history    — CP time series (unchanged, but FIXED)

Server: social (2 tools, conditional)
  news          — AskNews wrapper with web_search fallback
  reddit        — Search + hot posts by mode parameter

Server: context (2 tools)
  trends        — Google Trends single + compare by parameter
  census        — Census/ACS data (unchanged)

Server: sandbox (2 tools)
  execute_code    — Python execution in Docker REPL (unchanged)
  install_package — PyPI package install (unchanged)

Server: composition (1 tool)
  spawn_subquestions — Sub-forecast decomposition (unchanged)

Server: review (1 tool)
  reflection — Factor checkpoint + reviewer gate (unchanged)

SDK built-in (5 tools, trimmed)
  Read, Bash, Glob, Grep, Task

HIDDEN from agent (3 tools, internal only):
  WebSearch  — Used internally by search tool's Haiku sub-agent
  WebFetch   — Superseded by fetch tool
  Write      — Agent shouldn't create files (reviewer uses Read only)
```

**Total: ~23 tools across 9 servers + SDK built-ins.**

### Merge Specifications

#### 1. `search` (replaces `web_search` + `search_exa`)

**Intent:** "Find information about X on the web."

```python
class SearchInput(BaseModel):
    query: str
    sources: list[Literal["web", "exa"]] = ["web", "exa"]
    allowed_domains: list[str] | None = None
    blocked_domains: list[str] | None = None
    num_results: int = 10
```

**Behavior:**
- Fires both backends in parallel (web search via Haiku sub-agent, Exa via API)
- Deduplicates by URL
- Applies API augmentation to all results (domain dispatch)
- In retrodict: Exa uses `published_before`, web results get Wayback validation
- If one backend fails, returns the other's results (graceful degradation)
- AskNews results can be mixed in when `news` source is added later

**Why merge:** The agent currently has to decide "web_search or search_exa?" The answer is almost always "both would be useful." Merging eliminates the choice and improves result diversity.

**Migration:** `web_search` and `search_exa` become internal functions called by the unified `search` tool. No logic changes — just orchestration.

#### 2. `arxiv` (replaces `search_arxiv` + `fetch_arxiv`)

**Intent:** "Find or read an academic paper."

```python
class ArxivInput(BaseModel):
    query: str | None = None        # search mode
    paper_id: str | None = None     # fetch mode
    prompt: str | None = None       # extraction prompt (fetch mode)
    max_results: int = 10
```

**Behavior:**
- If `paper_id` is set: fetch that paper (HTML preferred, PDF fallback)
- If `query` is set: search arXiv, return abstracts
- If both: fetch the paper
- Optional `prompt` for targeted extraction (fetch mode only)

**Why merge:** These are always used in sequence (search → fetch). One tool with mode detection is cleaner. The agent doesn't currently use either tool, but having one clear entry point may increase adoption.

#### 3. `economic_data` (replaces `fred_series` + `fred_search` + `bls_series` + `world_bank_indicator` + `world_bank_search`)

**Intent:** "Get an economic indicator or find one."

```python
class EconomicDataInput(BaseModel):
    indicator: str | None = None     # series ID (UNRATE, LNS14000000, NY.GDP.MKTP.CD)
    search: str | None = None        # free-text search
    source: Literal["auto", "fred", "bls", "worldbank"] = "auto"
    country: str = "US"
    start_date: str | None = None
    end_date: str | None = None
    limit: int = 30
```

**Behavior:**
- `indicator` set → fetch time series data
  - `source="auto"`: detect from indicator format (BLS series IDs start with specific prefixes like `LNS`, `CES`, `CUUR`; World Bank uses dotted notation like `NY.GDP.MKTP.CD`; everything else → FRED)
  - `source="bls"`: force BLS API (more granular for BLS-specific data)
  - `source="worldbank"`: force World Bank API
- `search` set → search for indicators across sources
  - FRED search + World Bank search in parallel, merged results
- Both set → search is ignored, indicator takes precedence

**Why merge:** The agent uses `fred_series` (8 calls) and ignores `bls_series` (0 calls) and `world_bank_*` (0 calls). FRED mirrors most BLS data, so the agent's instinct is right — but when it needs BLS-specific granularity or international data, it can't find the tool. One unified entry point with `source` override solves both problems.

**Series ID auto-detection rules:**
- Starts with `LNS`, `CES`, `CUUR`, `CUSR`, `WPS`, `JTS` → BLS
- Contains `.` with 2-3 letter country prefix (e.g., `NY.GDP.MKTP.CD`) → World Bank
- Everything else → FRED

#### 4. `stock` (replaces `stock_price` + `stock_history` + `stock_conditional_returns`)

**Intent:** "Get stock/equity data for a ticker."

```python
class StockInput(BaseModel):
    symbol: str
    history_days: int = 0            # 0 = current price only
    target_price: float | None = None   # triggers conditional return analysis
    horizon_days: int = 14           # for conditional returns
```

**Behavior:**
- Always returns current price + key metrics
- `history_days > 0`: include historical prices and moving averages
- `target_price` set: compute conditional return probabilities (what's the probability of reaching target given historical volatility?)

**Why merge:** These three tools are literally the same yfinance data with different output shapes. The agent called `stock_price` (6), `stock_history` (8), `stock_conditional_returns` (2) — always on the same ticker in sequence. One call can serve all three needs.

#### 5. `market_prices` (replaces 7 prediction market tools)

**Intent:** "What do prediction markets say about X?"

```python
class MarketPricesInput(BaseModel):
    query: str
    platforms: list[Literal["polymarket", "manifold", "kalshi"]] = [
        "polymarket", "manifold", "kalshi"
    ]
    history_days: int = 7
    limit: int = 5
```

**Behavior:**
- Searches all specified platforms in parallel
- Returns aggregated results: best match per platform with current price and history
- Deduplicates similar markets across platforms
- Indicates volume/liquidity for each match

**Why merge:** The agent calls `polymarket_price` (8), `manifold_price` (5), `kalshi_price` (5) — usually all three for the same question. The separate `*_history` tools (0 calls each) are redundant because `*_price` already has `history_days`. `kalshi_event` (0 calls) can be an internal implementation detail.

**What gets demoted to internal:**
- `polymarket_history`, `manifold_history`, `kalshi_history` → removed (covered by `history_days` parameter)
- `kalshi_event` → internal helper called by `market_prices` when Kalshi returns event-level results

#### 6. `metaculus` (replaces 4 Metaculus tools)

**Intent:** "Get information from Metaculus."

```python
class MetaculusInput(BaseModel):
    action: Literal["get", "search", "tournament", "coherence"]
    post_ids: list[int] | None = None    # for "get"
    query: str | None = None             # for "search"
    tournament: str | None = None        # for "tournament"
    post_id: int | None = None           # for "coherence"
    limit: int = 20
```

**Behavior:**
- `action="get"`: fetch question details by post ID(s) — the 1/forecast baseline call
- `action="search"`: free-text search across Metaculus
- `action="tournament"`: list questions in a tournament
- `action="coherence"`: get related/linked questions

**Why merge:** Only `get` is used (20 calls). The other three have 0 calls — but they might be useful if the agent could discover them without scanning 48 tool names. One entry point with clear action names is more discoverable.

#### 7. `news` (replaces 4 AskNews tools)

**Intent:** "What's the latest news about X?"

```python
class NewsInput(BaseModel):
    query: str
    sources: list[Literal["news", "google", "twitter"]] = ["news"]
    depth: Literal["quick", "deep"] = "quick"
```

**Behavior:**
- `depth="quick"`: calls `search_news` (or `search_google` / `search_x_twitter` per sources)
- `depth="deep"`: calls `do_news_research` for multi-step synthesis
- When AskNews is unavailable: falls back to `web_search` with news-focused domain filters
- In retrodict mode: tool is excluded (AskNews has no date filtering)

**Why merge:** All 4 AskNews tools had 0 calls — possibly because the agent doesn't know which one to use, or because the API key isn't configured in the test environment. One clear "news" tool with sensible defaults may drive adoption.

#### 8. `trends` (replaces `google_trends` + `google_trends_compare`)

**Intent:** "What's the search interest trend for X?"

```python
class TrendsInput(BaseModel):
    keywords: list[str]              # 1 keyword = single, 2-5 = compare
    timeframe: str = "today 3-m"
    geo: str = ""
    tz: int = 360
    include_related: bool = True
```

**Behavior:**
- 1 keyword → single trends query (current `google_trends` behavior including tail stats and news augmentation)
- 2-5 keywords → comparison query (current `google_trends_compare` behavior)

**Why merge:** `google_trends` (2 calls) and `google_trends_compare` (0 calls) differ only in whether the input is a single keyword or a list. One tool with `keywords: list[str]` handles both cases.

#### 9. `reddit` (replaces `reddit_search` + `reddit_hot`)

**Intent:** "What's Reddit saying about X?"

```python
class RedditInput(BaseModel):
    mode: Literal["search", "hot"] = "search"
    query: str | None = None          # required for search
    subreddit: str | None = None      # optional for search, required for hot
    sort: str = "relevance"
    time_filter: str = "month"
    limit: int = 10
```

**Why merge:** Trivial — same API client, same output format, just a different Reddit endpoint.

---

## Hidden Tools

### Remove from `BUILTIN_TOOLS` / `allowed_tools`

| Tool | Reason | Internal Usage |
|------|--------|---------------|
| `WebSearch` | Wrapped by `search` tool. Direct use bypasses augmentation, snippet fetching, and retrodict safety. | Used internally by `search` tool's Haiku sub-agent |
| `WebFetch` | Wrapped by `fetch` tool. Direct use bypasses domain dispatch, Playwright fallback, and prompt extraction. | None — `fetch` uses `httpx` directly |
| `Write` | The forecasting agent should not create files. Session artifacts are written by infrastructure (reflection.yaml, trace.md). | None for main agent. Reviewer sub-agent uses `Read` only. |

### Keep in `BUILTIN_TOOLS` (verified usage)

| Tool | Reason |
|------|--------|
| `Read` | Used by reviewer sub-agent to read trace files and past forecasts |
| `Bash` | Occasionally useful for the agent to run shell commands (e.g., date math) |
| `Glob` | Used by reviewer sub-agent to list past forecast files |
| `Grep` | Used by reviewer sub-agent to search past forecasts |
| `Task` | Verify whether this is used — if not, remove |

---

## Infrastructure: What Stays Unchanged

These modules are load-bearing and well-designed. The overhaul changes the tool surface, not the plumbing.

| Module | Role | Change |
|--------|------|--------|
| `fetch_routes.py` | Domain dispatch (7 URL patterns → tool handlers) | Update handler references for renamed tools |
| `fetch_http.py` | HTTP fetch → trafilatura → Playwright pipeline | None |
| `extract.py` | Sonnet one-shot content extraction | None |
| `wayback.py` | Wayback Machine availability + content fetch | None |
| `cache.py` | TTL-based in-memory API cache | None |
| `throttle.py` | Per-API concurrency + temporal spacing | None |
| `metrics.py` | Tool call tracking (count, duration, errors) | Update tool names in reports |
| `redact.py` | Retrodict temporal redaction via Sonnet | None |
| `mcp_server.py` | Patched MCP server factory (fixes SDK `is_error` bug) | None |
| `responses.py` | `mcp_success()` / `mcp_error()` helpers | None |
| `retry.py` | Async retry decorator with exponential backoff | None |
| `tool_policy.py` | Centralized tool availability policy | Simplify — fewer tool sets to manage |
| `reflection.py` | Reflection + reviewer sub-agent + gate | Rename server from `notes` to `review` |
| `sandbox.py` | Docker container with persistent REPL | None |
| `composition.py` | Sub-forecast spawning via recursive `run_forecast` | None |

---

## P0: Fix Active Bugs

These are prerequisites. Fix before any restructuring.

### Fix 1: `get_cp_history` — 403 Forbidden

**Root cause:** The `aggregation_explorer` endpoint at `metaculus.com/aggregation_explorer/` is being blocked by Cloudflare. This started after switching from the `api2/questions/{id}/` endpoint (commit 8474912, Feb 11).

**Fix options (in order of preference):**

1. **Add proper request headers.** The `aggregation_explorer` endpoint may require the same `Authorization` header that works for other endpoints but is missing here. Check if `_get_headers()` is being called on this request path.

2. **Fallback chain.** Try `aggregation_explorer` first; on 403, fall back to the old `api2/questions/{id}/` endpoint and parse aggregations from the question JSON. The old endpoint worked before Feb 11.

3. **Use the `metaculus` library's built-in aggregation parsing.** The library may already have working access via `question.aggregations` or similar — check if fetching the full question object with `include_aggregations=True` works.

### Fix 2: `search_exa` — 400 Bad Request

**Root cause:** The `startPublishedDate` parameter added in commit 285f964 (Feb 26) appears to be incompatible with other payload options (possibly `livecrawl` or `useAutoprompt`).

**Fix:**

1. **Make `published_after` truly optional.** Only include `startPublishedDate` in the payload when explicitly passed by the caller (not None). Currently it may be included as `null` in the JSON payload, which Exa rejects.

2. **Test the fix.** Run `uv run aib-devtools api websearch "test query"` to verify Exa returns 200.

3. **Add a health check.** Add Exa to `uv run aib-devtools health check` so this class of regression is caught early.

---

## Implementation Plan

### Phase 0: Fix Bugs (prerequisite)

| Task | Effort | Files |
|------|--------|-------|
| Fix `get_cp_history` 403 | 1-2 hours | `src/metaculus/client.py`, `src/aib/tools/markets.py` |
| Fix `search_exa` 400 | 30 min | `src/aib/tools/exa.py` |
| Add Exa + CP history to health check | 30 min | `src/aib/devtools/health.py` |

### Phase 1: Hide SDK Tools (no code changes to tools)

| Task | Effort | Files |
|------|--------|-------|
| Remove `WebSearch`, `WebFetch`, `Write` from `BUILTIN_TOOLS` | 15 min | `src/aib/agent/tool_policy.py` |
| Verify reviewer sub-agent still works (it gets its own `allowed_tools`) | 15 min | `src/aib/tools/reflection.py` |
| Update system prompt if it references WebSearch/WebFetch directly | 15 min | `src/aib/agent/prompts.py` |

**Result:** 48 → 45 tools. Zero risk — the wrapped versions are strictly better.

### Phase 2: Merge Market Tools (7 → 1)

| Task | Effort | Files |
|------|--------|-------|
| Create `market_prices` unified tool | 2 hours | `src/aib/tools/markets.py` |
| Remove `polymarket_price`, `polymarket_history`, `manifold_price`, `manifold_history`, `kalshi_price`, `kalshi_event`, `kalshi_history` as registered tools | 1 hour | `src/aib/tools/markets.py` |
| Keep current implementations as internal `async def _polymarket_search(...)` etc. | — | Already exist |
| Update `tool_policy.py` sets | 30 min | `src/aib/agent/tool_policy.py` |
| Update `fetch_routes.py` Polymarket/Kalshi handlers | 15 min | `src/aib/tools/fetch_routes.py` |

**Result:** 45 → 39 tools. Biggest single reduction.

### Phase 3: Merge Metaculus Tools (4 → 1)

| Task | Effort | Files |
|------|--------|-------|
| Create `metaculus` unified tool with action parameter | 2 hours | `src/aib/tools/markets.py` |
| Remove `list_tournament_questions`, `search_metaculus`, `get_coherence_links` as registered tools; keep `get_metaculus_questions` logic as the `action="get"` path | 1 hour | `src/aib/tools/markets.py` |
| Update `tool_policy.py` | 15 min | `src/aib/agent/tool_policy.py` |

**Result:** 39 → 36 tools.

### Phase 4: Merge Stock Tools (3 → 1)

| Task | Effort | Files |
|------|--------|-------|
| Create `stock` unified tool | 1 hour | `src/aib/tools/financial.py` |
| Remove `stock_price`, `stock_history`, `stock_conditional_returns` as registered tools | 30 min | `src/aib/tools/financial.py` |
| Update `fetch_routes.py` Yahoo Finance handler | 15 min | `src/aib/tools/fetch_routes.py` |
| Update `tool_policy.py` | 15 min | `src/aib/agent/tool_policy.py` |

**Result:** 36 → 34 tools.

### Phase 5: Merge Economic Data Tools (5 → 1)

| Task | Effort | Files |
|------|--------|-------|
| Create `economic_data` unified tool with source auto-detection | 3 hours | `src/aib/tools/financial.py`, `src/aib/tools/government.py` |
| Move BLS logic from `government.py` into financial server (or shared module) | 1 hour | |
| Remove `fred_series`, `fred_search`, `bls_series`, `world_bank_indicator`, `world_bank_search` as registered tools | 30 min | |
| Remove `government` server (Census stays as its own server, or moves into `data`) | 30 min | `src/aib/agent/tool_policy.py` |
| Update `fetch_routes.py` FRED handler | 15 min | `src/aib/tools/fetch_routes.py` |

**Result:** 34 → 30 tools. Also removes the `government` MCP server.

### Phase 6: Merge Search Tools (2 → 1)

| Task | Effort | Files |
|------|--------|-------|
| Create `search` unified tool that runs web + Exa in parallel | 2 hours | `src/aib/tools/search.py` |
| Remove `search_exa` as registered tool; keep `exa_search()` as internal function | 30 min | |
| Update `tool_policy.py` | 15 min | |

**Result:** 30 → 29 tools.

### Phase 7: Merge News Tools (4 → 1)

| Task | Effort | Files |
|------|--------|-------|
| Create `news` tool wrapping AskNews with fallback | 2 hours | New file: `src/aib/tools/news.py` |
| Keep AskNews remote MCP server for internal use; `news` tool calls it via MCP client | 1 hour | |
| Update `tool_policy.py` | 15 min | |

**Result:** 29 → 26 tools.

### Phase 8: Minor Merges (arxiv 2→1, trends 2→1, reddit 2→1)

| Task | Effort | Files |
|------|--------|-------|
| Merge `search_arxiv` + `fetch_arxiv` → `arxiv` | 1 hour | `src/aib/tools/arxiv_search.py` |
| Merge `google_trends` + `google_trends_compare` → `trends` | 1 hour | `src/aib/tools/trends.py` |
| Merge `reddit_search` + `reddit_hot` → `reddit` | 30 min | `src/aib/tools/reddit.py` |
| Update `tool_policy.py` | 15 min | |

**Result:** 26 → 23 tools.

### Phase 9: Rename + Cleanup

| Task | Effort | Files |
|------|--------|-------|
| Rename `notes` server → `review` | 15 min | `src/aib/tools/reflection.py`, `src/aib/agent/tool_policy.py` |
| Rename `fetch_url` → `fetch` in tool registration | 15 min | `src/aib/tools/search.py` |
| Remove `company_financials` rename → `company_data` | 15 min | `src/aib/tools/financial.py` |
| Update system prompt tool references | 30 min | `src/aib/agent/prompts.py` |
| Update CLAUDE.md tool references | 15 min | `.claude/CLAUDE.md` |
| Verify all `aib-devtools` commands still work with new tool names | 30 min | |

---

## Phase Dependency Graph

```
Phase 0 (fix bugs)
  │
  ├──→ Phase 1 (hide SDK tools)     ← independent, do first
  │
  ├──→ Phase 2 (markets 7→1)        ← independent
  ├──→ Phase 3 (metaculus 4→1)      ← independent
  ├──→ Phase 4 (stock 3→1)          ← independent
  ├──→ Phase 5 (economic 5→1)       ← independent
  ├──→ Phase 6 (search 2→1)         ← depends on Phase 0 (exa fix)
  ├──→ Phase 7 (news 4→1)           ← independent
  └──→ Phase 8 (minor merges)       ← independent
          │
          └──→ Phase 9 (cleanup)     ← after all merges
```

Phases 1-8 are independent of each other. They can be done in any order, or in parallel across worktrees. Phase 9 is a cleanup pass after all merges are complete.

---

## Risks and Mitigations

### Risk: Agent Behavior Regression

**Concern:** Changing tool names and signatures could confuse the agent or break established patterns.

**Mitigation:**
- Each phase is a version bump with retrodict testing
- The system prompt's tool documentation is auto-generated from tool descriptions (`ToolPolicy.get_tool_docs`)
- Tool descriptions carry the same usage examples, just unified
- Old tool behaviors are preserved exactly — only the entry point changes

### Risk: Domain Dispatch Breakage

**Concern:** `fetch_routes.py` references specific tool handlers by name. Merges could break routing.

**Mitigation:**
- Domain dispatch calls handler functions, not tools by name. The handlers remain as internal functions even when the registered tool changes.
- Update `fetch_routes.py` handler references in the same PR as each merge.

### Risk: Tool Policy Complexity

**Concern:** `tool_policy.py` has many frozenset constants for tool groups. Merges change the names.

**Mitigation:**
- Fewer tools = fewer sets to manage. The policy actually gets simpler.
- Each phase updates tool_policy.py atomically.

### Risk: Metrics Continuity

**Concern:** Tool metrics keyed by name will break across version boundaries.

**Mitigation:**
- Tool metrics are per-session, not cross-session. The `aib-devtools` metrics commands aggregate from forecast JSONs which store the tool name used at that time.
- Old forecasts keep old tool names. New forecasts get new names. The `--version` filter handles this naturally.

---

## What This Does NOT Address

- **Missing capabilities** (polling data, WHO/health data, PubMed, base rates tool). These are additive features, not restructuring. They can be added as new tools to the simplified surface after the overhaul.
- **Spawn_subquestions adoption.** The tool exists but is never used. This may be a prompt issue, not a tool issue — the agent may not know when to decompose. Addressing this requires prompt work, not tool restructuring.
- **Reviewer fragility** (the StructuredOutput fallback that auto-approves after failures). This is a known bug tracked in MEMORY.md. It's orthogonal to the tool surface overhaul.
- **SDK `is_error` bug.** The patched `mcp_server.py` works around this. When the SDK fixes the bug upstream, the patch can be removed regardless of the overhaul status.

---

## Success Criteria

After full implementation:

1. **Tool count:** ≤25 tools visible to the agent (down from 48)
2. **Zero broken tools:** `search_exa` and `get_cp_history` error rates < 10%
3. **No functionality loss:** Every capability available before the overhaul is still available after
4. **Trace quality maintained:** Brier scores and calibration on resolved questions are not worse than v3.5.1 baseline
5. **Agent confusion eliminated:** No more "which search tool?" or "which market tool?" patterns in reasoning traces

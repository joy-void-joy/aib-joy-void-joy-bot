---
allowed-tools: Read, Grep, Glob, Bash(ls:*, uv run aib-devtools:*), Task, WebSearch, AskUserQuestion
description: Audit MCP tools and subagents — find gaps, overlaps, and refactoring opportunities
---

# Refactor MCP: Tool & Subagent Ontology Review

Single-pass analysis of the agent's MCP tools, subagents, and external servers. Explores what exists, whether the ontology makes sense, and brainstorms refactoring and new capabilities.

## Phase 1: Inventory — What Exists

### 1a. In-Process MCP Tools

Read every file in `src/aib/tools/` and catalog each tool:

For each tool file:
1. Read the file
2. List every `@tool`-decorated function with its name, docstring, and input schema
3. Note which MCP server it belongs to (look for `create_mcp_server` calls)
4. Note dependencies (external APIs, config keys, packages)

Build a table:

| Tool | Server | Purpose | External Deps | Config Keys |
|------|--------|---------|---------------|-------------|

### 1b. Remote MCP Servers

Check the agent configuration for remote/external MCP servers:

- Read `src/aib/agent/core.py` for MCP server setup (look for `McpSdkServerConfig`, `SdkMcpTool`, server lists)
- Read `src/aib/config.py` for MCP-related settings
- Check `pyproject.toml` for MCP server dependencies
- Grep for `npx`, `uvx`, or other MCP server launch patterns

Build a table:

| Server | Type (in-process/remote) | Tools Provided | Launch Method |
|--------|--------------------------|----------------|---------------|

### 1c. Subagents

Read `src/aib/tools/composition.py` and `src/aib/agent/core.py` to understand subagent spawning:

- How are subagents created?
- What tools do subagents get? (subset of main agent tools?)
- What's the subagent's system prompt?
- Are there specialized subagent types?

### 1d. Tool Policy & Gating

Read `src/aib/agent/tool_policy.py` to understand:

- Which tools are gated by question type?
- Which tools are gated by retrodict mode?
- Are there tools that are registered but never available?

## Phase 2: Ontology Assessment

With the full inventory, evaluate the conceptual organization:

### 2a. Categorization

Group tools into functional categories:
- **Information retrieval** (web search, news, Wikipedia, arxiv, etc.)
- **Data access** (financial APIs, prediction markets, Metaculus API)
- **Computation** (sandbox, code execution)
- **Agent orchestration** (subagents, composition)
- **Meta/reflection** (metrics, self-assessment)

Does the current file-per-server organization match these categories, or are concerns mixed?

### 2b. Naming Coherence

- Are tool names consistent? (verb_noun? noun? mixed?)
- Would a new user understand what each tool does from the name alone?
- Are there tools with overlapping names that do different things?

### 2c. Input/Output Patterns

- Do tools follow consistent patterns for inputs and outputs?
- Are error responses consistent across tools?
- Do tools use the shared response helpers (`mcp_error`, `mcp_success`)?

## Phase 3: Gap Analysis

### 3a. What's Missing

Based on the agent's purpose (forecasting), identify capability gaps:
- What data sources aren't covered? (government data, polling, scientific databases, etc.)
- What reasoning tools could help? (statistical computation, simulation, etc.)
- What workflow capabilities are missing? (caching, batching, etc.)

Cross-reference with:
- Agent meta-reflections that request capabilities (`grep -r "would benefit" notes/traces/`)
- Tool errors in traces (`uv run aib-devtools trace errors`)
- The agent's system prompt for referenced but non-existent tools

### 3b. What's Redundant

- Are there tools that do essentially the same thing?
- Are there tools that are never used in practice? (Check trace data)
- Are there tools whose functionality is better served by an MCP server?

### 3c. What's Misplaced

- In-process tools that should be remote MCP servers (heavy deps, external services)
- Remote MCP servers that should be in-process (tight integration needed)
- Tools in the wrong server (e.g., a financial tool in the search server)

## Phase 4: Refactoring Opportunities

Based on the analysis, brainstorm concrete changes:

### 4a. Data Augmentation (Single-Call Enrichment)

The **core design principle**: when tools are routinely called in sequence (A then B on the same entity), tool A should auto-include tool B's data in its response. The agent gets richer results in one turn instead of two.

**The pattern** (established in `web_search` → `fetch_routes.py`):
- `web_search` detects recognized domains in results (Yahoo Finance, arXiv, Wikipedia, FRED, Polymarket, Kalshi, Metaculus)
- For each match, it calls the specialized handler internally and attaches the result as `api_data`
- `SUGGEST_ONLY` domains get a `hint` string instead (for sites with API tools but no route handler)
- `fetch_url` hard-dispatches: if a route matches, the specialized handler replaces HTTP fetch entirely

**How to apply it to new tools:**
1. Check trace data for sequential call patterns (A always followed by B)
2. If A's handler already has the data needed for B (same API client, same object), include B's output directly
3. If B requires an extra API call, add it as opt-in (`include_X: bool = True` default on, or `False` if the payload is large)
4. The standalone B tool can remain registered for direct use, but should become rare in practice

**Known opportunities** (check if still applicable):
- `stock_price` → auto-include recent history (same `yf.Ticker` object)
- `*_price` prediction market tools → auto-include recent price history + expose IDs needed for history lookups
- `search_arxiv` → include full abstracts (already fetched, currently truncated)
- `fred_search` / `world_bank_search` → include recent data for top result
- `wikipedia` search mode → auto-fetch intro for top result
- `search_metaculus` → include full question details (objects already in memory)
- `google_trends` → include related queries via shared `pytrends` session
- AskNews `search_wikipedia` → augment results through in-process `wikipedia` handler for retrodict-aware revision fetch

**What to look for during audit:**
- Tools with 0 calls that are "follow-up" tools to a well-used tool → merge candidate
- Tools that always co-occur in traces at near 1:1 ratio → merge candidate
- Data already computed but dropped from output (e.g., IDs, full text truncated) → expose it

### 4b. Consolidation

Which tools could be merged? Look for:
- Multiple tools that hit the same API with different parameters
- Tools that could become one tool with a `mode` parameter
- Servers with only 1-2 tools that could merge into a related server

### 4b. New MCP Servers

What external MCP servers could replace in-process code?
- Search for well-maintained MCP servers on npm/PyPI
- Consider: Does the external server provide more tools than our custom code?
- Consider: Would an external server reduce our maintenance burden?

### 4c. New Tools

What new tools would most improve forecasting quality?
- Rank by expected impact (how many questions would benefit)
- Estimate implementation complexity
- Note whether a library/MCP server already exists

### 4d. Architecture Changes

Bigger structural ideas:
- Should the tool→server mapping change?
- Should subagent tool sets be restructured?
- Are there cross-cutting concerns (caching, rate limiting, retry) that need unification?

## Phase 5: Report

Present findings as:

```markdown
## MCP Tool Ontology Review

### Inventory Summary
- **N** in-process tools across **M** servers
- **P** remote MCP servers providing **Q** additional tools
- **R** subagent configurations

### Ontology Assessment
- [What works well about the current organization]
- [What doesn't — inconsistencies, misplacements, naming issues]

### Gaps
| Gap | Impact (questions affected) | Difficulty | Existing Solution? |
|-----|---------------------------|------------|-------------------|

### Redundancies
| Tools | Why Redundant | Recommendation |
|-------|--------------|----------------|

### Refactoring Proposals
1. **[Proposal name]** — [one-line description]
   - What: [specific changes]
   - Why: [expected benefit]
   - Effort: [low/medium/high]
   - Risk: [what could break]

2. ...

### New MCP Servers to Consider
| Server | What It Provides | Replaces | npm/PyPI |
|--------|-----------------|----------|----------|

### Recommended Priority Order
1. [Highest impact, lowest effort first]
2. ...
```

## Rules

- **Read the code, don't guess.** Open every tool file and read the actual implementations. Tool names and docstrings don't tell the full story.
- **Check trace data for usage.** A tool that exists but is never called is worse than a gap — it's clutter that confuses the agent's tool selection.
- **Think from the agent's perspective.** The agent sees a flat list of tools. Does the naming and organization help it choose the right tool for the task?
- **Propose, don't implement.** This is an audit, not a refactoring session. Present findings and let the user decide what to act on.
- **Use AskUserQuestion** for any decisions or prioritization that need user input.

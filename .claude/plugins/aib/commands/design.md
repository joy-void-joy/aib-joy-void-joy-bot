---
allowed-tools: Read, Grep, Glob, Bash(ls:*, uv run lup-devtools:*), AskUserQuestion
description: Evaluate agent capabilities, propose changes to improve forecasts
argument-hint: [focus area]
---

# Agent Design Review

Read the entire agent codebase with fresh eyes and evaluate: **what changes to tools, architecture, and pipeline would produce better forecasts?**

This is not a code quality review — `/refactor` handles that. This is about whether the agent has the right capabilities to forecast well.

## Phase 1: Read the System

Build your mental model purely from the code. No feedback-loop data yet — fresh eyes first.

### 1a. The prompt

`src/aib/agent/prompts.py` — The agent's instructions. Read every line. Understand what strategies it teaches, what guardrails it sets, what it asks the agent to do.

### 1b. The tools

Start with `src/aib/agent/tool_policy.py` for the inventory, then read every file in `src/aib/tools/`. For each tool, understand:
- What data does it give the agent?
- How much enrichment happens inside the tool vs. left to the agent?
- What domains or question types does it serve?

### 1c. The pipeline

`src/aib/agent/` — Orchestration, hooks, reflection, CDF generation. Trace the flow from question input to forecast output. Understand what the agent does, in what order, with what tools.

### 1d. Draw the map

Present a compact overview:
- Pipeline diagram: question → agent → tools/servers → forecast
- Tool inventory grouped by domain (data sources, computation, workflow)
- Prompt structure: what sections exist, what they teach
- Key stats: tool count, prompt token estimate, server count

Use AskUserQuestion to confirm your understanding before proceeding.

## Phase 2: Capability Assessment

With the system fresh in your mind, assess it through the **forecasting lens**. The question for every component is: does this help the agent make better forecasts?

### Data coverage

- What domains are well-covered by tools? (economics, markets, politics, science, tech, etc.)
- What domains have no dedicated tools — where is the agent relying entirely on web search?
- For each tool: does it follow the data augmentation pattern (enrich inside the tool), or does it return raw data and leave the agent to fish for meaning?
- Are there obvious data sources missing? (Government databases, polling aggregators, scientific repositories, prediction markets, etc.)

### Question type readiness

- How does the toolkit serve binary vs. numeric vs. multiple-choice questions differently?
- Are there question types where the agent is under-equipped? (e.g., questions requiring time series analysis, geopolitical judgment, technical domain knowledge)
- Does the CDF generation pipeline have the right inputs?

### Reasoning support

- Does the prompt teach useful forecasting strategies, or mostly defensive rules?
- Are there prompt sections that are doing the job of a tool? (e.g., "look up base rates" as a prompt rule instead of a base-rate tool)
- Where does the pipeline structure help the agent think well? Where does it get in the way?
- Do hooks and reflection stages add forecasting value, or mostly process overhead?

### Information flow

- Does the agent get the right information at the right time?
- Is there data available in the pipeline that doesn't reach the agent effectively?
- Are tool results structured so the agent can use them directly, or does it need to parse/interpret?

### What's earning its keep

Not everything needs to change. Identify components that are clearly pulling their weight — tools that provide high-value data, prompt sections that teach genuinely useful strategies, pipeline stages that improve forecast quality. These should be protected from unnecessary change.

## Phase 3: Cross-Reference with Performance Data

Now — and only now — look at how the agent actually performs. The goal is to validate, challenge, or enrich your Phase 2 assessment with ground truth.

### 3a. Recent feedback-loop findings

Read the most recent 2-3 analysis docs from `notes/feedback_loop/`. Extract:
- Recurring error types (wrong base rate, missed data, stale data, overconfident CDF, etc.)
- Tool health flags — which tools are failing or underperforming?
- Capability gaps — what has feedback-loop identified as missing?
- What the agent does well — patterns of strong performance

### 3b. Calibration data

```bash
uv run lup-devtools calibration summary
uv run lup-devtools scores summary
```

Where is the agent well-calibrated? Where is it systematically off?

### 3c. Reconcile

For each finding from Phase 2:
- **Confirmed**: Performance data supports this assessment
- **Challenged**: The data tells a different story — update your view
- **Blind spot**: Something the data reveals that your code read missed
- **Unconfirmed**: No performance data either way — flag as speculative

This reconciliation is the unique value of running /design. The feedback loop sees patterns in outcomes; the fresh code read sees structural gaps. The intersection is where the strongest proposals come from.

## Phase 4: Propose

Present changes ranked by **expected impact on forecast accuracy**.

For each proposal:
- **What**: The change — new tool, tool enhancement, pipeline modification, prompt restructure
- **Why**: What forecasting problem it solves, with evidence (Phase 2 assessment + Phase 3 data)
- **Bitter Lesson**: Classify as tool > capability > principle > prompt patch. Prefer the left side.
- **Effort**: Small / medium / large

Group proposals:
1. **High-confidence improvements** — Both code analysis and performance data point the same way
2. **Fresh-eye findings** — Code review surfaced issues not yet visible in performance data
3. **Data-confirmed gaps** — Performance data shows problems the code review can now explain

## Phase 5: Discussion

Use AskUserQuestion to present top 3-5 proposals and get the user's reaction. The output becomes the input to implementation work.

## Principles

- **Forecasting over engineering.** "The module boundaries are clean" is not a finding. "The agent has no tool for checking prediction market prices" is.
- **Fresh eyes matter.** Read the code before the performance data. Your unbiased assessment catches things the feedback loop can't.
- **The Bitter Lesson.** Tool > capability > principle > prompt patch. If the prompt says "look up X", that should probably be a tool that provides X.
- **Data augmentation pattern.** Tools should enrich data inside the tool, not return raw results for the agent to interpret. If a tool isn't doing this, that's a finding.
- **Propose, don't implement.** This is a review. Present findings and let the user decide.

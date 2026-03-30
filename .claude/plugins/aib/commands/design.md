---
allowed-tools: Read, Grep, Glob, Bash(ls:*, uv run aib-devtools version show:*, uv run aib-devtools analysis prompt-health:*), AskUserQuestion
description: Read all agent code from scratch, evaluate design quality, propose structural improvements
argument-hint: [focus area]
---

# Architecture Review

Read the entire agent codebase and evaluate whether the system is well-designed. The question is: **if we were building this today, would we build it this way?**

## Phase 1: Read the System

Read all agent code, building your mental model purely from the code. Start with the directories below and discover the structure yourself.

### 1a. The prompt

`src/aib/agent/prompts.py` — The agent's instructions. The most consequential file. Read every line.

```bash
uv run aib-devtools analysis prompt-health
```

### 1b. The tools

`src/aib/tools/` — All tool implementations. Start with `src/aib/agent/tool_policy.py` for the inventory, then read the implementations.

### 1c. The pipeline

`src/aib/agent/` — Orchestration, hooks, reflection, CDF generation. Trace the flow from question input to forecast output.

### 1d. Supporting code

Everything else in `src/aib/` — submission, scoring, configuration, utilities.

## Phase 2: The Greenfield Question

**If you were building this system today, from scratch, with the same goals — what would it look like?**

The gap between that answer and what exists is the review.

### Dimensions

For each, describe what the greenfield design would look like and where the current system diverges.

**Conceptual integrity** — Does the system have one coherent design philosophy, or is it a collection of independent decisions? Do the prompt, tools, and pipeline pull in the same direction?

**Responsibility boundaries** — Does each module own one thing? Is there logic that should move? Are there modules that do too much, or exist for historical reasons?

**Tool design** — Do the tools follow consistent patterns? Are they the right granularity — or could some be unified? Are there tools that exist because of a specific past problem but aren't the right abstraction? What tools would you build if starting fresh?

**Prompt architecture** — Is the prompt structured around principles or accumulated rules? What would the prompt look like if written from scratch today? What sections earn their token cost and which are patches?

**Pipeline design** — Is the flow from question to forecast the right flow? Are hooks/reflection/review adding value proportional to their complexity? Would you design the pipeline differently?

**Information flow** — How does data move through the system? Are there places where information is lost, duplicated, or transformed unnecessarily?

**What's no longer needed** — Code, tools, prompt sections, or pipeline stages that could be removed without loss.

## Phase 3: Propose

Present your findings as a **design document**.

### 1. System overview (as you understand it)

How the system works, from your reading. Validates your understanding — the user can correct misunderstandings before you build on them.

### 2. What's working well

Design choices that are sound and would survive a rewrite. Be specific about why — this protects good decisions from unnecessary change.

### 3. Structural proposals

For each:
- **What**: The change — consolidation, restructure, new abstraction, new tool, removal
- **Why**: What's wrong with the current design, or what gap exists
- **Greenfield**: What this would look like if built from scratch
- **Migration**: How to get from here to there

This includes building new things. If the system is missing a tool, an abstraction, or a pipeline stage that the greenfield design would have — propose it. Design review isn't just about trimming; it's about filling holes.

Order by structural importance, not ease of implementation.

## Phase 4: Discussion

Use AskUserQuestion to present your top 3 proposals and get the user's reaction. The output becomes the input to a `/refactor` session or a new worktree.

## Principles

- **Design over performance.** "The forecasts are inaccurate" is not a design finding. "The prompt conflates strategy guidance with output formatting" is.
- **Greenfield thinking.** For every component, ask "would I build it this way?" If not, that's a finding — even if the current version works.
- **Removal is a feature.** Every component should justify its existence.
- **Structural over incremental.** If your proposal could be a one-line fix, think bigger. If it requires rewriting everything, think smaller. The sweet spot is changes that simplify the system's conceptual model.

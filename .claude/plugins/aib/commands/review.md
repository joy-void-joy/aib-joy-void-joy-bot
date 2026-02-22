---
allowed-tools: Read, Grep, Glob, Bash(ls:*, wc:*, sort:*, tail:*, stat:*, uv run aib-devtools:*), AskUserQuestion
description: Deep review of a single forecast trace — tool use, reasoning, workflow, pipeline health
argument-hint: [paste trace.md, reflection.yaml, or forecast JSON]
---

# Review: Single-Trace Deep Analysis

Analyze a pasted forecast trace for tool use quality, reasoning soundness, workflow effectiveness, pipeline health, and subtle bugs. Start from the trace; dig into source code when the trace reveals something worth investigating.

## Input

**Pasted trace content**: $ARGUMENTS

The user pastes one or more of:
- **trace.md** — Full agent reasoning log (thinking blocks, tool calls, results)
- **reflection.yaml** — Agent self-assessment (factors, estimate, assessment, tool audit)
- **forecast JSON** — Final structured output with metrics and metadata

Work with whatever you get. A trace.md alone is enough for a thorough review. reflection.yaml and forecast JSON add quantitative depth.

## Step 1: Orient — What Kind of Trace Is This?

Read the pasted content and establish context before analyzing anything:

- **Question**: What was being forecast? (title, type, post ID if visible)
- **Question type**: Binary, numeric, discrete, or multiple choice?
- **Agent version**: From `agent_version` field or version directory path
- **Retrodict?**: Is there a `retrodict_date`? If so, note the cutoff — this affects how you evaluate tool results
- **Duration**: How long did the session take? (from `session_duration_seconds` or timestamps)
- **Outcome**: What did the agent forecast? (probability, percentiles, CDF)

State this context in 3-4 lines at the top of your report so the reader is oriented.

## Step 2: Tool Use Audit

Go through every tool call in the trace. For each, assess:

### 2a. Tool Call Inventory

List every tool call with:
- Tool name
- What the agent was trying to learn
- Whether it succeeded or failed
- Whether the result was actually useful for the forecast

### 2b. Tool Errors and Failures

For each failed tool call:
1. **What happened** — Quote the error from the trace
2. **Why it failed** — Read the relevant tool implementation in `src/aib/tools/` to understand the failure mode. Common locations:
   - `src/aib/tools/forecasting.py` — Metaculus API, CP history
   - `src/aib/tools/markets.py` — Prediction markets
   - `src/aib/tools/financial.py` — FRED, stock data
   - `src/aib/tools/search.py` — Web search
   - `src/aib/tools/sandbox.py` — Code execution
   - `src/aib/tools/composition.py` — Subagent spawning
3. **Was the agent's recovery reasonable?** — Did it try an alternative, or just move on?
4. **Is this a known issue or a new bug?** — Grep for the error pattern in the codebase

### 2c. Subtle Tool Bugs

Look for cases where a tool *succeeded* but returned misleading or incomplete data:
- Search results that missed obvious relevant sources
- API data that was stale, truncated, or misformatted
- Tool results the agent misinterpreted (the data was fine but the agent read it wrong)
- Tools that returned `is_error: True` as content rather than raising — check if the agent noticed

### 2d. Missing Tool Calls

What tools *should* the agent have called but didn't?
- Available tools the agent never used (check against the tool list in `src/aib/tools/`)
- Obvious follow-up searches the agent skipped
- Data sources that would have strengthened the forecast

## Step 3: Workflow Assessment

Evaluate the agent's forecasting *process*, separate from the quality of individual reasoning steps.

### 3a. Information Gathering

- Did the agent gather enough evidence before forming a view?
- Did it triangulate across multiple sources (markets, news, historical data)?
- Did it front-load research or jump to a conclusion early and then cherry-pick?

### 3b. Structured Reasoning

- Did the agent decompose the question into sub-questions or factors?
- Did it identify and weigh key uncertainties?
- Did it consider base rates?
- For numeric questions: Did the percentile estimates form a coherent distribution?

### 3c. Self-Correction

- Did the agent update its view when new evidence contradicted its initial take?
- Did it notice and flag its own uncertainty honestly?
- Did the reflection (if present) reveal any self-awareness about weaknesses?

### 3d. Time and Token Efficiency

- Were there wasted tool calls (same search repeated, irrelevant tangents)?
- Did the agent spend proportional effort on important vs. trivial factors?
- Was the session duration reasonable for the question complexity?

## Step 4: Reasoning Quality

Evaluate the *substance* of the agent's reasoning, not just the process.

### 4a. Evidence Quality

For each major evidence factor the agent cited:
- Is the evidence real and correctly interpreted?
- Is the source reliable?
- Did the agent weight it appropriately?

### 4b. Logic and Inference

- Are the logical steps valid? (No non-sequiturs, no conflation of correlation/causation)
- Did the agent account for both sides of the question?
- Are there obvious counterarguments the agent missed?

### 4c. Calibration Sense

- Does the final probability/estimate feel calibrated given the evidence presented?
- Is the agent overconfident or underconfident relative to the uncertainty it described?
- For numeric: Are the confidence intervals reasonable? Too tight? Too wide?

### 4d. Factors Assessment (if reflection.yaml present)

Review the factors list from the reflection:
- Do the logits and confidence values make sense?
- Are any factors double-counted or contradictory?
- Does the tentative estimate follow logically from the factors?

## Step 5: Pipeline Health

Look for system-level problems that aren't about the agent's reasoning:

- **MCP connection issues** — Tools timing out, returning empty results
- **Sandbox failures** — Docker issues, network restrictions blocking valid operations
- **Token/context pressure** — Did the agent hit limits? Was reasoning truncated?
- **Prompt issues** — Did the agent seem confused by its instructions? Did it follow the system prompt well?
- **Hook behavior** — Any signs of permission hooks blocking valid operations?

When you spot a pipeline issue, read the relevant source code:
- `src/aib/agent/core.py` — Main orchestration
- `src/aib/agent/prompts.py` — System prompt
- `src/aib/agent/numeric.py` — CDF generation
- `src/aib/agent/hooks.py` — Agent hooks

## Step 6: Report

Structure your findings as:

```markdown
## Trace Review: [Question Title]

**Context**: [question type] | [agent version] | [duration] | [forecast: X]

### Tool Use
- **Calls**: N total (N succeeded, N failed, N low-value)
- **Errors**: [list each with brief explanation]
- **Subtle issues**: [tools that succeeded but returned questionable data]
- **Missing**: [tools the agent should have used]

### Workflow
- **Information gathering**: [adequate / rushed / thorough but unfocused]
- **Structure**: [well-decomposed / ad-hoc / overly complex]
- **Self-correction**: [evidence of updating views, or lack thereof]
- **Efficiency**: [good / wasted N calls on X]

### Reasoning
- **Strengths**: [what the agent got right]
- **Weaknesses**: [logical gaps, missed evidence, calibration issues]
- **Calibration**: [does the forecast match the evidence presented?]

### Pipeline
- **Issues found**: [system-level problems, or "none"]
- **Source code investigation**: [what was found in src/ for each issue]

### Bugs Found
[For each bug — what happened, which source file, what the fix would be]

### Actionable Takeaways
1. [Most important finding — what to fix or improve]
2. [Second priority]
3. [Third priority]
```

## Rules

- **Start from the trace.** Read every line of the pasted content before reaching for source code. The trace is your primary evidence.
- **Dig into source code only when the trace gives you a reason.** A tool error, a suspicious result, a pipeline hiccup — these warrant reading `src/`. Don't read source code preemptively.
- **Quote the trace.** When you identify an issue, quote the exact lines from the pasted content that show it. Don't paraphrase.
- **Be specific about bugs.** "The search tool had issues" is useless. "web_search returned 0 results for 'Iran nuclear deal 2026' — checking src/aib/tools/search.py:L42, the query is passed through without date filtering" is useful.
- **Distinguish agent issues from system issues.** A bad search query is the agent's fault. A tool returning HTTP 500 is a pipeline issue. Don't conflate them.
- **Ask when the trace is ambiguous.** If the pasted content is incomplete or you need the reflection/JSON to assess something, use AskUserQuestion rather than guessing.

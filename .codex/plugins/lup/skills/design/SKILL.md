---
name: design
description: "Evaluate agent capabilities, propose changes to improve forecasts"
---

# Agent Design Review

**What changes to tools, architecture, and pipeline would produce better
forecasts?**

This is not a code quality review, and it is not a tool audit either. The tool
audit is a skill already, and this one starts by running it rather than
restating it. What only this skill does is hold the answer against the record
of how the agent actually scored.

Focus area, if one was given:

the arguments supplied with this skill invocation

## Phase 1: Map the system

Invoke $lup:refactor-tools and take its pipeline diagram, its tool
inventory, and its gap-and-overlap findings as this skill's phase 1. Do not
re-derive them.

Read `src/aib/agent/prompts.py` yourself on top of that — the audit covers
tools and subagents, not what the prompt teaches. Note what strategies it
teaches, what guardrails it sets, and which of its rules are standing in for a
tool that does not exist.

## Phase 2: Assess through the forecasting lens

The tool audit asks whether the toolkit is coherent. Ask instead whether it
wins:

- **Data coverage** — which domains have dedicated tools, and which leave the
  agent on general web search? Does each tool enrich its data inside the tool,
  or return raw results for the agent to interpret?
- **Question type readiness** — how does the toolkit serve binary against
  numeric against multiple-choice? Does the CDF pipeline have the right inputs?
- **Reasoning support** — does the prompt teach useful forecasting strategy, or
  mostly defensive rules? Where does the pipeline help the agent think, and
  where does it get in the way?
- **Information flow** — does the agent get the right information at the right
  time, or is there data in the pipeline that never reaches it usefully?
- **What is earning its keep** — name the components clearly pulling their
  weight. These should be protected from unnecessary change.

## Phase 3: Cross-reference against performance

Now, and only now, look at how the agent actually performs. This phase is why
the skill exists.

Read the most recent two or three analysis documents under
`notes/feedback_loop/` for recurring error types, tool health flags, and
capability gaps already identified. Then take the numbers:

```bash
uv run lup-devtools calibration summary
uv run lup-devtools scores summary
```

Where is the agent well calibrated, and where is it systematically off?

Reconcile every phase 2 finding against that record:

- **Confirmed** — the performance data supports the assessment
- **Challenged** — the data tells a different story; update the view
- **Blind spot** — something the data reveals that the code read missed
- **Unconfirmed** — no data either way; flag as speculative

The tool audit sees structure and the feedback loop sees outcomes. The
intersection is where the strongest proposals come from, and it is the one
thing neither skill reaches alone.

## Phase 4: Propose

Rank proposals by **expected impact on forecast accuracy**. For each: what the
change is, what forecasting problem it solves and on what evidence, and its
classification — a tool beats a capability beats a principle beats a prompt
patch. Prefer the left. If the prompt says "look up X", that should probably be
a tool that provides X.

Group them into high-confidence improvements where code and data agree,
fresh-eye findings not yet visible in the data, and data-confirmed gaps the
code read can now explain.

## Phase 5: Discussion

Present the top three to five proposals and get a reaction:

Ask the user directly, offering concrete options, and wait for the answer: which of these proposals to take forward, and which to set aside

The output is the input to implementation work.

## Principles

- **Forecasting over engineering.** "The module boundaries are clean" is not a
  finding. "The agent has no tool for prediction market prices" is.
- **Structure before outcomes.** Read the system before the performance data,
  so the assessment is not merely a retelling of the last analysis document.
- **Propose, do not implement.** This is a review.

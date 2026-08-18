---
name: audit
description: "Focused audit of specific forecasts \u2014 traces, reasoning, and version comparison"
---

# Audit: Focused Forecast Feedback

Analyze specific forecasts in depth: trace reasoning and tool-use quality,
compare the generating version's scaffolding against current, and report what
has been fixed, what has regressed, and what strengths to preserve.

## Input

**Post IDs**:

the arguments supplied with this skill invocation

Parse the space-separated post ids (one to ten). If none were provided, ask
which forecasts to audit.

## Phase 1: Discovery

Gather metadata for each post id and group by version.

```bash
uv run lup-devtools analysis dashboard
uv run lup-devtools trace show <post_id>
uv run lup-devtools scores show --post-id <post_id>
```

Extract the agent version, question type, forecast value, and score where the
question has resolved. The current version is `[tool.lup] agent_version` in
`pyproject.toml`.

Build a version-to-post-ids mapping and report it before proceeding. If any
post ids lack trace data, report and exclude them; if all of them do, say so
and stop.

## Phase 2: Resolution Investigation

For each **resolved** question, investigate the real-world outcome from the
actual data. Skip unresolved questions with a note.

```bash
# Update forecast records with any new resolutions first
uv run lup-devtools resolution sync
# Then inspect the full API data for each resolved question
uv run lup-devtools api post <post_id>
```

Extract the resolution value, resolution criteria, close date, and question
text.

Then investigate the underlying data. Start from the sources relevant to the
question — the same kinds the agent used — and use everything available: web
search, data APIs, page fetches. The goal is a first-hand understanding of what
happened, not a reading of the resolution value.

- How did the underlying data evolve before, during, and after the forecast
  period?
- At what point did the outcome become clear from the data?
- Was the direction predictable at forecast time, or was there a genuine
  surprise?

Where the investigation needs computation — trend analysis, CDF comparison,
threshold checks — evaluate it with `uv run lup-devtools py eval`, and add a
command under `src/aib/devtools/` when the same computation is wanted twice.

### Error classification

| Error Type | Description |
|---|---|
| **Wrong base rate** | Bad prior, missed relevant reference classes |
| **Missed key data** | A specific source existed but was not found or used |
| **Stale data** | Used outdated information when fresher data existed |
| **Misunderstood scope** | Misread question criteria or resolution conditions |
| **Overconfident CDF** | Directionally correct but tails too narrow |
| **Underconfident CDF** | Directionally correct but distribution too diffuse |
| **Directionally wrong** | Forecast pointed the wrong way entirely |
| **Timing error** | Right prediction, wrong timeframe |
| **Good forecast** | Well calibrated given available information |

### Counterfactual

Ground each counterfactual in what the data investigation revealed — which
source queried at forecast time would have shown which signal, or that the
outcome was a genuine surprise that shifted after the forecast. Carry this into
phase 3; the trace explorer needs it.

### Phase 2 gate

Before delegating, present the post-mortem table (post id, version, type,
forecast, resolution, score, error type), one or two sentences per resolved
post on what happened, and the counterfactuals. Then ask:

Ask the user directly, offering concrete options, and wait for the answer: whether to proceed to trace analysis, or investigate one of these posts more deeply first

Do not delegate until this is confirmed. The trace explorer needs the
resolution context, and rushing past it produces shallow analysis.

## Phase 3: Analysis

For each post id, read the session's summary document and extract the per-tool
assessment, the capability gaps and subtle bugs, the reasoning assessment
(evidence quality, logical coherence, calibration sense), the workflow
assessment, the future-leak verdict for retrodict traces, and the notable
observations. Cross-reference with the phase 2 investigation: where does the
summary agree or disagree with what actually happened?

Where a summary is missing, note it, and reach for `uv run lup-devtools trace
log <post_id>` when deeper investigation is warranted.

**Skip the version comparison if every forecast is from the current version**,
and note that the audit becomes a trace analysis without it. Otherwise:

Delegate to the lup:version-explorer custom agent with this task: Compare each generating version against the current one. Report prompt changes grouped by theme, tool policy changes, orchestration changes, and what the current version would do differently on the same question.

## Phase 4: Synthesis

Cross-reference trace findings against version diffs and the resolution
investigation. This is the audit's unique value.

For each issue found, check the version diff and classify it as **fixed** (the
diff addressed it), **unaddressed** (no relevant change), or a
**current-version issue**. For each strength found, classify it as
**preserved**, **at risk** (scaffolding modified), or **lost**.

For each unaddressed issue, write a recommendation that prefers a tool or
capability over a prompt patch, and a general principle over a specific rule.
Be concrete: "build a tool that provides X", not "add a prompt rule about Y".

### Phase 4 gate

Present the fixed issues with diff citations, the unaddressed issues with
recommendations, the strengths at risk, and the prioritized actions. Then ask:

Ask the user directly, offering concrete options, and wait for the answer: whether to write the report, investigate an issue further, or adjust the recommendations

Do not write the report until this is confirmed. If the "what has been fixed"
or "strengths to preserve" sections come out empty, the cross-referencing was
not done.

## Phase 5: Report

Write the report with a per-question overview table, a post-mortem for each
resolved question (forecast, resolution, error type, what happened, where the
reasoning diverged, what would have helped), then the sections "what has been
fixed", "what remains unaddressed", "strengths to preserve", a version delta
summary, and the recommended actions.

## Guidelines

- **Cross-reference is the whole point.** Connecting trace findings to version
  diffs is what makes this valuable — without it, use $lup:review instead.
- **Quote both sides.** Cite trace evidence and version-diff evidence for every
  finding.
- **Strengths matter as much as weaknesses.** Confirming what works prevents
  regressions.
- **Be honest about coverage.** If every forecast is current-version, say so.
- **Mark analyzed** once the report is written:
  `uv run lup-devtools analysis mark <post_ids>`

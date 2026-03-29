---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, Task, WebSearch, WebFetch, AskUserQuestion
description: Full feedback loop — orchestrates status, investigation, analysis, reflection, implementation, and retrodiction
argument-hint: [post_id1 post_id2 ...] [--refresh]
---

# Feedback Loop Orchestrator

Run the full feedback loop by invoking subcommands in sequence. Each subcommand is independently invocable — the orchestrator calls them in order with gates between phases.

## Core Principle: Resolution Data Drives Everything

The most valuable thing in each session is **ground truth** — forecasts that have resolved since last time. Start there. Everything else (tool health, trace quality, reviewer accuracy) is evaluated in the context of "did it produce accurate forecasts?"

## Version Annotation, Not Version Filtering

Don't scope the loop to a single version. Analyze everything new since the last session. **Annotate every data point with the version that produced it** — this tells us which code to credit or blame. A v3.6 forecast that resolves today is relevant to today's session.

## Sequence

### 1. `/fb-status` — State + resolutions + targets

Surfaces what resolved, what's new, what changed. Ends with a gate.

### 2. `/fb-investigate` — Resolution post-mortem

The most important phase. For each resolved forecast: score it, classify the error, build a counterfactual. Skip only if genuinely nothing resolved.

### 3. `/fb-analyze` — Tool health + capability gaps + trace quality

Aggregate from summary.json and tool_metrics. Cross-reference with investigation findings — did tool failures cause forecast errors?

### 4. Report — Synthesize findings

Write the analysis doc NOW, before discussing what to do about it. The report forces synthesis and becomes input to the discussion.

Save to `notes/feedback_loop/<worktree>/<timestamp>_analysis.md`:

```markdown
# Feedback Loop Analysis — <date>

Agent version: <version>

## Ground Truth
- Resolved forecasts analyzed: N (by version: vX.Y: M, vA.B: K)
- Brier by version: vX.Y: X.XXXX (n=M), vA.B: X.XXXX (n=K)
- Calibration: ECE X.XX, coverage XX%

## Post-Mortem
| Post | Ver | Type | Forecast | Resolution | Score | Error |
|------|-----|------|----------|------------|-------|-------|

## Per-Forecast Details
### <post_id>: <title>
- Version: X.Y.Z
- Error type:
- What happened:
- What would have helped:

## Tool Health
- Flagged tools (with version):
- Capability gaps:

## Trace Quality
- Summary of trace audit findings

## Open Questions
- Things that surprised us or need more investigation
```

### 5. `/fb-reflect` — Collaborative discussion

NOT a checklist. A genuine conversation about what the data means and what to do about it. Uses AskUserQuestion for back-and-forth. Discuss process quality, propose changes, challenge assumptions together.

### 6. `/fb-implement` — Make changes, commit, bump version

Entry gate requires user approval of the change list from the discussion.

### 7. `/fb-retrodict` — Queue next retrodictions

Find candidates and output ready-to-use commands.

### 8. Mark analyzed

```bash
uv run aib-devtools analysis mark <post_ids>
```

## Principles

### The Bitter Lesson

Give the agent tools and capabilities, not prescriptive rules. When a pattern appears:
- **Good**: Build a tool that provides the data the agent needs
- **OK**: Add a general principle that helps across many question types
- **Bad**: Add a specific rule for the observed pattern

### CP visibility constraint

The agent cannot see the community prediction for the question it is currently forecasting. CP data is only available post-hoc for calibration analysis. Never interpret CP divergence as a quality signal without resolution data.

### Anti-patterns

- Don't patch prompts for observed patterns — build tools or rewrite sections
- Don't over-rely on CP divergence — wait for resolution data
- Don't add unactionable rules — provide actionable tools instead
- Don't skip reading traces — when summary.json raises questions, read the actual trace
- Don't work around broken devtools — fix them in this session so the next loop benefits

### Offline mode

If API calls fail (scraping, resolution sync), proceed with local data. Most analysis commands read local JSON files and don't require network access. Use `--no-refresh` flags where available.

## Completion Checklist

- [ ] Dashboard reviewed
- [ ] Resolutions surfaced and cross-checked
- [ ] Previous analysis read (or noted "first session")
- [ ] Targets selected and confirmed
- [ ] Per-forecast post-mortem with error classifications (version-annotated)
- [ ] Calibration summary reviewed
- [ ] Tool health and capability gaps aggregated
- [ ] Analysis doc written (BEFORE discussion)
- [ ] Collaborative discussion with user (reflect phase)
- [ ] Priority list confirmed before implementation
- [ ] Changes implemented (or marked PROPOSED/DEFERRED)
- [ ] Version bumped (if behavioral changes)
- [ ] Analyzed posts marked
- [ ] Retrodiction queue proposed (or "none available")

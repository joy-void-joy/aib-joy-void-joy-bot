---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, Task, WebSearch, WebFetch, AskUserQuestion
description: Full feedback loop — orchestrates status, investigation, analysis, reflection, implementation, and retrodiction
argument-hint: [post_id1 post_id2 ...] [--refresh]
---

# Feedback Loop Orchestrator

Run the full feedback loop by invoking subcommands in sequence. Each subcommand is independently invocable — the orchestrator calls them in order with gates between phases.

## Three Levels of Analysis

- **Object Level**: The agent itself — tools, capabilities, runtime behavior
- **Meta Level**: The agent's self-assessment — are summary.json reviews accurate? Is the reflection schema capturing what matters?
- **Meta-Meta Level**: This feedback loop process — are the subcommands useful? Are the devtools providing the right data?

## Sequence

### 1. `/fb-status` — State + targets

Pass $ARGUMENTS through. Ends with a gate — confirm targets before proceeding.

### 2. `/fb-investigate` — Resolution investigation

Skip if no resolved forecasts among targets. Ends with a gate — confirm post-mortem before proceeding.

### 3. `/fb-analyze` — Tool health + capability gaps + patterns

Aggregate findings from summary.json via analysis devtools.

### 4. `/fb-reflect` — Meta + meta-meta reflection

Assess process quality and tracking data completeness. Gate: confirm priority list before implementation.

### 5. `/fb-implement` — Make changes, commit, bump version

Entry gate requires user approval of the change list.

### 6. `/fb-retrodict` — Queue next retrodictions

Find candidates and output ready-to-use commands.

### 7. Mark analyzed

```bash
uv run aib-devtools analysis mark <post_ids>
```

### 8. Write analysis doc

Save to `notes/feedback_loop/<timestamp>_analysis.md` using this template:

```markdown
# Feedback Loop Analysis — <date>

Agent version: <version>

## Ground Truth
- Resolved forecasts analyzed: N
- Average Brier: X.XXXX
- Calibration: ECE X.XX, coverage XX%

## Post-Mortem
| Post | Ver | Type | Forecast | Resolution | Score | Error |
|------|-----|------|----------|------------|-------|-------|

## Per-Forecast Details
### <post_id>: <title>
- Error type:
- What happened:
- What would have helped:

## Tool Health
- Flagged tools:
- Capability gaps:

## Changes
| Level | Change | Status | Rationale |
|-------|--------|--------|-----------|

## Retrodiction Queue
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

### Offline mode

If API calls fail (scraping, resolution sync), proceed with local data. Most analysis commands read local JSON files and don't require network access. Use `--no-refresh` flags where available.

## Completion Checklist

- [ ] Dashboard reviewed
- [ ] Previous analysis read (or noted "first session")
- [ ] Targets selected and confirmed
- [ ] Per-forecast post-mortem with error classifications
- [ ] Calibration summary reviewed
- [ ] Tool health and capability gaps aggregated
- [ ] Meta-level: tracking data sufficient?
- [ ] Priority list confirmed before implementation
- [ ] Changes implemented (or marked PROPOSED/DEFERRED)
- [ ] Version bumped (if behavioral changes)
- [ ] Analysis doc written
- [ ] Analyzed posts marked
- [ ] Retrodiction queue proposed (or "none available")

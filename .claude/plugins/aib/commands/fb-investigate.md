---
allowed-tools: Bash(uv run aib-devtools:*), Read, Grep, Glob, WebSearch, WebFetch, AskUserQuestion
description: Investigate resolved forecasts — error classification, counterfactuals, calibration
argument-hint: <post_id1> [post_id2 ...]
---

# Investigate: Resolution Post-Mortem

Build first-hand understanding of what happened with each resolved forecast.

## Per-Forecast Investigation

For each resolved target forecast:

### 1. Get score and resolution

```bash
uv run aib-devtools scores show <id> --no-refresh
```

### 2. Read summary.json

Find and read the summary.json from the session directory for this post. It contains:
- `tool_audit.by_tool` — per-tool qualitative assessment
- `reasoning` — evidence quality, logical coherence, calibration sense ratings
- `workflow` — info gathering, structured reasoning, self-correction, efficiency
- `future_leak` — for retrodict traces only

### 3. Investigate the real-world outcome

Use WebSearch and WebFetch to understand what actually happened. Don't just read the resolution value — understand the story.

### 4. Classify the error

Use this 9-type taxonomy:

| Type | Description |
|------|-------------|
| Good forecast | Correct direction, well-calibrated |
| Wrong base rate | Used inappropriate reference class |
| Missed key data | Critical information was available but not found |
| Stale data | Used outdated information |
| Misunderstood scope | Resolution criteria interpreted differently than intended |
| Overconfident CDF | Numeric: too narrow distribution |
| Underconfident CDF | Numeric: too wide distribution |
| Directionally wrong | Binary: wrong side of 50% |
| Timing error | Right direction but wrong about when |

### 5. Build counterfactual

What specific data source, tool call, or reasoning step would have changed the forecast? Be concrete — "should have checked X" not "should have been more careful."

## Retrodict airtightness

For retrodict traces, note the `future_leak` verdict from summary.json. Only trust CLEAN verdicts for calibration.

## Cross-reference with calibration

After investigating individual forecasts:

```bash
uv run aib-devtools calibration summary --no-refresh
```

Verify: does the calibration aggregate confirm or contradict individual findings?

## Gate

Use AskUserQuestion to present:
1. Post-mortem table: Post ID | Version | Type | Forecast | Resolution | Score | Error Type
2. Error classification summary (counts by type)
3. Calibration headline (Brier, ECE, coverage)
4. Key counterfactuals for 2-3 worst forecasts

Options: "Proceed to analysis" / "Dig deeper on specific posts" / "Skip to implementation"

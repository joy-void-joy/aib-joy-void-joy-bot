---
allowed-tools: Read, Grep, Glob, Bash(ls:*, wc:*, sort:*, tail:*, stat:*), WebSearch, AskUserQuestion
description: Investigate a suspected future leak in a retrodiction trace
argument-hint: [pasted log excerpt showing the suspected leak]
---

# Leak: Investigate a Future Leak in a Retrodiction

**Trace the leak — don't speculate.** Figure out what post-cutoff information the agent had, where it came from, and whether the retrodict guardrails should have caught it.

## Input

**Suspected leak excerpt**: $ARGUMENTS

This is typically a raw fragment of agent reasoning or tool output — not a full trace. It may not contain a post ID, cutoff date, or any metadata. Work with what you have.

## Step 1: Understand what the user is suspicious about

Read the excerpt carefully. What looks wrong? The user pasted this because something jumped out at them — a date that's too recent, a fact that shouldn't be known yet, a tool result that seems too fresh.

State what the suspected leak is in plain language:
> The excerpt mentions [X]. If the cutoff is before [when X became known], this is a leak.

## Step 2: Establish the timeline

You need the **cutoff date** to determine if something is actually a leak. Try these in order:

1. **Extract from the excerpt** — look for dates, `retrodict_cutoff`, `cutoff_date`, `forecast_date` mentions
2. **Find the post ID** — look for `[41987]`, `post_id`, question IDs in URLs, or question titles. If found:
   ```
   Glob(pattern="notes/traces/**/retrodict/<post_id>*/*.json")
   ```
   Read the JSON — the cutoff is in the filename (`YYYY-MM-DD_*.json`).
3. **Search recent retrodict logs** — grep for a distinctive phrase from the excerpt across `logs/`
4. **Ask the user** — if you can't determine the cutoff, ask. Don't proceed without it.

Once you have it:
> Cutoff date: YYYY-MM-DD. Information from after this date should not have been accessible.

## Step 3: Verify the timeline of the suspected information

Before investigating the tool chain, first establish whether this IS a leak:

- **Use `WebSearch`** to find when the information in question actually became publicly available
- **Check publication dates** — a FRED data point labeled "2026-02-13" was released on that date, not before
- **Consider data revision cycles** — economic data gets revised; the initial release may have been before cutoff even if the "last_updated" metadata is after

This step often resolves false alarms. If the information was legitimately available before the cutoff, say so and stop.

## Step 4: Trace how the information entered the agent's context

If the information IS post-cutoff, work backwards to find the source.

**If you have a post ID**, read the trace:
```bash
uv run python .claude/plugins/aib/scripts/trace_log.py show <post_id> --tools-only
```

**If you don't have a post ID**, work from the excerpt itself — the tool name, URL, API response, or reasoning pattern usually reveals the source.

**Common leak vectors to check:**

- **FRED / financial tools** — `last_updated` metadata vs. `observation_end`. Check if `observation_end` was capped to cutoff in `src/aib/tools/financial.py`
- **Web search snippets** — live snippets can contain post-cutoff info even when the page pre-dates the cutoff (dynamic pages). Check if snippets were replaced with Wayback content in `src/aib/tools/retrodict_search.py`
- **Direct URL fetch** — did it go through Wayback (`web.archive.org/web/...`)? In retrodict mode, all fetches must. Check `src/aib/tools/retrodict_search.py` fetch function
- **Wayback snapshot too recent** — the snapshot exists but its timestamp is after the cutoff. Check validation in `src/aib/tools/wayback.py`
- **Sandbox network access** — should be `pypi_only` in retrodict mode. If the sandbox made HTTP requests, check `src/aib/agent/core.py` sandbox config
- **CP history** — data points after cutoff should be filtered. Check `src/aib/tools/forecasting.py`
- **Market data** — prices should be capped to cutoff. Check `src/aib/tools/markets.py`
- **Training data** — the LLM just "knows" the outcome without any tool providing it. The agent states facts without citations, uses post-hoc language, or is suspiciously precise

**Read the relevant source code** once you identify the tool. The retrodict filtering logic is in the tool file — find the line where the cutoff should have been applied and check if this case slipped through.

## Step 5: Report

**What the agent had:** [the post-cutoff information]
**When it actually became available:** [date]
**How it got in:** [which tool / reasoning step, or "LLM parametric knowledge"]
**Why the guardrail missed it:** [specific code gap, or "no guardrail exists for this case"]
**Fix:** [specific file and what to change, or "training data — can't fix, flag for calibration"]

## Rules

- **Never guess.** If you can't trace the leak to a specific source, say so.
- **Quote exactly.** Show the actual tool result or reasoning text that contains the leak.
- **Verify the timeline first.** Many suspected leaks turn out to be false alarms — the information was available pre-cutoff. Check before blaming a tool.
- **Read the source code.** If a tool leaked, read the filtering logic to understand why. Point to the specific line.
- **Ask when stuck.** If the excerpt doesn't have enough context, ask the user for the cutoff date, post ID, or which retrodiction run this came from.

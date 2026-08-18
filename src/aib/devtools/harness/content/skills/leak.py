"""Canonical declaration for the leak skill."""

import lup.harness.models as models

SKILL = models.Skill(
    id="skill.leak",
    name="leak",
    description="Investigate a suspected future leak in a retrodiction trace",
    argument_hint="[pasted log excerpt showing the suspected leak]",
    arguments=[
        models.Argument(
            name="arguments",
            description="A log excerpt showing the suspected leak",
            required=False,
        ),
    ],
    tools=[
        "Read",
        "Grep",
        "Glob",
        "Bash(ls:*, wc:*, sort:*, tail:*, stat:*, uv run lup-devtools:*)",
        "WebSearch",
        "AskUserQuestion",
    ],
    prompt=models.PromptDocument(
        parts=[
            models.TextPart(
                text=r"""# Leak: Investigate a Future Leak in a Retrodiction

**Trace the leak — do not speculate.** Work out what post-cutoff information
the agent had, where it came from, and whether the retrodict guardrails should
have caught it.

## Input

**Suspected leak excerpt**:

"""
            ),
            models.ArgumentsRef(),
            models.TextPart(
                text=r"""

This is typically a raw fragment of agent reasoning or tool output, not a full
trace. It may carry no post ID, cutoff date, or metadata at all. Work with what
you have.

## Step 1: Understand the suspicion

Read the excerpt carefully. Something jumped out — a date that is too recent, a
fact that should not be known yet, a tool result that seems too fresh. State
the suspected leak in plain language:

> The excerpt mentions [X]. If the cutoff is before [when X became known], this
> is a leak.

## Step 2: Establish the timeline

You need the **cutoff date** before anything is a leak. Try these in order:

1. **Extract from the excerpt** — look for dates, or a mention of the cutoff or
   forecast date
2. **Find the post ID** — look for bracketed ids, question ids in URLs, or
   titles. With one in hand, the retrodict forecasts under
   `notes/traces/` carry the cutoff in the filename.
3. **Search recent retrodict logs** — grep a distinctive phrase from the
   excerpt across `logs/`
4. **Ask** — if you cannot determine the cutoff, ask. Do not proceed without
   it.

Once you have it, state it:

> Cutoff date: YYYY-MM-DD. Information from after this date should not have
> been accessible.

## Step 3: Verify the timeline of the suspected information

Before investigating the tool chain, establish whether this IS a leak:

- **Search the web** for when the information actually became publicly
  available
- **Check publication dates** — a data point labelled with a date was released
  on that date, not before
- **Consider revision cycles** — economic data gets revised, so the initial
  release may predate the cutoff even when the last-updated metadata does not

This step often resolves false alarms. If the information was legitimately
available before the cutoff, say so and stop.

## Step 4: Trace how it entered the agent's context

If the information IS post-cutoff, work backwards to the source. With a post ID
you can read the trace:

```bash
uv run lup-devtools trace log <post_id>
```

Without one, work from the excerpt itself — the tool name, URL, API response,
or reasoning pattern usually reveals the source.

**Common leak vectors to check:**

- **Financial series** — last-updated metadata against the observation end.
  Check whether the observation end was capped to the cutoff in
  `src/aib/tools/financial.py`
- **Web search snippets** — live snippets can carry post-cutoff information
  even when the page predates the cutoff. Check whether snippets were replaced
  with archived content in `src/aib/tools/retrodict_search.py`
- **Direct page fetch** — did it go through the archive? In retrodict mode
  every fetch must. Same file.
- **Archive snapshot too recent** — the snapshot exists but its timestamp is
  after the cutoff. Check the validation in `src/aib/tools/wayback.py`
- **Sandbox network access** — should be package-index-only in retrodict mode.
  If the sandbox made other requests, check the sandbox config in
  `src/aib/agent/core.py`
- **Community prediction history** — points after the cutoff should be
  filtered. Check `src/aib/tools/forecasting.py`
- **Market data** — prices should be capped to the cutoff. Check
  `src/aib/tools/markets.py`
- **Training data** — the model simply knows the outcome with no tool providing
  it. The agent states facts without citations, uses post-hoc language, or is
  suspiciously precise.

**Read the relevant source** once you identify the tool. The retrodict
filtering lives in the tool file — find the line where the cutoff should have
applied and check how this case slipped through.

## Step 5: Report

- **What the agent had**: the post-cutoff information
- **When it actually became available**: the date
- **How it got in**: which tool or reasoning step, or parametric knowledge
- **Why the guardrail missed it**: the specific code gap, or that none exists
- **Fix**: the specific file and change, or that training data cannot be fixed
  and should be flagged for calibration

## Rules

- **Never guess.** If you cannot trace the leak to a specific source, say so.
- **Quote exactly.** Show the actual tool result or reasoning text.
- **Verify the timeline first.** Many suspected leaks are false alarms.
- **Read the source.** If a tool leaked, read its filtering logic and point to
  the line.
- **Ask when stuck.** If the excerpt lacks context, ask for the cutoff date,
  post ID, or which retrodiction run it came from.
"""
            ),
        ]
    ),
)

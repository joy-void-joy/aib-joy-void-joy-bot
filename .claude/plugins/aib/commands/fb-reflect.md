---
allowed-tools: Bash(uv run lup-devtools:*), Read, Grep, Glob, Edit, Write, AskUserQuestion
description: Collaborative discussion about findings, process quality, and what to change
---

# Reflect: Collaborative Discussion

This is a conversation, not a checklist. You have the analysis doc and investigation findings. Now discuss what they mean with the user before deciding what to implement.

## How to Run This Phase

Use AskUserQuestion throughout. Share your observations, then ask genuinely — don't present conclusions as questions. The goal is to surface things neither of you would notice alone.

## Discussion Topics

Pick what's relevant from this session's findings. Don't cover everything mechanically.

### What surprised us?

Start here. What in the data was unexpected? Examples:
- A forecast scored much better/worse than the trace suggested
- A tool that "works fine" caused a real forecast error
- The reviewer flagged something (or missed something) interesting
- A version change had unexpected effects

Share the surprise, then ask the user if it matches their intuition.

### What are we not measuring?

Look at what was hard to analyze in this session:
- Did a devtools command fail to surface data we needed? → Fix the command
- Is summary.json missing a field that would have helped? → Restructure the schema
- Did we want to answer a question but couldn't with current tools? → Build the tool

### What assumptions are we making?

Challenge the loop's own assumptions:
- Are we analyzing the right forecasts? (selection bias)
- Is the error taxonomy capturing what actually goes wrong?
- Are the devtools showing us what matters or just what's easy to compute?
- Is the calibration data sufficient to draw conclusions?

### Process quality

Reflect on how this specific session went — not abstractly, but concretely:
- Which phases were useful vs mechanical?
- Where did we waste time?
- What would have made the session more productive?
- Should any subcommand files be updated based on how they were actually used?

## Output

End with a concrete proposal using AskUserQuestion:
- What changes to make (with Bitter Lesson classification)
- What to defer
- What to investigate further next session
- Any process/command changes

## Periodic (every 3rd session)

Reread all `/fb-*` subcommand files and the full forecasting prompt (`src/aib/agent/prompts.py`). Check for accumulated patches, stale guidance, and commands that don't match how they're actually used.

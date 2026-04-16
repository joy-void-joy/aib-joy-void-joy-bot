---
allowed-tools: Bash(uv run aib-devtools:*), Read, AskUserQuestion
description: Queue retrodictions to build calibration data
---

# Retrodict: Queue Next Retrodictions

Find good candidates for retrodiction and output ready-to-use commands.

## Why last

Retrodictions test the improvements made in this session. The cycle: analyze -> improve -> retrodict -> next session collects results.

## Process

### 1. Find candidates

Search broader Metaculus for recently resolved questions that test this session's improvements. Tournament questions (AIB, MiniBench) are always forecast live — retrodiction targets interesting non-tournament questions.

```bash
# Search by topic — target areas where we made improvements
uv run aib-devtools queue search "<topic>" --type <type> --limit 10

# Example searches based on common improvement areas:
uv run aib-devtools queue search "treasury yield" --type numeric
uv run aib-devtools queue search "community prediction" --type binary
uv run aib-devtools queue search "stock price" --type binary
uv run aib-devtools queue search "volatility" --type numeric
```

### 2. Filter

Only suggest questions where R=Y (confirmed resolution). Prefer:
- Questions that directly test this session's changes (e.g., numeric questions with crisis-period resolution for CDF width fixes, meta-predictions at threshold for momentum trap)
- Diverse question types (binary, numeric, discrete)
- Challenging topics (not obviously predictable)
- Sufficient pre-resolution time for meaningful research

### 3. Output

End the analysis doc with the retrodict command, including rationale for why each candidate tests the session's improvements.

## Reference

- Blind mode restricts agent to historical data (WebSearch `before:` filter, Wayback for WebFetch, sandbox network restricted)
- Future-leak detection is handled by the post-session reviewer (summary.json `future_leak` field)
- Known leak vectors: question fine_print sometimes redacted in retrodict; LLM training data leakage is distinct from tool leaks
- Only CLEAN retrodict verdicts count toward calibration

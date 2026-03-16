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

```bash
uv run aib-devtools queue missed aib --days 14
```

### 2. Filter

Only suggest questions where R=Y (confirmed resolution). Prefer:
- Diverse question types (binary, numeric, discrete)
- Challenging topics (not obviously predictable)
- Sufficient pre-resolution time for meaningful research

### 3. Output

End the analysis doc with the retrodict command from `missed` output, including rationale for selection.

## Reference

- Blind mode restricts agent to historical data (WebSearch `before:` filter, Wayback for WebFetch, sandbox network restricted)
- Future-leak detection is handled by the post-session reviewer (summary.json `future_leak` field)
- Known leak vectors: question fine_print sometimes redacted in retrodict; LLM training data leakage is distinct from tool leaks
- Only CLEAN retrodict verdicts count toward calibration

# Feedback Loop Analysis: 2026-02-15 (Session 2)

## Ground Truth Status
- Agent version analyzed: 1.1.0 → 1.2.0
- Resolved forecasts with our predictions: 30 (14 binary, 6 numeric, 10 multiple choice)
- Average Brier score (binary): 0.186 (n=14, best version)
- Binary ECE: 0.2811, bias: underconfident (-0.15)
- Numeric: PIT uniform (K-S p=0.664), 5/6 within 90% CI
- No new resolution data since session 1 (API rate-limited)

## Object-Level Findings

### Finding 1: Resolution Criteria Data Gap (PRIMARY ROOT CAUSE)

The Metaculus API returns `resolution_criteria: null` for ALL Google Trends MC questions. The agent never sees the +/-3 point threshold that defines "Doesn't change." It universally assumes "Doesn't change" requires exact integer equality.

**Trace evidence (all 6 Google Trends MC traces):**
- 41992: "Doesn't change requires the exact same integer value 11 days later — very unlikely given daily volatility"
- 41989: "Staying at exactly the same level is relatively unlikely"
- 42009: "Doesn't change (staying at exactly 5) is the least likely outcome since any small fluctuation would register"

The agent's reasoning is internally consistent — if DC meant exact match, its probabilities would be roughly right. The problem is missing data, not reasoning.

**Investigation path:** The `_enrich_post_json` method in `metaculus/client.py` should fall back to the HTML API to get resolution_criteria, but either:
- The HTML API itself lacks the field for these questions
- For group questions, the enrichment checks `post_json.question` which doesn't exist (data is in `group_of_questions`), causing early return
- Cannot verify due to 429 rate limiting — investigate when API is available

### Finding 2: Agent Has Data But Doesn't Always Compute

When the agent DID compute base rates (helicopter/41992), it produced the best forecast in the set:
- Used `google_trends` with 3 timeframes (3-month, 12-month, 5-year)
- Ran 4 `execute_code` blocks computing change distributions, conditional rates, day-of-week effects
- Result: "Base rate: 56% increase, 39% decrease, 5% unchanged" → gave Increases 65%

When it DIDN'T compute (steve tisch/42009, ilhan omar/42006, thom tillis/41989):
- Used `google_trends` with 1-2 timeframes
- Ran narrative analysis in code ("Decay rate: very fast")
- No base rate computation despite having 91 data points

The google_trends tool returned raw time series but no change statistics. The agent computed stats manually for helicopter but not reliably.

### Finding 3: Retrodict vs Live Paradox

For 42005 (charles victor thompson), the LIVE forecast (DC=87%) was excellent — the agent correctly identified floor constraints (value=1, can't decrease to negative). The retrodict version (DC=38%) was WORSE because it had more data and time, leading to "narrative overthinking."

For 41992 (helicopter), the retrodict run 2 (Increases=65%) was the best forecast, but earlier runs and the live submission (Decreases=45%) were worse. The "which run gets submitted" problem: retries don't guarantee the best analysis ships.

### Tool Failures
| Tool | Failure | Count | Fix |
|------|---------|-------|-----|
| resolution_criteria | Always null from API | 6/6 MC | Investigate enrichment pipeline (Priority 1) |
| web_search | Empty results (retrodict) | 2/6 | Expected in retrodict mode |
| google_trends_related | API error | 1/6 | Intermittent pytrends issue |

### Agent Capability Requests (Implicit)
- Agent searched for resolution criteria in notes: `notes(search, "Google Trends resolution criteria")` → 0 results
- Agent reasoning: "Without explicit resolution criteria, I need to think about what 'change' means" (5/6 traces)
- Agent tried hard to find the threshold definition and failed — this is the data gap

### Reasoning Quality Assessment
- **42014 (Brier 0.029)**: Best binary. CP 4pp above threshold with 151 forecasters. High-confidence call.
- **42005 (DC=87%, log_score=0.14)**: Best MC. Floor constraint reasoning correct.
- **41992 retrodict r2 (Increases=65%)**: Best MC analysis. Full quantitative pipeline.
- **42009 (DC=20%, resolved DC)**: Worst MC. Narrative decay reasoning overrode floor effects.
- **39935/41387 (Brier 0.36/0.42)**: Old meta retrodicts, still underconfident on YES.

### Future-Leak Analysis
All 8 retrodict traces: **CLEAN**. No evidence of future information leakage. Agent consistently operated within retrodict date boundary.

## Changes Made
| Level | Change | Rationale |
|-------|--------|-----------|
| Object (tool) | Add `change_stats` to google_trends output | Agent had data but didn't compute base rates reliably. Now sees period-over-period change counts/rates automatically. |
| Object (prompt) | Add MC guidance: DC resolution semantics, post-spike baseline behavior | Agent assumed DC=exact integer match. Guidance explains noise tolerance at low values and post-spike baseline stability. |
| Object (version) | Bump 1.1.0 → 1.2.0 | Minor: tool modification + prompt change |

## Meta-Level Findings
- **Critical data gap**: resolution_criteria null for all Google Trends questions. Must investigate enrichment pipeline when API available.
- **Calibration limited**: n=9 binary for calibration, too few to distinguish systematic bias from sample noise.
- **Retry mechanism**: "Take last result" policy means best analysis doesn't always ship (42005 live > retrodict, 41992 r2 > r1).

## Meta-Meta Findings
- **Trace explorer report quality**: Excellent this session. The data-focused prompt ("what DATA did the agent have vs need") produced actionable findings.
- **feedback-loop command**: Guidance to "not patch prompts" should be nuanced — prompt changes about resolution semantics ARE legitimate when the data pipeline can't deliver the information. The key is: patch for recurring factual details (resolution semantics), not for reasoning patterns.

## Retrodiction Queue

API is 429'd — no retrodict-ready questions available. When rate limits clear:

### Priority 1: Test v1.2.0 on Google Trends MC
Queue Google Trends MC questions to validate whether change_stats + prompt guidance improves DC weighting.
```bash
# Search for resolved Google Trends MC when API is available
uv run python .claude/plugins/aib/scripts/forecast_queue.py search "google trends" --resolved --limit 20
```

### Priority 2: Non-meta binary diversity
Current binary calibration is 11/14 meta questions. Need non-meta binary retrodictions.
```bash
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 21
```

### Priority 3: Resolution criteria investigation
When API is available, test whether `fetch_post_json` returns resolution_criteria for Google Trends MC questions (especially group question handling).
```bash
uv run python .claude/plugins/aib/scripts/test_question_endpoint.py 42009 --verbose
```

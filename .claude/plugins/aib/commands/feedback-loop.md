---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, Task, WebSearch, AskUserQuestion
description: Analyze forecasts and improve agent based on calibration and process quality
argument-hint: [post_id1 post_id2 ...] (optional — scope analysis to specific forecasts)
---

# Feedback Loop: Three Levels of Analysis

The feedback loop operates at three levels. Be clear about which level you're working at:

1. **Object Level** - The forecasting agent itself: tools, capabilities, data access, runtime behavior
2. **Meta Level** - The agent's self-assessment: meta-prompts, reflection templates, metrics emission, what the agent tracks about itself
3. **Meta-Meta Level** - This feedback loop process: the scripts, the analysis methods, this document itself

**Clarification**:
- Object level = "How can the agent forecast better?" (tools, APIs, reasoning)
- Meta level = "How can the agent track its own performance better?" (meta-reflection prompts, metrics formats, what the agent writes to notes/traces/<version>/sessions/)
- Meta-meta level = "How can this feedback loop command work better?" (aib-devtools feedback, this document, analysis workflows)

**Examples**:
- Object: Add a new stock_price tool, fix a failing API
- Meta: Update the meta-reflection prompt template, add new tracking fields to forecast JSON
- Meta-meta: Create a script to automate analysis, clarify confusing parts of this document

**IMPORTANT: Every feedback loop session should span all three levels thoroughly.**

Don't stop after finding object-level improvements. Ask yourself:
- Did I check if the agent's self-tracking is sufficient? (meta)
- Did I update this document with what I learned? (meta-meta)
- Are there scripts that would make next session easier? (meta-meta)

A good feedback loop session produces changes at multiple levels. If you only made object-level changes, you probably skipped the reflection phases.

## Input

**Post IDs**: $ARGUMENTS

If post IDs are provided, use them directly — skip discovery.

If none provided, discover automatically:
```bash
uv run aib-devtools scores extremes --non-meta
uv run aib-devtools scores extremes --meta-only
```

## Critical Constraint: What the Agent Can and Cannot See

**IMPORTANT**: The forecasting agent operates in the AIB tournament where:

- **Agent CAN see**: Prediction market prices (Polymarket, Manifold), underlying question CP (for meta-questions), news, APIs
- **Agent CANNOT see**: The CP of the question it is currently forecasting

This means:
- For meta-questions like "Will CP of Q be above X%?", the agent CAN see Q's current CP
- But the agent CANNOT see the meta-question's own CP

**Implication for feedback loop**: You can use CP divergence for post-hoc analysis to understand WHERE our reasoning differs from the crowd. But you CANNOT tell the agent to "adjust based on CP divergence" because it can't see that data during forecasting.

## Guiding Principle: The Bitter Lesson

Give the agent MORE capabilities and tools rather than MORE prescriptive rules.

| Prefer | Over |
|--------|------|
| Tools that provide data | Prompt rules that constrain behavior |
| General principles | Specific pattern patches |
| State/context via tools | F-string prompt engineering |
| Subagents for specialized work | Complex pipelines in main agent |

**The test**: Would this change still help if the question domain shifted completely? General principles yes, specific patches no.

**Clarification**: The bitter lesson does NOT mean never modifying prompts. It's fine to add:
- General guidance for categories of questions (e.g., "for meta-predictions, consider the underlying question's CP trajectory")
- Principles that help reasoning (e.g., "numeric questions require 201-point CDFs")
- Structural guidance (e.g., "check prediction markets for event questions")

What to AVOID:
- Specific numeric patches ("subtract 0.5 logits for definitional questions")
- Rules that hard-code observations from specific questions
- Prescriptive formulas that will become outdated

Keep the system prompt fresh - periodically review and remove guidance that no longer applies. Old prompt rules can sediment into an outdated system.

## Offline Mode

When the Metaculus API is rate-limited (429), skip all API-calling scripts. In offline mode:

1. **Skip** `aib-devtools feedback collect` (hits the authenticated DRF API) and `aib-devtools resolution check` (uses Playwright to scrape profile page)
2. **Ask the user** if they want to run `aib-devtools fetch-resolutions fetch` — it uses the unauthenticated `/api2/` endpoint with separate rate limits and may still work
3. **Use cached data**: `feedback_state.json` (CP cache), `data/api_cache/` (resolution cache)
4. **All analysis scripts work offline**: `aib-devtools calibration`, `aib-devtools scores`, `aib-devtools trace`, trace-explorer

## Phase 0: Read Previous Analysis

**Before collecting any data, read what was already done.** This prevents double-fixing.

```bash
# Check what the last session found and changed
ls notes/feedback_loop/$(git branch --show-current)/
cat notes/feedback_loop/$(git branch --show-current)/*_analysis.md | tail -50
```

Read the most recent `*_analysis.md` file. Understand:
- What problems were already identified and fixed
- What retrodictions were already analyzed
- What changes were already made

The `feedback_state.json` tracks which items have been analyzed. The `--new-only` flag (default) automatically filters these out.

## Phase 1: Discovery & Resolution

The ONLY true ground truth is **resolution outcomes**. Everything else is proxy signal.

### 1a. Overview

```bash
grep AGENT_VERSION src/aib/version.py
uv run aib-devtools resolution check
uv run aib-devtools resolution resolve --all  # expand tentative AI resolutions
uv run aib-devtools scores show <post_id1> <post_id2> ...
```

**Tentative AI resolutions count as ground truth for calibration.** The `resolution resolve --all`
command uses AI agents to check resolution criteria and populate resolution values for questions
that Metaculus hasn't officially resolved yet. These are stored with `resolution_source: "tentative"`
and are included in all calibration and scoring pipelines. Run this early to maximize calibration data.

Group posts by version, type, and resolution status.

### 1b. Resolution Investigation

For each **resolved** post, investigate what actually happened. Use the data sources relevant to the question (Google Trends, FRED, stock APIs, web search) to build first-hand understanding — don't just read the resolution value.

- How did the underlying data evolve before, during, and after the forecast period?
- Was the outcome predictable from data available at forecast time, or was there a genuine surprise?
- At what point did the outcome become clear?

Classify each resolved forecast:

| Error Type | Description |
|---|---|
| **Good forecast** | Well-calibrated given available information |
| **Wrong base rate** | Bad prior, missed relevant reference classes |
| **Missed key data** | A data source existed but wasn't found or used |
| **Stale data** | Used outdated information when fresher data existed |
| **Misunderstood scope** | Misinterpreted question criteria or resolution conditions |
| **Overconfident CDF** | Directionally correct but tails too narrow |
| **Underconfident CDF** | Directionally correct but distribution too diffuse |
| **Directionally wrong** | Forecast pointed the wrong way entirely |
| **Timing error** | Right prediction, wrong timeframe |

For each error, ground the counterfactual:
- "The data showed [trajectory] — querying [source] at forecast time would have shown [signal]"
- "The outcome was a genuine surprise — [data] shifted after [event], post-forecast"

Carry these findings into Phase 2 — the trace explorer needs this context.

### 1c. Calibration (Aggregate View)

Run calibration **after** individual investigation, not before. Use it to confirm or challenge patterns found in 1b.

```bash
uv run aib-devtools calibration summary --version <version>
```

If you find a systematic pattern (e.g., all numeric CDFs too narrow), verify it against the individual cases from 1b — don't take the aggregate at face value.

### 1d. Retrodict Missed Questions (and Check Airtightness)

If questions resolved before we forecast them, **retrodict** them to build calibration data. Blind mode restricts all tools to data that was available before the question resolved, ensuring the agent cannot "cheat" by looking up the answer.

```bash
# Check which questions we missed (validates resolution + shows CP status)
uv run aib-devtools queue missed aib --days 14

# Use --all to see questions without confirmed resolution too
uv run aib-devtools queue missed aib --days 14 --all

# Retrodict with blind mode (default - recommended)
# ONLY retrodict questions where the missed command shows R=Y
uv run forecast retrodict 41835 41521 41517

# Retrodict with a specific cutoff date
uv run forecast retrodict 41835 --forecast-date 2026-01-15

# Non-blind mode (for testing/debugging only)
uv run forecast retrodict 41835 --no-blind
```

**How blind mode works:**
- **WebSearch**: Appends `before:YYYY-MM-DD` to all queries
- **WebFetch**: Rewrites URLs to Wayback Machine (`web.archive.org/web/{timestamp}id_/{url}`)
- **Sandbox**: Network restricted to PyPI only - agent can install packages but cannot make arbitrary HTTP requests
- **Financial tools**: Caps `end_date` parameters to the forecast date
- **Live-only tools**: Blocked with hints to use historical alternatives (e.g., `stock_price` → `stock_history`)
- **CP history**: Filters response to exclude data after the cutoff
- **CP visibility**: Only hides CP for the forecasted question (not underlying questions in meta-predictions)
- **Fine print**: Redacted via haiku to remove post-cutoff temporal references

The agent forecasts as if it were making the prediction at the original question date, using only information that was available at that time.

**Data scarcity in blind mode**: Retrodict systematically has less data than live forecasting. Wayback Machine coverage is spotty (many pages uncached), date-restricted web searches return far fewer results, live-only tools (prediction markets, real-time APIs) are blocked entirely, and sandbox network access is PyPI-only. This means retrodict scores are expected to be worse than live scores for the same agent version — the gap reflects data availability, not reasoning quality. When comparing new retrodicts against old live forecasts, account for this baseline disadvantage before attributing score differences to agent changes.

**What retrodict outputs:**
- Saves forecasts to `notes/traces/<version>/retrodict/<post_id>/<forecast_date>_<timestamp>.json`
- The `retrodict_date` field in the JSON records the cutoff date used
- Filename includes the cutoff date for easy identification
- Shows actual resolution and final CP for comparison
- Computes Brier scores for binary questions

**Pulling resolution data:**

Use `aib-devtools scores scrape` to pull resolutions, peer scores, and baseline scores into forecast JSONs from the Metaculus profile page.

**Retrodict vs Live forecasts:**
- Live forecasts go to `notes/traces/<version>/forecasts/`
- Retrodicted forecasts go to `notes/traces/<version>/retrodict/` (separate folder)
- This prevents mixing calibration data with real predictions

#### Future-Leak Detection

After running retrodict, review traces for signs that the agent accessed post-resolution information.

**The trace-explorer handles this automatically.** When you include retrodict post IDs in the trace-explorer prompt (Phase 2a), it auto-detects retrodict traces and runs future-leak checks, returning a per-trace verdict (CLEAN/SUSPECT/LEAKED) in the "Future-Leak Analysis" section of its report.

**If the trace-explorer flags a leak:**
1. The forecast is invalid for calibration
2. Identify which tool allowed the leak
3. Report the gap — retrodict hooks need fixing
4. Exclude from Brier score calculations

**Known leak vectors (mitigated in v0.8.0):**
- **Question fine_print**: `get_metaculus_questions` redacts fine_print via haiku to remove post-cutoff temporal references. Example: Q40971's fine_print contained an OPM archive from Jan 31 that leaked the government shutdown outcome. Haiku redaction removes such references but may not catch all cases — still check manually.

**LLM training data leakage (distinct from tool leaks):**

Tool-level sandboxing prevents the agent from *fetching* future data, but the LLM's training data may contain knowledge of past outcomes. This is especially dangerous for retrodicting questions about well-known historical events (elections, economic crises, wars). Signs of training data leakage:
- Subagent reasoning that states the actual outcome without citing a source
- Suspiciously precise forecasts on events with clear historical outcomes
- Analyst subagent "reasoning" that mirrors post-hoc narratives

**Mitigation:** For historical retrodictions (pre-training-cutoff), the forecast is still useful if the *main agent's* reasoning chain doesn't reference the outcome. Subagent leaks can be tolerated if the main agent's probability reflects genuine uncertainty. However, flag these in the analysis so calibration data isn't contaminated.

**Expected behavior in proper retrodict:**
- Agent uses historical data and base rates
- Uncertainty reflects what was knowable at `forecast_date`
- No mentions of resolution or what "actually happened"

### 1e. Collect and Analyze Retrodiction Results

Retrodictions are our **best** calibration signal — they have known resolutions by definition. After running retrodictions (1b) and checking for future leaks, incorporate them into analysis.

**Collect retrodiction data:**
```bash
# List all retrodictions
ls notes/traces/*/retrodict/*/

# Summarize retrodiction accuracy (uses known resolutions embedded in the JSON)
uv run aib-devtools feedback collect --include-retrodict
```

**For each retrodiction, evaluate:**
1. **Accuracy**: Compare forecast vs actual resolution (Brier score for binary, error for numeric)
2. **Airtightness**: Did the agent access post-resolution information? (see Future-Leak Detection above)
3. **Reasoning quality**: Read the session trace — was the reasoning sound given only pre-resolution data?
4. **Tool effectiveness**: Which tools worked under blind-mode constraints? Which failed?
5. **Calibration contribution**: After collecting retrodictions, run `uv run aib-devtools calibration summary` to see how new data points shift ECE and bucket-level gaps.

**Airtightness**: The trace-explorer checks all of the following automatically for retrodict traces and assigns CLEAN/SUSPECT/LEAKED verdicts. Only trust retrodictions with CLEAN verdicts for calibration.

**If a retrodiction fails airtightness**: Exclude it from calibration data and file a bug against the retrodict hooks.

**Note**: `uv run aib-devtools feedback collect --include-retrodict` processes both `notes/traces/<version>/forecasts/` and `notes/traces/<version>/retrodict/`.

### 1f. About Community Prediction

CP is just another forecaster. Diverging from CP is not inherently bad - we WANT an edge.

**Correct framing**:
- If our reasoning is sound and we have better information, divergence is GOOD
- If divergence correlates with poor Brier scores after resolution, THEN investigate
- Do NOT treat "matching CP" as a goal

**When CP divergence is useful**:
- Understanding WHERE our reasoning differs (not WHETHER we're wrong)
- After resolution, checking if divergence predicted error

**When CP divergence is misleading**:
- As a primary signal without resolution data
- When the agent has information CP lacks (breaking news, specific API data)

### Phase 1 Gate (MANDATORY)

Before proceeding to trace analysis, use **AskUserQuestion** to present:

1. **Per-forecast post-mortem table** (Post ID, Version, Type, Forecast, Resolution, Score, Error Type)
2. **Error classification summary** — how many of each type?
3. **Calibration headline** — ECE, coverage, any systematic patterns
4. **Key counterfactuals** — for the 3 worst forecasts, what data would have helped?

Options: "Proceed to trace analysis" / "Dig deeper on specific posts" / "Skip to implementation (only if no resolved forecasts)"

**Do NOT continue until the user confirms.** This forces you to synthesize Phase 1 findings before moving on. If you can't fill out the post-mortem table, Phase 1 isn't done.

## Phase 2: Trace Analysis

**This is the most important phase.** Do not skip to aggregate patterns.

**Do NOT read traces directly in this conversation.** Traces consume ~1160 lines each and will
exhaust the context window before you reach later phases. Instead, launch the `trace-explorer`
subagent which reads traces in its own context and returns a compact pattern report.

### Version Scoping

All devtools commands **default to the current AGENT_VERSION** with progressive semver
fallback (exact → X.Y.* → X.* → all) when the current version has insufficient data.
You do NOT need to manually pass `--version` — commands auto-scope.

**For learning phases** that need resolved outcomes from older versions, use `--all-versions`:
```bash
uv run aib-devtools calibration summary --all-versions
uv run aib-devtools scores extremes --all-versions
```

**For version-to-version comparisons:**
```bash
uv run aib-devtools scores compare 2.0.0 3.0.0
```

### 2a. Launch Trace Explorer (Subagent)

Pass the resolution investigation from Phase 1b so the explorer has context about what actually happened.

```
Task(subagent_type="aib-workflow:trace-explorer", prompt="""
Analyze traces for these post IDs: [list]

Context:
- Version grouping: [from 1a]
- Resolution findings: [from 1b — error classifications and counterfactuals]
- Calibration patterns: [from 1c, if any]

Return the standard pattern report.
""")
```

**What to include in the prompt:**
- Post IDs to analyze (from extremes, or all recent forecasts)
- Current agent version (so the explorer can filter)
- Resolution investigation results from Phase 1b (error classifications, counterfactuals)
- Any specific focus areas from Phase 1c calibration findings
- Known issues from the previous feedback session (Phase 0)

**What you get back:**
- Tool failure patterns (aggregated across all traces)
- Capability requests (what the agent asked for)
- Reasoning patterns and quality issues
- Tool usage patterns (high-value vs low-value tools)
- **Future-leak analysis** — per-trace CLEAN/SUSPECT/LEAKED verdicts for any retrodict traces (auto-detected, no extra prompt needed)
- 2-3 specific traces worth reading in full (outliers or interesting cases)

**Other subagents for deeper analysis:**

- **Version reviewer**: For a holistic assessment of a single past version (especially before prompt rewrites), use:
  ```
  Task(subagent_type="aib-workflow:version-reviewer", prompt="Review version [X.Y.Z]")
  ```
- **Version explorer**: For quick file retrieval and diffs across versions (e.g., "fetch me the prompt at v0.3" or "compare v0.3 and v0.9 prompts"):
  ```
  Task(subagent_type="aib-workflow:version-explorer", prompt="Compare v0.3.1 and v0.9.2")
  ```

The trace explorer finds cross-cutting patterns; the version reviewer explains why those patterns exist by connecting them to the prompt; the version explorer retrieves and diffs the actual code. You can run all three — they serve complementary purposes.

### 2b. Deep-Dive on Flagged Traces (Optional)

The trace explorer flags 2-3 traces worth reading fully. **Only read these if the pattern
report raises specific questions** that need full-trace context to answer.

If you do read a trace, use `uv run aib-devtools trace log <id>` (NOT raw logs) and read it with a
specific question in mind — don't just browse.

### 2c. Evaluate Findings

Based on the trace explorer's pattern report:

1. **Tool failures**: Which tools fail most? Are they fixable or should we add alternatives?
2. **Capability requests**: What does the agent say it needs? Trust these requests.
3. **Reasoning quality**: Are there systematic reasoning errors, or just individual misjudgments?
4. **Tool value**: Are expensive tools (sandbox, web search) providing proportional value?

**If reasoning is sound but diverges from CP**: May be an edge. Wait for resolution.
**If reasoning is systematically flawed**: Identify whether it's a capability gap or a prompt issue.

## Phase 3: Meta Level - Analysis Process Quality

Evaluate whether this feedback loop is finding the right things to improve.

### 3a. Did the Analysis Surface Actionable Insights?

Ask yourself:
- Did I find specific tools to fix or build?
- Did I identify concrete capability gaps?
- Did the analysis lead to clear next steps?

If the analysis felt circular or unproductive, the meta-process needs improvement.

### 3b. Evaluate Tracking Data Quality

Check if the data we collect is sufficient for analysis:
- Are forecasts linked to their reasoning traces?
- Can we correlate tool usage with forecast quality?
- Do we have resolution data to evaluate accuracy?

```bash
# Check what tracking data we have
uv run aib-devtools trace list
```

### 3c. Identify Missing Data

Common gaps:
- **No resolution data** → Can't evaluate accuracy, only process
- **No tool-to-forecast linkage** → Can't identify which tools help
- **No question type tagging** → Can't identify patterns by category

If you find gaps, add tracking in Phase 4.

### Phase 2+3 Gate (MANDATORY)

Before implementing anything, use **AskUserQuestion** to present:

1. **Tool failure summary** — which tools fail, how often, is it fixable?
2. **Capability requests** — what the agent says it needs (quote directly)
3. **Reasoning quality verdict** — systematic errors or individual misjudgments?
4. **What's already been fixed** — cross-reference with Phase 0 findings
5. **What remains unaddressed** — prioritized list
6. **Meta-level assessment** — is the agent tracking its own performance well enough?
7. **Proposed changes** — ranked by priority, with Bitter Lesson classification (tool/capability/principle)

Options: "Proceed with proposed changes" / "Adjust priorities" / "Need deeper investigation on [topic]"

**Do NOT implement changes until the user approves the priority list.** This prevents rushing to implementation with shallow analysis. If the "What's already been fixed" section is empty, you skipped Phase 0.

## Phase 4: Implement Changes (Bitter Lesson Order)

**Do NOT edit `version.py` manually.** Use `uv run aib-devtools version bump <patch|minor|major> "<summary>"` -- pick the right level based on the scope of changes (see Version Bumps below).

**Log every change** in the analysis document (see Documentation Template). The next feedback session reads this to avoid re-deriving the same improvements. Be specific: "Added X to Y because Z" — not just "improved prompts."

### Priority 0: Evaluate Prompt Health

Before patching individual issues, assess whether the system prompt needs a structural
rewrite rather than another incremental patch.

**When to rewrite vs patch:**

A full rewrite is warranted when:
- Sections read as addendums rather than integrated guidance (conditional exceptions, "if X fails, do Y" patches)
- The same question type (meta-predictions, numeric) has been patched 3+ times across sessions
- Best-performing traces succeed despite the prompt, not because of it
- Worst-performing traces fail because the prompt's decision tree doesn't match how the agent should think
- The prompt has grown >20% since the last rewrite without corresponding accuracy improvement

**How to do a principled rewrite:**
1. **Study the best-performing traces.** Use `uv run aib-devtools scores show --resolved` and `uv run aib-devtools trace log <id>` to read the full reasoning for the top 5-10 forecasts by Brier score. What patterns do they follow? What decisions led to success?
2. **Study the worst-performing traces.** Same process for the bottom 5-10. What went wrong — capability gap or reasoning error the prompt could have prevented?
3. **Read the full current prompt** (`src/aib/agent/prompts.py`). Identify sections that feel patched, redundant, or irrelevant. Look for conditional exceptions that accumulated over time.
4. **Draft from scratch.** Write the prompt as you would if starting today with all accumulated knowledge. Don't copy-paste from the old prompt — rewrite each section from first principles, incorporating the patterns from best traces.
5. **Ensure monolithic coherence.** The result must read as a single authored document — no references to "previous behavior," no "Exception:" patches, no "Note: as of version X."

**When NOT to rewrite:**
- If you found only 1-2 clear bugs or gaps, a targeted patch is better
- If the prompt's structure is sound and only needs a new principle or tool reference
- If there isn't enough calibration data (< 20 resolved forecasts) to identify structural issues

### Priority 1: Fix Failing Tools

If a tool fails repeatedly, fix it or add an alternative.

```bash
# Example: Wikipedia 403 errors
# → Check if redirects param is set
# → Add error handling and fallback
```

### Priority 2: Build Requested Tools

What did the agent explicitly request? **Don't just build—discuss with the user first.**

For each capability gap found in meta-reflections:

1. **Quantify**: How many questions mentioned this need? (grep the meta-reflections)
2. **Research**: What APIs or approaches exist? What would implementation look like?
3. **Ask the user**: Use `AskUserQuestion` to present:
   - The capability gap and how many questions it affected
   - Concrete implementation options (APIs, costs, complexity)
   - Your recommendation and why

**Example discussion format:**
> "The agent requested X in 7 meta-reflections. Options:
> - Option A: Use [API] (~$X/mo, handles Y)
> - Option B: Build custom tool with [approach]
> - Option C: Skip—agent worked around it with [alternative]
>
> I recommend [X] because [reason]. What do you think?"

This ensures tool decisions are collaborative and the user understands the tradeoffs.

### Priority 3: Improve Subagents

If subagents aren't used:
- Are they providing unique value?
- Are they too expensive (time/compute)?
- Should they be lighter/faster?

### Priority 4: Simplify Prompts (Not Add Rules)

For incremental prompt changes (when Priority 0 determined a full rewrite isn't needed):
- ADD general principles that help across domains
- REMOVE prescriptive rules that add complexity
- PREFER "use tool X for Y" over "when pattern P, do Q"

**Do NOT add**:
- Specific rules for specific question types
- Numeric adjustments ("subtract 0.5 logits when...")
- Patches for observed patterns
- Conditional exceptions that reference specific failure modes

**Track patch count.** If you add a patch this session, count how many patches have been
added since the last rewrite. If the count exceeds 3, flag it in your analysis — the next
session should evaluate a full rewrite (Priority 0).

### Version Bumps

After implementing changes that affect agent behavior, **always bump the version** at the appropriate level using the bump script:

```bash
uv run aib-devtools version bump <level> "<summary>" [--detail "a, b, c"]
```

- **Patch (0.x.Y)**: Bug fixes, tool fixes, config tweaks. Default when unsure.
- **Minor (0.X.0)**: Small prompt changes, new tools, subagent modifications.
- **Major (X.0.0)**: Architecture changes (new LLM, new framework, major restructuring).

Data-only or infrastructure changes (scripts, feedback-loop docs) don't need a bump.

### Phase 4 Verification (MANDATORY)

After listing changes in the analysis document, **verify each one actually exists**:

```bash
git diff --stat
git diff --name-only
```

For each change in your "Changes Made" table:
- If `git diff` shows the file was modified → mark as **COMMITTED** (or STAGED)
- If `git diff` shows nothing → mark as **PROPOSED** (not yet implemented)
- If the change was a prompt/tool fix, grep for the specific text you added to confirm it's there

**Never mark a change as DONE/COMMITTED without verifying it in the diff.** The previous session listed 3 changes as "made" that were never committed — this verification step prevents that.

## Phase 5: Meta-Meta Level - Improve This Document

This phase is about improving the feedback loop infrastructure itself.

### 5a. Was This Document Helpful?

Ask:
- Did the phases guide you to useful insights?
- Was any guidance outdated or confusing?
- Did you have to improvise steps not documented here?

If yes to any, update this document NOW before you forget.

### 5b. Build Missing Scripts

If you found yourself doing repetitive analysis, automate it:

```bash
# Commands that already exist:
uv run aib-devtools feedback collect --help
uv run aib-devtools trace --help
uv run aib-devtools calibration --help
```

If you need a command that doesn't exist, add it to `src/aib/devtools/` and document it in CLAUDE.md.

### 5c. Improve Data Collection

If the feedback loop lacked data, fix the source:
- Add fields to forecast JSON schema
- Update the agent to emit more tracking data
- Add scripts to collect missing metrics

### 5d. Update This Document

Every session should leave this document better:
- Remove outdated guidance
- Add new commands to the "Commands Available" section
- Clarify confusing terminology
- Add examples from actual analysis

**Note**: This feedback loop data is now saved to `notes/feedback_loop/<branch_name>/` to keep different worktrees organized.

## Anti-Patterns to Avoid

### DON'T: Patch prompts for observed patterns
❌ "When forecasting meta-predictions, subtract 0.5 logits"
❌ "For definitional questions, cap confidence at 70%"
❌ Adding "Exception:" clauses to existing rules
❌ "If X fails, do Y" conditional patches
✅ Build tool that provides historical calibration data
✅ Add general principle about interpretation uncertainty
✅ When patches accumulate, rewrite the section from scratch (Priority 0)

### DON'T: Over-rely on CP divergence
❌ "Large CP divergence means we're wrong"
❌ "Tell agent to trust CP when divergence > 20pp"
✅ Wait for resolution data to know if divergence correlates with error
✅ Use CP divergence to understand WHERE reasoning differs, not WHETHER it's wrong

### DON'T: Add rules the agent can't act on
❌ "Adjust based on the meta-question's CP" (agent can't see this)
✅ Provide tools that give the agent actionable information

### DON'T: Skip reading traces
❌ Jump to aggregate statistics (average divergence)
✅ Read 5-10 meta-reflections deeply first
✅ Understand what actually happened in individual forecasts

## Documentation Template

Write to `notes/feedback_loop/<branch_name>/<timestamp>_analysis.md`:

The `aib-devtools feedback collect` command automatically organizes data by branch. When writing analysis, use the same structure:

```markdown
# Feedback Loop Analysis: YYYY-MM-DD

## Ground Truth Status
- Agent version analyzed: X.Y.Z
- Resolved forecasts with our predictions: N
- Average Brier score: X.XX (or "none yet - process analysis only")

## Per-Forecast Post-Mortem

| Post ID | Version | Type | Forecast | Resolution | Score | Error Type |
|---------|---------|------|----------|------------|-------|------------|

### Post [ID]: [question title]
- **Forecast**: [prediction]
- **Resolution**: [actual outcome]
- **Error type**: [classification from Phase 1b]
- **What happened**: [1-2 sentences — what data/event determined the resolution]
- **Where reasoning diverged**: [specific trace point, or "N/A — good forecast"]
- **What would have helped**: [concrete tool, data source, or reasoning direction]

## Object-Level Findings

### Tool Failures
| Tool | Failure | Count | Fix |
|------|---------|-------|-----|
| WebFetch | 403 on site X | N | Add X API tool |

### Agent Capability Requests
- "Would benefit from X" → [action taken]
- "Tool Y failed" → [action taken]

### Reasoning Quality Assessment
- [For 3-5 forecasts, brief assessment of reasoning soundness]

## Meta-Level Findings (Analysis Process)

### Was This Analysis Productive?
- Did it surface actionable insights? [yes/no]
- What data was missing?
- What would have made analysis easier?

## Meta-Meta Findings (Feedback Loop Infrastructure)

### Updates to This Document
- [Changes made to feedback-loop.md]

### Commands Created/Updated
- [New commands added to src/aib/devtools/]

### Data Collection Improvements
- [Changes to forecast tracking, metrics, etc.]

## Changes Made
| Level | Change | Status | Rationale |
|-------|--------|--------|-----------|
| Object | Added X tool | COMMITTED | Agent requested it in N meta-reflections |
| Meta | Improved analysis queries | PROPOSED | Was missing Y data |
| Meta-Meta | Updated feedback-loop.md | COMMITTED | Clarified Z section |

Status must be one of: **COMMITTED** (verified in git diff), **PROPOSED** (not yet implemented), **DEFERRED** (for next session).

## Retrodiction Queue
uv run forecast retrodict <ids>
```

## Commands Available

```bash
# Scores for specific posts (positional args or --post-id)
uv run aib-devtools scores show 42408 42380 42400
uv run aib-devtools scores show --resolved

# Best/worst forecasts (for deep trace reading)
uv run aib-devtools scores extremes
uv run aib-devtools scores extremes --non-meta
uv run aib-devtools scores extremes --meta-only

# Version comparison
uv run aib-devtools scores compare 3.4.0 3.5.0

# Check resolutions (scrapes profile page)
uv run aib-devtools resolution check

# Feedback collection (resolutions + CP + Brier scores)
uv run aib-devtools feedback collect --include-retrodict
uv run aib-devtools feedback collect --all-time --no-new-only --include-retrodict

# Check missed questions for retrodiction
uv run aib-devtools queue missed aib --days 14

# Retrodict resolved questions (blind mode - restricts to historical data)
uv run forecast retrodict 41835 41521 41517
uv run forecast retrodict 41835 --forecast-date 2026-01-15
uv run forecast retrodict 41835 --no-blind  # debugging only

# Trace a forecast
uv run aib-devtools trace show 41906
uv run aib-devtools trace log 41906

# Calibration analysis (ECE, reliability diagrams, PIT)
uv run aib-devtools calibration summary --version 3.5.0
uv run aib-devtools calibration binary --version 3.5.0
uv run aib-devtools calibration numeric --version 3.5.0

# Aggregate metrics
uv run aib-devtools metrics summary
```

## Periodic Maintenance

Every few feedback loop sessions, take time to:

1. **Reread this entire document** - Is it still accurate? Remove outdated guidance.
2. **Prompt health audit** - Read the entire system prompt (`src/aib/agent/prompts.py`) with fresh eyes. Does it read as a coherent, monolithic document? Are there visible patches? Would a new reader understand the decision tree? If not, trigger a rewrite (Phase 4, Priority 0).
3. **Refactor devtools** - Consolidate duplicate functionality, improve error handling.
4. **Clean up notes/** - Archive old analysis files, ensure naming is consistent.
5. **Update CLAUDE.md** - Sync any learnings that should persist to the main project docs.

## Key Questions to Answer Each Session

1. **What AGENT_VERSION am I analyzing?** Filter ALL data by version. Pass `--version` to every command. Do not mix versions.
2. **Do we have resolution data?** If no, focus on process not accuracy. Check HTML enrichment status (may return 406).
3. **How is calibration FOR THIS VERSION?** Run `uv run aib-devtools calibration summary --version X.Y.Z`. Compare to previous version with `uv run aib-devtools scores compare`.
4. **What tools fail repeatedly?** Fix or replace them.
5. **What tools go unused?** Check traces for tools/subagents that were available but never called.
6. **Is the subagent structure coherent?** Are subagents well-scoped and well-used?
7. **What does the agent say it needs?** Trust and provide.
8. **Is the agent's reasoning sound?** Read traces deeply to find out.
9. **Are retrodictions airtight?** Check for future leaks in reasoning (LLM training data, post-cutoff references).
10. **Is the prompt accumulating patches?** Count conditional exceptions and "if X fails" clauses added in recent sessions. If >3 patches since last rewrite, evaluate a structural rewrite (Phase 4, Priority 0).
11. **What would make this process better?** Update this document.

## Phase 6: Queue Retrodictions

**This is the final output of every feedback loop session.** After all analysis and changes are complete, propose retrodictions for the user to run before the next session.

### Why This Is Last

Retrodictions build calibration data. Each feedback loop session should:
1. Analyze existing retrodictions (Phase 1c)
2. Make improvements based on findings (Phase 4)
3. Queue NEW retrodictions that will test whether those improvements helped

### Selection Criteria

**Use the `missed` command to find candidates** — it validates resolution and CP automatically:

```bash
uv run aib-devtools queue missed aib --days 14
```

The command filters to questions with confirmed resolutions, shows CP availability,
marks already-retrodicted questions, and outputs a ready-to-use retrodict command.

**Only suggest questions where `R=Y`** (confirmed resolution). The Metaculus API often
lists questions as `status: "resolved"` before the resolution value is populated.
Running retrodict on these wastes API credits and produces zero calibration data.

**Note on CP:** The listing API (`/api/posts/?status=resolved`) strips aggregation
data, so CP may show as unavailable in listing results. Individual API fetches
(`/api/posts/{id}/`) include full CP data. The `missed` command fetches individually
when needed. The agent cannot see CP for its own question during live forecasting
(tournament rule), but CP is available post-hoc for calibration analysis.

Additional criteria for manual selection:
- Diverse in type (binary, numeric, multiple choice)
- Would test the agent's reasoning on challenging topics
- Have enough pre-resolution time for blind mode to be meaningful

### Output Format

End your analysis document with the retrodict command from the `missed` output (or a subset):

```bash
# Retrodiction queue from feedback loop YYYY-MM-DD
# Rationale: [brief explanation of why these were chosen]
uv run forecast retrodict <id1> <id2> <id3> [--forecast-date YYYY-MM-DD]
```

### Feedback Cycle

The user runs the retrodictions, then the next feedback loop session:
1. Collects those retrodictions in Phase 1c
2. Checks airtightness
3. Evaluates accuracy against the improvements made
4. Queues more retrodictions → repeat

## Completion Checklist (MANDATORY)

**Before writing the final analysis document, fill out this checklist.** If any item is unchecked, go back and complete it. Do not skip items — the whole point of the feedback loop is thoroughness.

| Phase | Deliverable | Done? |
|-------|------------|-------|
| 0 | Read previous analysis, noted what was already fixed | [ ] |
| 1a | Scores table for all target posts | [ ] |
| 1b | Per-forecast post-mortem with error classifications | [ ] |
| 1c | Calibration summary (ECE, coverage, Brier) | [ ] |
| 1-gate | User confirmed findings before trace analysis | [ ] |
| 2a | Trace explorer launched with resolution context | [ ] |
| 2c | Tool failures enumerated with root causes | [ ] |
| 2c | Capability requests quoted from agent | [ ] |
| 3a | Meta-level: is the agent's self-tracking sufficient? | [ ] |
| 3b | What data was missing for this analysis? | [ ] |
| 2+3-gate | User approved priority list before implementation | [ ] |
| 4 | Changes implemented (or clearly marked PROPOSED) | [ ] |
| 4-verify | `git diff` confirms each COMMITTED change exists | [ ] |
| 5 | This document reviewed for outdated guidance | [ ] |
| 6 | Retrodict queue proposed (or "none available" noted) | [ ] |

**If you only made object-level changes, you skipped Phase 3 and 5.** Go back.
**If "What's already been fixed" is empty, you skipped Phase 0.** Go back.
**If no tool failures are listed, you didn't read the traces carefully enough.** Go back.

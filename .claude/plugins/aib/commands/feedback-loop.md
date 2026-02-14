---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, Task, WebSearch, AskUserQuestion
description: Analyze forecasts and improve agent based on calibration and process quality
---

# Feedback Loop: Three Levels of Analysis

The feedback loop operates at three levels. Be clear about which level you're working at:

1. **Object Level** - The forecasting agent itself: tools, capabilities, data access, runtime behavior
2. **Meta Level** - The agent's self-assessment: meta-prompts, reflection templates, metrics emission, what the agent tracks about itself
3. **Meta-Meta Level** - This feedback loop process: the scripts, the analysis methods, this document itself

**Clarification**:
- Object level = "How can the agent forecast better?" (tools, APIs, reasoning)
- Meta level = "How can the agent track its own performance better?" (meta-reflection prompts, metrics formats, what the agent writes to notes/sessions/)
- Meta-meta level = "How can this feedback loop command work better?" (feedback_collect.py, this document, analysis workflows)

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

## Phase 1: Ground Truth - What Actually Matters

The ONLY true ground truth is **resolution outcomes**. Everything else is proxy signal.

### 1a. Collect Resolution Data

```bash
# Default: only new data since last feedback session
uv run python .claude/plugins/aib/scripts/feedback_collect.py --include-retrodict

# Full view when needed (e.g., first run, or to recompute everything)
uv run python .claude/plugins/aib/scripts/feedback_collect.py --all-time --no-new-only
```

**If we have resolved forecasts**: Run calibration analysis first, then check Brier.
- Calibration tells you WHERE you're wrong (actionable diagnostic)
- Brier/log scores tell you HOW you're scoring (tournament metric)
- **Always pass `--version`** to scope analysis to the current agent version
```bash
# Get current version
grep AGENT_VERSION src/aib/version.py

# Calibration analysis scoped to current version
uv run python .claude/plugins/aib/scripts/calibration_analysis.py summary --version 0.7.2

# Detailed binary calibration with reliability diagram
uv run python .claude/plugins/aib/scripts/calibration_analysis.py binary --version 0.7.2

# Numeric PIT calibration
uv run python .claude/plugins/aib/scripts/calibration_analysis.py numeric --version 0.7.2

# Cross-version comparison via scores table
uv run python .claude/plugins/aib/scripts/scores_table.py compare 0.6.0 0.7.2
```
- Which probability ranges have the worst calibration gaps? Read those traces.
- Are there systematic patterns (overconfidence? underconfidence in a range?)

**If we have NO resolved forecasts yet**: We're flying blind on accuracy. Focus on:
- Process quality (is the agent reasoning well?)
- Tool failures (what's blocking the agent?)
- Do NOT treat CP divergence as evidence of error

### 1b. Retrodict Missed Questions (and Check Airtightness)

If questions resolved before we forecast them, **retrodict** them to build calibration data. Blind mode restricts all tools to data that was available before the question resolved, ensuring the agent cannot "cheat" by looking up the answer.

```bash
# Check which questions we missed (validates resolution + shows CP status)
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 14

# Use --all to see questions without confirmed resolution too
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 14 --all

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

**What retrodict outputs:**
- Saves forecasts to `notes/retrodict/<post_id>/<forecast_date>_<timestamp>.json`
- The `retrodict_date` field in the JSON records the cutoff date used
- Filename includes the cutoff date for easy identification
- Shows actual resolution and final CP for comparison
- Computes Brier scores for binary questions

**Resolution data workaround (as of Feb 2026):**

The Metaculus DRF HTML endpoint (`Accept: text/html`) returns 406 since ~Feb 12, 2026. This means `fetch_post_json()` can no longer enrich resolution data — the `resolution` field is null for all questions. Until this is fixed upstream:
- Retrodict will save forecasts with `resolution: null` and `comparison: null`
- Use `resolution_update.py set <post_id> <value>` to manually apply known resolutions
- For re-retrodictions of questions with existing v0.3.1 data, the resolution is cached in `notes/scores.csv`
- Run `scores_table.py build` after setting resolutions to rebuild calibration data

**Retrodict vs Live forecasts:**
- Live forecasts go to `notes/forecasts/`
- Retrodicted forecasts go to `notes/retrodict/` (separate folder)
- This prevents mixing calibration data with real predictions

#### Future-Leak Detection

After running retrodict, review traces for signs that the agent accessed post-resolution information:

**Red flags in agent reasoning:**
- References events after the `forecast_date`
- Phrases like "the outcome was", "it resolved to", "we now know"
- Reasoning that mentions post-resolution news
- Suspiciously high confidence (95%+) on genuinely uncertain questions

**How to check:**
```bash
# Scan for future-leak phrases
grep -rh "resolved\|outcome\|result\|happened\|we know\|actually" notes/sessions/*/meta.md

# Check the full reasoning trace
cat logs/<question_id>/*.log
```

**If you find future leak:**
1. The forecast is invalid for calibration
2. Identify which tool allowed the leak
3. Report the gap - retrodict hooks need fixing
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

### 1c. Collect and Analyze Retrodiction Results

Retrodictions are our **best** calibration signal — they have known resolutions by definition. After running retrodictions (1b) and checking for future leaks, incorporate them into analysis.

**Collect retrodiction data:**
```bash
# List all retrodictions
ls notes/retrodict/*/

# Summarize retrodiction accuracy (uses known resolutions embedded in the JSON)
uv run python .claude/plugins/aib/scripts/feedback_collect.py --include-retrodict
```

**For each retrodiction, evaluate:**
1. **Accuracy**: Compare forecast vs actual resolution (Brier score for binary, error for numeric)
2. **Airtightness**: Did the agent access post-resolution information? (see Future-Leak Detection above)
3. **Reasoning quality**: Read the session trace — was the reasoning sound given only pre-resolution data?
4. **Tool effectiveness**: Which tools worked under blind-mode constraints? Which failed?
5. **Calibration contribution**: After collecting retrodictions, run `calibration_analysis.py summary` to see how new data points shift ECE and bucket-level gaps.

**Airtightness checklist** (run for every retrodiction before trusting its calibration value):
- [ ] No references to events after `retrodict_date` in reasoning trace
- [ ] No suspiciously high confidence on genuinely uncertain questions
- [ ] WebSearch results all predate the cutoff
- [ ] WebFetch URLs went through Wayback Machine (check logs)
- [ ] No financial data beyond the cutoff date
- [ ] Related questions' fine_print doesn't contain post-cutoff resolution data

**If a retrodiction fails airtightness**: Exclude it from calibration data and file a bug against the retrodict hooks.

**Note**: `feedback_collect.py --include-retrodict` processes both `notes/forecasts/` and `notes/retrodict/`.

### 1d. About Community Prediction

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

## Phase 2: Object Level - Read Traces Deeply

**This is the most important phase.** Do not skip to aggregate patterns.

### CRITICAL: Filter by AGENT_VERSION

**Every analysis must be version-aware.** Different agent versions have different prompts,
tools, and subagent configurations. Mixing data across versions produces meaningless
aggregate statistics.

1. Check the current version: `grep AGENT_VERSION src/aib/version.py`
2. **Pass `--version` to all scripts** that support it:
   - `calibration_analysis.py summary --version 0.7.2`
   - `calibration_analysis.py binary --version 0.7.2`
   - `scores_table.py show --version 0.7.2`
3. When comparing to previous versions, always report metrics PER VERSION
4. If the `agent_version` field is missing or inconsistent, note this as a data quality
   issue — do not silently include unversioned data in current-version metrics

**Use `scores_table.py compare` for version-to-version comparisons:**
```bash
uv run python .claude/plugins/aib/scripts/scores_table.py compare 0.6.0 0.7.2
```

**Use `scores_table.py extremes` to find best/worst forecasts for deep trace reading:**
```bash
# All forecasts — best and worst by Brier (binary) and abs error (numeric)
uv run python .claude/plugins/aib/scripts/scores_table.py extremes

# Non-meta only (exclude CP questions) — for event-level analysis
uv run python .claude/plugins/aib/scripts/scores_table.py extremes --non-meta

# Meta-predictions only
uv run python .claude/plugins/aib/scripts/scores_table.py extremes --meta-only

# Filter by version, source, or type
uv run python .claude/plugins/aib/scripts/scores_table.py extremes --version 0.11.0 --type numeric
```

### 2a. Launch Trace Explorer (Subagent)

**Do NOT read traces directly in this conversation.** Traces consume ~1160 lines each and will
exhaust the context window before you reach later phases. Instead, launch the `trace-explorer`
subagent which reads traces in its own context and returns a compact pattern report.

**Select which traces to analyze:**

```bash
# Use extremes to find best/worst forecasts
uv run python .claude/plugins/aib/scripts/scores_table.py extremes --version <current>

# Or list all available traces
uv run python .claude/plugins/aib/scripts/trace_log.py list
```

**Launch the trace explorer:**

```
Task(subagent_type="aib-workflow:trace-explorer", prompt="""
Analyze traces for these post IDs: [list of 5-15 IDs]

Context:
- Current agent version: [X.Y.Z]
- Focus areas: [e.g., "tool failures", "reasoning on meta-predictions", "numeric CDF quality"]
- Known issues from Phase 1: [brief summary of calibration findings]

Return the standard pattern report.
""")
```

**What to include in the prompt:**
- Post IDs to analyze (from extremes, or all recent forecasts)
- Current agent version (so the explorer can filter)
- Any specific focus areas from Phase 1 calibration findings
- Known issues from the previous feedback session (Phase 0)

**What you get back:**
- Tool failure patterns (aggregated across all traces)
- Capability requests (what the agent asked for)
- Reasoning patterns and quality issues
- Tool usage patterns (high-value vs low-value tools)
- 2-3 specific traces worth reading in full (outliers or interesting cases)

### 2b. Deep-Dive on Flagged Traces (Optional)

The trace explorer flags 2-3 traces worth reading fully. **Only read these if the pattern
report raises specific questions** that need full-trace context to answer.

If you do read a trace, use `trace_log.py show <id>` (NOT raw logs) and read it with a
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
uv run python .claude/plugins/aib/scripts/trace_forecast.py list
```

### 3c. Identify Missing Data

Common gaps:
- **No resolution data** → Can't evaluate accuracy, only process
- **No tool-to-forecast linkage** → Can't identify which tools help
- **No question type tagging** → Can't identify patterns by category

If you find gaps, add tracking in Phase 4.

## Phase 4: Implement Changes (Bitter Lesson Order)

**Do NOT edit `version.py` manually.** Use `version_tag.py bump <patch|minor|major> "<summary>"` — pick the right level based on the scope of changes (see Version Bumps below).

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
1. **Study the best-performing traces.** Use `scores_table.py show --resolved` and `trace_log.py show <id>` to read the full reasoning for the top 5-10 forecasts by Brier score. What patterns do they follow? What decisions led to success?
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
uv run python .claude/plugins/aib/scripts/version_tag.py bump <level> "<summary>" [--detail "a, b, c"]
```

- **Patch (0.x.Y)**: Bug fixes, tool fixes, config tweaks. Default when unsure.
- **Minor (0.X.0)**: Small prompt changes, new tools, subagent modifications.
- **Major (X.0.0)**: Architecture changes (new LLM, new framework, major restructuring).

Data-only or infrastructure changes (scripts, feedback-loop docs) don't need a bump.

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
# Scripts that already exist:
uv run python .claude/plugins/aib/scripts/feedback_collect.py --help
uv run python .claude/plugins/aib/scripts/trace_forecast.py --help
uv run python .claude/plugins/aib/scripts/calibration_report.py --help
```

If you need a script that doesn't exist, create it in `.claude/plugins/aib/scripts/` and document it in CLAUDE.md.

### 5c. Improve Data Collection

If the feedback loop lacked data, fix the source:
- Add fields to forecast JSON schema
- Update the agent to emit more tracking data
- Add scripts to collect missing metrics

### 5d. Update This Document

Every session should leave this document better:
- Remove outdated guidance
- Add new scripts to the "Scripts Available" section
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

The feedback_collect.py script automatically organizes data by branch. When writing analysis, use the same structure:

```markdown
# Feedback Loop Analysis: YYYY-MM-DD

## Ground Truth Status
- Resolved forecasts with our predictions: N
- Average Brier score: X.XX (or "none yet - process analysis only")

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

### Scripts Created/Updated
- [New scripts added to .claude/plugins/aib/scripts/]

### Data Collection Improvements
- [Changes to forecast tracking, metrics, etc.]

## Changes Made
| Level | Change | Rationale |
|-------|--------|-----------|
| Object | Added X tool | Agent requested it in N meta-reflections |
| Meta | Improved analysis queries | Was missing Y data |
| Meta-Meta | Updated feedback-loop.md | Clarified Z section |
```

## Scripts Available

```bash
# Incremental collection (default: only new since last session)
uv run python .claude/plugins/aib/scripts/feedback_collect.py --include-retrodict

# Full collection (all-time, no filtering)
uv run python .claude/plugins/aib/scripts/feedback_collect.py --all-time --no-new-only --include-retrodict

# Collect from specific tournament
uv run python .claude/plugins/aib/scripts/feedback_collect.py --tournament spring-aib-2026

# Check missed questions
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 14

# Check resolutions for specific questions
uv run python .claude/plugins/aib/scripts/resolution_update.py check

# Retrodict resolved questions (blind mode - restricts to historical data)
uv run forecast retrodict 41835 41521 41517

# Retrodict with specific cutoff date
uv run forecast retrodict 41835 --forecast-date 2026-01-15

# Retrodict without time restriction (for debugging)
uv run forecast retrodict 41835 --no-blind

# Trace a forecast to its logs and metrics
uv run python .claude/plugins/aib/scripts/trace_forecast.py show 41906

# Aggregate metrics across all forecasts
uv run python .claude/plugins/aib/scripts/aggregate_metrics.py summary

# Calibration analysis (primary diagnostic — ECE, reliability diagrams, PIT)
# Always pass --version to scope to the current agent version
uv run python .claude/plugins/aib/scripts/calibration_analysis.py summary --version 0.7.2
uv run python .claude/plugins/aib/scripts/calibration_analysis.py binary --version 0.7.2 --source retrodict
uv run python .claude/plugins/aib/scripts/calibration_analysis.py numeric --version 0.7.2

# Basic calibration report (Brier/log scores, bucket table)
uv run python .claude/plugins/aib/scripts/calibration_report.py summary

# Best/worst forecasts (for deep trace reading)
uv run python .claude/plugins/aib/scripts/scores_table.py extremes
uv run python .claude/plugins/aib/scripts/scores_table.py extremes --non-meta
uv run python .claude/plugins/aib/scripts/scores_table.py extremes --meta-only --version 0.11.0

# Version comparison
uv run python .claude/plugins/aib/scripts/scores_table.py compare 0.10.0 0.11.0

# (Add more scripts as you build them — this tooling is in constant evolution)
```

## Periodic Maintenance

Every few feedback loop sessions, take time to:

1. **Reread this entire document** - Is it still accurate? Remove outdated guidance.
2. **Prompt health audit** - Read the entire system prompt (`src/aib/agent/prompts.py`) with fresh eyes. Does it read as a coherent, monolithic document? Are there visible patches? Would a new reader understand the decision tree? If not, trigger a rewrite (Phase 4, Priority 0).
3. **Refactor scripts** - Consolidate duplicate functionality, improve error handling.
4. **Clean up notes/** - Archive old analysis files, ensure naming is consistent.
5. **Update CLAUDE.md** - Sync any learnings that should persist to the main project docs.

## Key Questions to Answer Each Session

1. **What AGENT_VERSION am I analyzing?** Filter ALL data by version. Pass `--version` to every script. Do not mix versions.
2. **Do we have resolution data?** If no, focus on process not accuracy. Check HTML enrichment status (may return 406).
3. **How is calibration FOR THIS VERSION?** Run `calibration_analysis.py summary --version X.Y.Z`. Compare to previous version with `scores_table.py compare`.
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
uv run python .claude/plugins/aib/scripts/forecast_queue.py missed aib --days 14
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

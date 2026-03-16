---
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, AskUserQuestion, WebSearch, WebFetch
description: Implement prioritized changes from feedback loop analysis
---

# Implement: Make Changes

Implement changes identified during investigation, analysis, and reflection.

## Entry Gate

Use AskUserQuestion to present the prioritized change list with Bitter Lesson classification. User must approve before implementation.

**Bitter Lesson classification:**
- **Tool/capability** (preferred): Build or fix a tool, add a data source, improve automation
- **Principle** (acceptable): Add a general principle to prompts that helps across many cases
- **Rule/patch** (avoid): Question-type-specific rules, numeric adjustments, conditional exceptions

## Priority Order

### P0: Prompt health

Use `analysis prompt-health` data. If patches have accumulated:
- Study the 3 best traces — what did the agent do right?
- Study the 3 worst traces — where did the prompt mislead?
- Read the full prompt
- Rewrite the affected section from scratch (monolithic, no addendums)

### P1: Fix failing tools

From `analysis tool-health` flags. Fix the root cause, not the symptom.

### P2: Build requested tools

From `analysis tool-needs`. Discuss with user before building — use AskUserQuestion to present the capability gap, proposed approach, and alternatives.

### P3: Improve subagents

From summary.json workflow assessments. Evaluate value vs cost.

### P4: Simplify prompts

Remove prescriptive rules. Add general principles. Don't add:
- Specific rules for question types
- Numeric adjustments ("add 5% for...")
- Patches for observed patterns
- Conditional exceptions

## After Implementation

1. Version bump: `uv run aib-devtools version bump <level> "<summary>"`
2. Commit changes
3. Verify: `git diff --stat` confirms each change
4. Log changes in analysis doc:
   - **COMMITTED**: In git, verified
   - **PROPOSED**: Discussed but not implemented
   - **DEFERRED**: Identified but deprioritized

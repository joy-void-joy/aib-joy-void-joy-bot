#!/bin/bash
# PLAN.md existence check for git push
# Warns if PLAN.md doesn't exist when pushing a feature branch

set -euo pipefail

# Read input from stdin
input=$(cat)

# Extract command from tool input
command=$(echo "$input" | jq -r '.tool_input.command // ""')

# Only check for git push commands
if [[ ! "$command" =~ ^git[[:space:]]+push ]]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Check if we're on a feature branch
current_branch=$(git branch --show-current)
if [[ ! "$current_branch" =~ ^feat/ ]]; then
  # Not a feature branch, skip PLAN.md check
  exit 0
fi

# Check if PLAN.md exists
if [[ ! -f "PLAN.md" ]]; then
  echo '{"systemMessage": "Warning: PLAN.md does not exist. Consider creating a PLAN.md that documents the feature implementation, its goals, and current status before pushing."}' >&2
  # Don't block, just warn
  exit 0
fi

# PLAN.md exists, let the prompt-based Stop hook do the deeper review
exit 0

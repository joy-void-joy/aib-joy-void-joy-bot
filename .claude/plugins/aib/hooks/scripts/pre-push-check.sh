#!/bin/bash
# Pre-push quality check hook
# Intercepts git push commands and runs pyright, ruff, and tests
# Auto-fixes formatting issues where possible

set -euo pipefail

# Read input from stdin
input=$(cat)

# Extract command from tool input
command=$(echo "$input" | jq -r '.tool_input.command // ""')

# Only intercept git push commands
if [[ ! "$command" =~ ^git[[:space:]]+push ]]; then
  # Not a push command, allow it
  exit 0
fi

echo "Pre-push checks triggered for: $command" >&2

# Change to project directory
cd "$CLAUDE_PROJECT_DIR"

# Check for uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
  echo '{"hookSpecificOutput": {"permissionDecision": "deny"}, "systemMessage": "Cannot push: working tree has uncommitted changes. Please commit or stash changes first."}' >&2
  exit 2
fi

echo "Working tree is clean, running quality checks..." >&2

# Track if we need to re-run checks after auto-fix
needs_recheck=false

# 1. Run pyright
echo "Running pyright..." >&2
if ! uv run pyright 2>&1; then
  echo '{"hookSpecificOutput": {"permissionDecision": "deny"}, "systemMessage": "Cannot push: pyright found type errors. Please fix them before pushing."}' >&2
  exit 2
fi
echo "pyright passed" >&2

# 2. Run ruff format (auto-fix)
echo "Running ruff format..." >&2
format_output=$(uv run ruff format . 2>&1) || true
if [[ -n "$format_output" && "$format_output" != *"0 files"* ]]; then
  echo "Ruff formatted files:" >&2
  echo "$format_output" >&2
  needs_recheck=true
fi

# 3. Run ruff check with auto-fix
echo "Running ruff check..." >&2
if ! uv run ruff check . --fix 2>&1; then
  # Check if there are still errors after auto-fix
  if ! uv run ruff check . 2>&1; then
    echo '{"hookSpecificOutput": {"permissionDecision": "deny"}, "systemMessage": "Cannot push: ruff found linting errors that could not be auto-fixed. Please fix them manually."}' >&2
    exit 2
  fi
  needs_recheck=true
fi
echo "ruff check passed" >&2

# 4. Run tests
echo "Running tests..." >&2
if ! uv run pytest 2>&1; then
  echo '{"hookSpecificOutput": {"permissionDecision": "deny"}, "systemMessage": "Cannot push: tests failed. Please fix failing tests before pushing."}' >&2
  exit 2
fi
echo "Tests passed" >&2

# If we auto-fixed anything, check for new uncommitted changes
if [[ "$needs_recheck" == "true" ]]; then
  if [[ -n $(git status --porcelain) ]]; then
    echo '{"hookSpecificOutput": {"permissionDecision": "deny"}, "systemMessage": "Cannot push: ruff auto-fixed some files. Please review and commit the formatting changes, then try pushing again."}' >&2
    exit 2
  fi
fi

echo "All checks passed! Allowing push." >&2
# Allow the push to proceed
exit 0

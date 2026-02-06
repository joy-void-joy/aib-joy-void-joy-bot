#!/bin/bash
# Test file protection hook
# - Hard blocks test file edits when TDD mode is active (flag file exists)
# - Warns about test file edits when TDD mode is not active
# This enforces TDD discipline: tests are written first, implementation follows

set -euo pipefail

# Read input from stdin
input=$(cat)

# Extract file path from tool input
file_path=$(echo "$input" | jq -r '.tool_input.file_path // ""')

# If no file path, allow (probably not a file operation)
if [[ -z "$file_path" ]]; then
  exit 0
fi

# Get just the filename for pattern matching
filename=$(basename "$file_path")

# Check if this is a test file
is_test_file=false

# Pattern 1: test_*.py
if [[ "$filename" =~ ^test_.*\.py$ ]]; then
  is_test_file=true
fi

# Pattern 2: *_test.py
if [[ "$filename" =~ ^.*_test\.py$ ]]; then
  is_test_file=true
fi

# Pattern 3: conftest.py
if [[ "$filename" == "conftest.py" ]]; then
  is_test_file=true
fi

# Pattern 4: file is in tests/ directory
if [[ "$file_path" =~ /tests/ || "$file_path" =~ ^tests/ ]]; then
  is_test_file=true
fi

# If not a test file, allow without comment
if [[ "$is_test_file" != "true" ]]; then
  exit 0
fi

# It's a test file - check if TDD mode is active
TDD_FLAG_FILE="$CLAUDE_PROJECT_DIR/.tdd-mode"

if [[ -f "$TDD_FLAG_FILE" ]]; then
  # TDD mode is active - HARD BLOCK test edits
  # This is the "implementer agent" context where tests should not be modified
  echo '{"hookSpecificOutput": {"permissionDecision": "deny"}, "systemMessage": "BLOCKED: Cannot modify test files during TDD implementation phase. Test file: '"$file_path"'. If tests need changes, return a detailed analysis report explaining what modifications are needed and why, then exit to let the user make the changes."}' >&2
  exit 2
fi

# TDD mode not active - require user permission
# Use "ask" decision to prompt user before allowing test modifications
echo '{"hookSpecificOutput": {"permissionDecision": "ask"}, "systemMessage": "Test file modification requested: '"$file_path"'. This requires explicit user approval. Please confirm you want to modify this test file."}' >&2
exit 0

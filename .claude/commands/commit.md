---
allowed-tools: Bash(git:*), Read, Grep, Glob
description: Review all diffs and create atomic commits covering all changes
---

# Atomic Commit Review

Review all current changes and create atomic commits—each commit should represent a single logical change.

## Process

1. **Review the current state**:
   - Run `git status` to see all modified, staged, and untracked files
   - Run `git diff` to see unstaged changes
   - Run `git diff --cached` to see staged changes

2. **Analyze and group changes**:
   - Read the changed files to understand what each change does
   - Group related changes together (e.g., a feature + its tests, a refactor across multiple files)
   - Identify independent changes that should be separate commits

3. **Create atomic commits**:
   - For each logical group of changes:
     - Stage only the related files: `git add <specific-files>`
     - Create a commit with a clear, descriptive message
   - Use conventional commit format when appropriate (feat:, fix:, refactor:, docs:, test:, chore:)

4. **Verify**:
   - Run `git log --oneline -10` to show the commits created
   - Confirm all changes have been committed

## Guidelines

- **One logical change per commit** — If you need "and" in the commit message, consider splitting
- **Don't bundle unrelated changes** — A typo fix shouldn't be in the same commit as a feature
- **Tests with implementation** — Keep tests in the same commit as the code they test
- **Clear commit messages** — Focus on *what* and *why*, not *how*

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

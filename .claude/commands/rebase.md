---
allowed-tools: Bash(git:*), Bash(gh:*), Read, Grep, Glob
description: Create a clean rebase branch with atomic commits and open a PR
---

# Rebase and PR

Create a temporary rebase branch with a clean, logical commit history, then open a pull request.

## Process

1. **Gather context**:
   - Identify the current branch and its base (typically `main`)
   - Review the full diff from base to HEAD: `git diff main...HEAD`
   - List existing commits: `git log --oneline main..HEAD`

2. **Understand all changes**:
   - Read the changed files to understand the complete set of modifications
   - Think about what logical units of work exist (features, refactors, fixes, tests, docs)
   - **Ignore the existing commit history** — focus on what makes sense as a clean sequence

3. **Create rebase branch**:
   ```bash
   git checkout -b <branch>-rebase main
   ```

4. **Build clean commits**:
   - For each logical unit of work, cherry-pick or manually stage the relevant changes
   - Create atomic commits with clear messages
   - Order commits logically (dependencies first, then features, then polish)
   - Use conventional commit format: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`

5. **Push and create PR**:
   ```bash
   git push -u origin <branch>-rebase
   gh pr create --title "..." --body "..."
   ```

## Guidelines

- **Fresh perspective** — Don't feel bound by how commits were originally organized
- **Logical ordering** — Put foundational changes before features that depend on them
- **Atomic commits** — Each commit should compile/run independently if possible
- **Meaningful messages** — Commit messages should explain *what* and *why*

## PR Format

```markdown
## Summary
- [1-3 bullet points describing the changes]

## Test plan
- [How to verify the changes work]

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

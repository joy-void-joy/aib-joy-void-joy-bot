# lup: ignore[constant-declaration]
# Both constants are this repository's own composition — which skills and
# agents its generated plugin ships. A composition root is where a judgement
# is finally made rather than passed on, so there is no caller above it.
"""This repository's harness content: what it inherits, and what it does not.

The whole roster is the library's. The forecasting skills this repository
also has — `/aib:audit`, `/aib:design`, `/aib:leak`, `/aib:fb-retrodict`,
`/aib:clean-gone`, `/aib:merge-conflict` — stay hand-written under
`.claude/plugins/aib/`, where they answer to their own prefix and cannot
collide with anything here. Moving them into a declaration is worth doing
and is not what this change is: one migration that both replaced the hooks
engine and rewrote six skills would leave any later surprise unattributable.
"""

import lup.harness.models as models
from lup.devtools.harness.content.catalog import LIBRARY_AGENTS, LIBRARY_SKILLS

PROJECT_SKILLS: list[models.Skill] = []
"""No skill here is declared yet; the ones this repository has are hand-written.

# lup: defer: The six `/aib:*` skills under `.claude/plugins/aib/commands/`
# are the last hand-maintained half of this tree. Declaring them here would
# put every skill this repository ships under one generator, and retire the
# `aib` plugin entirely.
"""

PROJECT_AGENTS: list[models.Agent] = []
"""The four agents this repository had were lup's, copied. They come back
from the library rather than being declared again.

# lup: defer: This project's `dev` sub-app is its own four commands, so it
# has none of the library's — `check`, `comments`, `rules`, `report-friction`,
# `conflict`, `git-hooks`. Composing `create_dev_app` would bring them, and
# needs one decision first: the library's `dev worktree` is a sub-tree with
# `create`/`list`/`remove` where this project's is a flat command, and they
# collide on the name.
"""

SKILLS = [*LIBRARY_SKILLS, *PROJECT_SKILLS]
"""Every skill this repository's generated plugin ships."""

AGENTS = [*LIBRARY_AGENTS, *PROJECT_AGENTS]
"""Every agent it ships."""

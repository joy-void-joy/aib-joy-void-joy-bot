# lup: ignore[constant-declaration]
# Both constants are this repository's own composition — which skills and
# agents its generated plugin ships. A composition root is where a judgement
# is finally made rather than passed on, so there is no caller above it.
"""This repository's harness content: what it inherits, and what it does not.

Most of the roster is the library's. What this repository adds is the work no
library word covers, because it is forecasting rather than development:
auditing a forecast against how its question actually resolved, queueing
retrodictions, and tracing a future leak in one.

A skill that only *looked* like this repository's own is not here. Clearing
branches and worktrees is `land`, resolving a conflicted tree is `merge`, and
the feedback-loop phases are the library's own — each was maintained twice
under a second plugin until this declaration replaced it.
"""

import lup.harness.models as models
from lup.devtools.harness.content.catalog import LIBRARY_AGENTS, LIBRARY_SKILLS

from aib.devtools.harness.content.skills.audit import SKILL as SKILL_AUDIT
from aib.devtools.harness.content.skills.design import SKILL as SKILL_DESIGN
from aib.devtools.harness.content.skills.fb_retrodict import (
    SKILL as SKILL_FB_RETRODICT,
)
from aib.devtools.harness.content.skills.leak import SKILL as SKILL_LEAK

PROJECT_SKILLS: list[models.Skill] = [
    SKILL_AUDIT,
    SKILL_DESIGN,
    SKILL_FB_RETRODICT,
    SKILL_LEAK,
]
"""The forecasting skills this repository declares beyond the library's."""

PROJECT_AGENTS: list[models.Agent] = []
"""The four agents this repository had were lup's, copied. They come back
from the library rather than being declared again."""

SKILLS = [*LIBRARY_SKILLS, *PROJECT_SKILLS]
"""Every skill this repository's generated plugin ships."""

AGENTS = [*LIBRARY_AGENTS, *PROJECT_AGENTS]
"""Every agent it ships."""

# lup: ignore[constant-declaration]
# Every constant here is this project's own composition — which of the
# library's sub-apps its CLI serves, and what it tells them about itself. A
# composition root is where a judgement is finally made rather than passed
# on, so there is no caller above it to take these from.
"""What this project's CLI takes from the library, and what it declines.

The library's default is everything, and a project states its delta. That is
the whole reason this file is short: a sub-app lup grows next month arrives
here by existing, where an inherited list would have had to be re-copied and
the copy that fell behind is indistinguishable from a decision.

The declines are stated for the same reason. A retirement nobody can see
becomes permanent by default — the roster it was taken from goes on growing,
and the project that opted out once never meets the decision again.

Nothing here constructs a Typer app for a library sub-app. `main.py` is where
each name meets the app answering to it; this module is imported by the
harness catalog too, which must not pull a CLI in to learn what was declined.
"""

from lup.devtools.feedback.models import AgentPrompt
from lup.devtools.subapps import SubAppSelection
from lup.harness.models import ContentSelection

RETIRED_SUBAPPS = SubAppSelection(
    retired=[
        # Both walk an operator through external services, and this project
        # declares no `Integration` for either to show. An empty wizard is a
        # decision a reader has to discover; this is one they can read.
        "dashboard",
        "setup",
        # `analysis` is this project's feedback loop, and it is forecasting's
        # rather than development's: tool health and capability gaps across
        # agent versions, calibration drift, prompt patch accumulation. The
        # library's asks the same questions of a repository instead.
        "feedback",
        # This project reads its own accounts, under `claude usage`, where the
        # runner that spends them lives.
        "usage",
    ]
)
"""The library sub-apps this project's CLI does not serve, and why.

`trace` and `version` are absent because they are not declined: this project
declares its own under both names — forecast traces rather than session
traces, and the release ritual rather than a bare bump — and an added entry
naming a default replaces it.
"""

RETIRED_CONTENT = ContentSelection()
"""The library skills and agents this project's plugin does not ship: none.

Stated rather than left to a default so the gate reports a real answer. The
four agents this repository once had were the library's, copied, and PR #67
retired the copies rather than the agents; every skill it declares is beside
the library's rather than instead of one.
"""


def agent_prompt() -> AgentPrompt:
    """This project's forecasting system prompt, as the health report weighs it.

    Rendered rather than read off disk: the report measures what a session
    actually receives, and the sections are assembled at call time from a
    table no file reproduces in order.

    Imported inside the call because this module is on the harness catalog's
    import path, and the prompt reaches the whole agent package behind it.
    """
    from pathlib import Path

    from aib.agent.prompts import SECTIONS, get_forecasting_system_prompt

    return AgentPrompt(
        sections=list(SECTIONS.values()),
        rendered=get_forecasting_system_prompt(),
        source=Path("src/aib/agent/prompts.py"),
    )

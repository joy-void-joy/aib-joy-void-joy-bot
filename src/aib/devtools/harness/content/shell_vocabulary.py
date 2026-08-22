"""Where this project's shell vocabulary differs from the one lup offers.

The rule models and the groups in :mod:`lup.policy.vocabulary` are library
mechanism; what is *this project's* is the selection below — the commands it
judges differently, and the runner targets no other project has.

Stated as differences rather than as a table, the way a project states which
anti-patterns it retires: :func:`~lup.policy.vocabulary.default_vocabulary` is
what a selection layers over, so adding one command costs one entry instead of
a copy of every command the library already judged.

Both of those rules exist because this repository spends money when it runs.
A forecast opens agent sessions against paid APIs, runs for tens of minutes,
and writes into `notes/`. It is the user's to start, and an agent that wants
one prints the command rather than issuing it. The predecessor of this file
said the same thing as a regex denylist over the raw command string; the
difference is that a declaration is matched against a parsed command, so
`git status && uv run forecast x` is judged by the forecast rather than by
the `git status` in front of it.
"""

from lup.policy.shell_rules import (
    RunnerTargetRule,
    ShellCommandRule,
    ShellOperationRule,
    ShellSubcommandRule,
)
from lup.policy.vocabulary import runner_target_rules
from lup.selection import Selection

SPAWNS_A_FORECAST = (
    "this spawns a forecasting agent: it spends API credits, runs for tens of"
    " minutes, and writes into notes/ — print the exact command and say what"
    " to look for in its output, and let the user run it"
)
"""Why the two refusals below refuse, and what to do instead.

One sentence rather than two, because the two commands differ only in
spelling: both open the same agent against the same paid APIs, and an agent
told different things about them would learn there was a quieter way in.
"""


def agent_opening_verbs() -> ShellSubcommandRule:
    """Refuse the devtools verbs that reach a forecasting agent, one each.

    Every one of these is the same agent as `uv run forecast`, reached
    through the development CLI instead of the bot's own entry point. The
    rest of `lup-devtools` reads this repository and is blessed with it, so
    the refusal sits on the verbs rather than on the toolchain.
    """
    return ShellSubcommandRule(
        name="worldview",
        effect="allow",
        operations=[
            ShellOperationRule(name="loop", effect="deny", reason=SPAWNS_A_FORECAST)
        ],
    )


def forecast_targets() -> list[RunnerTargetRule]:
    """The `uv run` spellings that open a forecasting agent, all refused.

    `forecast` is the bot itself and is refused whole. `lup-devtools` is
    mostly a reader of this repository, so it stays blessed and names the
    three verbs beneath it that open the same agent.

    A refusal rather than a question because the question is not this
    session's to answer: the cost lands on the user's account and the run
    outlives the turn that started it.
    """
    return [
        RunnerTargetRule(name="forecast", effect="deny", reason=SPAWNS_A_FORECAST),
        RunnerTargetRule(
            name="lup-devtools",
            sandbox="outside",
            subcommands=[
                agent_opening_verbs(),
                ShellSubcommandRule(
                    name="resolution",
                    effect="allow",
                    operations=[
                        ShellOperationRule(
                            name="tentative",
                            effect="deny",
                            reason=SPAWNS_A_FORECAST,
                        )
                    ],
                ),
                ShellSubcommandRule(
                    name="analysis",
                    effect="allow",
                    operations=[
                        ShellOperationRule(
                            name="review", effect="deny", reason=SPAWNS_A_FORECAST
                        )
                    ],
                ),
            ],
        ),
    ]


RUNNER_TARGETS: list[RunnerTargetRule] = [
    *runner_target_rules(session_opening=()),
    *forecast_targets(),
]
"""What `uv run <target>` may reach here, and what it may not.

The library group carries the checkers. `lup-devtools` is taken out of it
and declared below instead: the group's version is a bare blessing, and this
project needs the same target carrying the verbs it refuses. Its placement
is restated there for the same reason the group gives it — a toolchain that
opens agent sessions cannot run confined.
"""


SHELL_RULES: Selection[ShellCommandRule] = Selection[ShellCommandRule]()
"""Where this project's shell vocabulary differs from the one lup offers: nowhere.

Empty, and that is the whole claim. Every group `default_vocabulary()` composes
is one this repository wants at the arguments the library offers it — `git` with
its force-push guard, because forecast commits publish to a branch other runs
read back and replacing what a remote ref points at is worth the question it
costs; `docker` because the sandbox tool runs code in a container; `gh` because
the workflow opens and reads pull requests.

Stated as a selection rather than as a copy of that table, so a command the
library judges next arrives here instead of being missed. The copy that stood
here restated seven groups to disagree with none of them, and would have gone
on reading as a decision the first time it fell behind.

What this project *does* judge differently is which `uv run` targets open a
forecasting agent, and that is `RUNNER_TARGETS` above — a table the library
holds no opinion on, so it is declared rather than selected.
"""

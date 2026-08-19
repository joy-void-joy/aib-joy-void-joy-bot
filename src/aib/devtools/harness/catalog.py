# lup: ignore[constant-declaration]
# Every constant here is this repository's own composition — which runtimes it
# builds for, and what it calls its own harness session. A composition root is
# where a judgement is finally made rather than passed on, so there is no
# caller above it to take these from.
"""Root of the project-owned harness declaration graph.

The declaration leaves — the guidance, the settings, the shell vocabulary,
and the skill and agent rosters — live under ``content/``. This module
assembles them with the hook policy into the portable ``Harness`` that
``harness generate`` compiles into the native tree.

Everything this file declares was, until the fork ended, a regex list in a
hook script under ``.claude/plugins/aib/hooks/scripts/``. The reason for
moving it is not tidiness: those scripts judged the raw command *string* with
unanchored patterns, so ``rm -rf x && git status`` matched the ``git status``
allow and was approved. This is matched against a parsed command.
"""

from pathlib import Path

from pydantic import AnyHttpUrl

from lup.adapters.claude.harness import ClaudeSpellings
from lup.harness.contracts import NativeSpellings
from lup.harness.models import (
    Harness,
    HookPathRole,
    HookSandbox,
    HookSet,
    HookUrlScope,
    LiteralWord,
    McpServer,
    Plugin,
    ProjectRootWord,
    ResolveSpec,
    SkillInvocation,
)
from lup.policy.refused_tools import RefusedTool
from lup.workspace.paths import project_root, read_project_name

from aib.devtools.harness.content.catalog import AGENTS, SKILLS
from aib.devtools.harness.content.guidance import document as guidance_document
from aib.devtools.harness.content.shell_vocabulary import RUNNER_TARGETS, SHELL_RULES

EXCLUDED_COMMANDS = [
    # Egress the sandbox proxy cannot carry: it allowlists hostnames over
    # HTTP, and the transport underneath a git remote is SSH on port 22.
    "ssh *",
    "git *",
    # `gh` reaches hosts the allowlist admits, but it drives `git` for
    # anything touching a remote, and a child of a confined command is
    # confined too.
    "gh *",
    # Docker talks to its daemon over a Unix socket the isolation blocks
    # outright. The sandbox tool is what runs a forecast's code, so a
    # boundary that stops it stops the bot rather than protecting it.
    "docker *",
]
"""Commands this project runs with no OS boundary beneath them.

Each is a requirement the boundary cannot express any other way, and the
count is the point: an exclusion is not a widened rule but a removed one."""

RESEARCH_TOOL_GROUPS = [
    "search",
    "financial",
    "government",
    "markets",
    "trends",
    "wayback",
]
"""The research tool groups an interactive session is offered.

Written down rather than read from ``build_research_tool_groups()``, which
adds ``reddit`` only when its credentials are configured: a generated tree
that changed shape with the environment would drift for whoever generated it
last rather than for anyone's reason.
"""

HARNESS_SESSION = "harness"
"""The session a natively launched tool server opens for itself."""

NATIVE_RUNTIMES: list[NativeSpellings] = [ClaudeSpellings()]
"""Every runtime this project generates a tree for.

Claude alone, because that is what the bot runs on and what the hand-written
tree already targeted. A Codex tree costs one entry here and nothing else,
since every declaration below is runtime-neutral."""


def research_servers() -> list[McpServer]:
    """Offer this project's research tools to an interactive session.

    The same groups the forecasting agent uses, served over stdio by the
    devtools command that already serves them, so a session opened by hand
    reaches the tools a forecast reaches rather than a smaller set.
    """
    return [
        McpServer(
            id=f"mcp.{name}",
            name=name,
            description=f"Research tools in the {name} group, served over stdio",
            command="uv",
            arguments=[
                LiteralWord(text="run"),
                LiteralWord(text="--directory"),
                ProjectRootWord(),
                LiteralWord(text="lup-devtools"),
                LiteralWord(text="agent"),
                LiteralWord(text="serve-tools"),
                LiteralWord(text="--server"),
                LiteralWord(text=name),
            ],
        )
        for name in RESEARCH_TOOL_GROUPS
    ]


ARTIFACT_REFUSAL = (
    "publishing a page leaves the repository, and this project already owns"
    " surfaces that do not — run `uv run lup-devtools report` for everything"
    " left to implement, or /lup:report to write it whole under tmp/"
)
"""Why an artifact is the wrong reflex here, and what answers the same need.

The redirect is the point rather than the refusal. This repository already
refuses the paper version of the same move — a `TODO.md` or a roadmap file
parks a decision where no workflow surfaces it again — and a published page
is that failure with a URL: further out of reach of `report`, the note
passes, and the gates, not nearer.
"""

REFUSED_TOOLS = [
    RefusedTool(tool="Artifact", reason=ARTIFACT_REFUSAL),
    RefusedTool(tool="Skill", specifier="artifact-design", reason=ARTIFACT_REFUSAL),
]
"""The calls this project has decided against, each naming what to reach for.

Declaring one is also what lets a runtime see it. The Codex dispatcher
registers the tools it decodes widened by the tools refused here, so a table
that named nothing left its matcher at the three tools the runtime already
routes — and a refusal no hook is registered for is a refusal in name.

Neither is walled off: a deliberate use escalates with the marker the shell
lattice already uses, and gets an approval question carrying this reason.
"""


def declared_hook_set() -> HookSet:
    """The hook set this project declares, for a session composed in process."""
    return portable_harness().declared_hooks


def documentation_scopes() -> list[HookUrlScope]:
    """Every origin a session here may fetch without being asked.

    Carried over from the fetch hook's allowlist unchanged, plus the runtime
    documentation the guidance sends a session to read. Each is a place this
    project's own work is documented; anything else is a question.
    """
    origins = [
        # Runtime and framework documentation the guidance points at.
        "https://docs.claude.com",
        "https://code.claude.com",
        "https://platform.claude.com",
        "https://ai.pydantic.dev",
        # Metaculus: the tournament this bot forecasts in, and the client
        # library it reads questions through.
        "https://www.metaculus.com",
        "https://metaculus.com",
        # Prediction markets the market tools read.
        "https://docs.polymarket.com",
        "https://docs.manifold.markets",
        # The news API one research group is served by.
        "https://docs.asknews.app",
        "https://mcp.asknews.app",
        # Where the code and its dependencies live.
        "https://github.com",
        "https://api.github.com",
        "https://pypi.org",
        "https://files.pythonhosted.org",
    ]
    return [
        *[HookUrlScope(origin=AnyHttpUrl(origin)) for origin in origins],
        HookUrlScope(
            origin=AnyHttpUrl("https://githubusercontent.com"),
            include_subdomains=True,
        ),
        # This machine's own services, on whatever port they took. Reaching
        # one is how a session establishes that something it just started
        # came up at all.
        *[
            HookUrlScope(
                origin=AnyHttpUrl(f"http://{host}"),
                any_port=True,
                reason="this machine's own pages, on whatever port they took",
            )
            for host in ("127.0.0.1", "localhost")
        ],
    ]


def path_roles() -> list[HookPathRole]:
    """What each root here is for, which decides how much of the lattice applies.

    ``notes/`` is deliberately absent. It looks disposable — it is generated
    output — but a forecast written there is the record of a run that cost
    money and cannot be reproduced, so it is production and the verbs that
    ask before destroying something keep asking.
    """
    return [
        HookPathRole(root=Path("tests"), role="test"),
        HookPathRole(root=Path("tmp"), role="scratch"),
        HookPathRole(root=Path("logs"), role="scratch"),
        HookPathRole(root=Path(".venv"), role="scratch"),
        HookPathRole(root=Path(".ruff_cache"), role="scratch"),
        HookPathRole(root=Path(".pytest_cache"), role="scratch"),
        HookPathRole(root=Path("build"), role="scratch"),
        HookPathRole(root=Path("dist"), role="scratch"),
    ]


def portable_harness(version: str = "0.2.0", root: Path | None = None) -> Harness:
    """Build the canonical declaration graph the adapter compiles."""
    plugin = Plugin(
        id="plugin.lup",
        name="lup",
        # Marketplace names share one global namespace per runtime, so this
        # is per-project. `aib` is already taken by the hand-written plugin
        # beside this one, which is exactly the collision the suffix avoids.
        marketplace=f"{read_project_name(root or project_root())}-repository",
        version=version,
        description=(
            "Self-improvement harness with feedback, review, and safe resolution flows"
        ),
        skills=SKILLS,
        agents=AGENTS,
        mcp_servers=research_servers(),
        hooks=HookSet(
            id="hooks.lup-policy",
            policy_ids=["fetch", "shell", "edit", "unknown-tool"],
            refused_tools=REFUSED_TOOLS,
            allowed_fetch=documentation_scopes(),
            protected_edit_roots=[
                Path(".claude"),
                Path(".githooks"),
                Path("pyproject.toml"),
                Path("sync.json"),
                # The variant registry decides which agent configuration an
                # A/B arm runs under, so an edit to it silently changes what
                # a comparison is comparing.
                Path("notes/variants.json"),
            ],
            path_roles=path_roles(),
            human_owned_files=[Path("README.md")],
            diagnostics_command=[".venv/bin/pyright", "--outputjson"],
            shell_rules=SHELL_RULES,
            runner_targets=RUNNER_TARGETS,
            sandbox=HookSandbox(
                extra_domains=["api.anthropic.com"],
                credential_paths=["~/.ssh", "~/.aws/credentials"],
                # Every command reaches the toolchain through `uv`, which
                # locks its cache whenever it resolves dependencies.
                writable_paths=["~/.cache/uv"],
                excluded_commands=EXCLUDED_COMMANDS,
            ),
        ),
    )
    return Harness(
        generator_version=version,
        source_evidence={"content": "typed-python"},
        plugins=[plugin],
        guidance=guidance_document(),
        resolver=ResolveSpec(
            id="resolver.lup",
            worker_identity="resolver-worker",
            worker_skill=SkillInvocation(plugin="lup", skill="implementer"),
            review_skill=SkillInvocation(plugin="lup", skill="resolve-reviewer"),
            merge_skill=SkillInvocation(plugin="lup", skill="merge"),
        ),
    )

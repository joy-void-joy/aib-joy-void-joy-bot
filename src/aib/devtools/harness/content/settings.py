"""What this repository grants, refuses, and enables for itself.

The rendering is the library's (:mod:`lup.devtools.harness.settings`), which
derives the marketplace key, the plugin enablement, the served-tool grants,
and the sandbox boundaries from the declaration itself. Named here is only
the half no derivation can reach: which other plugins this repository turns
on, and which tools it grants or refuses by judgement.
"""

from lup.devtools.harness.settings import Settings, project_settings as render
from lup.harness.models import Plugin
from lup.types import JsonObject

DECLARED = Settings(
    base={"coauthorship": False},
    official_plugins={
        "agent-sdk-dev@claude-plugins-official": True,
        "claude-md-management@claude-plugins-official": True,
        "github@claude-plugins-official": True,
        "pyright-lsp@claude-plugins-official": True,
    },
    allowed=[
        "WebSearch",
        "Read(./.claude/settings.json.local*)",
    ],
    denied=[
        "Read(./**/*.local*)",
    ],
)
"""The half of the settings artifact that is this repository's judgement.

The permissions come from what the hand-written settings granted before the
plugin was generated, unchanged: a migration that also retuned them would
make any later surprise impossible to attribute.
"""


def project_settings(plugin: Plugin | None) -> JsonObject:
    """Render this repository's settings artifact from its declaration."""
    return render(DECLARED, plugin)

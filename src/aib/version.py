"""Agent version tracking.

AGENT_VERSION tracks the forecasting agent's behavior — prompts, tools,
tools, scoring logic. Bump this when agent behavior changes, NOT
for data commits, dependency updates, or infrastructure changes.

Bump rules:
- Patch (0.3.x): bug fixes, config tweaks, tool fixes
- Minor (0.x.0): prompt changes, new tools, tool modifications
- Major (x.0.0): architecture changes (new LLM, new framework)
"""

import importlib.util
from pathlib import Path

AGENT_VERSION = "6.3.0"

VERSION_FILE = Path(__file__)


def load_agent_version(path: Path = VERSION_FILE) -> str:
    """Read AGENT_VERSION from source, bypassing the import cache.

    A long-lived process imports this module once at startup, so its in-memory
    AGENT_VERSION never reflects a later change to the working tree. Executing
    the source file into a throwaway module returns the value currently on disk
    without mutating the imported module.
    """
    spec = importlib.util.spec_from_file_location("aib_version_probe", path)
    if spec is None or spec.loader is None:
        return AGENT_VERSION
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    version = module.AGENT_VERSION
    assert isinstance(version, str)
    return version

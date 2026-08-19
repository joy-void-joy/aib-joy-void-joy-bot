"""The agent version is declared once, in `[tool.lup] agent_version`.

That single declaration is what `lup.workspace.paths` reads to key
`notes/traces/<version>/`, and what `lup-devtools version` shows and bumps.
These pin that both readers agree, and that this repository still understands
the pre-migration spelling, so `version list` can walk history across the move.

Writing the version belongs to the library now. What stays here is reading
one, because only this repository knows the spelling its own history used
before the value moved into the manifest.
"""

from lup.workspace.paths import agent_version, project_root, read_agent_version

from aib.devtools.version import VERSION_FILE, parse_version


def test_declared_version_is_what_lup_resolves() -> None:
    assert read_agent_version(project_root()) == agent_version()


def test_devtools_reads_the_same_declaration() -> None:
    assert parse_version(VERSION_FILE.read_text()) == agent_version()


def test_version_file_is_the_project_manifest() -> None:
    assert VERSION_FILE == project_root() / "pyproject.toml"


def test_parses_the_pre_migration_spelling() -> None:
    """`version list` reads commits older than the [tool.lup] table."""
    assert parse_version('AGENT_VERSION = "6.4.0"\n') == "6.4.0"

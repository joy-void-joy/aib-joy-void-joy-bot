"""The agent version is declared once, in `[tool.lup] agent_version`.

That single declaration is what `lup.workspace.paths` reads to key
`notes/traces/<version>/`, and what `lup-devtools version` shows and bumps.
These pin the two halves together: that both readers agree, and that the
bump command still understands the pre-migration spelling so `version list`
can walk history across the move.
"""

from pathlib import Path

import pytest
import tomlkit
from lup.workspace.paths import agent_version, project_root, read_agent_version

from aib.devtools.version import VERSION_FILE, _parse_version, _write_version


def test_declared_version_is_what_lup_resolves() -> None:
    assert read_agent_version(project_root()) == agent_version()


def test_devtools_reads_the_same_declaration() -> None:
    assert _parse_version(VERSION_FILE.read_text()) == agent_version()


def test_version_file_is_the_project_manifest() -> None:
    assert VERSION_FILE == project_root() / "pyproject.toml"


def test_parses_the_pre_migration_spelling() -> None:
    """`version list` reads commits older than the [tool.lup] table."""
    assert _parse_version('AGENT_VERSION = "6.4.0"\n') == "6.4.0"


def test_bump_rewrites_only_the_version(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """A bump must not reformat the manifest around the value it changes."""
    manifest = tmp_path / "pyproject.toml"
    manifest.write_text(
        '[project]\nname = "aib"  # kept\n\n[tool.lup]\nagent_version = "1.2.3"\n',
        encoding="utf-8",
    )
    monkeypatch.setattr("aib.devtools.version.VERSION_FILE", manifest)

    _write_version("2.0.0")

    written = manifest.read_text(encoding="utf-8")
    assert "# kept" in written
    assert _parse_version(written) == "2.0.0"
    assert tomlkit.parse(written)["project"]["name"] == "aib"

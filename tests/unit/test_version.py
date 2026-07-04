"""Tests for agent version tracking and on-disk drift detection."""

from pathlib import Path

from aib.version import AGENT_VERSION, load_agent_version


def test_load_agent_version_matches_imported_constant() -> None:
    assert load_agent_version() == AGENT_VERSION


def test_load_agent_version_reads_from_disk(tmp_path: Path) -> None:
    probe = tmp_path / "version.py"
    probe.write_text('AGENT_VERSION = "9.9.9"\n', encoding="utf-8")
    assert load_agent_version(probe) == "9.9.9"

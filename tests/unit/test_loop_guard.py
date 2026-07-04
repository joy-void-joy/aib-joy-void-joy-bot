"""The forecast loop must re-exec on an agent-version change before forecasting."""

import pytest

import aib.cli as cli


class LoopRestart(Exception):
    """Sentinel standing in for os.execv replacing the process."""


def test_loop_restarts_when_version_changes_on_disk(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    def fake_execv(executable: str, argv: list[str]) -> None:
        raise LoopRestart

    monkeypatch.setattr(cli, "load_agent_version", lambda: cli.AGENT_VERSION + "-next")
    monkeypatch.setattr(cli.os, "execv", fake_execv)

    with pytest.raises(LoopRestart):
        cli.loop(tournaments=["minibench"])

    assert "restarting loop" in capsys.readouterr().out.lower()

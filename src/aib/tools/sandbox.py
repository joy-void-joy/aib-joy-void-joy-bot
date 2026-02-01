"""Docker-based Python sandbox for code execution.

Use `Sandbox` as a context manager to create an isolated container for
code execution. The sandbox provides tools for the Claude Agent SDK.
"""

import logging
import time
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Self, TypedDict

import docker
from claude_agent_sdk import SdkMcpTool, tool
from pydantic import BaseModel, Field

from aib.tools.mcp_server import create_mcp_server
from claude_agent_sdk.types import McpSdkServerConfig
from docker.errors import APIError, DockerException, NotFound
from docker.models.containers import Container, ExecResult

from aib.config import settings
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


# --- Pydantic input schemas ---


class ExecuteCodeInput(BaseModel):
    """Input schema for the execute_code tool."""

    code: str = Field(min_length=1)


class InstallPackageInput(BaseModel):
    """Input schema for the install_package tool."""

    packages: list[str] = Field(min_length=1)


# --- TypedDict definitions for result types ---


class ExecuteCodeResult(TypedDict):
    """Result from executing Python code in the sandbox."""

    exit_code: int
    stdout: str
    stderr: str
    duration_ms: int


class InstallPackageResult(TypedDict):
    """Result from installing packages in the sandbox."""

    exit_code: int
    output: str
    packages: list[str]


# --- Helper functions ---


def _decode_output(output: bytes | None) -> str:
    """Decode bytes output to string, handling None and errors."""
    if output is None:
        return ""
    return output.decode("utf-8", errors="replace")


# --- Sandbox class ---


class SandboxNotInitializedError(RuntimeError):
    """Raised when sandbox operations are called on an inactive sandbox."""


class CodeExecutionTimeoutError(RuntimeError):
    """Raised when code execution exceeds the timeout."""


class Sandbox:
    """Docker-based Python sandbox for isolated code execution.

    Manages a Docker container lifecycle and provides tools for executing
    Python code and installing packages.

    Args:
        container_name: Name for the Docker container.
        docker_image: Docker image to use for the sandbox.
        volume_name: Name of the Docker volume for persistent workspace.
        shared_dir: Local directory to mount for file sharing (default: ./tmp/sandbox-shared).

    Example:
        with Sandbox() as sandbox:
            result = sandbox.run_code("print('hello')")
            server = sandbox.create_mcp_server()
    """

    DEFAULT_CONTAINER_NAME = "aib-sandbox"
    DEFAULT_DOCKER_IMAGE = "ghcr.io/astral-sh/uv:python3.12-bookworm-slim"
    DEFAULT_VOLUME_NAME = "aib-sandbox-workspace"
    DEFAULT_SHARED_DIR = "./tmp/sandbox-shared"

    def __init__(
        self,
        container_name: str = DEFAULT_CONTAINER_NAME,
        docker_image: str = DEFAULT_DOCKER_IMAGE,
        volume_name: str = DEFAULT_VOLUME_NAME,
        shared_dir: str = DEFAULT_SHARED_DIR,
    ) -> None:
        self._container_name = container_name
        self._docker_image = docker_image
        self._volume_name = volume_name
        self._shared_dir = Path(shared_dir).resolve()
        self._container: Container | None = None
        self._client: docker.DockerClient | None = None

    @property
    def container(self) -> Container:
        """Get the active container.

        Raises:
            SandboxNotInitializedError: If sandbox is not running.
        """
        if self._container is None:
            raise SandboxNotInitializedError(
                "Sandbox not initialized. Use 'with Sandbox() as sandbox:' first."
            )
        return self._container

    @property
    def is_active(self) -> bool:
        """Check if the sandbox container is currently running."""
        return self._container is not None

    def _cleanup_stale_container(self) -> None:
        """Remove any stale container from previous runs."""
        if self._client is None:
            return
        try:
            old = self._client.containers.get(self._container_name)
            logger.info("Removing stale sandbox container")
            old.stop(timeout=5)
            old.remove()
        except NotFound:
            pass

    def _destroy_container(self) -> None:
        """Stop and remove the current container."""
        if self._container is None:
            return
        try:
            self._container.stop(timeout=5)
            self._container.remove()
        except (APIError, DockerException) as e:
            logger.warning("Failed to cleanup container: %s", e)
        finally:
            self._container = None

    def start(self) -> None:
        """Start the sandbox container.

        Creates a new Docker container for code execution. Removes any
        stale container with the same name first.

        Raises:
            DockerException: If container creation fails.
        """
        self._client = docker.from_env()
        self._cleanup_stale_container()

        # Ensure shared directory exists
        self._shared_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Creating sandbox container: %s", self._container_name)
        logger.info("Mounting shared directory: %s -> /shared", self._shared_dir)
        self._container = self._client.containers.run(
            self._docker_image,
            name=self._container_name,
            command="sleep infinity",
            detach=True,
            volumes={
                self._volume_name: {"bind": "/workspace", "mode": "rw"},
                str(self._shared_dir): {"bind": "/shared", "mode": "rw"},
            },
            working_dir="/workspace",
            mem_limit="1g",
            network_mode="bridge",
        )

    def stop(self) -> None:
        """Stop and remove the sandbox container."""
        logger.info("Destroying sandbox container")
        self._destroy_container()
        self._client = None

    def __enter__(self) -> Self:
        """Enter context manager, starting the sandbox."""
        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Exit context manager, stopping the sandbox."""
        self.stop()

    # --- Code execution methods ---

    def run_code(
        self, code: str, timeout_seconds: int | None = None
    ) -> ExecuteCodeResult:
        """Execute Python code in the sandbox container.

        Args:
            code: Python code to execute.
            timeout_seconds: Max execution time in seconds. If None, uses
                settings.sandbox_timeout_seconds. Set to 0 for no timeout.

        Returns:
            Result containing exit code, stdout, stderr, and duration.

        Raises:
            SandboxNotInitializedError: If sandbox is not running.
            CodeExecutionTimeoutError: If execution exceeds timeout.
        """
        if timeout_seconds is None:
            timeout_seconds = settings.sandbox_timeout_seconds

        start = time.perf_counter()

        # Use `timeout` command inside container for reliable timeout handling.
        # The `timeout` utility (from coreutils) returns exit code 124 on timeout
        # and actually kills the process, unlike threading-based timeouts which
        # leave zombie processes running.
        if timeout_seconds > 0:
            cmd = ["timeout", str(timeout_seconds), "python", "-c", code]
        else:
            cmd = ["python", "-c", code]

        result: ExecResult = self.container.exec_run(
            cmd,
            demux=True,
            workdir="/workspace",
        )

        duration_ms = int((time.perf_counter() - start) * 1000)

        # Check for timeout (exit code 124 from `timeout` command)
        if result.exit_code == 124:
            raise CodeExecutionTimeoutError(
                f"Code execution timed out after {timeout_seconds} seconds"
            )

        # When demux=True, output is a tuple of (stdout, stderr)
        stdout_bytes, stderr_bytes = result.output

        return {
            "exit_code": result.exit_code,
            "stdout": _decode_output(stdout_bytes),
            "stderr": _decode_output(stderr_bytes),
            "duration_ms": duration_ms,
        }

    def run_install(self, packages: list[str]) -> InstallPackageResult:
        """Install Python packages using uv.

        Args:
            packages: List of package names to install.

        Returns:
            Result containing exit code, output, and package list.

        Raises:
            SandboxNotInitializedError: If sandbox is not running.
        """
        cmd = ["uv", "pip", "install", "--system", *packages]
        result: ExecResult = self.container.exec_run(cmd, demux=False)

        # When demux=False, output is just bytes
        output_text = _decode_output(result.output)

        return {
            "exit_code": result.exit_code,
            "output": output_text,
            "packages": packages,
        }

    # --- MCP tool creation ---

    def create_tools(
        self,
    ) -> list[SdkMcpTool[ExecuteCodeInput] | SdkMcpTool[InstallPackageInput]]:
        """Create MCP tools bound to this sandbox instance.

        Returns:
            List of MCP tools for code execution and package installation.
        """

        timeout_seconds = settings.sandbox_timeout_seconds

        @tool(
            "execute_code",
            (
                "Execute Python code in an isolated Docker container. Returns exit code, "
                "stdout, stderr, and duration. The container has network access, a "
                "persistent /workspace directory, and a /shared directory for file exchange "
                f"with the host. Timeout: {timeout_seconds}s."
            ),
            {"code": str},
        )
        @tracked("execute_code")
        async def execute_code(args: dict[str, Any]) -> dict[str, Any]:
            try:
                validated = ExecuteCodeInput.model_validate(args)
            except Exception as e:
                return mcp_error(f"Invalid input: {e}")

            try:
                result = self.run_code(validated.code)
                return mcp_success(result)
            except SandboxNotInitializedError as e:
                logger.error("Sandbox not initialized: %s", e)
                return mcp_error(f"Sandbox error: {e}")
            except CodeExecutionTimeoutError as e:
                logger.warning("Code execution timed out")
                return mcp_error(str(e))
            except (APIError, DockerException) as e:
                logger.exception("Docker execution failed")
                return mcp_error(f"Docker error: {e}")

        @tool(
            "install_package",
            "Install one or more Python packages from PyPI using uv. Packages persist "
            "in the container across executions.",
            {"packages": list},
        )
        @tracked("install_package")
        async def install_package(args: dict[str, Any]) -> dict[str, Any]:
            try:
                validated = InstallPackageInput.model_validate(args)
            except Exception as e:
                return mcp_error(f"Invalid input: {e}")

            try:
                result = self.run_install(validated.packages)
                return mcp_success(result)
            except SandboxNotInitializedError as e:
                logger.error("Sandbox not initialized: %s", e)
                return mcp_error(f"Sandbox error: {e}")
            except (APIError, DockerException) as e:
                logger.exception("Docker execution failed")
                return mcp_error(f"Docker error: {e}")

        return [execute_code, install_package]

    def create_mcp_server(
        self,
        name: str = "sandbox",
        version: str = "1.0.0",
    ) -> McpSdkServerConfig:
        """Create an MCP server with sandbox tools.

        Args:
            name: Server name.
            version: Server version.

        Returns:
            Configured MCP server with execute_code and install_package tools.
        """
        return create_mcp_server(
            name=name,
            version=version,
            tools=self.create_tools(),
        )


# --- Convenience context manager ---


@contextmanager
def sandbox_context(
    container_name: str = Sandbox.DEFAULT_CONTAINER_NAME,
    docker_image: str = Sandbox.DEFAULT_DOCKER_IMAGE,
    volume_name: str = Sandbox.DEFAULT_VOLUME_NAME,
) -> Generator[Sandbox, None, None]:
    """Context manager that creates a sandbox and destroys it on exit.

    This is a convenience wrapper around `Sandbox` for cases where you
    prefer a functional style.

    Args:
        container_name: Name for the Docker container.
        docker_image: Docker image to use for the sandbox.
        volume_name: Name of the Docker volume for persistent workspace.

    Yields:
        The running Sandbox instance.

    Example:
        with sandbox_context() as sandbox:
            result = sandbox.run_code("print('hello')")
    """
    sandbox = Sandbox(
        container_name=container_name,
        docker_image=docker_image,
        volume_name=volume_name,
    )
    with sandbox:
        yield sandbox

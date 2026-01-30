"""Docker-based Python sandbox for code execution.

Use `Sandbox` as a context manager to create an isolated container for
code execution. The sandbox provides tools for the Claude Agent SDK.
"""

import logging
import time
from collections.abc import Generator
from contextlib import contextmanager
from typing import Any, Self, TypedDict

import docker
from claude_agent_sdk import SdkMcpTool, create_sdk_mcp_server, tool
from claude_agent_sdk.types import McpSdkServerConfig
from docker.errors import APIError, DockerException, NotFound
from docker.models.containers import Container, ExecResult

logger = logging.getLogger(__name__)


# --- TypedDict definitions for tool inputs ---


class ExecuteCodeInput(TypedDict):
    """Input schema for the execute_code tool."""

    code: str


class InstallPackageInput(TypedDict):
    """Input schema for the install_package tool."""

    packages: list[str]


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


def _success_response(
    result: ExecuteCodeResult | InstallPackageResult,
) -> dict[str, Any]:
    """Create a successful MCP tool response."""
    return {"content": [{"type": "text", "text": str(result)}]}


def _error_response(message: str) -> dict[str, Any]:
    """Create an error MCP tool response."""
    return {"content": [{"type": "text", "text": message}], "is_error": True}


# --- Sandbox class ---


class SandboxNotInitializedError(RuntimeError):
    """Raised when sandbox operations are called on an inactive sandbox."""


class Sandbox:
    """Docker-based Python sandbox for isolated code execution.

    Manages a Docker container lifecycle and provides tools for executing
    Python code and installing packages.

    Args:
        container_name: Name for the Docker container.
        docker_image: Docker image to use for the sandbox.
        volume_name: Name of the Docker volume for persistent workspace.

    Example:
        with Sandbox() as sandbox:
            result = sandbox.run_code("print('hello')")
            server = sandbox.create_mcp_server()
    """

    DEFAULT_CONTAINER_NAME = "aib-sandbox"
    DEFAULT_DOCKER_IMAGE = "ghcr.io/astral-sh/uv:python3.12-bookworm-slim"
    DEFAULT_VOLUME_NAME = "aib-sandbox-workspace"

    def __init__(
        self,
        container_name: str = DEFAULT_CONTAINER_NAME,
        docker_image: str = DEFAULT_DOCKER_IMAGE,
        volume_name: str = DEFAULT_VOLUME_NAME,
    ) -> None:
        self._container_name = container_name
        self._docker_image = docker_image
        self._volume_name = volume_name
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

        logger.info("Creating sandbox container: %s", self._container_name)
        self._container = self._client.containers.run(
            self._docker_image,
            name=self._container_name,
            command="sleep infinity",
            detach=True,
            volumes={self._volume_name: {"bind": "/workspace", "mode": "rw"}},
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

    def run_code(self, code: str) -> ExecuteCodeResult:
        """Execute Python code in the sandbox container.

        Args:
            code: Python code to execute.

        Returns:
            Result containing exit code, stdout, stderr, and duration.

        Raises:
            SandboxNotInitializedError: If sandbox is not running.
        """
        start = time.perf_counter()

        result: ExecResult = self.container.exec_run(
            ["python", "-c", code],
            demux=True,
            workdir="/workspace",
        )

        duration_ms = int((time.perf_counter() - start) * 1000)

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

        @tool(
            "execute_code",
            "Execute Python code in an isolated Docker container. Returns exit code, "
            "stdout, stderr, and duration. The container has network access and a "
            "persistent /workspace directory.",
            ExecuteCodeInput,
        )
        async def execute_code(args: ExecuteCodeInput) -> dict[str, Any]:
            try:
                result = self.run_code(args["code"])
                return _success_response(result)
            except SandboxNotInitializedError as e:
                logger.error("Sandbox not initialized: %s", e)
                return _error_response(f"Sandbox error: {e}")
            except (APIError, DockerException) as e:
                logger.exception("Docker execution failed")
                return _error_response(f"Docker error: {e}")

        @tool(
            "install_package",
            "Install one or more Python packages from PyPI using uv. Packages persist "
            "in the container across executions.",
            InstallPackageInput,
        )
        async def install_package(args: InstallPackageInput) -> dict[str, Any]:
            packages = args["packages"]
            if not packages:
                return _error_response("No packages specified")

            try:
                result = self.run_install(packages)
                return _success_response(result)
            except SandboxNotInitializedError as e:
                logger.error("Sandbox not initialized: %s", e)
                return _error_response(f"Sandbox error: {e}")
            except (APIError, DockerException) as e:
                logger.exception("Docker execution failed")
                return _error_response(f"Docker error: {e}")

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
        return create_sdk_mcp_server(
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

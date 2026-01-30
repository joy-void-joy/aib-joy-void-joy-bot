"""Configuration management using pydantic-settings."""

import logging
from typing import Self

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Application settings loaded from environment variables.

    All settings can be overridden via environment variables with AIB_ prefix.
    Example: AIB_MODEL=claude-sonnet-4-20250514
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="AIB_",
        extra="ignore",
    )

    @model_validator(mode="after")
    def warn_missing_api_keys(self) -> Self:
        """Warn at startup if API keys are missing (but don't fail)."""
        missing = []
        if not self.metaculus_token:
            missing.append("METACULUS_TOKEN (or AIB_METACULUS_TOKEN)")
        if not self.exa_api_key:
            missing.append("EXA_API_KEY (or AIB_EXA_API_KEY)")
        if not self.asknews_client_id or not self.asknews_client_secret:
            missing.append("ASKNEWS_CLIENT_ID/SECRET (or AIB_ prefixed)")

        if missing:
            logger.warning(
                "Missing API keys (some tools may fail): %s", ", ".join(missing)
            )
        return self

    # === Metaculus ===
    metaculus_token: str | None = Field(
        default=None,
        description="Metaculus API token (also checks METACULUS_TOKEN env var)",
    )

    # === Search APIs ===
    exa_api_key: str | None = Field(default=None, description="Exa search API key")
    asknews_client_id: str | None = Field(default=None, description="AskNews client ID")
    asknews_client_secret: str | None = Field(
        default=None, description="AskNews client secret"
    )

    # === Model ===
    model: str = Field(
        default="claude-opus-4-5-20251101",
        description="Claude model to use for forecasting",
    )
    max_thinking_tokens: int | None = Field(
        default=None,
        description="Max thinking tokens (None = unlimited)",
    )

    # === Sandbox ===
    docker_image: str = Field(
        default="ghcr.io/astral-sh/uv:python3.12-bookworm-slim",
        description="Docker image for sandbox",
    )
    sandbox_memory_limit: str = Field(
        default="1g",
        description="Memory limit for sandbox container",
    )
    sandbox_volume_name: str = Field(
        default="aib-sandbox-workspace",
        description="Docker volume name for sandbox workspace",
    )
    sandbox_container_name: str = Field(
        default="aib-sandbox",
        description="Docker container name for sandbox",
    )

    # === Paths ===
    notes_path: str = Field(
        default="./notes",
        description="Base path for notes folders",
    )

    # === Rate Limits ===
    metaculus_max_concurrent: int = Field(
        default=5,
        description="Max concurrent Metaculus API requests",
    )
    search_max_concurrent: int = Field(
        default=3,
        description="Max concurrent search requests",
    )

    # === Tool Defaults ===
    search_default_limit: int = Field(
        default=10,
        description="Default number of web search results",
    )
    news_default_limit: int = Field(
        default=10,
        description="Default number of news results",
    )
    metaculus_default_limit: int = Field(
        default=20,
        description="Default number of Metaculus search results",
    )
    tournament_default_limit: int = Field(
        default=50,
        description="Default number of tournament questions to list",
    )
    market_default_limit: int = Field(
        default=5,
        description="Default number of market results to return",
    )

    # === Agent Limits ===
    max_budget_usd: float | None = Field(
        default=None,
        description="Maximum budget in USD for a single forecast (None = unlimited)",
    )
    max_turns: int | None = Field(
        default=None,
        description="Maximum agent turns for a single forecast (None = unlimited)",
    )
    subforecast_max_turns: int = Field(
        default=50,
        description="Maximum turns for sub-forecasts spawned by spawn_subquestions",
    )
    subforecast_max_budget_usd: float = Field(
        default=5.0,
        description="Maximum budget for each sub-forecast spawned by spawn_subquestions",
    )
    sandbox_timeout_seconds: int = Field(
        default=30,
        description="Timeout for code execution in sandbox",
    )
    http_timeout_seconds: int = Field(
        default=30,
        description="Timeout for HTTP requests to external APIs",
    )


# Singleton instance
settings = Settings()

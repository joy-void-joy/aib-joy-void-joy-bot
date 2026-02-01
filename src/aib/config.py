"""Configuration management using pydantic-settings."""

import logging
import os
from typing import Self

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Application settings loaded from environment variables.

    External API keys use standard names (METACULUS_TOKEN, EXA_API_KEY, etc.)
    for compatibility with external libraries.

    AIB-specific settings use the AIB_ prefix (e.g., AIB_MODEL, AIB_MAX_BUDGET_USD).
    """

    # NOTE: We don't use env_prefix="AIB_" because of a pydantic-settings bug where
    # dotenv files incorrectly apply the prefix to aliased fields. Instead, we
    # explicitly add AIB_ to validation_alias for fields that need it.
    # See: https://github.com/pydantic/pydantic-settings/issues/220
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.local"),
        extra="ignore",
    )

    @model_validator(mode="after")
    def warn_missing_optional_api_keys(self) -> Self:
        """Warn at startup if optional API keys are missing."""
        missing = []
        if not self.exa_api_key:
            missing.append("EXA_API_KEY")
        if not self.asknews_client_id or not self.asknews_client_secret:
            missing.append("ASKNEWS_CLIENT_ID/ASKNEWS_SECRET")

        if missing:
            logger.warning(
                "Missing API keys (some tools may fail): %s", ", ".join(missing)
            )
        return self

    # === Metaculus ===
    # NOTE: Uses METACULUS_TOKEN (no AIB_ prefix) for compatibility with forecasting-tools library
    metaculus_token: str = Field(
        validation_alias="METACULUS_TOKEN",
        description="Metaculus API token (reads from METACULUS_TOKEN env var)",
    )

    # === Search APIs ===
    # NOTE: No AIB_ prefix for external library compatibility
    exa_api_key: str | None = Field(
        default=None, validation_alias="EXA_API_KEY", description="Exa search API key"
    )
    asknews_client_id: str | None = Field(
        default=None, validation_alias="ASKNEWS_CLIENT_ID", description="AskNews client ID"
    )
    asknews_client_secret: str | None = Field(
        default=None, validation_alias="ASKNEWS_SECRET", description="AskNews client secret"
    )

    # === Model ===
    model: str = Field(
        default="claude-opus-4-5-20251101",
        validation_alias="AIB_MODEL",
        description="Claude model to use for forecasting",
    )
    max_thinking_tokens: int | None = Field(
        default=None,
        validation_alias="AIB_MAX_THINKING_TOKENS",
        description="Max thinking tokens (None = unlimited)",
    )

    # === Sandbox ===
    docker_image: str = Field(
        default="ghcr.io/astral-sh/uv:python3.12-bookworm-slim",
        validation_alias="AIB_DOCKER_IMAGE",
        description="Docker image for sandbox",
    )
    sandbox_memory_limit: str = Field(
        default="1g",
        validation_alias="AIB_SANDBOX_MEMORY_LIMIT",
        description="Memory limit for sandbox container",
    )
    sandbox_volume_name: str = Field(
        default="aib-sandbox-workspace",
        validation_alias="AIB_SANDBOX_VOLUME_NAME",
        description="Docker volume name for sandbox workspace",
    )
    sandbox_container_name: str = Field(
        default="aib-sandbox",
        validation_alias="AIB_SANDBOX_CONTAINER_NAME",
        description="Docker container name for sandbox",
    )

    # === Paths ===
    notes_path: str = Field(
        default="./notes",
        validation_alias="AIB_NOTES_PATH",
        description="Base path for notes folders",
    )

    # === Rate Limits ===
    metaculus_max_concurrent: int = Field(
        default=5,
        validation_alias="AIB_METACULUS_MAX_CONCURRENT",
        description="Max concurrent Metaculus API requests",
    )
    search_max_concurrent: int = Field(
        default=3,
        validation_alias="AIB_SEARCH_MAX_CONCURRENT",
        description="Max concurrent search requests",
    )

    # === Tool Defaults ===
    search_default_limit: int = Field(
        default=10,
        validation_alias="AIB_SEARCH_DEFAULT_LIMIT",
        description="Default number of web search results",
    )
    news_default_limit: int = Field(
        default=10,
        validation_alias="AIB_NEWS_DEFAULT_LIMIT",
        description="Default number of news results",
    )
    metaculus_default_limit: int = Field(
        default=20,
        validation_alias="AIB_METACULUS_DEFAULT_LIMIT",
        description="Default number of Metaculus search results",
    )
    tournament_default_limit: int = Field(
        default=50,
        validation_alias="AIB_TOURNAMENT_DEFAULT_LIMIT",
        description="Default number of tournament questions to list",
    )
    market_default_limit: int = Field(
        default=5,
        validation_alias="AIB_MARKET_DEFAULT_LIMIT",
        description="Default number of market results to return",
    )

    # === Agent Limits ===
    max_budget_usd: float | None = Field(
        default=None,
        validation_alias="AIB_MAX_BUDGET_USD",
        description="Maximum budget in USD for a single forecast (None = unlimited)",
    )
    max_turns: int | None = Field(
        default=None,
        validation_alias="AIB_MAX_TURNS",
        description="Maximum agent turns for a single forecast (None = unlimited)",
    )
    subforecast_max_turns: int = Field(
        default=50,
        validation_alias="AIB_SUBFORECAST_MAX_TURNS",
        description="Maximum turns for sub-forecasts spawned by spawn_subquestions",
    )
    subforecast_max_budget_usd: float = Field(
        default=5.0,
        validation_alias="AIB_SUBFORECAST_MAX_BUDGET_USD",
        description="Maximum budget for each sub-forecast spawned by spawn_subquestions",
    )
    sandbox_timeout_seconds: int = Field(
        default=30,
        validation_alias="AIB_SANDBOX_TIMEOUT_SECONDS",
        description="Timeout for code execution in sandbox",
    )
    http_timeout_seconds: int = Field(
        default=30,
        validation_alias="AIB_HTTP_TIMEOUT_SECONDS",
        description="Timeout for HTTP requests to external APIs",
    )


# Singleton instance (required fields are populated from environment by pydantic-settings)
settings = Settings.model_validate({})

# Export API keys to os.environ for external libraries (e.g., forecasting-tools)
# that read directly from environment variables rather than using our settings.
_ENV_EXPORTS = [
    ("METACULUS_TOKEN", settings.metaculus_token),
    ("EXA_API_KEY", settings.exa_api_key),
    ("ASKNEWS_CLIENT_ID", settings.asknews_client_id),
    ("ASKNEWS_SECRET", settings.asknews_client_secret),
]

for env_name, value in _ENV_EXPORTS:
    if value and env_name not in os.environ:
        os.environ[env_name] = value

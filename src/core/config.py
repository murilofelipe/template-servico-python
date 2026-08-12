"""Centralized application configuration module using pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Centralized application settings using Pydantic 2 BaseSettings."""

    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    PORT: int = 8080
    DATABASE_URL: str = "sqlite:///:memory:"
    APP_NAME: str = "template-servico-python"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()

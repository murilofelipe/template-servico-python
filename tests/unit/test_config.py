"""Unit tests for core configuration settings using pydantic-settings."""

import pytest
from pydantic import ValidationError

from core.config import Settings, settings
from main import create_app


def test_default_settings() -> None:
    """Verify default configuration values when no environment variables are set."""
    config = Settings()
    assert config.ENVIRONMENT == "development"
    assert config.DEBUG is True
    assert config.PORT == 8080
    assert config.DATABASE_URL == "sqlite:///:memory:"
    assert config.APP_NAME == "template-servico-python"


def test_env_var_override(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify environment variable overrides for configuration settings."""
    monkeypatch.setenv("ENVIRONMENT", "production")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("PORT", "9000")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@db:5432/custom_db")
    monkeypatch.setenv("APP_NAME", "custom-service")

    config = Settings()
    assert config.ENVIRONMENT == "production"
    assert config.DEBUG is False
    assert config.PORT == 9000
    assert config.DATABASE_URL == "postgresql://user:pass@db:5432/custom_db"
    assert config.APP_NAME == "custom-service"


def test_invalid_port_type(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify ValidationError is raised when PORT is assigned a non-integer value."""
    monkeypatch.setenv("PORT", "not-an-integer")
    with pytest.raises(ValidationError):
        Settings()


def test_global_settings_instance() -> None:
    """Verify global settings instance exists and contains expected attributes."""
    assert isinstance(settings, Settings)
    assert hasattr(settings, "ENVIRONMENT")
    assert hasattr(settings, "DEBUG")
    assert hasattr(settings, "PORT")
    assert hasattr(settings, "DATABASE_URL")
    assert hasattr(settings, "APP_NAME")


def test_flask_app_config_population() -> None:
    """Verify Flask application populates app.config from settings."""
    app = create_app()
    assert app.config["ENVIRONMENT"] == settings.ENVIRONMENT
    assert app.config["DEBUG"] == settings.DEBUG
    assert app.config["PORT"] == settings.PORT
    assert app.config["DATABASE_URL"] == settings.DATABASE_URL
    assert app.config["APP_NAME"] == settings.APP_NAME

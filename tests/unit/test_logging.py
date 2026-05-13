"""Unit tests for the logging module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any
from unittest import mock

import pytest
from loguru import logger as global_logger
from pydantic_settings import BaseSettings

from project_name.logging import LoggingSettings, configure_logger


@pytest.fixture(autouse=True)
def reset_logger_fixture() -> Generator[None, None, None]:
    """Ensure loggers are cleared after each test."""
    yield
    global_logger.remove()
    global_logger.enable("project_name")


class TestLoggingSettings:
    """Test suite for the LoggingSettings model."""

    @pytest.fixture(
        params=[
            {},
            {"enabled": True, "level": "DEBUG"},
            {"enabled": False, "sink": "stdout"},
        ]
    )
    def valid_instances(self, request: pytest.FixtureRequest) -> LoggingSettings:
        """Fixture providing valid instances of LoggingSettings."""
        return LoggingSettings(**request.param)

    @pytest.mark.smoke
    @pytest.mark.unit
    def test_signature(self) -> None:
        """Verify the class signature and fields."""
        assert issubclass(LoggingSettings, BaseSettings)
        assert hasattr(LoggingSettings, "model_config")
        assert (
            LoggingSettings.model_config.get("env_prefix") == "PROJECT_NAME__LOGGING__"
        )
        assert "enabled" in LoggingSettings.model_fields
        assert "level" in LoggingSettings.model_fields

    @pytest.mark.sanity
    @pytest.mark.unit
    def test_initialization(self, valid_instances: LoggingSettings) -> None:
        """Test proper initialization."""
        assert isinstance(valid_instances.enabled, bool)
        assert isinstance(valid_instances.level, str)

    @pytest.mark.regression
    @pytest.mark.unit
    def test_marshalling(self, valid_instances: LoggingSettings) -> None:
        """Test Pydantic dumping and validation."""
        data_dict = valid_instances.model_dump()
        recreated_settings = LoggingSettings.model_validate(data_dict)
        assert recreated_settings.enabled == valid_instances.enabled
        assert recreated_settings.level == valid_instances.level


class TestConfigureLogger:
    """Test suite for the configure_logger function."""

    @pytest.mark.regression
    @pytest.mark.unit
    @pytest.mark.parametrize(
        "kwargs",
        [
            {"enabled": False},
            {"enabled": True, "level": "DEBUG", "clear_loggers": True},
            {
                "enabled": True,
                "filter": ("project_name", "__main__"),
                "clear_loggers": True,
            },
        ],
    )
    def test_invocation(self, kwargs: dict[str, Any]) -> None:
        """Test successful configuration of the global logger."""
        settings_obj = LoggingSettings(**kwargs)  # type: ignore[arg-type]
        configure_logger(settings_obj)

        if settings_obj.enabled:
            global_logger.debug("Test invocation")

    @pytest.mark.sanity
    @pytest.mark.unit
    def test_invalid(self) -> None:
        """
        Test ImportError when otel_formatting is explicitly enabled without package.
        """
        settings_obj = LoggingSettings(enabled=True, otel_formatting="enable")
        with (
            mock.patch("project_name.logging.opentelemetry_trace", None),
            pytest.raises(ImportError, match="OpenTelemetry is not installed"),
        ):
            configure_logger(settings_obj)

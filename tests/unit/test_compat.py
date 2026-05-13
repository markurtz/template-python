"""Unit tests for the compat module."""

from __future__ import annotations

import types

import pytest

from project_name import compat


@pytest.mark.smoke
@pytest.mark.unit
def test_opentelemetry_trace() -> None:
    """Verify opentelemetry_trace param is correctly exported."""
    assert hasattr(compat, "opentelemetry_trace")
    assert compat.opentelemetry_trace is None or isinstance(
        compat.opentelemetry_trace, types.ModuleType
    )

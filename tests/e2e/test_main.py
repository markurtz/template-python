"""End-to-end tests for the project's main entry point."""

from __future__ import annotations

import os
import subprocess
import sys

import pytest


class TestMain:
    """Test suite for the __main__ module and CLI entry point."""

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.e2e
    @pytest.mark.parametrize(
        ("env_vars", "expected_outputs", "unexpected_outputs"),
        [
            (
                {},
                ["Hello from {project_name}", "Settings:"],
                [],
            ),
            (
                {
                    "PROJECT_NAME__ENVIRONMENT": "production",
                    "PROJECT_NAME__LOGGING__FORMAT": "{level} - {message}",
                    "PROJECT_NAME__LOGGING__OTEL_FORMATTING": "disable",
                },
                [
                    "INFO - Hello from {project_name}",
                    "INFO - Settings: Settings(environment='production'",
                ],
                ["DEBUG"],
            ),
        ],
    )
    def test_invocation(
        self,
        env_vars: dict[str, str],
        expected_outputs: list[str],
        unexpected_outputs: list[str],
    ) -> None:
        """Test the main entry point execution via CLI with various configurations."""
        env = os.environ.copy()
        env.update(env_vars)

        exe_result = subprocess.run(
            [sys.executable, "-m", "project_name"],
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )

        assert exe_result.returncode == 0
        output = exe_result.stdout + exe_result.stderr

        for expected in expected_outputs:
            assert expected in output

        for unexpected in unexpected_outputs:
            assert unexpected not in output

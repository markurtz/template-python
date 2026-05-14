"""End-to-end tests for the bootstrap.py script."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest


class TestBootstrap:
    """Test suite for the bootstrap.py script."""

    @pytest.fixture
    def repo_copy(self, tmp_path: Path) -> Path:
        """Fixture to create a copy of the repository in a temporary directory."""
        repo_root = Path(__file__).resolve().parent.parent.parent
        target_dir = tmp_path / "repo_copy"

        # Ignore typical large/irrelevant directories
        ignore_patterns = shutil.ignore_patterns(
            ".git",
            ".venv",
            ".tox",
            "__pycache__",
            "dist",
            "build",
            ".pytest_cache",
            ".mypy_cache",
            ".ruff_cache",
            "node_modules",
            "site",
        )

        shutil.copytree(repo_root, target_dir, ignore=ignore_patterns)
        return target_dir

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.parametrize(
        ("cli_args", "expected_replacements"),
        [
            (
                [
                    "--repository",
                    "my-new-app",
                    "--project-desc",
                    "A cool new app.",
                    "--organization",
                    "myorg",
                    "--disable-pypi",
                    "--disable-docs",
                ],
                {
                    "template-python": "my-new-app",
                    "template_python": "my_new_app",
                    "markurtz": "myorg",
                    "conduct@example.com": "conduct@myorg.com",
                    "An opinionated, production-ready Apache 2.0 template repository "
                    "for bootstrapping modern software projects.": "A cool new app.",
                },
            ),
            (
                [
                    "--repository",
                    "template-python",
                    "--project-desc",
                    "An opinionated, production-ready Apache 2.0 template repository for bootstrapping modern software projects.",
                    "--organization",
                    "markurtz",
                    "--email",
                    "conduct@example.com",
                    "--author-name",
                    "markurtz",
                    "--slack-url",
                    "https://slack.example.com",
                    "--blog-url",
                    "https://blog.example.com",
                ],
                {
                    "template-python": "template-python",
                    "template_python": "template_python",
                    "markurtz": "markurtz",
                    "conduct@example.com": "conduct@example.com",
                    "An opinionated, production-ready Apache 2.0 template repository "
                    "for bootstrapping modern software projects.": "An opinionated, production-ready Apache 2.0 template repository for bootstrapping modern software projects.",
                },
            ),
        ],
    )
    def test_bootstrap(
        self,
        repo_copy: Path,
        cli_args: list[str],
        expected_replacements: dict[str, str],
    ) -> None:
        """Test that bootstrap.py replaces placeholders and renames directories."""
        script_path = repo_copy / "scripts" / "bootstrap.py"

        # Run bootstrap.py
        cmd = [sys.executable, str(script_path)] + cli_args
        result = subprocess.run(
            cmd,
            cwd=repo_copy,
            capture_output=True,
            text=True,
            check=False,
        )

        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)

        assert result.returncode == 0, (
            f"Bootstrap script failed:\n{result.stderr}\n{result.stdout}"
        )

        # Verify old text is gone (excluding the script and .git)
        self._verify_file_contents(repo_copy, expected_replacements, cli_args)

        # Verify python package directory renaming
        old_pkg_dir = repo_copy / "src" / "template_python"
        new_pkg_name = expected_replacements["template_python"]
        new_pkg_dir = repo_copy / "src" / new_pkg_name

        if old_pkg_dir != new_pkg_dir:
            assert not old_pkg_dir.exists(), "Old package directory still exists."
        assert new_pkg_dir.exists(), "New package directory was not created."

    def _verify_file_contents(
        self,
        repo_copy: Path,
        expected_replacements: dict[str, str],
        cli_args: list[str],
    ) -> None:
        """Helper to verify file contents after bootstrap."""
        for file_path in repo_copy.rglob("*"):
            if not file_path.is_file():
                continue

            # Skip the script itself
            if file_path.name == "bootstrap.py":
                continue

            # Skip binary files
            if file_path.suffix in (
                ".pyc",
                ".png",
                ".svg",
                ".jpg",
                ".jpeg",
                ".ico",
                ".woff",
                ".woff2",
                ".ttf",
                ".eot",
            ):
                continue

            try:
                content = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue

            print("EXPECTED_REPLACEMENTS:", expected_replacements)

            for old_text, new_text in expected_replacements.items():
                print(f"Checking {old_text=} against {new_text=}")

                if old_text == new_text:
                    continue
                if old_text in content:
                    lines = content.split("\n")
                    for i, line in enumerate(lines):
                        if old_text in line:
                            pytest.fail(
                                f"Found '{old_text}' in {file_path.name} on line {i + 1}: {line.strip()}"
                            )

            # Check email uncommenting in mkdocs.yml
            if "mkdocs.yml" in file_path.name:
                assert "#  org_email:" not in content
                assert "  org_email:" in content

            # Check email uncommenting in CODE_OF_CONDUCT.md
            if "CODE_OF_CONDUCT.md" in file_path.name:
                # Get the email from expected_replacements
                expected_email = expected_replacements.get("conduct@example.com")
                if expected_email:
                    assert f"<!-- {expected_email} -->" not in content
                    assert expected_email in content

            if "--disable-pypi" in cli_args:
                if file_path.name in ("release.yml", "nightly.yml"):
                    assert "      - name: Publish to PyPI" not in content
                    assert "#      - name: Publish to PyPI" in content
                if file_path.name == "README.md":
                    assert '<!-- <a href="https://pypi.org' in content

            if "--slack-url" in cli_args and "mkdocs.yml" in file_path.name:
                assert "#  slack_url:" not in content
                assert "  slack_url:" in content

            if "--blog-url" in cli_args and "mkdocs.yml" in file_path.name:
                assert "#  blog_url:" not in content
                assert "  blog_url:" in content

"""
Main entrypoint for the {{project_name}} package.

This module provides the executable routine when the package is run directly
via the command line (e.g., ``python -m project_name``). It initializes the logger
and settings, outputting the current version and configuration to verify
the installation and environment setup.
"""

from __future__ import annotations

import sys

from project_name import (
    LoggingSettings,
    Settings,
    __version__,
    configure_logger,
    logger,
)

__all__ = ["main"]


def main() -> int:
    """
    Execute the main routine.

    Initializes application settings and logging, demonstrating the basic startup
    flow of the application. It logs the current version and the loaded configuration
    settings.

    Example:
        .. code-block:: python

            import sys
            from project_name.__main__ import main

            sys.exit(main())

    :return: The exit code of the execution (0 for success).
    :rtype: int
    """
    configure_logger(
        LoggingSettings(
            enabled=True,
            level="INFO",
            clear_loggers=True,
            filter=("project_name", "__main__"),
        )
    )
    logger.info("Hello from {{project_name}} v{}!", __version__)
    settings = Settings()
    logger.info("Settings: {}", settings)
    return 0


if __name__ == "__main__":
    sys.exit(main())

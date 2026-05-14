# Quick Start TODO: need to change quickstart doc to be for this specific template walkthrough rather than general purpose quickstart

This guide gets you from a fresh installation to running your first command in under 5 minutes.

> [!NOTE]
> Make sure you have completed [Installation](installation.md) before continuing. If you are the maintainer and just instantiated this repository from the template, please complete the [Repository Setup](../guides/repository-setup.md) first.

## Step 1 — Initialize Your Environment

If you haven't already, set up your project and install `template-python`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install template-python
```

## Step 2 — Verify the Install

```bash
template-python
```

Expected output:

```console
Hello from template_python v0.1.0!
Settings: Settings(environment='development', project_root=PosixPath('...'))
```

## Step 3 — Run Your First Command

```python
from template_python import Settings, configure_logger, logger
from template_python.logging import LoggingSettings

# Initialize the global logger
configure_logger(LoggingSettings(enabled=True, level="INFO"))

# Load application settings
settings = Settings(environment="production")

# Log the current configuration
logger.info("Application initialized with settings: {}", settings)
```

Expected output:

```console
2026-05-13 12:00:00 | INFO     | __main__:<module> - Application initialized with settings: Settings(environment='production', project_root=PosixPath('...'))
```

> [!TIP]
> See the [Reference](../reference/index.md) for all available configuration options.

## Step 4 — Explore Further

Now that your first command works, explore what `template-python` can do:

- **[Guides](../guides/index.md)** — Task-specific deep dives including CI/CD and repository setup
- **[Reference](../reference/index.md)** — Full API and CLI documentation
- **[Examples](../examples/index.md)** — Runnable code examples

**Next:** [Guides →](../guides/index.md)

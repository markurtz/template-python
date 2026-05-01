# Developing `{{project_name}}`

This guide provides instructions for setting up your development environment, navigating the project structure, and adhering to our coding standards.

## Prerequisites

Ensure your system meets the following requirements before getting started:

- **[Docker](https://docs.docker.com/get-docker/)** (Recommended for isolated environments)
- **[Git](https://git-scm.com/)** (Version control)
- <!-- Add language-specific prerequisites, e.g., Python 3.10+, Node.js 18+ -->

> [!NOTE]
> We strongly recommend using our Docker setup to ensure your local environment exactly matches our CI/CD pipelines.

## Quick Start (Docker)

> [!IMPORTANT]
> The `Dockerfile` and `docker-compose.yml` files included in this template are **placeholders** that must be filled in for your specific language stack before they are usable. The default `CMD` in both files will exit with an error if run without modification.
>
> Once implemented, you can spin up the development environment with:
> ```bash
> git clone https://github.com/{{organization}}/{{project_name}}.git
> cd {{project_name}}
>
> # Build and start the development environment in the background
> docker-compose up -d --build
> ```

To view the logs of your running containers:
```bash
docker-compose logs -f
```

## Local Setup

If you prefer to develop directly on your host machine, follow the steps for your language stack.

> [!NOTE]
> **A note on shared tooling:** This project uses [MkDocs](https://www.mkdocs.org/) for documentation. MkDocs requires Python, regardless of your application's primary language. Install it once globally or in a dedicated virtual environment using `docs/requirements.txt`.

### Python

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install the package and development dependencies
pip install -e ".[dev]"


```

### Node.js / TypeScript

```bash
# 1. Install all dependencies (uses lockfile for reproducibility)
npm ci


```

### Go

```bash
# 1. Download module dependencies
go mod download


```

### Rust

```bash
# 1. All dependencies are managed by Cargo automatically
cargo build


```

## Running Tests

We maintain strict testing standards. Our tests are located in the `tests/` directory and are categorized by tier.

| Test Tier | Directory | Description |
| :--- | :--- | :--- |
| **Unit** | `tests/unit/` | Fast, isolated tests for individual functions and classes. |
| **Integration** | `tests/integration/` | Slower tests that verify interactions between multiple components. |
| **End-to-End** | `tests/e2e/` | Full-stack tests simulating real user workflows. |

Replace the commands below with those appropriate for your language stack:

```bash
# Python (pytest)
pytest tests/unit/
pytest tests/integration/
pytest tests/         # full suite with coverage
pytest tests/ --cov=src --cov-report=xml

# Node.js (Jest)
npx jest tests/unit/
npx jest --ci --coverage

# Go
go test ./tests/unit/...
go test ./...

# Rust
cargo test --lib           # unit tests
cargo test --test '*'      # integration tests
```

## Code Quality and Formatting

We use opinionated formatters and linters to maintain consistency.

- **Formatters & Linters:** We enforce code quality through CI/CD pipelines. Please refer to your language-specific guidelines for setting up local linting.

> [!TIP]
> **IDE Configuration:** We highly recommend configuring your editor (e.g., VSCode, IntelliJ) to format on save using the project's formatting tools. For VSCode, ensure you have the relevant extensions installed and check `.vscode/settings.json` if available.

## Git Workflow & Branching

We follow a structured branching strategy to maintain a clean git history.

1. **Branch Naming:**
   - Feature branches: `feature/short-description`
   - Bug fixes: `bugfix/short-description`
   - Documentation: `docs/short-description`

2. **Commit Messages:**
   We encourage following [Conventional Commits](https://www.conventionalcommits.org/).
   - `feat: add new user endpoint`
   - `fix: resolve crash on startup`
   - `docs: update developing guide`

3. **Pull Requests:**
   - Push your branch to the remote repository.
   - Open a Pull Request against the `main` branch.
   - Ensure all CI checks (tests, linters) pass.
   - Request a review from at least one core maintainer.

## CI/CD Architecture

This repository uses a modular, standardized GitHub Actions architecture. Workflows are divided into core lifecycle events and reusable helper templates.

### Lifecycle Workflows

| Workflow | Trigger | Purpose |
| :--- | :--- | :--- |
| **Development** (`development.yml`) | Pull Request to `main` | Runs quality gates, security audits, unit/integration tests, and builds documentation previews. Blocks merges if checks fail. |
| **Main** (`main.yml`) | Push to `main` | Post-merge validation. Runs unit/integration/e2e tests, quality/security checks, and updates the `latest` documentation. |
| **Nightly** (`nightly.yml`) | Cron (Daily 00:00 UTC) | Runs extended regression tests, alpha builds, nightly documentation deployment, and deeper security analysis. |
| **Release** (`release.yml`) | Push of `v*.*.*` tag | Performs full verification, builds immutable release packages, versioned documentation, and publishes artifacts. |
| **Weekly** (`weekly.yml`) | Cron (Sun 00:00 UTC) | Conducts dependency hygiene and full test suite regression to catch configuration drift. |

### PR Feedback & Cleanup

- **Safe PR Commenting:** The `pr_comment.yml` workflow uses `workflow_run` to securely post CI status comments on pull requests, circumventing write permission limits on forks.
- **Environment Cleanup:** When a PR is closed or merged, `development_cleanup.yml` automatically removes ephemeral documentation environments and artifacts to maintain a clean workspace.

### Reusable Templates

Our pipelines rely on modular templates located in `.github/workflows/_*.yml` (e.g., `_tests.yml`, `_quality.yml`, `_docs.yml`, `_security.yml`, `_build_package.yml`). This ensures testing granularity and linting rules remain perfectly consistent across all stages of the software lifecycle.

## Building Documentation

Our documentation is built using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). To preview documentation changes locally:

```bash
# Install docs dependencies (if not already installed)
pip install mkdocs-material

# Serve documentation on http://127.0.0.1:8000 with hot-reload
mkdocs serve
```

For further assistance, please refer to our [SUPPORT.md](SUPPORT.md).

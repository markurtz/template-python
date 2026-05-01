# AGENTS.md — AI Agent & Coding Assistant Guide

> **This file provides repository-specific instructions to AI coding agents** (e.g., OpenAI Codex, GitHub Copilot, Gemini, Claude, Cursor).
> Human contributors should refer to [DEVELOPING.md](DEVELOPING.md).

## Project Context

**`{{project_name}}`** is a production-ready Apache 2.0 template repository for bootstrapping modern software projects.
**Primary language:** `<!-- TODO: Replace with your stack -->`  
**Package manager:** `<!-- TODO: e.g., pip / npm -->`  

## Critical Constraints

> [!CAUTION]
> 1. **Never commit secrets.** Do not add API keys, tokens, or credentials anywhere.
> 2. **Do not modify `LICENSE` or `NOTICE`.** These are legally binding.
> 3. **Do not modify workflow trigger conditions** without human review.
> 4. **All new source files must include the Apache 2.0 copyright header.**
> 5. **Use `{{double_braces}}` for template placeholders.** Never hard-code them.

## Repository Layout

- `.github/workflows/`: CI/CD pipelines. Files prefixed with `_` are reusable templates.
- `docs/`: MkDocs Material source.
- `src/`: Primary application source code.
- `tests/`: Organized into `unit/`, `integration/`, and `e2e/`.

## Executable Commands

- **Linting:** `<!-- TODO: language specific lint command -->`
- **Testing:** `<!-- TODO: language specific test command -->`
- **Docs:** `mkdocs serve` / `mkdocs build`
- **Build:** `<!-- TODO: language specific build command -->`

## Code Style & Patterns

- **No magic strings or numbers** — define constants.
- **Prefer explicit over implicit.**
- **One responsibility per module.**
- Every public function, class, and module must have a docstring.
- Follow [Conventional Commits](https://www.conventionalcommits.org/).

## GitHub Actions Workflows

- **Reusable Templates (`_*.yml`):** Never trigger directly. Ensure changes are backward-compatible.
- **Lifecycle:**
  - `development.yml`: PR open/sync (unit + smoke)
  - `main.yml`: Push to `main` (unit + integration + sanity)
  - `nightly.yml`, `weekly.yml`, `release.yml`: Standard scheduled/release flows.

## Documentation

- **`docs/`** and **`mkdocs.yml`** control the site. Do not create docs outside the `nav:` tree.
- `docs/index.md` dynamically includes `README.md` via MkDocs snippets.
- Use `{{placeholder}}` variables for templated fields (e.g., `{{project_name}}`, `{{organization}}`).

## Agent Notes

_Add notes here when updating instructions for AI agents._

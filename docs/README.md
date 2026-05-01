# Documentation

This directory contains the source files for the `{{project_name}}` documentation site, built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Directory Structure

```
docs/
├── assets/              # Branding assets (logos, diagrams, favicons)
├── community/           # Contributing, Code of Conduct, Security, Support
├── examples/            # Runnable code examples and demos
├── getting-started/     # Installation, quick start, and workflow guides
├── guides/              # Task-oriented how-to guides
├── reference/           # API reference and configuration schema
├── scripts/             # Custom JavaScript for the docs site (extra.js)
├── stylesheets/         # Custom CSS for the docs site (extra.css)
├── index.md             # Docs home page (hero landing page)
└── README.md            # This file
```

The MkDocs configuration lives at the repository root: [`mkdocs.yml`](../mkdocs.yml).


## Prerequisites

- **Python 3.9+** — Required to run MkDocs and its plugins.
- **pip** — For installing documentation dependencies.

All documentation dependencies are listed in `docs/requirements.txt`. Install them with:

```bash
pip install -r docs/requirements.txt
```

> **Tip:** See [DEVELOPING.md](../DEVELOPING.md) for the full local setup guide. Even if your main project is not in Python, the documentation is built with MkDocs and requires a Python environment to build locally.



## Local Development

### Serve the Docs Locally

Start the live-reloading development server from the **repository root**:

```bash
mkdocs serve
```

The site will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000). Any change you save to a source file is reflected immediately in the browser — no manual refresh needed.

### Specify a Custom Host or Port

```bash
mkdocs serve --dev-addr 0.0.0.0:8080
```

### Template Variables

All `{{ variable }}` references in the docs (e.g. `{{ project_name }}`, `{{ org_name }}`) are driven by the `extra:` block in [`mkdocs.yml`](../mkdocs.yml). Update those values once and the change propagates across the entire site:

```yaml
# mkdocs.yml
extra:
  project_name: "my-project"
  org_name:     "my-org"
  # ... other variables
```


## Building the Docs

Produce a static build of the site in the `site/` directory:

```bash
mkdocs build
```

> The `site/` directory is intentionally excluded from version control via `.gitignore`. Do **not** commit it manually.

To perform a clean build (removes the previous `site/` output first):

```bash
mkdocs build --clean
```

Validate that all internal links resolve correctly:

```bash
mkdocs build --strict
```

The `--strict` flag is recommended before opening a pull request or cutting a release to catch broken links early.


## Publishing the Docs

### Automated Publishing (Recommended)

Documentation is published automatically to **GitHub Pages** on every merge to `main` (or on a tagged release, depending on your workflow configuration). No manual steps are required — simply merge your changes and the CI/CD pipeline handles the rest.

See the relevant workflow file in [`.github/workflows/`](../.github/workflows/) for the exact trigger and deployment steps.

### Manual Publishing

If you need to publish outside of the normal CI/CD cycle, run the following from the **repository root**:

```bash
mkdocs gh-deploy --force
```

This command builds the static site and force-pushes it to the `gh-pages` branch of your repository, which GitHub Pages then serves automatically.

> **Note:** Manual deploys require you to have write access to the repository and a configured `git` identity (`user.name` and `user.email`).

#### Dry-run First

To preview what `gh-deploy` would do without actually pushing:

```bash
mkdocs gh-deploy --dry-run
```


## Adding and Editing Pages

1. **Create a new `.md` file** in the appropriate subdirectory (e.g., `guides/my-new-guide.md`).
2. **Register it in the nav** by adding an entry to the `nav:` block in [`mkdocs.yml`](../mkdocs.yml).
3. **Preview locally** with `mkdocs serve` before opening a pull request.

### Page Metadata

Every page should include a top-level `# Heading` that matches its nav label. Optionally, add MkDocs front matter for advanced layout control:

```yaml
---
hide:
  - toc        # Hide the table of contents
  - navigation # Hide the left-hand nav
---
```

### Admonitions

This site uses [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/) and MkDocs Material admonitions. Use them liberally:

```markdown
!!! note
    This is an informational note.

!!! warning
    This is a warning.
```


## Common Troubleshooting

| Symptom | Likely Cause | Fix |
| :--- | :--- | :--- |
| `mkdocs: command not found` | Dependencies not installed | `pip install mkdocs mkdocs-material mkdocs-macros-plugin pymdown-extensions` |
| `{{ variable }}` renders literally | `mkdocs-macros-plugin` missing or misconfigured | Confirm `macros` is listed under `plugins:` in `mkdocs.yml` |
| Broken links on `--strict` build | Missing or misnamed file in `nav:` | Verify file path and `nav:` registration in `mkdocs.yml` |
| Styles missing in local preview | Custom CSS path wrong | Confirm `extra_css` path in `mkdocs.yml` matches `docs/stylesheets/extra.css` |
| `gh-deploy` push rejected | Stale `gh-pages` branch | Use `mkdocs gh-deploy --force` or delete and re-create the `gh-pages` branch |


## Related Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs Macros Plugin](https://mkdocs-macros-plugin.readthedocs.io/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
- [GitHub Pages — Publishing Source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

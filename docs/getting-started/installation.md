# Installation

This page covers all supported installation methods for `{{ project_name }}`.


## Requirements

Before installing, ensure your system meets the following prerequisites:

| Requirement | Minimum Version | Notes |
| :--- | :--- | :--- |
| **Language** | <!-- INSERT VERSION --> | Required for all installation methods |
| **Package Manager**| <!-- INSERT VERSION --> | Required for dependencies |
| **Git** | 2.x | Required for source installs |
| **Docker** | 24.x | Optional — for containerized installs |


## Standard Installation

The recommended way to install `{{ project_name }}` for most users:

```bash
<!-- INSERT INSTALLATION COMMAND HERE -->
# e.g., npm install {{project_name}} OR pip install {{project_name}} OR cargo add {{project_name}}
```

### Verify the Installation

After installation, confirm it is working correctly:

```bash
{{ project_name }} --version
```

You should see output similar to:

```console
{{ project_name }} 0.1.0
```


## Install from Source

To install the latest unreleased code directly from the repository:

```bash
git clone https://github.com/{{ org_name }}/{{ project_name }}.git
cd {{ project_name }}

# Install dependencies for development
<!-- INSERT SOURCE INSTALLATION COMMAND HERE -->
# e.g., npm ci OR pip install -e ".[dev]" OR cargo build
```

> [!TIP]
> This is the recommended setup for contributors looking to make changes to the source code.


## Docker Installation

A pre-built Docker image is available for containerized environments:

```bash
# Pull the latest image
docker pull ghcr.io/{{ org_name }}/{{ project_name }}:latest

# Run a one-off command
docker run --rm ghcr.io/{{ org_name }}/{{ project_name }}:latest {{ project_name }} --version
```

For a persistent, volume-mounted setup using Docker Compose, see the `docker-compose.yml` in the root of the repository.


## Platform-Specific Notes

=== "macOS"

    <!-- INSERT MACOS INSTRUCTIONS HERE -->

=== "Linux"

    <!-- INSERT LINUX INSTRUCTIONS HERE -->

=== "Windows"

    <!-- INSERT WINDOWS INSTRUCTIONS HERE -->


## Upgrading

To upgrade an existing installation to the latest release:

```bash
<!-- INSERT UPGRADE COMMAND HERE -->
```


## Uninstalling

```bash
<!-- INSERT UNINSTALL COMMAND HERE -->
```


## Troubleshooting

| Problem | Solution |
| :--- | :--- |
| `command not found: {{ project_name }}` | Ensure the binaries directory is on your `$PATH`. |
| Import errors after install | Ensure you have the latest version installed. |
| Version conflicts | Isolate your dependencies using your language's recommended tool. |

If you continue to experience issues, please visit our [Support page](../community/support.md).


**Next:** [Quick Start &rarr;](quickstart.md)

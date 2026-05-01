# Workflows

This page walks through the most common end-to-end usage patterns for `{{ project_name }}`. Each workflow is a self-contained user story — pick the one that matches your use case.

> [!NOTE]
> These are placeholder workflows. Replace each section with the real workflows that users of your project will follow.


## Workflow 1 — Basic Usage

**Goal:** Perform the most common, standard operation with `{{ project_name }}`.

### Steps

1. **Initialize the client**

    ```text
    <!-- INSERT CLIENT INITIALIZATION CODE HERE -->
    ```

2. **Configure your inputs**

    ```text
    <!-- INSERT CONFIGURATION CODE HERE -->
    ```

3. **Execute the action**

    ```text
    <!-- INSERT EXECUTION CODE HERE -->
    ```

4. **Handle the output**

    ```text
    <!-- INSERT OUTPUT HANDLING CODE HERE -->
    ```


## Workflow 2 — Docker-Based Execution

**Goal:** Run `{{ project_name }}` in a containerized environment without any local setup.

### Steps

1. **Pull the image**

    ```bash
    docker pull ghcr.io/{{ org_name }}/{{ project_name }}:latest
    ```

2. **Run with environment variables**

    ```bash
    docker run --rm \
      -e API_KEY="YOUR_KEY" \
      -v $(pwd)/output:/app/output \
      ghcr.io/{{ org_name }}/{{ project_name }}:latest \
      {{ project_name }} run --output /app/output
    ```

3. **Inspect the output**

    ```bash
    ls ./output/
    ```


## Workflow 3 — CI/CD Integration

**Goal:** Integrate `{{ project_name }}` into a GitHub Actions pipeline.

```yaml
# .github/workflows/run.yml
name: Run {{ project_name }}

on: [push]

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up environment
        # <!-- INSERT LANGUAGE SETUP ACTION HERE -->

      - name: Install {{ project_name }}
        run: |
          # <!-- INSERT INSTALLATION COMMAND HERE -->

      - name: Run action
        env:
          API_KEY: ${{ "{{" }} secrets.API_KEY {{ "}}" }}
        run: {{ project_name }} run --config config.yaml
```


**Need more?** See the [Guides](../guides/index.md) section for in-depth task-specific documentation or browse the [Examples](../examples/index.md) for runnable code.

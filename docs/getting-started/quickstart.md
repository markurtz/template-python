# Quick Start

This guide gets you from a fresh installation to running your first command in under 5 minutes.

> [!NOTE]
> Make sure you have completed [Installation](installation.md) before continuing.


## Step 1 — Initialize Your Environment

If you haven't already, set up your project and install `{{ project_name }}`:

```bash
<!-- INSERT SETUP AND INSTALLATION COMMAND HERE -->
# e.g., npm init && npm install {{project_name}}
```


## Step 2 — Verify the Install

```bash
{{ project_name }} --version
```

Expected output:

```console
{{ project_name }} 0.1.0
```


## Step 3 — Run Your First Command

```text
<!-- INSERT YOUR LANGUAGE SPECIFIC HELLO WORLD SNIPPET HERE -->
// e.g., Javascript, Python, Go, Rust
import { Client } from '{{ project_name }}';

// Initialize the client
const client = new Client({ apiKey: "YOUR_KEY" });

// Run a core action
const result = await client.runAction("hello_world");
console.log(result);
```

Expected output:

```console
[INFO] Initializing {{ project_name }} client...
[SUCCESS] Action completed! Result: Hello, World from {{ project_name }}!
```

> [!TIP]
> Replace `"YOUR_KEY"` with your actual API key or credentials. See the [Reference](../reference/index.md) for all available client configuration options.


## Step 4 — Explore Further

Now that your first command works, explore what `{{ project_name }}` can do:

- **[Workflows](workflows.md)** — Common end-to-end usage patterns
- **[Guides](../guides/index.md)** — Task-specific deep dives
- **[Reference](../reference/index.md)** — Full API and CLI documentation
- **[Examples](../examples/index.md)** — Runnable code examples


**Next:** [Workflows &rarr;](workflows.md)

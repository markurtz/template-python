# ---------------------------------------------------------
# {{project_name}} Dockerfile
# Licensed under the Apache License, Version 2.0
# ---------------------------------------------------------
# Standardized Multi-stage Dockerfile Template

# ---------------------------------------------------------
# Build Stage
# ---------------------------------------------------------
# Choose an appropriate base image for building (e.g., ubuntu, alpine, node, golang)
FROM ubuntu:24.04 AS builder

# Set working directory
WORKDIR /app

# Install system build dependencies (if any)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------
# [DEPENDENCIES]
# Copy package manifests (package.json, Cargo.toml, go.mod, etc.) 
# and install dependencies to leverage Docker layer caching.
# Example: 
# COPY package*.json ./
# RUN npm ci
# ---------------------------------------------------------

# Copy application source code
COPY src/ ./src/

# ---------------------------------------------------------
# [BUILD]
# Run your compilation or build step here.
# Example:
# RUN npm run build
# RUN make build
# ---------------------------------------------------------

# ---------------------------------------------------------
# Runtime Stage
# ---------------------------------------------------------
# Choose a minimal base image for runtime (e.g., ubuntu, alpine, distroless)
FROM ubuntu:24.04

# OCI Standard Labels
LABEL org.opencontainers.image.title="{{project_name}}"
LABEL org.opencontainers.image.description="Production-ready application container"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.source="https://github.com/{{organization}}/{{project_name}}"

# Define environment variables
ENV APP_ENV=production

# Set working directory
WORKDIR /app

# Create a non-root user and set permissions
RUN useradd -m appuser && chown -R appuser /app

# ---------------------------------------------------------
# [RUNTIME_ARTIFACTS]
# Copy necessary built artifacts from the builder stage.
# Example:
# COPY --from=builder --chown=appuser:appuser /app/dist ./dist
# COPY --from=builder --chown=appuser:appuser /app/bin/server ./server
# ---------------------------------------------------------

# Copy generic source files if needed (uncomment or modify as required)
# COPY --chown=appuser:appuser src/ ./src/

# Switch to the non-root user for security
USER appuser

# Expose necessary ports
EXPOSE 8080

# Define the command to run the application
# Replace with the language-specific startup command (e.g., ["node", "dist/index.js"])
CMD ["/bin/sh", "-c", "echo 'Please define a runtime command in the Dockerfile!'; exit 1"]

# Adapted from backend/Dockerfile
# Also see https://docs.astral.sh/uv/guides/integration/docker/

# ---
# Stage 1: build the application in the `/app` directory.
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}astral/uv:python3.14-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Omit development dependencies
ENV UV_NO_DEV=1

# Disable Python downloads - use the system interpreter across both images.
ENV UV_PYTHON_DOWNLOADS=0

# Increase HTTP timeout for slow networks
ENV UV_HTTP_TIMEOUT=300

WORKDIR /app

# Copy root workspace files using additional_contexts
COPY --from=workspace pyproject.toml uv.lock /app/

# Copy mcp packages for workspace dependencies
COPY --from=workspace mcp /app/mcp

# Copy nanobot-websocket-channel packages for workspace dependencies
COPY --from=workspace nanobot-websocket-channel /app/nanobot-websocket-channel

# Copy nanobot project
COPY pyproject.toml /app/nanobot/pyproject.toml

# Install nanobot dependencies first (before copying all source)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-workspace --package nanobot

# Copy all nanobot source files
COPY . /app/nanobot/

# Sync nanobot package with all dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --package nanobot

# ---
# Stage 2: use a final image without uv
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}python:3.14.2-slim-bookworm

# Set environment variables for Python and application
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Make sure we use UTF-8 encoding
ENV LANG=C.UTF-8

# Setup a non-root user with configurable UID/GID
ARG APP_UID=999
ARG APP_GID=999
RUN groupadd --system --gid ${APP_GID} nonroot \
    && useradd --system --gid ${APP_GID} --uid ${APP_UID} --create-home nonroot

# Copy the application from the builder
COPY --from=builder --chown=nonroot:nonroot /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"
# Add nanobot to PYTHONPATH so the package can be found
ENV PYTHONPATH="/app/nanobot:${PYTHONPATH:-}"

# Use the non-root user
USER nonroot

# Use /app as working directory
WORKDIR /app

# Run the nanobot gateway via entrypoint
CMD ["python", "/app/nanobot/entrypoint.py"]

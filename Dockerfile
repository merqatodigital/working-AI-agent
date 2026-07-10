# KAPWA Resort OS - Backend Dockerfile
FROM python:3.12-slim AS base

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Set working directory
WORKDIR /app

# Copy workspace configuration first for caching
COPY pyproject.toml uv.lock ./
COPY packages/resort-types/pyproject.toml packages/resort-types/
COPY packages/resort-data/pyproject.toml packages/resort-data/
COPY packages/resort-tools/pyproject.toml packages/resort-tools/
COPY packages/agent-core/pyproject.toml packages/agent-core/
COPY apps/agent-api/pyproject.toml apps/agent-api/

# Install dependencies (cached layer)
RUN uv sync --frozen --no-dev

# Copy source code
COPY packages/ packages/
COPY apps/agent-api/ apps/agent-api/

# Ensure all packages are installed
RUN uv sync --frozen --no-dev

# Expose port
EXPOSE 8001

# Start the FastAPI server
CMD ["uv", "run", "--package", "agent-api", "uvicorn", "agent_api.main:app", "--host", "0.0.0.0", "--port", "8001"]
FROM python:3.12-slim

WORKDIR /app

# System deps (keep minimal; add build tools only if needed later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy project
COPY . /app

# Install dependencies (uses uv.lock if present)
RUN uv sync --frozen || uv sync

# Default command: run tests
CMD ["uv", "run", "pytest", "-q"]

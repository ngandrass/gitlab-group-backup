FROM python:3.10-slim

# Install runtime dependencies
ENV RUN_DEPS="curl"
RUN set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends $RUN_DEPS && \
    rm -rf /var/lib/apt/lists/*

# Add dependency management files
COPY ./poetry.lock /app/
COPY ./pyproject.toml /app/
WORKDIR /app

# Install Poetry and Python packages
ENV POETRY_VERSION=1.2.0
RUN set -ex && \
    curl -sSL https://install.python-poetry.org | python - --version=${POETRY_VERSION} && \
    export PATH="/root/.local/bin:${PATH}" && \
    poetry config virtualenvs.create false && \
    # Install dependencies using poetry
    poetry install && \
    # Create output directory
    mkdir -p /data

# Add application code
COPY . /app

# Run application
CMD ["/bin/bash", "-c", "/app/main.py --gitlab-url=${GITLAB_URL} --access-token=${GITLAB_ACCESS_TOKEN} --group-id=${GITLAB_GROUP_ID} --output-dir=/data"]

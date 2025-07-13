# Start from a slim Python image
FROM python:3.13-slim-bookworm
LABEL maintainer="Hyan Batista"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY pyproject.toml uv.lock /code/
COPY . /code
COPY ./scripts /scripts

WORKDIR /code

ARG LOCAL=false

RUN uv venv --seed && \
    . .venv/bin/activate && \
    if [ "$LOCAL" = "true" ]; then \
        echo "--- Installing all dependencies for development ---" && \
        uv sync --locked; \
    else \
        echo "--- Installing production dependencies ---" && \
        uv sync --locked --no-group dev; \
    fi && \
    adduser \
        --disabled-password \
        --gecos "" \
        --home /code \
        --shell /bin/bash \
        --uid 1000 \
        appuser && \
    chmod -R +x /scripts

ENV PATH=/code/.venv/bin:/scripts:$PATH

USER appuser

CMD [ "run.sh" ]
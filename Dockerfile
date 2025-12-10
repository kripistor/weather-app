FROM python:3.13-slim
RUN pip install --upgrade pip
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root
COPY main.py ./
EXPOSE 8000
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]
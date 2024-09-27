FROM python:3.11

EXPOSE 9090

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./src ./src

CMD ["python", "-m", "src", "--host", "0.0.0.0", "--port", "9090"]
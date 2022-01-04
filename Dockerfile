FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

EXPOSE 80
ADD Pipfile.lock /app
ADD Pipfile /app

RUN python -m pip install pipenv
RUN python -m pipenv install --system --deploy --ignore-pipfile

COPY ./app /app

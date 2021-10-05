FROM python:3.8

COPY ./app /app

WORKDIR /app

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install \
    && rm -rf /tmp/pip-tmp

WORKDIR  /var/log/gunicorn

ENV TZ Asia/Tokyo

ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /app

CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker",  "main:app", "--log-config", "logging.conf"]

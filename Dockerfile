FROM python:3.8-slim-buster

RUN set -ex \
    && apt-get update -y \
    && apt-get install -y libpq-dev build-essential postgresql-client \
    && mkdir /code \
    && groupadd -g 999 appuser \
    && useradd -r -d /code -u 999 -g appuser appuser

WORKDIR /code

COPY . /code

COPY requirements/main.txt ./requirements/main.txt

RUN pip install -U pip \
    && pip install -r requirements/main.txt \
    && chown -R appuser:appuser -R /code

USER appuser

ENTRYPOINT ["bash", "/code/build_test.sh"]

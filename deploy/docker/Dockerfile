FROM python:3.9

ENV PYTHONPATH "${PYTHONPATH}:/srv:/srv/src"

COPY . /srv/
WORKDIR /srv

RUN pip install pipenv \
    && adduser -u 1000 --gecos "" --disabled-password tgo \
    && mkdir /venv \
    && chown -R tgo:tgo /venv \
    && chown -R tgo:tgo /srv

USER tgo

RUN pipenv install --ignore-pipfile --dev

EXPOSE 8000
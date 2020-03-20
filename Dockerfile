FROM  python:3.8.2-slim-buster

LABEL maintainer = "Ian Wang <ian.wang@qbe.com>"

USER root

RUN apt-get update && apt-get -y --no-install-recommends install \
    ca-certificates \
    curl \
    gcc \
    g++ \
    vim \
    gpg

RUN apt-get install -y gosu

WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

WORKDIR /opt/server

RUN pip3 --no-cache-dir install -r /tmp/requirements.txt

COPY app /opt/server/app
COPY config.py /opt/server/
COPY main.py /opt/server/


# ---- Base python ----
ARG PYTHON_VERSION=3.6-alpine
FROM python:$PYTHON_VERSION as base

WORKDIR /app

ENV PYTHONDONTWRITEBYECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache --virtual .build-deps \
    build-base \
    freetype-dev \
    linux-headers \
    openssl-dev \
    libffi-dev \
    python3-dev \
    jpeg-dev \
    zlib-dev \
    musl-dev \
    gettext \
    gcc \
    py-pip \
    wget \
    libxslt-dev \
    xmlsec-dev

COPY . /app


CMD ["python", "./kombat.py"]

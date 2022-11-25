# ---- Base python ----
ARG PYTHON_VERSION=3.6-alpine
FROM python:$PYTHON_VERSION as base

WORKDIR /app

COPY . /app

CMD ["python", "./kombat.py"]

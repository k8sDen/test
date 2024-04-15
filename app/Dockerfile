FROM --platform=linux/amd64 python:3.10-slim-buster
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app/ .
COPY scripts/docker-entrypoint.sh .
RUN chmod +x /code/docker-entrypoint.sh
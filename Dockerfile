FROM python:3.10.2-alpine3.15

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade --available
RUN pip install -r requirements.txt

WORKDIR /app
ADD . /app


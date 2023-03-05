FROM python:3.9-slim

RUN apt-get update && apt-get install gcc -y
RUN pip install --upgrade pip
RUN mkdir /backend
WORKDIR /backend

ADD requirements.txt /backend/
RUN pip install -r requirements.txt

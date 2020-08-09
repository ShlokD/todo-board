FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -g python-pip python-dev

RUN pip install -r requirements.txt

EXPOSE 5000

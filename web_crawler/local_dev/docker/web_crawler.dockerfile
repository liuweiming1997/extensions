FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 libmysqlclient-dev python3-pip python3-mysqldb

RUN pip3 install --no-cache-dir --upgrade pip
RUN ["/bin/bash", "-c", "pip3 install --upgrade setuptools"]

ARG WORKSPACE="/python3/web_crawler"
COPY ./app ${WORKSPACE}/app
COPY ./local_dev/docker ${WORKSPACE}/local_dev/docker

WORKDIR ${WORKSPACE}/local_dev/docker
RUN pip3 install -r ./requirements.txt

WORKDIR ${WORKSPACE}/app

ENTRYPOINT ["python3", "-u", "main.py"]

FROM ubuntu:16.04

# proxy for apt-get
COPY ./local_dev/docker/sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 uwsgi libmysqlclient-dev python3-pip python3-mysqldb nginx uwsgi-plugin-python3

# proxy for pip3 install
COPY ./local_dev/docker/pip.conf /etc/pip.conf

RUN pip3 install --no-cache-dir --upgrade pip
RUN ["/bin/bash", "-c", "pip3 install --upgrade setuptools"]

ARG WORKSPACE="/python3/server"
COPY ./app ${WORKSPACE}/app
COPY ./local_dev/docker ${WORKSPACE}/local_dev/docker

WORKDIR ${WORKSPACE}/local_dev/docker
RUN pip3 install -r ./chrome_server_requirements.txt

WORKDIR ${WORKSPACE}/app

ENTRYPOINT nginx -g "daemon on;" && uwsgi myapp.ini

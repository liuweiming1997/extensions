FROM ubuntu:16.04

# proxy for apt-get
COPY ./local_dev/docker/sources.list /etc/apt/sources.list

# proxy for pip3 install
COPY ./local_dev/docker/pip.conf /etc/pip.conf

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 libmysqlclient-dev python3-pip python3-mysqldb cron vim

RUN pip3 install --no-cache-dir --upgrade pip
RUN ["/bin/bash", "-c", "pip3 install --upgrade setuptools"]

ARG WORKSPACE="/python3/web_crawler"
COPY ./app ${WORKSPACE}/app
COPY ./local_dev/docker ${WORKSPACE}/local_dev/docker

WORKDIR ${WORKSPACE}/local_dev/docker
RUN pip3 install -r ./requirements.txt

ADD ./app/crontab-crawler /var/spool/cron/crontabs/root
RUN chmod 600 /var/spool/cron/crontabs/root

WORKDIR ${WORKSPACE}

ENTRYPOINT cron && ":" >> /log/crawler/crontab.log && tail -f /log/crawler/crontab.log

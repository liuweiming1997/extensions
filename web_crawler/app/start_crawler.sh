#!/bin/bash
set -e

CHECK_FILE_NAME="check_file_name"

cd /python3/web_crawler
echo -n "start doing in ${PWD} ---> "

PID=`ps -aux | grep "start_crawler.sh" | awk '{print $2}'`

if [[ ${PID} ]]; then
  echo "PID in ${PID} job exists"
  exit;
fi

python3 app/main.py

echo "job finish"

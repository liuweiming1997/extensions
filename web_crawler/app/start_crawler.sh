#!/bin/bash
set -e

CHECK_FILE_NAME="check_file_name"

cd /python3/web_crawler
echo -n "start doing in ${PWD} ---> "

if [[ -f ${CHECK_FILE_NAME} ]]; then
  echo "file in ${PWD}/${CHECK_FILE_NAME}, so job exists"
  exit;
fi

touch ${CHECK_FILE_NAME}
python3 app/main.py
rm -rf ${CHECK_FILE_NAME}
echo "rm -rf ${PWD}/${CHECK_FILE_NAME}, so job finish"

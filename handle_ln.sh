#!/bin/bash

rm -rf server/app/common
rm -rf server/app/models

cp -r web_crawler/app/common server/app/
cp -r web_crawler/app/models server/app/

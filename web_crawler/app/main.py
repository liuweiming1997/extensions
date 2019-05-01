#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from request_client.meituan.meishi import web_crawler_meituan_meishi
from request_client.douban.dianying import web_crawler_douban_dianying
from request_client.medium.programming import web_crawler_medium_programming

if __name__ == '__main__':
    web_crawler_meituan_meishi.do()
    web_crawler_douban_dianying.do()
    web_crawler_medium_programming.do()

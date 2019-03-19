#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from request_client.meituan.meishi import web_crawler_meituan_meishi
from request_client.douban.dianying import web_crawler_douban_dianying

if __name__ == '__main__':
    web_crawler_meituan_meishi.do()
    web_crawler_douban_dianying.do()

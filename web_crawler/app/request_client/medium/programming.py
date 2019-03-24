#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from lxml import etree
import requests

from lib.re_util import ReUtil
from common.lib.logger import log
from models.douban.dianying import Dianying
from request_client.base import BaseApi
from .programming_config import cookies_str

base_programming_url = 'https://medium.com/topic/programming'
popular_in_programmer = '//*[@id="root"]/div/section/section[2]/div/div[9]'

proxy = '127.0.0.1:1080'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}

class web_crawler_medium_programming(BaseApi):
    def __init__(self):
        super().__init__()

    @classmethod
    def get_cookies(cls):
        return cookies_str

    @classmethod
    def get_headers(cls):
        return None

    @classmethod
    def do(cls):
        response = cls.get('https://ip.cn/', proxies=proxies)
        print(response.text)
        # root = etree.HTML(response.text)
        # div_list_popluar = root.xpath(popular_in_programmer)
        # print(div_list_popluar)

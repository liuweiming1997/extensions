#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from lxml import etree
import requests

from lib.re_util import ReUtil
from lib.hash_util import HashUtil
from common.lib.logger import log
from models.medium.programming import Programming
from request_client.base import BaseApi
from .programming_config import cookies_str

base_programming_url = 'https://medium.com/topic/programming'
popular_in_programmer = '//*[@id="root"]/div/section/section[2]/div/div[9]/div'

proxy = '127.0.0.1:1080'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5h://' + proxy
}

def format_url(url):
    if url.startswith('http'):
        return url
    return 'https://medium.com' + url

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
    def get_by_proxies(cls, url):
        return cls.get(base_programming_url, proxies=proxies)

    @classmethod
    def fetch_avatar_url(cls, url):
        response = cls.get_by_proxies(url)
        root = etree.HTML(response.text)
        img_class = root.xpath('//*[@id="_obv.shell._surface_1553479885925"]/div/main/article/div/section[1]/div[2]/div/div/div[1]/a/img')
        print(img_class)

    @classmethod
    def handle_one_page(cls, one_page):
        try:
            url = one_page.xpath('article/div/div/a/@href')[0]
            title = one_page.xpath('article/div/div/a/div/h4/text()')[0]
            hash_id = HashUtil.get_hash_by_string(url)
            Programming.load_or_create(hash_id, title, format_url(url))
        except Exception as e:
            log.error(str(e))

    @classmethod
    def do(cls):
        response = cls.get_by_proxies(base_programming_url)
        root = etree.HTML(response.text)
        div_list_popluar = root.xpath(popular_in_programmer)
        for one_page in reversed(div_list_popluar):
            cls.handle_one_page(one_page)

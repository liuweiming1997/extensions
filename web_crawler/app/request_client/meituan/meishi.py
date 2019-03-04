#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

from request_client.base import BaseApi
from .meituan_config import cookies_str
from lib.re_util import ReUtil

base_url = 'https://sd.meituan.com/meishi/'

class web_crawler_meituan_meishi(BaseApi):
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
        response = cls.get(base_url)
        regex = ReUtil.get_regex(begin_with=['"poiInfos":'], end_with=['},"comHeader"'])
        result = regex.findall(response.text)
        print(result[0][1])

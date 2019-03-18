#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import requests

from request_client.base import BaseApi
from .dianying_config import cookies_str
from lib.re_util import ReUtil

base_url = 'https://maoyan.com/board/6'

class web_crawler_maoyan_dianying(BaseApi):
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
        print(response.text)

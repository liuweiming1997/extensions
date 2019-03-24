#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy

import requests

origin_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'
}

def parse_headers(headers: dict):
    result = copy.deepcopy(origin_headers)
    if not headers:
        return result
    for key, value in headers.items:
        result.setdefault(key, value)
    return result

def parse_cookies(cookies_str: str):
    cookies_dict = {}
    if not cookies_str:
        return cookies_dict
    for cookie in cookies_str.split(";"):
        k, v = cookie.split("=", 1)
        cookies_dict[k.strip()] = v.strip()
    return cookies_dict

class BaseApi:
    def __init__(self):
        pass

    @classmethod
    def get(cls, url, proxies=None):
        session = requests.Session()
        response = session.get(
            url=url,
            cookies=parse_cookies(cls.get_cookies()),
            headers=parse_headers(cls.get_headers()),
            timeout=12, #in seconds
            proxies=proxies,
        )
        response.encoding = 'utf-8'
        return response

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from lxml import etree
import requests

from request_client.base import BaseApi
from .dianying_config import cookies_str

base_url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'

on_show = '//*[@id="nowplaying"]/div[2]/ul/li'

class web_crawler_douban_dianying(BaseApi):
    def __init__(self):
        super().__init__()

    @classmethod
    def get_cookies(cls):
        return cookies_str

    @classmethod
    def get_headers(cls):
        return None

    @classmethod
    def handle_one_item(cls, one_item):
        html = etree.HTML(etree.tostring(one_item).decode('utf-8'))
        title = html.xpath('//li/@data-title')[0]
        score = html.xpath('//li/@data-score')[0]
        region = html.xpath('//li/@data-region')[0]
        img = html.xpath('//li/ul/li/a/img/@src')[0]
        url, buy_ticket = html.xpath('//li/ul/li/a/@href')[0], html.xpath('//li/ul/li/a/@href')[2]
        print([title, score, region, img, url, buy_ticket])


    @classmethod
    def do(cls):
        response = cls.get(base_url)
        root = etree.HTML(response.text)
        li_list_on_show = root.xpath(on_show)
        for one_item in li_list_on_show:
            cls.handle_one_item(one_item)

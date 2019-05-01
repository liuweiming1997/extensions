#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from lxml import etree
import requests

from lib.re_util import ReUtil
from common.lib.logger import log
from models.douban.dianying import Dianying
from request_client.base import BaseApi
from .dianying_config import cookies_str

base_onshow_url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
base_upcoming_url = 'https://movie.douban.com/cinema/later/guangzhou/'


on_show = '//*[@id="nowplaying"]/div[2]/ul/li'
upcoming = '//*[@id="showing-soon"]/div'

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
    def handle_onshow_one_item(cls, one_item):
        # print(etree.tostring(one_item).decode('utf-8'))
        # html = etree.HTML(etree.tostring(one_item).decode('utf-8'))
        try:
            file_id = one_item.xpath('@id')[0]
            title = one_item.xpath('@data-title')[0]
            score = one_item.xpath('@data-score')[0]
            region = one_item.xpath('@data-region')[0]
            img = one_item.xpath('ul/li/a/img/@src')[0]
            url, buy_ticket = one_item.xpath('ul/li/a/@href')[0], one_item.xpath('ul/li/a/@href')[2]

            dianying_obj = {
                'fileId': file_id,
                'img': img,
                'title': title,
                'score': score,
                'region': region,
                'url': url,
                'buyTicket': buy_ticket,
                'onShowTime': None,
            }
            return dianying_obj
        except Exception as e:
            log.error("crawler onshow file list error " + repr(e))

    @classmethod
    def do_onshow(cls):
        response = cls.get(base_onshow_url)
        root = etree.HTML(response.text)
        li_list_on_show = root.xpath(on_show)

        onshow_list = []
        for one_item in li_list_on_show:
            obj = cls.handle_onshow_one_item(one_item)
            if obj:
                onshow_list.append(obj)
        Dianying.load_or_create(onshow_list, is_onshow=True)

    # buy_ticket will be a forward look
    @classmethod
    def handle_upcoming_one_item(cls, one_item):
        # print(etree.tostring(one_item).decode('utf-8'))
        try:
            url = one_item.xpath('a/@href')[0]
            img = one_item.xpath('a/img/@src')[0]
            title = one_item.xpath('div/h3/a/text()')[0]
            detail_list = one_item.xpath('div/ul/li')
            onshow_time, region, score = detail_list[0].xpath('text()')[0], detail_list[2].xpath('text()')[0], detail_list[3].xpath('span/text()')[0]
            buy_ticket = one_item.xpath('div/ul/a/@href')

            dianying_obj = {
                'fileId': ReUtil.get_all_number_to_list(url)[0],
                'img': img,
                'title': title,
                'score': score[:-3],
                'region': region,
                'url': url,
                'buyTicket': buy_ticket,
                'onShowTime': onshow_time,
            }
            return dianying_obj
        except Exception as e:
            log.error("crawler upcoming file list error " + repr(e))

    @classmethod
    def do_upcoming(cls):
        response = cls.get(base_upcoming_url)
        root = etree.HTML(response.text)
        div_list_upcoming = root.xpath(upcoming)
        upcoming_list = []
        for item in div_list_upcoming:
            obj = cls.handle_upcoming_one_item(item)
            if obj:
                upcoming_list.append(obj)
        Dianying.load_or_create(upcoming_list, is_onshow=False)

    @classmethod
    def do(cls):
        cls.do_onshow()
        cls.do_upcoming()

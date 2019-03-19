import json

import requests
from lxml import etree

from request_client.base import BaseApi
from .dianying_config import cookies_str
from lib.re_util import ReUtil

base_url = 'https://maoyan.com/'
on_show = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/dl'

class web_crawler_maoyan_dianying(BaseApi):
    DD = '<dd>'
    Finish_DD = '</dd>'

    def __init__(self):
        super().__init__()

    @classmethod
    def get_cookies(cls):
        return cookies_str

    @classmethod
    def get_headers(cls):
        return None

    @classmethod
    def handle_dd(cls, one_item) -> 'string[8]':
        base_string = etree.tostring(one_item).decode('utf-8')
        print(base_string)
        ans = []
        one_ans, complete_word, before = '', '', False

        for idx in range(len(base_string)):
            ch = base_string[idx]
            complete_word += ch
            if ch == '>':
                if cls.DD in complete_word:
                    if before:
                        one_ans += cls.Finish_DD
                        ans.append(one_ans)
                        one_ans = cls.DD
                        complete_word = ''
                    else:
                        before = True
                        one_ans += complete_word
                        complete_word = ''
                elif cls.Finish_DD in complete_word:
                    one_ans += cls.Finish_DD
                    ans.append(one_ans)
                    break
                else:
                    one_ans += complete_word
                    complete_word = ''
        return ans;


    @classmethod
    def handle_one_html(cls, html):
        root = etree.HTML(html)
        file_url = base_url + root.xpath('//dd/div/a/@href')[0]
        print(file_url)

    @classmethod
    def do(cls):
        response = cls.get(base_url)
        root = etree.HTML(response.text)
        on_show_movie_list = root.xpath(on_show)[0]
        html_list = cls.handle_dd(on_show_movie_list[0])
        # for one_html in html_list:
        #     cls.handle_one_html(one_html)

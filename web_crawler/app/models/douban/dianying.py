#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
import functools

from common.lib.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text, JSON
from sqlalchemy.sql import func

def convert_to_static_dianying(search_result):
    if not search_result:
        return None
    if isinstance(search_result, Iterable):
        result = []
        for one_dianying in search_result:
            result.append(convert_to_static_dianying(one_dianying))
        return result
    else:
        return Dianying(
            id=search_result.id,
            file_id=search_result.file_id,
            url=search_result.url,
            title=search_result.title,
            region=search_result.region,
            score=search_result.score,
            img=search_result.img,
            buy_ticket=search_result.buy_ticket if search_result.buy_ticket else None,
            onshow_time=search_result.onshow_time,
            create_time=search_result.create_time,
        )

def return_static_dianying(the_func):
    @functools.wraps(the_func)
    def wrapper_func(*args, **kwargs):
        dianying_obj = convert_to_static_dianying(the_func(*args, **kwargs))
        Database.commit()
        return programming_obj
    return wrapper_func

class Dianying(MODEL_BASE):
    __tablename__ = 'douban_dianying'
    id = Column(Integer, primary_key=True)
    file_id = Column(Integer)
    url = Column(String(2000))
    title = Column(String(200))
    region = Column(String(200))
    score = Column(Float)
    img = Column(String(2000))
    buy_ticket = Column(String(2000))
    onshow_time=Column(String(200), server_default=None)
    create_time = Column(
        TIMESTAMP,
        nullable=False,
        # default=datetime.datetime.utcnow,
        server_default=func.now()
    )

    @classmethod
    @return_static_dianying
    def load_or_create(cls, file_id, url, title, region, score, img, buy_ticket, onshow_time=None):
        dianying_obj = cls.by_id(file_id)
        if dianying_obj:
            return dianying_obj
        dianying_obj = cls(
            file_id=file_id,
            url=url,
            title=title,
            region=region,
            score=score,
            img=img,
            buy_ticket=buy_ticket if buy_ticket else None,
            onshow_time=onshow_time,
        )
        try:
            Database.add(dianying_obj)
            Database.commit()
            return dianying_obj
        #TODO(weiming liu) cache sqlalchemy for not cache base exception
        except Exception as e:
            log.error(str(e))
            Database.rollback()
            # TODO(weiming liu) raise error for not return None
            return None

    @classmethod
    def by_id(cls, file_id):
        return Database.get_one_by(Dianying, Dianying.file_id == file_id)

    @classmethod
    def del_by_id(cls, file_id):
        try:
            Database.delete_one_by(Dianying, Dianying.file_id == file_id)
            Database.commit()
            return True
        except Exception as e:
            Database.rollback()
            return False

    @classmethod
    @return_static_dianying
    def get_all_dianying(cls):
        # latest update -24:00
        return Database.get_many_by(Dianying, order_by='score', limit=3)

    @classmethod
    @return_static_dianying
    def get_onshow(cls):
        return Database.get_many_by(Dianying, Dianying.onshow_time == None, order_by='-score')

    @classmethod
    @return_static_dianying
    def get_upcoming(cls):
        return Database.get_many_by(Dianying, Dianying.onshow_time != None, order_by=['onshow_time', '-score'])

    def to_json(self):
        return {
            'fileId': self.file_id,
            'img': self.img,
            'title': self.title,
            'score': self.score,
            'region': self.region,
            'url': self.url,
            'buyTicket': self.buy_ticket,
            'onShowTime': self.onshow_time,
            'createTime': str(self.create_time),
        }

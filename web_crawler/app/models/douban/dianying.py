#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
import functools

from common.lib.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE
from models.cache.DianYingCache import DianYingCache

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text, JSON
from sqlalchemy.sql import func


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
    def load_or_create(cls, dianying_list, is_onshow):
        try:
            if is_onshow:
                DianYingCache.set_onshow_dianying(dianying_list)
            else:
                DianYingCache.set_upcoming_dianying(dianying_list)
        except Exception as e:
            log.error(str(e))
            raise

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
    def get_all_dianying(cls):
        # latest update -24:00
        return Database.get_many_by(Dianying, order_by='score', limit=3)

    @classmethod
    def get_onshow(cls):
        return DianYingCache.get_onshow_dianying_list()
        # return Database.get_many_by(Dianying, Dianying.onshow_time == None, order_by=['-id', '-score'])

    @classmethod
    def get_upcoming(cls):
        return DianYingCache.get_upcoming_dianying_list()
        # return Database.get_many_by(Dianying, Dianying.onshow_time != None, order_by=['-id', 'onshow_time', '-score'])

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

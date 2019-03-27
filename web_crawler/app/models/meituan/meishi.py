#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
import functools

from common.lib.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text, JSON
from sqlalchemy.sql import func

def convert_to_static_meishi(search_result):
    if not search_result:
        return None
    if isinstance(search_result, Iterable):
        result = []
        for one_meishi in search_result:
            result.append(convert_to_static_meishi(one_meishi))
        return result
    else:
        return Meishi(
            id=search_result.id,
            poiId=search_result.poiId,
            frontImg=search_result.frontImg,
            title=search_result.title,
            avgScore=search_result.avgScore,
            allCommentNum=search_result.allCommentNum,
            address=search_result.address,
            avgPrice=search_result.avgPrice,
            dealList=search_result.dealList,
            create_time=search_result.create_time,
        )

def return_static_meishi(the_func):
    @functools.wraps(the_func)
    def wrapper_func(*args, **kwargs):
        meishi_obj = convert_to_static_meishi(the_func(*args, **kwargs))
        Database.commit()
        return meishi_obj
    return wrapper_func

class Meishi(MODEL_BASE):
    __tablename__ = 'meituan_meishi'
    id = Column(Integer, primary_key=True)
    poiId = Column(Integer)
    frontImg = Column(String(200))
    title = Column(String(200))
    avgScore = Column(Integer)
    allCommentNum = Column(Integer)
    address = Column(String(200))
    avgPrice = Column(Float)
    dealList = Column(JSON, nullable=True)
    create_time = Column(
        TIMESTAMP,
        nullable=False,
        # default=datetime.datetime.utcnow,
        server_default=func.now()
    )

    @classmethod
    @return_static_meishi
    def load_or_create(cls, poiId, frontImg, title, avgScore, allCommentNum, address, avgPrice, dealList):
        meishi_obj = cls.by_id(poiId)
        if meishi_obj:
            return meishi_obj
        meishi_obj = cls(
            poiId=poiId,
            frontImg=frontImg,
            title=title,
            avgScore=avgScore,
            allCommentNum=allCommentNum,
            address=address,
            avgPrice=avgPrice,
            dealList=dealList,
        )
        try:
            Database.add(meishi_obj)
            Database.commit()
            return meishi_obj
        #TODO(weiming liu) cache sqlalchemy for not cache base exception
        except Exception as e:
            log.error(str(e))
            Database.rollback()
            # TODO(weiming liu) raise error for not return None
            return None

    @classmethod
    def by_id(cls, poiId):
        return Database.get_one_by(Meishi, Meishi.poiId == poiId)

    @classmethod
    def del_by_id(cls, poiId):
        try:
            Database.delete_one_by(Meishi, Meishi.poiId == poiId)
            Database.commit()
            return True
        except Exception as e:
            Database.rollback()

    @classmethod
    @return_static_meishi
    def get_all_meishi(cls):
        # latest update -24:00
        return Database.get_many_by(Meishi, order_by='-id', limit=3)

    def to_json(self):
        return {
            'poiId': self.poiId,
            'frontImg': self.frontImg,
            'title': self.title,
            'avgScore': self.avgScore,
            'allCommentNum': self.allCommentNum,
            'address': self.address,
            'avgPrice': self.avgPrice,
            'dealList': self.dealList,
            'createTime': str(self.create_time),
        }

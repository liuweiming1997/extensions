#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.lib.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text, JSON
from sqlalchemy.sql import func


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
            return True
        except Exception as e:
            Database.rollback()

    @classmethod
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

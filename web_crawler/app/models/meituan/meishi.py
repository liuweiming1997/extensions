#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.log.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text
from sqlalchemy.sql import func


class Meituan_Meishi(MODEL_BASE):
    __tablename__ = 'meituan_meishi'
    id = Column(Integer, primary_key=True)
    poiId = Column(Integer)
    frontImg = Column(String(200))
    title = Column(String(200))
    avgScore = Column(Integer)
    allCommentNum = Column(Integer)
    address = Column(String(200))
    avgPrice = Column(Integer)
    create_time = Column(
        TIMESTAMP,
        nullable=False,
        # default=datetime.datetime.utcnow,
        server_default=func.now()
    )

    @classmethod
    def load_or_create(cls, pidId, frontImg, title, avgScore, allCommentNum, address, avgPrice):
        meituan_meishi_obj = Meituan_Meishi.by_id()
        if meituan_meishi_obj:
            return meituan_meishi_obj
        meituan_meishi_obj = cls(
            pidId=pidId,
            frontImg=frontImg,
            title=title,
            avgScore=avgScore,
            allCommentNum=allCommentNum,
            address=address,
            avgPrice=avgPrice
        )
        try:
            Database.add(meituan_meishi_obj)
            Database.commit()
            return meituan_meishi_obj
        #TODO(weiming liu) cache sqlalchemy for not cache base exception
        except Exception as e:
            log.error(str(e))
            # TODO(weiming liu) raise error for not return None
            return None

    @classmethod
    def by_id(cls, pidId):
        return Database.get_one_by(Meituan_Meishi, Meituan_Meishi.pidId == pidId)

    def to_json(self):
        return {
            'poiId': self.poiId,
            'frontImg': self.frontImg,
            'title': self.title,
            'avgScore': self.avgScore,
            'allCommentNum': self.allCommentNum,
            'address': self.address,
            'avgPrice': self.avgPrice,
            'create_time': self.create_time,
        }
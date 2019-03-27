#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
import functools

from common.lib.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text, JSON
from sqlalchemy.sql import func

def convert_to_static_programming(search_result):
    if not search_result:
        return None
    if isinstance(search_result, Iterable):
        result = []
        for one_programming in search_result:
            result.append(convert_to_static_programming(one_programming))
        return result
    else:
        return Programming(
            id=search_result.id,
            hash_id=search_result.hash_id,
            title=search_result.title,
            url=search_result.url,
            create_time=search_result.create_time,
        )

def return_static_programming(the_func):
    @functools.wraps(the_func)
    def wrapper_func(*args, **kwargs):
        programming_obj = convert_to_static_programming(the_func(*args, **kwargs))
        Database.commit()
        return programming_obj
    return wrapper_func

class Programming(MODEL_BASE):
    __tablename__ = 'medium_programming'
    id = Column(Integer, primary_key=True)
    hash_id = Column(Integer)
    url = Column(String(2000))
    title = Column(String(200))
    create_time = Column(
        TIMESTAMP,
        nullable=False,
        # default=datetime.datetime.utcnow,
        server_default=func.now()
    )

    @classmethod
    @return_static_programming
    def load_or_create(cls, hash_id, title, url):
        programming_obj = cls.by_hash_id(hash_id)
        if programming_obj:
            return programming_obj
        programming_obj = cls(
            hash_id=hash_id,
            title=title,
            url=url,
        )
        try:
            Database.add(programming_obj)
            Database.commit()
            return programming_obj
        #TODO(weiming liu) cache sqlalchemy for not cache base exception
        except Exception as e:
            Database.rollback()
            log.error(str(e))
            # TODO(weiming liu) raise error for not return None
            return None

    @classmethod
    def by_hash_id(cls, hash_id):
        return Database.get_one_by(Programming, Programming.hash_id == hash_id)

    @classmethod
    def del_by_hash_id(cls, hash_id):
        try:
            Database.delete_one_by(Programming, Programming.hash_id == hash_id)
            Database.commit()
            return True
        except Exception as e:
            Database.rollback()
            return False

    @classmethod
    @return_static_programming
    def get_all_programming(cls):
        return Database.get_many_by(Programming, order_by='-id', limit=3)

    def to_json(self):
        return {
            'hash_id': self.hash_id,
            'title': self.title,
            'url': self.url,
            'createTime': str(self.create_time),
        }

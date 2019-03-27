#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
import functools

from common.lib.errors.expection import DatabaseError, ArgsError
from common.lib.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text
from sqlalchemy.sql import func

def convert_to_static_user(search_result):
    if not search_result:
        return None
    if isinstance(search_result, Iterable):
        result = []
        for one_user in search_result:
            result.append(convert_to_static_user(one_user))
        return result
    else:
        return User(
            id=search_result.id,
            username=search_result.username,
            password=search_result.password,
            create_time=search_result.create_time,
        )

def return_static_user(the_func):
    @functools.wraps(the_func)
    def wrapper_func(*args, **kwargs):
        user_obj = convert_to_static_user(the_func(*args, **kwargs))
        Database.commit()
        return user_obj
    return wrapper_func

class User(MODEL_BASE):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    password = Column(String(200))
    create_time = Column(
        TIMESTAMP,
        nullable=False,
        # default=datetime.datetime.utcnow,
        server_default=func.now()
    )

    @classmethod
    @return_static_user
    def load_or_create(cls, username, password):
        user_obj = cls.by_name(username)
        if user_obj:
            if user_obj.password == password:
                return user_obj
            else:
                raise ArgsError('unmatch password')
        user_obj = cls(
            username=username,
            password=password,
        )
        try:
            Database.add(user_obj)
            Database.commit()
            return user_obj
        #TODO(weiming liu) cache sqlalchemy error for not cache base exception
        except Exception as e:
            log.error(str(e))
            Database.rollback()
            raise DatabaseError('can not create user {username}'.format(username=username))

    @classmethod
    def by_name(cls, username):
        return Database.get_one_by(User, User.username == username)

    @classmethod
    @return_static_user
    def by_id(cls, user_id):
        return Database.get_one_by(User, User.id == user_id)

    @classmethod
    def del_by_id(cls, user_id):
        try:
            Database.delete_one_by(User, User.id == user_id)
            Database.commit()
            return True
        except Exception as e:
            Database.rollback()
            return False

    def to_json(self):
        return {
            'username': self.username,
            'createTime': str(self.create_time),
        }

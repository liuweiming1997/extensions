#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.lib.errors.expection import DatabaseError, ArgsError
from common.lib.logger import log
from common.database.orm import Database
from common.database.model_base import MODEL_BASE

from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text
from sqlalchemy.sql import func


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
    def load_or_create(cls, username, password):
        user_obj = cls.by_name(username, password)
        if user_obj:
            return user_obj
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
            raise DatabaseError('can not create user {username}'.format(usernmae=usernmae))

    @classmethod
    def by_name(cls, username, password):
        user_obj = Database.get_one_by(cls, cls.username == username)
        if user_obj.password == password:
            return user_obj
        else:
            raise ArgsError('unmatch password')

    @classmethod
    def by_id(cls, user_id):
        return Database.get_one_by(cls, cls.id == user_id)

    @classmethod
    def del_by_id(cls, user_id):
        return Database.delete_one_by(cls, cls.id == user_id)

    def to_json(self):
        return {
            'username': self.username,
            'createTime': str(self.create_time),
        }

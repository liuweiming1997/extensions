#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from common.singleton.metaclass_base import Singleton

class Config_Base(metaclass=Singleton):
    MYSQL_ROOT_USER = 'root'
    MYSQL_ROOT_PASSWORD = 'root'
    DB_HOST = '192.18.0.3'
    MYSQL_DATABASE = 'chrome_db'

    REDIS_HOST = '192.18.0.4'
    REDIS_PORT = 6379
    
    def __init__(self):
        pass

    def __getattribute__(self, key):
        value = os.getenv(key, default=None)
        if value:
            return value
        try:
            return super().__getattribute__(key)
        except AttributeError as e:
            raise AttributeError('in config, not found {}'.format(key))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from common.singleton.metaclass_base import Singleton

class Config_Base(metaclass=Singleton):
    def __init__(self):
        pass

    def __getattr__(self, key):
        value = os.getenv(key, default=None)
        if value:
            return value
        else:
            raise Exception('config error, not found {}'.format(key))

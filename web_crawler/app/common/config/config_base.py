#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from common.singleton.metaclass_base import Singleton

class config_base(metaclass=Singleton):
    def __init__(self):
        pass

    def __getattr__(self, key):
        if os.getenv(key, default=None):
            return os.getenv(key)
        else:
            raise Exception('config error, not found {}'.format(key))

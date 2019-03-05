#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class config_base:
    def __init__(self):
        pass

    def __getattr__(self, key):
        if os.getenv(key, default=None):
            return os.getenv(key)
        else:
            raise Exception('config error, not found {}'.format(key))

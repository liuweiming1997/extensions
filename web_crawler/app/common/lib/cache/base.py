#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.lib.errors.expection import UnCompleteError

class BaseCache:

    @classmethod
    def get(cls, key):
        raise UnCompleteError('uncomplete BaseCache.get')

    @classmethod
    def set(cls, key):
        raise UnCompleteError('uncomplete BaseCache.set')

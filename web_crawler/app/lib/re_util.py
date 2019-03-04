#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


class ReUtil:
    need_escape = {
        '\\': True,
        '^': True,
        '$': True,
        '.': True,
        '*': True,
        '+': True,
        '?': True,
        '{': True,
        '}': True,
        '(': True,
        ')': True,
        '[': True,
        ']': True,
        '|': True,
    }
    exits = {}

    @classmethod
    def get_regex(cls, begin_with=None, must_contain=None, end_with=None) -> 're object':
        begin_with = cls.conver_to_list(begin_with)
        must_contain = cls.conver_to_list(must_contain)
        end_with = cls.conver_to_list(end_with)

        pattern = ''
        pattern += cls.list_to_restring(begin_with)
        pattern += '(.*)?'
        pattern += cls.list_to_restring(must_contain)
        pattern += '(.*)?'
        pattern += cls.list_to_restring(end_with)

        if cls.exits.get(pattern):
            return cls.exits[pattern]
        regex_obj = re.compile(pattern)
        cls.exits[pattern] = regex_obj
        return regex_obj

    @classmethod
    def list_to_restring(cls, args: list) -> 'str':
        ans = '((?i)' # ignore capitals
        for i, arg in enumerate(args):
            for j in range(len(arg)):
                if arg[j] in cls.need_escape:
                    ans += '\\'
                ans += arg[j]
            if i != len(args) - 1:
                ans += '|'
        ans += ')'
        return ans

    @classmethod
    def conver_to_list(cls, value) -> 'list':
        return [] if not value else [value] if not isinstance(value, list) else value

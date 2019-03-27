#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
import functools

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

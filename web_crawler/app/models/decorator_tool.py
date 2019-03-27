#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
import functools

from common.database.orm import Database
from models.user import User
from models.douban.dianying import Dianying
from models.medium.programming import Programming
from models.meituan.meishi import Meishi

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


def convert_to_static_meishi(search_result):
    if not search_result:
        return None
    if isinstance(search_result, Iterable):
        result = []
        for one_meishi in search_result:
            result.append(convert_to_static_meishi(one_meishi))
        return result
    else:
        return Meishi(
            id=search_result.id,
            poiId=search_result.poiId,
            frontImg=search_result.frontImg,
            title=search_result.title,
            avgScore=search_result.avgScore,
            allCommentNum=search_result.allCommentNum,
            address=search_result.address,
            avgPrice=search_result.avgPrice,
            dealList=search_result.dealList,
            create_time=search_result.create_time,
        )

def return_static_meishi(the_func):
    @functools.wraps(the_func)
    def wrapper_func(*args, **kwargs):
        meishi_obj = convert_to_static_meishi(the_func(*args, **kwargs))
        Database.commit()
        return meishi_obj
    return wrapper_func


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



def convert_to_static_dianying(search_result):
    if not search_result:
        return None
    if isinstance(search_result, Iterable):
        result = []
        for one_dianying in search_result:
            result.append(convert_to_static_dianying(one_dianying))
        return result
    else:
        return Dianying(
            id=search_result.id,
            file_id=search_result.file_id,
            url=search_result.url,
            title=search_result.title,
            region=search_result.region,
            score=search_result.score,
            img=search_result.img,
            buy_ticket=search_result.buy_ticket if search_result.buy_ticket else None,
            onshow_time=search_result.onshow_time,
            create_time=search_result.create_time,
        )

def return_static_dianying(the_func):
    @functools.wraps(the_func)
    def wrapper_func(*args, **kwargs):
        dianying_obj = convert_to_static_dianying(the_func(*args, **kwargs))
        Database.commit()
        return programming_obj
    return wrapper_func

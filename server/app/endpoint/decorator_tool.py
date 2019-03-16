#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import g, session, make_response, request
import functools
from common.lib.errors.expection import ArgsError
from models.user import User

"""
    load user from cookies
"""
def parse_user():
    def decorator(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            user_id = session.get('user_id')
            g.current_user = User.by_id(user_id)
            if not g.current_user:
                raise ArgsError('Require login')
            return func(*args, **kwargs)
        return wrapper_func
    return decorator

"""
    parse args from request
"""
def parse_args(arg_name: str, arg_type: type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            value = request.form.getlist(arg_name) if issubclass(arg_type, list) else request.form.get(arg_name)
            value = request.args.get(arg_name) if not value else value
            value = request.json.get(arg_name) if not value and request.json else value

            if not value:
                raise ArgsError('Require args {}'.format(arg_name))

            if issubclass(arg_type, int) and issubclass(type(value), str):
                try:
                    value = int(value)
                except ValueError:
                    raise ArgsError('Require args {}, require type: {}, but found type: {}'.format(arg_name, str(arg_type), str(type(value))))
            else:
                if not issubclass(type(value), arg_type):
                    raise ArgsError('Require args {}, require type: {}, but found type: {}'.format(arg_name, str(arg_type), str(type(value))))   

            return func(*args, *kwargs.values(), value)
        return wrapper_func
    return decorator

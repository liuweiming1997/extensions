#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .expection_base import ChromeServerExpectionBase
from .const import (ExpectionErrorMapping, HttpStatusCode)

class ArgsError(ChromeServerExpectionBase):
    def __init__(self, message = None, status = None, http_status_code = None):
        if message is None:
            message = "invalid_user_input"
        if status is None:
            status = ExpectionErrorMapping.INVALID_USER_INPUT
        if http_status_code is None:
            http_status_code = HttpStatusCode.BAD_REQUEST

        super().__init__(message, status, http_status_code)

class DatabaseError(ChromeServerExpectionBase):
    def __init__(self, message = None, status = None, http_status_code = None):
        if message is None:
            message = "internal database error"
        if status is None:
            status = ExpectionErrorMapping.INTERNAL_DATABASE_ERROR
        if http_status_code is None:
            http_status_code = HttpStatusCode.SERVER_ERROR

        super().__init__(message, status, http_status_code)    

class UnknownError(ChromeServerExpectionBase):
    def __init__(self, message = None, status = None, http_status_code = None):
        if message is None:
            message = "unknown error"
        if status is None:
            status = ExpectionErrorMapping.UNKNOWN_ERROR
        if http_status_code is None:
            http_status_code = HttpStatusCode.SERVER_ERROR

        super().__init__(message, status, http_status_code)

class CacheError(ChromeServerExpectionBase):
    def __init__(self, message = None, status = None, http_status_code = None):
        if message is None:
            message = "Cache error"
        if status is None:
            status = ExpectionErrorMapping.CACHE_ERROR
        if http_status_code is None:
            http_status_code = HttpStatusCode.SERVER_ERROR

        super().__init__(message, status, http_status_code)

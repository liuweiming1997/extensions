#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HttpStatusCode:
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500

class ExpectionErrorMapping:
    INVALID_USER_INPUT = 1
    INTERNAL_DATABASE_ERROR = 2
    UNKNOWN_ERROR = 3
    CACHE_ERROR = 4
    UN_COMPLETE_ERROR = 5

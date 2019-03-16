#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from common.config.config_base import Config_Base

class LoggerConfig:
    LOG_BASE_DIR = '/log/crawler/'
    LOG_FILES = {
        'error': os.path.join(LOG_BASE_DIR, 'error.log'),
        'info': os.path.join(LOG_BASE_DIR, 'info.log'),
    }
    CONFIG = {
        'ERROR': {
            'logger_name': 'ERROR_LOG',
            'log_file': LOG_FILES.get("error"),
            'lever': 'DEBUG',

            'formatter': '%(asctime)s - %(levelname)s - %(funcName)s \n%(message)s',

            'backup_count': 7,
            'encoding': 'utf-8',
            'when': 'midnight',
            'interval': 1,
            'filemode': 'a',
        },
        'INFO': {
            'logger_name': 'info_log',
            'log_file': LOG_FILES.get("info"),
            'lever': 'DEBUG',

            'formatter': '%(asctime)s - %(levelname)s - %(funcName)s \n%(message)s',

            'backup_count': 7,
            'encoding': 'utf-8',
            'when': 'midnight',
            'interval': 1,
            'filemode': 'a',
        }
    }

class Web_Crawler_Config(Config_Base):
    def __init__(self):
        super().__init__()

    LOGGER = LoggerConfig()
    SECRET_KEY = 'no_secret'
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    SESSION_COOKIE_HTTPONLY = True

config = Web_Crawler_Config()

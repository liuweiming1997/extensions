#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging.handlers

from config import config

class Logger:
    def __init__(self):
        self.info_logger = self.get_logger('INFO')
        self.error_logger = self.get_logger('ERROR')

    def get_logger(self, logger_name):
        handler = logging.handlers.TimedRotatingFileHandler(
                        config.LOGGER.CONFIG[logger_name]['log_file'],
                        interval=config.LOGGER.CONFIG[logger_name]['interval'],
                        when=config.LOGGER.CONFIG[logger_name]['when'],
                        backupCount=config.LOGGER.CONFIG[logger_name]['backup_count'],
                        encoding=config.LOGGER.CONFIG[logger_name]['encoding']
                    )
        formatter = logging.Formatter(config.LOGGER.CONFIG[logger_name]['formatter'])
        handler.setFormatter(formatter)
        logger = logging.getLogger(config.LOGGER.CONFIG[logger_name]['logger_name'])
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def info(self, msg):
        self.info_logger.info(msg)

    def error(self, msg):
        self.error_logger.error(msg)

log = Logger()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from common.lib.logger import log

class ChromeServerExpectionBase(Exception):

    def __init__(self, message = None, status = None, http_status_code = None):
        super().__init__(message, status)
        self.message = message
        self.status = status
        self.http_status_code = http_status_code

        log.error("an raise happen with message: {}, status: {}, http_status_code: {}".format(message, str(status), str(http_status_code)))

    def get_message(self):
        return self.message

    def get_status(self):
        return self.status

    def get_http_status_code(self):
        return self.http_status_code

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import jsonify
from .const import HttpStatusCode

def chrome_server_error_handler(error):
    response = jsonify({
        'message': error.get_message(),
        'status': error.get_status(),
    })
    response.status_code = error.get_http_status_code()
    return response

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:57:26 2020

@author: kanthi
"""

from os import getcwd
from os import environ
from os import getenv

print('current directory:  ',getcwd())
print('environment variables:  ',environ)
print('specific environment variable USER:  ',getenv('USER'))


import sys
print('system platform ',sys.platform)
print('system version ',sys.version)

import datetime
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
print(datetime.date.isoformat(datetime.date.today()))

import time
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))
print(time.strftime("%A %H:%M %p"))

import html
print(html.unescape(html.escape("This HTML fragment contains a <script>script" \
                         + "</script> tag.")))


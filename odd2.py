#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:26:10 2020

@author: kanthi
"""

from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55,
        59]

for num in range(5):   
    right_this_minute = datetime.today().minute
    
    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute')
    time.sleep(random.randint(1,5))
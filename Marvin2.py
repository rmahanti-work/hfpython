# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:51:35 2020

@author: Ravi
"""


paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t',char)
print()    
for char in letters[-7:]:
    print('\t'*2,char)
print()
for char in letters[12:20]:
    print('\t'*3,char)
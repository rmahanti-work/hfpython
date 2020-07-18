# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 18:02:02 2020

@author: Ravi
"""

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# plist = plist[1:3]+plist[5:6]+plist[4:5]+plist[7:8]+plist[6:7]
new_phase = ''.join(plist[1:3])
new_phase = new_phase + ''.join([plist[5],plist[4],plist[7],plist[6]])
print(plist)
print(new_phase)


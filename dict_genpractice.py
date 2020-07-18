# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:37:27 2020

@author: Ravi
"""


found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

print (found)

found['u'] += 2

print (found)

for kv in found:
    print(kv)

for kv in found:
    print(kv, 'was found', found[kv], 'time(s).')

for kv in sorted(found):
    print(kv, 'was found', found[kv], 'time(s).')

for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
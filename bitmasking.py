# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:32:10 2020

@author: Ravi
"""


# Bit masking in python ... code from stackoverflow
mask0 = 0x07
mask1 = 0x40
mask2 = 0x80

def parse_byte(byte):
    return byte & mask2, byte & mask1, byte & mask0

value1 = 0x01
value2 = 0x02
value3 = 0x03
value4 = 0x04
value5 = 0x05
value6 = 0x06
value7 = 0x40
value8 = 0x80

# Example 1
byte = value3 | value7
print("byte = "+str(byte))
value8_set, value7_set, base_value = parse_byte(byte)
print("base_value = "+str(base_value))
if value7_set: print("value7set ",value7_set)
if value8_set: print("value8_set ",value8_set)
print()

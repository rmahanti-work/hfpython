# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:51:06 2020

@author: Ravi
"""


# =============================================================================
# Bitwise operators in python 
# =============================================================================

i = 10
# Shift bits by given number to left .. in this case by 2 positions
print(i >> 2)

# Shift bits by given number to right .. in this case by 2 positions
print(i << 2)

j = 22
# Bitwise and 
print(i & j)

# Bitwise or 
print(i | j)

# Returns bitwise complement
print(~i)

# XOR
i = 3
j = 5
print(i^j)

i = 0x80
print(i)

# convert numbers into bits
j = 10
print(format(j,'08b'))
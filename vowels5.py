# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:54:00 2020

@author: Ravi
"""


vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found = {}
for letter in word:
    if letter in vowels:
        found[letter] += 1

for k,v in sorted(found.items()):
    print(k, ' was found ', v, ' item(s)')
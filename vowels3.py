# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:57:38 2020

@author: Ravi
"""

vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for letter in found:
    print(letter)
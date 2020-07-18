# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:57:38 2020

@author: Ravi
"""

# vowels = ['a','e','i','o','u']  (or)
# vowels = 'aeiou' (or)
vowels_set = set('aeiou')    
word = input("Provide a word to search for vowels: ")
found = vowels_set.intersection(set(word))
for letter in found:
    print(letter)
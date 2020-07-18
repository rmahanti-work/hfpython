# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:12:34 2020

@author: Ravi
"""

# =============================================================================
# def search4vowels():
#     """Display any vowels found in an asked-for word."""
#     vowels_set = set('aeiou')    
#     word = input('Provide a word to search for vowels: ')
#     found = vowels_set.intersection(set(word))
#     for letter in found:
#         print(letter)
# =============================================================================

def search4vowels(word):
    """Display any vowels found in an asked-for word."""
    vowels_set = set('aeiou')    
    word = input('Provide a word to search for vowels: ')
    found = vowels_set.intersection(set(word))
    return bool(found)
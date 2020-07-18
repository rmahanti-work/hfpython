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

# =============================================================================
# def search4vowels(word):
#     """Display any vowels found in an asked-for word."""
#     vowels_set = set('aeiou')
#     word = input('Provide a word to search for vowels: ')
#     found = vowels_set.intersection(set(word))
#     return bool(found)
# =============================================================================


def search4vowels(word: str) -> set:
    """Display any vowels found in an asked-for word."""
    vowels_set = set('aeiou')
    return vowels_set.intersection(set(word))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

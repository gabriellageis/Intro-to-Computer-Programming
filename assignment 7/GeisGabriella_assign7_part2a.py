"""
Gabriella Geis
14 November, 2019
Section 002
Assignment 7 - Problem 2a
"""
import random

def add_letters(word, num):
    new_word=""
    for char in word:
        new_word += char
        for n in range(num):
            letters = chr(random.choice([random.randint(65,90), random.randint(97,122)]))
            new_word += letters
    return new_word         

def remove_letters(word, num):
    new_word = word[0: len(word): num+1]
    return new_word             

def shift_characters(word, num):
    new_word = ""
    for char in word:
        new_char = chr(ord(char) + num)
        new_word += new_char
    return new_word




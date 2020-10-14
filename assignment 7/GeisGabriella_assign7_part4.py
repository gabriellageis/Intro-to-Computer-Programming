"""
Gabriella Geis
14 November, 2019
Section 002
Assignment 7 - Problem 4
"""

def string_length(string):
    count = 0
    for char in string:
        count += 1
    return count

def string_isalpha(string):
    alpha = 0
    for char in string:
        if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122):
            alpha += 1
    if alpha == len(string) and len(string)!=0:
        allalpha = True
    else:
        allalpha = False
    return allalpha

def string_isupper(string):
    upper = 0
    for char in string:
        if ord(char)>=65 and ord(char)<=90:
            upper += 1
    if upper == len(string) and len(string)!=0:
        allupper = True
    else:
        allupper = False
    return allupper

def string_isdigit(string):
    digit = 0
    for char in string:
        if ord(char)>=48 and ord(char)<=57:
            digit += 1
    if digit == len(string) and len(string)!=0:
        alldigit = True
    else:
        alldigit = False
    return alldigit

def string_swapcase(string):
    new_string = ""
    for char in string:
        if ord(char)>=65 and ord(char)<=90:
            new = chr(ord(char) + 32)
        elif ord(char)>=97 and ord(char)<=122:
            new = chr(ord(char) - 32)
        else:
            new = char
        new_string += new
    return new_string
            
def string_lower(string):
    new_string = ""
    for char in string:
        if ord(char)>=65 and ord(char)<=90:
            new = chr(ord(char) + 32)
        else:
            new = char
        new_string += new
    return new_string

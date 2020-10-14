"""
Gabriella Geis
31 October, 2019
Section 002
Assignment 6 - Problem 2
"""

# functions
def is_even(x):
    if x % 2 == 0:
        even = True
        return even
    else:
        even = False
        return even

def is_odd(x):
    if x % 2 == 0:
        odd = False
        return odd
    else:
        odd = True
        return odd

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            prime = False
            return prime
        else:
            if i == x-1:
                prime = True
                return prime
    
def is_perfect(x):
    number = 0
    for i in range(1,x-1):
        if x % i == 0:
            factor = i
            number += factor
    if x == number:
        perfect = True
        return perfect
    else:
        perfect = False
        return perfect

def is_abundant(x):
    number = 0
    for i in range(1,x-1):
        if x % i == 0:
            factor = i
            number += factor
    if x < number:
        abundant = True
        return abundant
    else:
        abundant = False
        return abundant

# user input starting number
while True:
    start = int(input("Enter starting number: "))
    if start > 0:
        break
    else:
        print("Invalid, try again")

# user input ending number
while True:
    end = int(input("Enter ending number: "))
    if end > 0 and end > start:
        break
    else:
        print("Invalid, try again")

# check if even/odd/prime/perfect/abundant
for i in range(start, end+1):
    print(i, "is ...", end = " ")
    if is_even(i) == True:
        print("even", end = " ")
    if is_odd(i) == True:
        print("odd", end = " ")
    if is_prime(i) == True:
        print("prime", end = " ")
    if is_perfect(i) == True:
        print("perfect", end = " ")
    if is_abundant(i) == True:
        print("abundant", end = " ")
    print()


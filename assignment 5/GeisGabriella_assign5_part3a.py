"""
Gabriella Geis
24 October, 2019
Section 002
Assignment 5 - Problem 3a
"""

# user input positive number
while True:
    number = int(input("Enter a positive number to test: "))
    if number < 1:
        print("Invalid number, try again!")
        print()
    else:
        print()
        break

# determine if prime number

for i in range(2, number):
    if number % i == 0:
        print(i, "is a divisor of", number, "... stopping")
        print()
        print(number, "is not a prime number.")
        break
    else:
        print(i, "is NOT a divisor of", number, "... continuing")
        if i == number-1:
            print()     
            print(number, "is a prime number!")

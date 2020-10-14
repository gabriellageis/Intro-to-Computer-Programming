"""
Gabriella Geis
24 October, 2019
Section 002
Assignment 5 - Problem 3b
"""

# determine if prime number
"""
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
"""

start = 1
end = 1000

# from 1 - 1000
for number in range(start, end + 1):
    if number == 1:
        print("1 is technically not a prime number.")
    else:
        prime = True
        # test divisibility of every number 
        for test in range(2, number):
            # if number 
            if number % test == 0:
                prime = False
                break
        if prime == True:
                print(number, "is a prime number!")

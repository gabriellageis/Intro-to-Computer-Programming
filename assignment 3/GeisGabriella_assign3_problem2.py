"""
Gabriella Geis
26 September, 2019
Section 002
Assignment 3 - Problem 2
"""

# import the random function
import random

# generate random number
secret_number = random.randint(1, 10)

# give the user the numbers to guess between
print("I'm thinking of a number between 1 and 10!")

# get the user input
user_guess = int(input("What's your guess? "))

# 1st round
if user_guess == secret_number:
    print("You got it!")
    print("It took you 1 try to guess the number.")
elif user_guess > secret_number:        # 1 too high
    print("Too high, try again.")
    user_guess = int(input("What's your guess? "))
    # 2nd round 
    if user_guess == secret_number:
        print("You got it!")
        print("It took you 2 tries to guess the number.")
    elif user_guess > secret_number:    # 2 too high
        print("Too high, try again.")
        user_guess = int(input("What's your guess? "))
        # 3rd round
        if user_guess == secret_number:
            print("You got it!")
            print("It took you 3 tries to guess the number.")
        else:                           # 3 doesn't get it
            print("The secret number was", secret_number)
            print("You didn't guess the number.")
    else:                               # 2 too low
        print("Too low, try again.")
        user_guess = int(input("What's your guess? "))
        # 3rd round
        if user_guess == secret_number:
            print("You got it!")
            print("It took you 3 tries to guess the number.")
        else:                           #3 doesn't get it
            print("The secret number was", secret_number)
            print("You didn't guess the number.")
else:                                   # 1 too low
    print("Too low, try again.")
    user_guess = int(input("What's your guess? "))
    # 2nd round 
    if user_guess == secret_number:
        print("You got it!")
        print("It took you 2 tries to guess the number.")
    elif user_guess > secret_number:    # 2 too high
        print("Too high, try again.")
        user_guess = int(input("What's your guess? "))
        # 3rd round
        if user_guess == secret_number:
            print("You got it!")
            print("It took you 3 tries to guess the number.")
        else:                           # 3 doesn't get it
            print("The secret number was", secret_number)
            print("You didn't guess the number.")
    else:                               # 2 too low
        print("Too low, try again.")
        user_guess = int(input("What's your guess? "))
        # 3rd round
        if user_guess == secret_number:
            print("You got it!")
            print("It took you 3 tries to guess the number.")
        else:                           #3 doesn't get it
            print("The secret number was", secret_number)
            print("You didn't guess the number.")

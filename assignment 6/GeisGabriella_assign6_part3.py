"""
Gabriella Geis
31 October, 2019
Section 002
Assignment 6 - Problem 3
"""
# import functions
import digitalclock
import random

# number of problems
while True:
    problems = int(input("How many problems would you like to attempt? "))
    if problems > 0:
        print()
        break
    else:
        print("Invalid number, try again")

# width
while True:
    digits = int(input("How wide do you want your digits to be? 5-10: "))
    if digits >= 5 and digits <=10:
        print()
        break
    else:
        print("Invalid width, try again")

# character
while True:
    character = input("What character would you like to use? ")
    if len(character) == 1:
        print()
        break
    else:
        print("String too long, try again")

print("Here we go!")
print()
correct = 0

# loop thru number of problems
for i in range(problems):
    print("What is .....")
    print()
    # get number 1
    number1 = random.randint(0,9)
    digitalclock.print_number(number1, digits, character)
    print()
    # choose plus or minus
    operator = random.randint(0,1)
    if operator == 0:
        operator = "+"
        plus = digitalclock.plus(digits, character)
        print(plus)
        print()
    else:
        operator = "-"
        minus = digitalclock.minus(digits, character)
        print(minus)
        print()
    # get number 2
    number2 = random.randint(0,9)
    digitalclock.print_number(number2, digits, character)
    print()
    # user answer input
    answer = int(input("= "))
    print()
    # check if user answer is correct
    if digitalclock.check_answer(number1, number2, answer, operator) == True:
        correct += 1
        print("Correct!")
        print()
    else:
        print("Sorry, that's not correct.")
        print()
    

# print number of problems correct
print("You got", correct, "out of", problems, "correct!")



"""
Gabriella Geis
12 September, 2019
Section 002
Assignment 1 - Problem 2
"""

# user input enter 3 names and store in separate variables
name1 = input("Please enter name #1: ") # Allison
name2 = input("Please enter name #2: ") # Jeremy
name3 = input("Please enter name #3: ") # Emily

# print in every possible order
print("Here are your names in every possible order:")
print()
print("1. ", name1, ", ", name2, ", ", name3, " ,", sep="", end="")
print(" 2.", " *", name1, "* ", "*", name3,"*", " *", name2, "*", " ,", sep="", end="")
print(" 3. ", name2, "-", name1, "-", name3, sep="")
print("4.", name2, "\n", name3, "\n", name1)
print("5.", name3, "\n  ", name2, "\n  ", name1)
print("6. ", name3, "\n---", name1, "\n---", name2, sep="")



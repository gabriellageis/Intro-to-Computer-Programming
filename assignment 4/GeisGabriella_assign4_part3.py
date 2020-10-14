"""
Gabriella Geis
10 October, 2019
Section 002
Assignment 4 - Problem 3
"""

# Decimal to Binary

# prompt user for integer greater than or equal to zero
while True:
    number = int(input("Enter a number greater than or equal to 0: "))
    original_number = number
    if number < 0:
        print("Invalid, try again")
    else:
        break
# divide number by 2
bit = ""
while number > 0:
    mod = number % 2
    new_number = int(number / 2)
    if mod == 1:
        bit = "1" + bit
    else:
        bit = "0" + bit
    print(number, "% 2 =", mod, "---", bit)
    print(number, "/ 2 =", new_number)
    number = new_number
print()
print(original_number, "in binary is", bit)



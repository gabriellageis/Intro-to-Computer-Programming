"""
Gabriella Geis
14 November, 2019
Section 002
Assignment 7 - Problem 1a
"""
while True:
    username = input("Enter a username: ")

    # length of username
    size = len(username)
    print("* Length of username:", size)

    # alphanumeric characters
    allalnum = username.isalnum()
    print("* All characters alpha numeric:", allalnum)

    # first character cannot be a digit
    if username[0].isdigit():
        print("* First character is a digit")
    else:
        print("* First character is NOT a digit")

    # last character cannot be a digit
    if username[-1].isdigit():
        print("* Last character is a digit")
    else:
        print("* Last character is NOT a digit")

    # count number of uppers, lowers, and digits
    uppers = 0
    lowers = 0
    digits = 0
    invalid = 0

    for c in username:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
        else:
            invalid += 1

    print("* # of uppercase characters in the username:", uppers)
    print("* # of lowercase characters in the username:", lowers)
    print("* # of digits in the username:", digits)

    # check if username is valid
    valid = True
    if size < 8 or size > 15:
        valid = False
    if invalid > 0:
        valid = False
    if username[0].isdigit() or username[-1].isdigit():
        valid = False
    if uppers == 0 or lowers == 0 or digits == 0:
        valid = False

    # print if username is valid
    if valid == False:  
        print("Username is invalid, please try again")
        print()
    else:
        print("Username is valid!")
        break








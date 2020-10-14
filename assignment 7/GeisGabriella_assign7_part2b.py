"""
Gabriella Geis
14 November, 2019
Section 002
Assignment 7 - Problem 2b
"""

import GeisGabriella_assign7_part2a

while True:
    program = input("(e)ncode, (d)ecode or (q)uit: ")
    # use for quitting
    if program == "q":
        break
    # use for encoding
    elif program == "e":
        while True:
            num = int(input("Enter a number between 1 and 5: "))
            if num >= 1 and num <= 5:
                break
            else:
                print("Invalid number, try again!")
        phrase = input("Enter a phrase to encode: ")
        # add letters
        add = GeisGabriella_assign7_part2a.add_letters(phrase, num)
        # shift up one
        shift = GeisGabriella_assign7_part2a.shift_characters(add, num)
        print("Your encoded word is:", shift)
        print()
    # use for decoding
    elif program == "d":
        while True:
            num = int(input("Enter a number between 1 and 5: "))
            if num >= 1 and num <= 5:
                break
            else:
                print("Invalid number, try again!")
        phrase = input("Enter a phrase to decode: ")
        # remove letters
        remove = GeisGabriella_assign7_part2a.remove_letters(phrase, num)
        # make number negative
        str_num = "-" + str(num)
        num = int(str_num)
        # shift down one
        shift = GeisGabriella_assign7_part2a.shift_characters(remove, num)
        print("Your decoded word is:", shift)
        print()

"""
Gabriella Geis
14 November, 2019
Section 002
Assignment 7 - Problem 3
"""

# get 6 digit seed
while True:
    seed = input("Enter a six digit seed: ")
    if seed.isdigit() and len(seed) == 6:
        seed = int(seed)
        break
    else:
        print("Invalid seed, please try again")
        print()

# get low/high integers
while True:
    low = input("Enter lowest possible random integer: ")
    high = input("Enter highest possible random integer: ")
    if low.isdigit() and high.isdigit() and low > high:
        low = int(low)
        high = int(high)
        print()
        break
    else:
        print("Invalid low/high values, please try again.")
        print()

# number of random integers to generate
while True:
    rand_num = input("How many random numbers do you want to generate? ")
    if rand_num.isdigit():
        if int(rand_num) >= 1:
            rand_num = int(rand_num)
            print()
            break
        else:
            print("Invalid integer, try again")
    else:
        print("Invalid, enter an integer")
        print()

while rand_num > 0:
    # print seed value
    print()
    print("Seed value:", seed)

    # square seed
    square = seed ** 2
    print("Square of seed:", square)

    # middle 6
    if len(str(square)) == 11:
        middle6 = int(str(square)[2:8])
    elif len(str(square)) == 12:
        middle6 = int(str(square)[3:9])
    print(middle6)

    # percentage value
    percentage = middle6 / 999999
    print("Percentage =", middle6, "/ 999999 =", percentage)

    # scaling up number
    print("Scaling up to a number between", low, "and", high)
    up = ((high - low) * percentage) + low
    print("(", high, "-", low, ") *", percentage, "+", low, "=", up)
    integer = int(up)
    print("Converted to an integer:", integer)

    # set new seed
    seed = middle6

    # decrease random numbers left to create
    rand_num -= 1


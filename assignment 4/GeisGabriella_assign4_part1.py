"""
Gabriella Geis
10 October, 2019
Section 002
Assignment 4 - Problem 1
"""

# Roll the Dice

import random

# get size of dice and validate number

while True:
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12, or 20)? "))

    if sides == 4 or sides == 6 or sides == 8 or sides == 10 or sides == 12 or sides == 20:
        print()
        print("Thanks, here we go!")
        print()
        break
    else:
        print("Invalid size, try again.")

# roll until you get snake eyes

num_rolls = 0
total_1 = 0
total_2 = 0
doubles = 0
highs = 0
high_lows = 0
evens = 0
odds = 0
sums = 0

while True:
    
    d1 = random.randint(1, sides)
    d2 = random.randint(1, sides)
    
    
    num_rolls += 1
    total_1 += d1
    total_2 += d2

        
    if d1 == 1 and d2 == 1:
        print(num_rolls, "die #1 is", d1, "and die #2 is", d2, end = "")
        print(" Odds! Doubles! Snake Eyes!")
        break
    else:
        if True:
            print(num_rolls, "die #1 is", d1, "and die #2 is", d2, end = " ")
            if d1 == d2:
                print(" Doubles!", end = " ")
                doubles += 1
            if (sides == d1 == d2 == 4) or (sides == d1 == d2 == 6) or (sides == d1 == d2 == 8) or (sides == d1 == d2 == 10) or(sides == d1 == d2 == 12) or (sides == d1 == d2 == 20):
                print(" High roll!", end = " ")
                highs += 1
            if (sides==4 and ((d1==1 and d2==4) or (d1==4 and d2==1))) or (sides==6 and ((d1==1 and d2==6) or (d1==6 and d2==1))) or(sides==8 and ((d1==1 and d2==8) or (d1==8 and d2==1))) or (sides==10 and ((d1==1 and d2==10) or (d1==10 and d2==1)))or (sides==12 and ((d1==1 and d2==12) or (d1==12 and d2==1))) or (sides==20 and ((d1==1 and d2==20) or (d1==20 and d2==1))):
                print(" High / Low!", end = " ")
                high_lows += 1
            if d1==d2==2 or d1==d2==4 or d1==d2==6 or d1==d2==8 or d1==d2==10 or d1==d2==12 or d1==d2==14 or d1==d2==16 or d1==d2==18 or d1==d2==20:
                print(" Evens!", end = " ")
                evens += 1
            if d1==d2==1 or d1==d2==3 or d1==d2==5 or d1==d2==7 or d1==d2==9 or d1==d2==11 or d1==d2==13 or d1==d2==15 or d1==d2==17 or d1==d2==19:
                print(" Odds!", end = " ")
                odds += 1
            if d1 + d2 == sides:
                print(" Sum value is size value!", end = " ")
                sums += 1
            print()

# tell how long it took to get snake eyes
print()
print("You finally got snake eyes on roll #", num_rolls)

# calculate percentages
avg_doubles = format(((doubles / num_rolls) *100), ".2f")
print("Along the way you rolled DOUBLES", doubles, "times.", avg_doubles, "% of all rolls were doubles")
avg_highs = format(((highs / num_rolls) *100), ".2f")
print("Along the way you rolled TWO HIGH VALUES", doubles, "times.", avg_highs, "% of all rolls were two high values")
avg_high_lows = format(((high_lows / num_rolls) *100), ".2f")
print("Along the way you rolled HIGH / LOW", doubles, "times.", avg_high_lows, "% of all rolls were two evens")
avg_evens = format(((evens / num_rolls) *100), ".2f")
print("Along the way you rolled TWO EVENS", doubles, "times.", avg_evens, "% of all rolls were two odds")
avg_odds = format(((odds / num_rolls) *100), ".2f")
print("Along the way you rolled TWO ODDS", doubles, "times.", avg_odds, "% of all rolls were high/low")
avg_sums = format(((sums / num_rolls) *100), ".2f")
print("Along the way you rolled A SUM VALUE", doubles, "times.", avg_sums, "% of all rolls were a sum value")


# average roll
average1 = total_1 / num_rolls
print("Average roll for die #1:", format(average1, ".2f"))
average2 = total_2 / num_rolls
print("Average roll for die #2:", format(average2, ".2f"))

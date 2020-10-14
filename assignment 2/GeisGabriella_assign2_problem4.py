"""
Gabriella Geis
19 September, 2019
Section 002
Assignment 2 - Problem 4
"""

# name of program
print("-" * 50)
print(format("mL Conversion Calculator", "^50s"))
print("-" * 50)
print()

# user input a number of milliliters
milliliters = float(input("How many mL would you like to convert? "))

# conversions
mL_to_tsp = 0.202884
tbsp_to_tsp = 3
mL_to_uL = 1000
mL_to_nL = 1000000

# convert the input to tsp, tbsp, uL, nL
teaspoons = float(format(mL_to_tsp * milliliters, ",.2f"))
tablespoons = format(teaspoons / tbsp_to_tsp, ",.2f")
microliters = format(mL_to_uL * milliliters, ",.2f")
nanoliters = format(mL_to_nL * milliliters, ",.2f")

# output results in table
print()
print(milliliters, "mL in teaspoons", format(teaspoons, ">23"), "tsp")
print(milliliters, "mL in tablespoons", format(tablespoons, ">21"), "tbsp")
print(milliliters, "mL in microliters", format(microliters, ">21"), "uL")
print(microliters, "mL in nanoliters", format(nanoliters, ">17"), "nL")

# 5 ways to crash program
"""
1. logic error - when converting to tablespoons, have the teaspoons and tbsp_to_tsp in the wrong position (numerator/denominator swapped)
2. syntax error - no quotes used around center align formatting in name of program
3. runtime error - the user inputs a word for millimeters which cannot be used to do mathematical conversions
4. runtime error - adding more than two arguments in format function, ex. format(teaspoons, "tsp", ">16")
5. runtime error - having the incorrect letter in the formatting ex. using ",.2d" when it should be ",.2f" for floating point number
"""

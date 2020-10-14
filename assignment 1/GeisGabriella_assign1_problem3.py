"""
Gabriella Geis
12 September, 2019
Section 002
Assignment 1 - Problem 3
"""

# create variables with conversions
ml_to_tsp = 0.202884
tbsp_from_tsp = 3
cup_from_tbsp = 16
pint_from_cups = 2
quart_from_pints = 2
gallon_from_quarts = 4
floz_from_ml = 29.5735

# convert 250 milliliters to US Fluid Volume units
mL = 250.0
tsp = mL * ml_to_tsp
tbsp = tsp / tbsp_from_tsp
cups = tbsp / cup_from_tbsp
pints = cups / pint_from_cups
quarts = pints / quart_from_pints
gallons = quarts / gallon_from_quarts
floz = gallons * mL

# print the conversion of 250 milliliters to US Fluid Volume units
print("mL to US Fluid Volume Units")
print()
print(format("mL:", "15s"), mL)
print(format("tsp:", "15s"), tsp)
print(format("tbsp:", "15s"), tbsp)
print(format("cup(s):", "15s"), cups)
print(format("pint(s):", "15s"), pints)
print(format("quart(s):", "15s"), quarts)
print(format("gallon(s):", "15s"), gallons)
print(format("fl oz:", "15s"), floz)


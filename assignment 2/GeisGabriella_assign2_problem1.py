"""
Gabriella Geis
19 September, 2019
Section 002
Assignment 2 - Problem 1
"""

# explain program
print("This program will project how much you can earn by investing money in a\nhigh-yield savings accound over a 3 month period.")
print()

# get initial investment and interest rate
initial_investment = float(input("To begin, enter how much money you would like to initially invest (i.e. 500): "))
rate = float(input("Next, enter your projected annual interest rate. For example, enter 5 for 5%: ")) / 100 / 12

# compute the 1st months interest
month1_interest = initial_investment * rate

# compute how much $ they have after the 1st month is over
month1_ending = initial_investment + month1_interest

# repeat process for month 2
initial_investment2 = month1_ending
month2_interest = initial_investment2 * rate
month2_ending = initial_investment2 + month2_interest


# repeat process for month 3
initial_investment3 = month2_ending
month3_interest = initial_investment3 * rate
month3_ending = initial_investment3 + month3_interest

# print out table
print()
print("-" * 7, "Calculating", "-" * 7)
print()
print("Month  ", "Starting Balance  ", "Interest  ", "Ending Balance")
print("1      ", format(initial_investment, "<18,.2f"), format(month1_interest, "<10,.2f"), format(month1_ending, ",.2f"))
print("2      ", format(month1_ending, "<18,.2f"), format(month2_interest, "<10,.2f"), format(month2_ending, ",.2f"))
print("3      ", format(month2_ending, "<18,.2f"), format(month3_interest, "<10,.2f"), format(month3_ending, ",.2f"))





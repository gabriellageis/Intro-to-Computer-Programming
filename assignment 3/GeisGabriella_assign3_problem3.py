"""
Gabriella Geis
26 September, 2019
Section 002
Assignment 3 - Problem 3
"""

# user input date in format YYYYMMDD
user_date = int(input("Enter a date in YYYYMMDD format (i.e. 20190918 for September 18th, 2019): "))

# sepearate day, month, year
day = user_date % 100

month_nomod = int((user_date - day) / 100)
month = month_nomod % 100

year = int((month_nomod - month) / 100)

# date is invalid
if month > 12 or month < 1 or day > 31 or day < 1:
    print("That's not a valid date!")
elif month == 2  and day > 28:
    print("That's not a valid date!")
elif (month == 9 or month == 4 or month == 6 or month == 11) and day > 30:
    print("That's not a valid date!")

# date is before beginning of semester 20190903
if user_date < 20190903:
    print("This date is before the Fall 2019 semester")

# date is after end of semester 20191213
if user_date > 20191213:
    print("This date is after the Fall 2019 semester")

# see if there is class that date
if year == 2019:
    if month == 9 and (day == 3 or day == 5 or day == 10 or day == 12 or day == 17 or day == 19 or day == 24 or day == 26):
        print("You have class today")
    elif month == 10 and (day == 1 or day == 3 or day == 8 or day == 10 or day == 17 or day == 21 or day == 24 or day == 29 or day == 31):
        print("You have class today")
    elif month == 11 and (day == 5 or day == 7 or day == 12 or day == 14 or day == 19 or day == 21 or day == 26):
        print("You have class today")
    elif month == 12 and (day == 3 or day == 5 or day == 10 or day == 12):
        print("You have class today")
    else:
        print("You do not have class today")

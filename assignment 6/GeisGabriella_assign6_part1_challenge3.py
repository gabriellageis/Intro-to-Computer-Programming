"""
Gabriella Geis
31 October, 2019
Section 002
Assignment 6 - Problem 1 - Challenge 3
"""

# function: valid_date
# input: month (integer), day (integer)
# processing: determine if given month/day values give a valid date
# output: return True or False value

# 30 days: september, april, june, november: 4, 6, 9, 11
# 28 days: february: 2
# 31 days: 1, 3, 5, 7, 8, 10, 12

def valid_date(m,d):
    if m == 2 and (d > 0 and d <= 28):
        return True
    elif (m==4 or m==6 or m==9 or m==11) and (d > 0 and d <= 30):
        return True
    elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d > 0 and d <= 31):
        return True
    else:
        return False

print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False

print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False

print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False

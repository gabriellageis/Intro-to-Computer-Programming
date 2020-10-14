"""
Gabriella Geis
31 October, 2019
Section 002
Assignment 6 - Problem 1 - Challenge 4
"""

def simple_sort_version1(x,y):
    if x > y:
        return y,x
    else:
        return x,y


# your function should work perfectly with the following lines of code
a,b = simple_sort_version1(10,20)
print (a,b) # 10 20

a,b = simple_sort_version1(20,10)
print (a,b) # 10 20

a,b = simple_sort_version1(30,30)
print (a,b) # 30 30

"""
Gabriella Geis
31 October, 2019
Section 002
Assignment 6 - Problem 1 - Challenge 5
"""
# 1,2,3
# 1,3,2
# 2,1,3
# 2,3,1
# 3,1,2
# 3,2,1

def simple_sort_version2(x,y,z):
    if x > y and (y > z or y==z):
        return z,y,x
    elif x > z and (z > y or z==y):
        return y,z,x
    elif y > x and (x > z or x==z):
        return z,x,y
    elif y > z and (z > x or z==x):
        return x,z,y
    elif z > x and (x > y or x==y):
        return y,x,z
    elif z > y and (y > x or y==x):
        return x,y,z
    else:
        return x,y,z

# your function should work perfectly with the following lines of code
a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30

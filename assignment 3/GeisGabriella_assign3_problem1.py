"""
Gabriella Geis
26 September, 2019
Section 002
Assignment 3 - Problem 1
"""

# name of program
print("Valid Triangle Tester")
print()

# user input 3 points on coordinate plane
x1_position = float(input("Enter Point #1 - x position: "))
y1_position = float(input("Enter Point #1 - y position: "))
x2_position = float(input("Enter Point #2 - x position: "))
y2_position = float(input("Enter Point #2 - y position: "))
x3_position = float(input("Enter Point #3 - x position: "))
y3_position = float(input("Enter Point #3 - y position: "))

# compute the distance bewteen points
side1_distance = ((x1_position - x2_position)**2 + (y1_position - y2_position)**2)**0.5
side2_distance = ((x3_position - x1_position)**2 + (y3_position - y1_position)**2)**0.5
side3_distance = ((x2_position - x3_position)**2 + (y2_position - y3_position)**2)**0.5

# print the distance rounded to 2 decimal places
print()
print("The length of each side of your test shape is:")
print()
print("Side 1:", format(side1_distance, ".2f"))
print("Side 2:", format(side2_distance, ".2f"))
print("Side 3:", format(side3_distance, ".2f"))
print()

# determine if points form a valid triangle
if (side1_distance + side2_distance > side3_distance) and (side2_distance + side3_distance > side1_distance) and (side3_distance + side1_distance > side2_distance):
    print("This is a valid triangle!")
# report whether it is equilateral, isosceles, or scalene
    if format(side1_distance, ".2f") == format(side2_distance, ".2f") == format(side3_distance, ".2f"):
        print("This is an equilateral triangle")
    elif side1_distance == side2_distance or side2_distance == side3_distance or side3_distance == side1_distance:
        print("This is an isosceles triange")
    else:
        print("This is a scalene triangle")
else:
    print("This is not a valid triangle")



"""
Gabriella Geis
19 September, 2019
Section 002
Assignment 2 - Problem 3
"""

# print name of program
print("Minecraft block distance calculator")
print()

# user input two block's x/y/z components
block_1_x = float(input("Block #1 x: "))
block_1_y = float(input("Block #1 y: "))
block_1_z = float(input("Block #1 z: "))
block_2_x = float(input("Block #2 x: "))
block_2_y = float(input("Block #2 y: "))
block_2_z = float(input("Block #2 z: "))

# compute x/y/z distance between two blocks
x_distance = abs(block_1_x - block_2_x)
y_distance = abs(block_1_y - block_2_y)
z_distance = abs(block_1_z - block_2_z)

# compute straight line distance between the two blocks
straightline_distance = format((((x_distance ** 2) + (y_distance ** 2) + (z_distance ** 2))**0.5), ",.2f")

# print the distances
print()
print("X distance:", x_distance)
print("Y distance:", y_distance)
print("Z distance:", z_distance)
print("Straight line distance:", straightline_distance)

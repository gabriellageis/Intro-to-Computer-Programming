"""
Gabriella Geis
10 October, 2019
Section 002
Assignment 4 - Problem 2b
"""

# Pick Up Sticks

# number of sticks on the table

while True: 
    num_sticks = int(input("How many sticks (10-100)? "))
    if num_sticks < 10:
        print("Sorry, that's too few sticks. Try again.")
    elif num_sticks > 100:
        print("Sorry, that's too many sticks. Try again.")
    else:
        print("Great Let's play ...")
        print()
        print()
        break
    
# ask how many sticks to take away

turn = 0

while num_sticks >= 0:
    # check if even because this will switch everytime num_sticks is changed
    if (turn % 2) == 0:
        print("Turn: Player 1")
        player = 2
    else:
        print("Turn: Player 2")
        player = 1
    print("There are", num_sticks, "on the table.")
    take = int(input("How many sticks do you want to take (1, 2, or 3)? "))
    if take < 1 or take > 3:
        print("Sorry, that's not a valid number.")
        print()
    elif take > num_sticks:
        print("Sorry that would bring the total # of sticks below 0. Try again.")
        print()
    else:
        num_sticks = num_sticks - take
        print()
        # switch player
        turn += 1
    if num_sticks == 0: 
        print()
        print("There are no sticks left on the table! Game over.")
        print("Player", player, "wins!")
        break
        

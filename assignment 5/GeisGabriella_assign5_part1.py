"""
Gabriella Geis
24 October, 2019
Section 002
Assignment 5 - Problem 1
"""
# Pizza Party

# user input of number people attending party, budget, prices
num_people = int(input("How many people will be attending your party? "))
budget = float(input("Enter budget for your party: "))
slice_price = float(input("Cost per slice of pizza: "))
pie_price = float(input("Cost per whole pizza pie (8 slices): "))
slices = 0

# number of slices for each person --> for loop
    # data validation --> while loop
for p in range(1, num_people+1):
    while p < num_people + 1:
        person_slices = int(input("Enter number of slices for person #" + str(p) + ": "))
        if person_slices > 0:
            slices += person_slices
            break
        else:
            print("Not a valid entry, try again!")
            print()
            
# determine number of pies and slices to purchase
total_pies = slices // 8
total_slices = slices % 8

# determine total cost
pies_cost = total_pies * pie_price
slices_cost = total_slices * slice_price
total_cost = pies_cost + slices_cost
left_over = budget - total_cost

# if total cost greater than budget order cannot be completed
    # determine how over budget you are
if total_cost > budget:
    print("Your order cannot be completed.")
    print("You would need to purchase", total_pies, "pies and", total_slices, "slices")
    over_budget = abs(left_over)
    print("This would put you over budget by", format(over_budget, ".2f"))
# print how much money left after order
else:
    print("You should purchase", total_pies, "pies and", total_slices, "slices")
    print("Your total cost will be:", format(total_cost, ".2f"))
    if left_over == 0:
        print("You will have no money left after your order.")
    else:
        print("You will still have", format(left_over, ".2f"), "left after your order")
    
    

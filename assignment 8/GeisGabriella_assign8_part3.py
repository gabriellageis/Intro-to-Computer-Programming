"""
Gabriella Geis
21 November, 2019
Section 002
Assignment 8 - Problem 3
"""

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_quantity = [10, 5, 20]

# ask for product
while True:
    search = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    # quit
    if search == 'q':
        print("See you soon!")
        break
    # search
    elif search == 's':
        product = input("Enter a product name: ")
        if product in product_names:
            position = product_names.index(product)
            print("We sell", product, "at", product_costs[position], "per unit")
            print("We currently have", product_quantity[position], "in stock")
            product_quantity[position] -= 1
            print()
        else:
            print("Sorry we don't sell", product)
            print()
    # list
    elif search == 'l':
        print(format("Product", "<20s"), format("Price", "<10s"), format("Quantity", "<10s"))
        for i in range(len(product_names)):
            print(format(product_names[i], "<20s"), format(product_costs[i], ">5.2f"), format(product_quantity[i], ">13d"))
        print()
    # add
    elif search == "a":
        # product name
        while True:
            new_product = input("Enter a new product name: ")
            if new_product in product_names:
                print("Sorry, we already sell that product. Try again.")
            else:
                break
        product_names.append(new_product)
        # product cost
        while True:
            new_cost = float(input("Enter a product cost: "))
            if new_cost <= 0:
                print("Invalid cost. Try again.")
            else:
                break
        product_costs.append(new_cost)
        # product quantity
        while True:
            new_quantity = int(input("How many of these products do we have? "))
            if new_quantity <= 0:
                print("Invalid quantity. Try again.")
            else:
                break
        product_quantity.append(new_quantity)
        print("Product added!")
        print()
    # remove
    elif search == 'r':
        remove_product = input("Enter a product name: ")
        if remove_product in product_names:
            remove_position = product_names.index(remove_product)
            product_names.remove(remove_product)
            product_costs.remove(product_costs[remove_position])
            product_quantity.remove(product_quantity[remove_position])
            print("Product removed!")
            print()
        else:
            print("Product doesn't exist. Can't remove.")
            print()
    # update
    elif search == 'u':
        update_product = input("Enter a product name: ")
        if update_product in product_names:
            update_position = product_names.index(update_product)
            print("What would you like to update?")
            update_search = input("(n)ame, (c)ost or (q)uantity: ")
            # update names
            if update_search == 'n':
                while True:
                    update_name = input("Enter a new name: ")
                    if update_name in product_names:
                        print("Duplicate name!")
                    else:
                        product_names[update_position] = update_name
                        print("Product name has been updated")
                        print()
                        break
            # update costs
            elif update_search == 'c':
                while True:
                    update_cost = float(input("Enter a new cost: "))
                    if update_cost == product_costs[update_position] or update_cost <= 0:
                        print("Invalid cost!")
                    else:
                        product_costs[update_position] = update_cost
                        print("Product cost has been updated")
                        print()
                        break
            # update quantity
            elif update_search == 'q':
                while True:
                    update_quantity = int(input("Enter a new quantity: "))
                    if update_quantity == product_quantity[update_position] or update_quantity <= 0:
                        print("Invalid quantity!")
                    else:
                        product_quantity[update_position] = update_quantity
                        print("Product quantity has been updated")
                        print()
                        break
            else:
                print("Invalid option")
                print()
        else:
            print("Product doesn't exist. Can't update.")
            print()
    # report
    elif search == 'e':
        # highest
        highest = max(product_costs)
        highest_position = product_costs.index(highest)
        highest_name = product_names[highest_position]
        print("Most expensive product:      ", highest, highest_name)
        # lowest
        lowest = min(product_costs)
        lowest_position = product_costs.index(lowest)
        lowest_name = product_names[lowest_position]
        print("Least expensive product:     ", lowest, lowest_name)
        # total
        total = 0
        for i in range(len(product_costs)):
            total_costs = product_costs[i] * product_quantity[i]
            total += total_costs
        print("Total value of all products:", format(total, ".2f"))
        print()
    # invalid 
    else:
        print("Invalid option, try again")
        print()

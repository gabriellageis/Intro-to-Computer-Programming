"""
assignment 8 - warmup
"""

# fitbit application

"""
weight on first and last day
change from first to last day
average, highest, lowest weights
"""

weights = []

for i in range(7):
    
    # ask for weight
    w = int(input("Weight for today: "))

    # add weight to list
    weights += [w]

print()
print("Weight on first day:", weights[0])
print("Weight on last day:", weights[-1])
print("Change from first to last:", weights[-1] - weights[0])
print("Average:", sum(weights)/len(weights))
print("Highest:", max(weights))
print("Lowest:", min(weights))

"""
Gabriella Geis
24 October, 2019
Section 002
Assignment 5 - Problem 3c
"""

# user input starting and ending numbers
while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start < 1 or end < 1:
        print("Start and end must be positive")
        print()
    elif start > end:
        print("End number must be greater than start number")
        print()
    else:
        print()
        break


# from start - end
print("Prime numbers: ")
for number in range(start, end + 1):
    if number == 1:
        continue
    else:
        prime = True
        # test divisibility of every number 
        for test in range(2, number):
            # if number 
            if number % test == 0:
                prime = False
                break
        if prime == True:
                print(number)

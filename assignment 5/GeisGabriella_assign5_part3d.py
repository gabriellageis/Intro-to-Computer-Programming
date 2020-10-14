"""
Gabriella Geis
24 October, 2019
Section 002
Assignment 5 - Problem 3d
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

# find total number of spaces
end_spaces = 0
end_num = end
while end_num > 0:
    end_num = end_num // 10
    end_spaces = end_spaces + 1
total_spaces = end_spaces + 1
    
counter = 0
# from start - end
print("Prime numbers: ")
print()
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
            
        # printing the prime numbers
        if prime == True:
            # calculate number of spaces for each number
            calc_num = number
            end_spaces = 0
            
            while calc_num > 0:
                calc_num = calc_num // 10
                end_spaces = end_spaces + 1
            each_spaces = end_spaces + 1
            number_spaces = total_spaces - each_spaces
            
            # determine when to start new line
            empty = " "

            while prime == True:
                counter += 1
                if counter < 10:
                    print(number_spaces * empty, number, end = "")
                    break
                elif counter == 10:
                    print(number_spaces * empty, number, end = "\n")
                    counter = 0
                    break


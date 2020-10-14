"""
Gabriella Geis
31 October, 2019
Section 002
Assignment 6 - Problem 3
"""

# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)
def horizontal_line(width,char):
    return width*char + "\n"

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)
def vertical_line(shift,height,char):
    pattern = ""
    for i in range(height):
        pattern += shift*" " + char + "\n"
    return pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)
def two_vertical_lines(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += char + " "*(width-2) + char + "\n"
    return pattern

# function: number_0
def number_0(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(two_vertical_lines(width, height-2, char)) + str(horizontal_line(width, char))
    return pattern 
    
# function:   number_1
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_1(width, character):
    pattern = vertical_line(width-1, 5, character)
    return pattern

# function: number_2
def number_2(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(vertical_line(width-1, height-4, char)) + str(horizontal_line(width, char)) + str(vertical_line(0, height-4, char)) + str(horizontal_line(width, char))
    return pattern    

# function: number_3
def number_3(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(vertical_line(width-1, height-4, char)) + str(horizontal_line(width, char)) + str(vertical_line(width-1, height-4, char)) + str(horizontal_line(width, char))
    return pattern

# function: number_4
def number_4(width, char):
    height = 5
    pattern = str(two_vertical_lines(width, height-3, char)) + str(horizontal_line(width, char)) + str(vertical_line(width-1, height-3, char))
    return pattern
                                                                            
# function: number_5
def number_5(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(vertical_line(0, height-4, char)) + str(horizontal_line(width, char)) + str(vertical_line(width-1, height-4, char)) + str(horizontal_line(width, char))
    return pattern

# function: number_6
def number_6(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(vertical_line(0, height-4, char)) + str(horizontal_line(width, char)) + str(two_vertical_lines(width, height-4, char)) + str(horizontal_line(width, char))
    return pattern

# function: number_7
def number_7(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(vertical_line(width-1, height-1, char))
    return pattern

# function: number_8
def number_8(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(two_vertical_lines(width, height-4, char)) + str(horizontal_line(width, char)) + str(two_vertical_lines(width, height-4, char)) + str(horizontal_line(width, char)) 
    return pattern

# function: number_9
def number_9(width, char):
    height = 5
    pattern = str(horizontal_line(width, char)) + str(two_vertical_lines(width, height-4, char)) + str(horizontal_line(width, char)) + str(vertical_line(width-1, height-3, char))
    return pattern

# function: print_number
def print_number(number, width, char):
    if number == 0:
        number = number_0(width, char)
        print(number)
    elif number == 1:
        number = number_1(width, char)
        print(number)
    elif number == 2:
        number = number_2(width, char)
        print(number)
    elif number == 3:
        number = number_3(width, char)
        print(number)
    elif number == 4:
        number = number_4(width, char)
        print(number)
    elif number == 5:
        number = number_5(width, char)
        print(number)
    elif number == 6:
        number = number_6(width, char)
        print(number)
    elif number == 7:
        number = number_7(width, char)
        print(number)
    elif number == 8:
        number = number_8(width, char)
        print(number)
    elif number == 9:
        number = number_9(width, char)
        print(number)

# function: plus
def plus(width, char):
    height = 5
    if width % 2 == 0:
        pattern = str(two_vertical_lines(0, height - 3, char))+ str(horizontal_line(width, char)) + str(two_vertical_lines(0, height - 3, char))
    else:
        pattern = str(vertical_line(width-3, height - 3, char))+ str(horizontal_line(width, char)) + str(vertical_line(width-3, height - 3, char))
    return pattern

# function: minus
def minus(width, char):
    height = 5
    pattern = str(horizontal_line(width, char))
    return pattern

# function: check_answer
def check_answer(number1, number2, answer, operator):
    if operator == "+":
        if number1 + number2 == answer:
            correct = True
            return correct
        else:
            correct = False
            return correct
    elif operator == "-":
        if number1 - number2 == answer:
            correct = True
            return correct
        else:
            correct = False
            return correct



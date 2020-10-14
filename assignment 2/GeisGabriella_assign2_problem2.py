"""
Gabriella Geis
19 September, 2019
Section 002
Assignment 2 - Problem 2
"""

# enter 2 numbers between 0 and 999
first_number = int(input("Enter a number between 0 and 999: "))
second_number = int(input("Enter another number between 0 and 999: "))

# separate the numbers in the ones place
first_number_ones = first_number%10
second_number_ones = second_number%10

# compute the sum of ones
sum_of_ones = first_number_ones + second_number_ones

# separate the numbers in the tens place
first_number_tens = int((first_number - first_number_ones) / 10)
first_number_tens_mod = first_number_tens % 10

second_number_tens = int((second_number - second_number_ones) / 10)
second_number_tens_mod = second_number_tens % 10

# compute the sum of tens
sum_of_tens = first_number_tens_mod + second_number_tens_mod

# separate the numbers in the hundreds place
first_number_hundreds = int((first_number_tens - first_number_tens_mod) / 10)
second_number_hundreds = int((second_number_tens - second_number_tens_mod) / 10)

# compute the sum of hundreds
sum_of_hundreds = first_number_hundreds + second_number_hundreds

# print sums

print("Sum of ones     = ", first_number_ones, "+", second_number_ones, "=", sum_of_ones)
print("Sum of tens     = ", first_number_tens_mod, "+", second_number_tens_mod, "=", sum_of_tens)
print("Sum of hundreds = ", first_number_hundreds, "+", second_number_hundreds, "=", sum_of_hundreds)


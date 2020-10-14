"""
Gabriella Geis
24 October, 2019
Section 002
Assignment 5 - Problem 2
"""

# Dynamic Gradebook

# accumulator variables --> average_class = 0
total_grades = 0
total_tests = 0

# input number of students in class, number of tests given
    # while loop --> validate information (numbers are positive)
while True:
    num_students = int(input("How many students are in your class? "))
    if num_students < 1:
        print("Invalid # of students, try again.")
        print()
    else:
        while True:
            num_tests = int(input("How many tests in this class? "))
            if num_tests < 1:
                print("Invalid # of tests, try again.")
                print()
            else:
                print()
                print("Here we go!")
                print()
                break
        break

# for loop --> enter scores for each student
    # while loop --> validate information (numbers are positive)
    # display average for student, add to accumulator variable
for s in range(1, num_students+1):
    print("**** Student #" + str(s) + "****")
    student_grades = 0
    for t in range(1, num_tests+1):
        while True:
            test_score = int(input("Enter score for test #" + str(t) + ": "))
            if test_score < 1:
                print("Invalid score, try again.")
            else:
                student_grades += test_score
                total_grades += test_score
                total_tests += 1
                break
    average_score = student_grades / num_tests
    print("Average score for student #" + str(s) + " is", format(average_score, ".2f"))
    print()
    
# overall average for entire class
average_all = total_grades / total_tests
print("Average score for all students is:", format(average_all, ".2f"))

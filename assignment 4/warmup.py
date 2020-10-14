"""
warmup
"""

# print 1 - 100 (inclusive)
"""
# starting number
c = 1

# set up a loop to continue as long as c has not reached our ending number
while c <= 100:
    print(c)
    c += 1
"""

# write a program that lets user enter potentially unlimited number of grades

# when finished, compute average grade for the student
"""
total = 0
numtests = 0

while True:
    # ask for grade
    grade = int(input("Enter a score: "))
    
    # put grade into total
    total += grade
    
    # update numtests for this test
    numtests += 1
    
    again = input("Another ? ")
    if again == "no":
        break

print("Your total points:", total)
print("Your average score:", total/numtests)
"""

# user input
"""
num = int(input("Enter a positive number: "))

while num < 1:
    print("BAD USER!")
    num = int(input("Enter a POSITIVE number: "))
    
print("You gave me:", num)
"""

while True:

    num = int(input("Enter a positive number: "))
    if num < 1:
        print("BAD USER!")
    else:
        break

"""
Gabriella Geis
3 Decmeber, 2019
Section 002
Assignment 9
"""
import math

answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
split_key = answerkey.split(",")

# ask user for a filename they want to open
filename = input("Enter a filename to open: ")

# open the file that they asked for
try:
    connection = open(filename, "r")
except:
    print("File could not be opened!")
else:
    # read in all the data
    data = connection.read()

    # close the file
    connection.close()

    # print success
    print("Successfully opened", filename)
    print()

    # isolate the students from one another
    students = data.split("\n")

    # examine every line in the file
    valid = 0
    invalid = 0
    highest = 0
    lowest = 100
    scores_list = []
    num_list = []
    
    for line in students:
        # split apart each line based on the comma
        items = line.split(",")
        
        # if we have exactly 26 items, this is a valid line
        if len(items) == 26:
            valid += 1

            # this is where scoring happens!
            num = items[0]
            student_answer = items[1:]
            score = 0

            # compare students answers to correct answers
            # compute a score
            for i in range(len(student_answer)):
                if student_answer[i] == split_key[i]:
                    score += 4
                elif student_answer[i] == "":
                    score += 0
                else:
                    score -= 1
            
            # store in a list
            scores_list.append(score)
            num_list.append(num)
            
            
            # generating results file
            results_name = filename[0:6] + "_grades.txt"

            results_open = open(results_name, "a")
    
            results_open.write(str(num))
            results_open.write(", ")
            results_open.write(str(score))
            results_open.write("\n")

            results_open.close()


            # figure out higher and lower
            if score > highest:
                highest = score
            if score < lowest:
                lowest = score

        else:
            invalid += 1

    # mean score (average)
    mean = sum(scores_list) / len(scores_list)

    # figure out median value
    sorted_scores = [] + scores_list
    sorted_scores.sort()
    
    if len(sorted_scores) % 2 == 0:
        id1 = int(len(sorted_scores) / 2)
        id2 = int((len(sorted_scores) / 2) - 1)
        median = math.ceil((sorted_scores[id1] + sorted_scores[id2]) / 2)
    else:
        id1 = math.ceil(len(sorted_scores) / 2)
        median = sorted_scores[id1]
    
    # figure out mode value
    unique = []
    seen = []
    for i in range(len(sorted_scores)):
        if sorted_scores[i] in unique:
            position = unique.index(sorted_scores[i])
            seen[position] += 1
        else:
            unique.append(sorted_scores[i])
            seen.append(1)

    most = max(seen)
    most_position = seen.index(most)
    mode = unique[most_position]

    # figure out range
    largest = max(unique)
    smallest = min(unique)
    range1 = largest - smallest


    # Grade Summary
    print("Grade Summary:")
    print("Total students:", valid)
    
    # print data
    print("Unusable lines in the file:", invalid)
    print("Highest score:", highest)
    print("Lowest score:", lowest)
    print("Mean score:", format(mean, ".2f"))
    print("Median score:", median)
    print("Mode:", mode)
    print("Range:", range1)


    # curve
    curve = input("Would you like to curve the exam? 'y' or 'n': ")
    if curve == 'y':
        while True:
            new_mean = float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0: "))
            if new_mean > mean:
                increase = new_mean - mean
                
                results_clear = open(results_name, "w")
                # generating curved results file
                for i in range(len(scores_list)):
                    position = scores_list.index(scores_list[i])
                    score = scores_list[position]
                    num = num_list[position]
                    results_open = open(results_name, "a")
                    
                    results_open.write(str(num))
                    results_open.write(", ")
                    results_open.write(str(score))
                    results_open.write(", ")
                    results_open.write(str(format(score + increase, ".2f")))
                    results_open.write("\n")

                    results_open.close()
                    
                print("Done! Check your grade file!")
                break
            else:
                print("Invalid curve, try again.")
    else:
        print("End of program")


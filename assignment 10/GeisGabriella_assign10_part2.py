"""
Gabriella Geis
10 December, 2019
Section 002
Assignment 10 - Part 1
"""
import time

"""
# method 2: opening data file from the web

import urllib.request

try:
    url = 'https://cs.nyu/.edu/~kapp/python/novie_reviews.txt'
    connection = urllib.request.urlopen(url).decode('utf-8')
except:
    print("Something went wrong")
else:
    print("Everything is OK")
"""

# method 1: open data file from hard drive

try:
    connection = open("movie_reviews.txt", "r")
    data = connection.read()
    connection.close()
except:
    print("Something went wrong:")
else:
    # print("Everything is OK")

    # get first time
    first_time = time.time()
    print("Initializing sentiment database")
    
    # cut apart the data based on the line break
    lines = data.split("\n")
    # print("There are", len(lines), "records in the data file")
    
    # set up a dictionary to keep track of our words
    sentiment = {}

    # examine every single line in the data file
    for item in lines:

        # extract score
        score = int(item[0])

        # extract the rest of the line
        rest = item[2 :]
        rest = str.lower(rest)
        
        # isolate each word
        words = rest.split(' ')

        # visit each word
        for w in words:

            # clean up each word by removing non-alphabetic characters
            clean = ""
            for c in w:
                if c.isalpha():
                    clean += c
                    
            # is this a new word?
            if clean not in sentiment:
                sentiment[clean] = [score, 1]
            else:
                sentiment[clean][0] += score
                sentiment[clean][1] += 1

    # outside of initial 'for' loop
    last_time = time.time()
    print("Sentiment database initialization complete")
    
    total_time = last_time - first_time


    # get length of dictionary
    count = 0
    for value in sentiment.values():
        count += 1
    
    print("Total unique words analyzed:", count)

    print("Analysis took", format(total_time, ".2f"), "seconds to complete")

    # ask the user for a phrase
    print()
    phrase = input("Enter a phrase: ")

    # i am so happy
    words = phrase.split(" ")
    #print("words:", words)

    total = 0
    num = 0

    # visit every word
    for w in words:
        w = str.lower(w)
        if w in sentiment:
            average = sentiment[w][0] / sentiment[w][1]
            print(w, "has a score of", average)
            
            total += average
            num += 1
        else:
            print(w, "does not have a score")

    if total != 0:
        final_average = total / num
        print("Overall average is:", final_average)
        
        if final_average >= 2.1:
            print("This is a POSITIVE phrase")
        else:
            print("This is a NEGATIVE phrase")
    else:
        print("Not enough data to compute sentiment")
    
    



        
    

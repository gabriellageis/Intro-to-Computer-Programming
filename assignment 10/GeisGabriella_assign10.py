"""
Gabriella Geis
10 December, 2019
Section 002
Assignment 10
"""
import time

# function to modularize sentiment analysis program

def compute_sentiment(data):

    words = data.split(" ")
    
    total = 0
    num = 0

    # visit every word
    for w in words:
        w = str.lower(w)
        clean_word = ""
        
        for char in w:
            if char.isalpha():
                clean_word += char
                
        if clean_word in sentiment:
            average = sentiment[clean_word][0] / sentiment[clean_word][1]
            #print(clean_word, "has a score of", average)
            
            total += average
            num += 1
        #else:
            #print(clean_word, "does not have a score")

    if total != 0:
        final_average = total / num
        return final_average
        
    else:
        return "Not enough data to compute sentiment"


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

        # clean up data - remove any non alphabetic characters
        # also make everything lowercase
        rest = str.lower(rest)

        clean = ""
        for c in rest:
            if c.isalpha():
                clean += c
            else:
                clean += " "
        words = clean.split(" ")

        # visit every words nad associate with point values
        for w in words:

            # is this a new word?
            if w not in sentiment:
                sentiment[w] = [score, 1]
            else:
                sentiment[w][0] += score
                sentiment[w][1] += 1

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
    print()



    # TESTING
    a1 = compute_sentiment("The happy dog and the sad cat")
    a2 = compute_sentiment("It made me want to poke out my eyeballs")
    a3 = compute_sentiment("I loved this movie!")
    a4 = compute_sentiment("Pikachu charmander!!!")

    print (a1, a2, a3) # 2.280133625200816 1.768915591909414 2.07085642181999 2.0

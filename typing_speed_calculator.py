from time import *
from random import randrange
import numpy as np

def mistake(str1, str2):

    #create matrix of zeros
    len1=len(str1)+1
    len2=len(str2)+1
    matrix = np.zeros((len1,len2))

    #number x and y indices in matrix
    for i in range(len1):
        matrix[i,0] = i
    for j in range(len2):
        matrix[0,j] = j
    
    #two for loops to compare strings letter by letter
    for i in range(1, len1):
        for j in range(1, len2):
            if str1[i-1]==str2[j-1]:
                matrix[i,j] = min(
                matrix[i-1,j] + 1,
                matrix[i,j-1] + 1,
                matrix[i-1,j-1])
            else:
                matrix[i,j] = min(
                matrix[i-1,j] + 1,
                matrix[i-1,j-1] + 1,
                matrix[i,j-1] + 1)
    return(matrix[len1-1,len2-1])

def speed(t1, t2, inp):
    time_taken = np.round(t2 - t1, 3)
    word_count = len(inp.split(" "))
    typing_speed = round((word_count*60)/time_taken)
    print("Time taken: {0}sec\nWords Typed: {1}"
            .format(time_taken, word_count))
    return typing_speed

if __name__ == '__main__':

    names=["We","I","They","He","She","Jack","Jim"]
    verbs=["was","is","are","were"]
    nouns=["playing a game","watching television",
            "talking","dancing","speaking"]
    sentences_to_type = []
    while len(sentences_to_type) <= 2:
        sentences_to_type.append(names[randrange(0,len(names)-1)]+
                                " "+verbs[randrange(0,len(verbs)-1)]+
                                " "+nouns[randrange(0,len(nouns)-1)]+
                                ".")

    to_type = ''.join(sentences_to_type)

    print("********* Typing Speed Test********\n\n")
    print(to_type)
    t1 = time()
    testinput = input("\nEnter: ")
    t2 = time()
    time_taken = t2 - t1
    err = mistake(to_type, testinput)
    t_speed = speed(t1, t2, testinput)
    print("Speed: {0} w/min\nErrors: {1}".format(t_speed,int(err)))
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())
    
    scoreList = []

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        
        totalScore = 0
    
        for i in range(first, last+1):
            matchList = re.findall("?=(%s)"%genes[i], d)
            totalScore += health[i] * len(matchList)
            
        scoreList.append(totalScore)
        
    print(min(scoreList), max(scoreList))

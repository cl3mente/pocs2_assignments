#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    
    freqArr = [ [] for i in range(10)]

    for i in range(len(arr)):
        
        if i < len(arr)//2:
            
            arr[i][1] = "-"
        
        freqArr[int(arr[i][0])].append((arr[i][1]))

    for i in freqArr:
        for j in i:
            print(j, end = " ")
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

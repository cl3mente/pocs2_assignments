#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    
    notif = 0
    
    for i in range(d, len(expenditure)):
        
        arr = expenditure[i-d:i]
        arr.sort()
        if d%2 == 1:
            median = arr[(len(arr)//2)]
        else:
            n1 = arr[(len(arr)//2)]
            n2 = arr[(len(arr)//2)+1]
            median = (n1 + n2)/2
        if expenditure[i] >= 2*median:
            notif += 1
    return notif


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

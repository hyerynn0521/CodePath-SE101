#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'first_missing_positive_integer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY integers as parameter.
#
# It will check the integer array and return the first 
# missing positive integer. 
#

def first_missing_positive_integer(integers):
    integers = sorted(integers)
    if integers[-1] <= 0:
        return 1
    consecutive = True
    answer = 0
    for i in range(len(integers)-1):
        if integers[i+1] - integers[i] > 1 and integers[i] >= 0:
            consecutive = False
            answer = integers[i] + 1
            break
    if consecutive == True:
        return integers[-1]+1
    return answer
    
if __name__ == '__main__':

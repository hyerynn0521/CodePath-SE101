#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'rotate_array' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY input_array
#  2. INTEGER k
#  And will rotate the input_array to the right by 
#  k steps. The resulting array will be returned.
#

def rotate_array(input_array, k):
    # Write your code here
    if len(input_array) == 1 or len(input_array) == 0:
        return input_array
    for j in range(k):
        last = input_array[-1]
        for i in range(len(input_array)-2, -1, -1):
            input_array[i+1] = input_array[i]
        input_array[0] = last
    return input_array

def rotate_once(input_array):
    if len(input_array) == 1 or len(input_array) == 0:
        return input_array
    last = input_array[-1]
    for i in range(len(input_array)-2, -1, -1):
        input_array[i+1] = input_array[i]
    input_array[0] = last
    return input_array
if __name__ == '__main__':

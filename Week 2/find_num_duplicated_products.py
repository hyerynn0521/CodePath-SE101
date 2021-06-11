#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numDuplicates' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY name
#  2. INTEGER_ARRAY price
#  3. INTEGER_ARRAY weight
#

def numDuplicates(name, price, weight):
    # Write your code here
    all_array = []
    count = {}
    duplicates = 0
    for i in range(len(name)):
        array = [name[i], price[i], weight[i]]
        count[str(array)] = 0
        all_array.append(array)
    for k in range(len(name)):
        count[str(all_array[k])] += 1
    for l in list(count.keys()):
        if count[l] > 1:
            duplicates += count[l] - 1
    return duplicates

if __name__ == '__main__':

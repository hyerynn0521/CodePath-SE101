#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getUniqueCharacter' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getUniqueCharacter(s):
    # Write your code here
    count = {}
    unique = ""
    i = 0
    for j in range(len(s)):
        count[s[j]] = 0
    for char in range(len(s)):
        count[s[char]] += 1
    for key in list(count.keys()):
        if count[key] == 1:
            unique = key
            break
    if unique == "":
        return -1
    for ch in range(len(s)):
        if s[ch] == unique:
            break
        i += 1
    return i +1
            

if __name__ == '__main__':

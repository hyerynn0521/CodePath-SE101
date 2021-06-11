#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
# Check if a is a palindrome and return 1 if it
# is a palindrome and 0 if it is not. 
#
#

def isPalindrome(a):
    inOrder = ""
    opposite = ""
    j = len(a) - 1
    for i in range(len(a)):
        if a[i].isalnum():
            inOrder += a[i]
        if a[j].isalnum():
            opposite += a[j]
        j -= 1
    
    if inOrder.lower() == opposite.lower():
        return 1
    return 0

if __name__ == '__main__':

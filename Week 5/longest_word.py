#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY words as parameter.
# This function will go through an array of strings, 
# identify the largest word, and return that word. 
#
'''
given array of strings (that could have multiple words) return the longest word.
'''
def longestWord(sentences):
    # Write your code here
    longest = ""
    longest_length = 0
    for strings in sentences:
        words = strings.split(" ")
        for word in words:
            if len(word) > longest_length:
                longest = word
                longest_length = len(word)
    return longest
            
            
        
    

if __name__ == '__main__':

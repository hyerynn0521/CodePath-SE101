#!/bin/python3

import math
import os
import random
import re
import sys
'''
Two strings are anagrams if they are permutations of each other.
In other words, both strings have the same size and the sma echaracters.
For example, "aaagmnrs" is an anagram of "anagrams". Given an array of strings, 
remove each string that is an anagram of an earlier string, then return the 
remaining array in sorted order.
'''

#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#

def funWithAnagrams(text):
    # Write your code here
    dict_text = {}
    dict_count = {}
    for index in range(len(text)):
        dict_text[index] = list(text[index])
        print(dict_text[index])
    for key in dict_text.keys():
        sort_list = ''.join(sorted(dict_text[key]))
        
        
        if sort_list in dict_count.keys():
            dict_count[sort_list] += 1
            text[key] = ""
        
        else:
            dict_count[sort_list] = 1
        print(text)
    index = 0
    while index < len(text):
        if text[index] == "":
            text.pop(index)
        else:
            index += 1
    
    return sorted(text)
        
    
        
if __name__ == '__main__':

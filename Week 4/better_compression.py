#!/bin/python3

import math
import os
import random
import re
import sys
'''
Consider a string, S, that is a series of characters, each followed
by its frequency as an integer. The string is not compressed correctly, 
so there may be multple occurrences of the same character. A properly
compressed string will consist of one instance of each character in 
alphabetical order followed by the total count of the character 
within the string.
'''

#
# Complete the 'betterCompression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def betterCompression(s):
    # Write your code here
    dictionary = {}
    curr_alpha = ''
    curr_numstring = ""
    curr_num = 0
    result = ""
    for i in range(len(s)):
        
        if s[i].isalpha():
            curr_alpha = s[i]
        elif s[i].isnumeric():
            curr_numstring += s[i]
            if i == len(s) - 1 or s[i+1].isalpha():
                curr_num = int(curr_numstring)
                if curr_alpha in dictionary.keys():
                    dictionary[curr_alpha] += curr_num
                else:
                    dictionary[curr_alpha] = curr_num
                curr_numstring = ""
        
        
    for key in sorted(dictionary):
        result += key
        result += str(dictionary[key])
    return result
    
            
            
                
                
                
        
if __name__ == '__main__':

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countErrors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY logs as parameter.
# Check the logs string array for errors and return
# the numbers of error messages. 
#
'''
given a stream of logging statements as a list, return the number of errors
hint: log lines with code 200 are neither warnings nor errors
'''

def countErrors(logs):
    # Write your code here
    error_count = 0
    for log in logs:
        words = log.split(" ")
        if words[1] != "200":
            error_count += 1
    return error_count
            
            
if __name__ == '__main__':

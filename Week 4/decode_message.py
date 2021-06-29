#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decodeMessage' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING encoded_message
#  2. 2D_STRING_ARRAY encoder
#
'''
Given an encoded string and a mapping of the original character to the 
encoded letters, can you decode the message?
'''

def decodeMessage(encoded_message, encoder):
    # Write your code here
    encoder_dict = dict(encoder)
    decrypted = ""
    found = False
    for msg_index in range(len(encoded_message)):
        if encoded_message[msg_index].isalpha():
            for key in encoder_dict.keys():
                if encoder_dict[key] == encoded_message[msg_index]:
                    decrypted += key
                    found = True
                    break
            if found == False:
                decrypted += encoded_message[msg_index]
            found = False       
        else:
           decrypted += encoded_message[msg_index] 
    return decrypted
        
    
        
if __name__ == '__main__':

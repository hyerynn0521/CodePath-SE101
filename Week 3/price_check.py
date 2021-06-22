#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'priceCheck' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY products
#  2. FLOAT_ARRAY productPrices
#  3. STRING_ARRAY productSold
#  4. FLOAT_ARRAY soldPrice
#

def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    actual = {}
    sold = {}
    error = 0
    for i in range(len(products)):
        actual[products[i]] = productPrices[i]
    for j in range(len(productSold)):
        sold[productSold[j]] = soldPrice[j]
    for k in range(len(productSold)):
        if actual[productSold[k]] != sold[productSold[k]]:
            error += 1
    return error
if __name__ == '__main__':
  
  
  

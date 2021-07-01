#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mostPeoplePerFloor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY people_per_floor as parameter.
#
'''
given list of list of number of people on each floor, calculate which floor has the most people
ex:
ppl_per_floor = [
[0, 3, 9, 11],
[2, 4, 8],
[1, 1, 1, 1, 1],
[7, 7]
]
0th floor 10 ppl, 1st 15 ppl, 2nd 18 ppl, 3rd 12 ppl, 4th 1 person.
Therefore, the function would return 2 (floor starts at zero like index)
'''

def mostPeoplePerFloor(people_per_floor):
    # Write your code here
    floors_people = {}
    most_people = 0
    most_ppl_floor = 0
    for people in people_per_floor:
        for floor in range(len(people)):
            if floor in floors_people.keys():
                floors_people[floor] += people[floor]
            else:
                floors_people[floor] = people[floor]
    for key in floors_people:
        if floors_people[key] >= most_people:
            most_people = floors_people[key]
            most_ppl_floor = key
    return most_ppl_floor
        
if __name__ == '__main__':

#
# Complete the 'countLongestAscending' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY number_array as parameter.
#
"""
Count the length of the longest ascending sequence in an array.
For instance, given [-1, 3, 5, 2, 5, 3, 9, 4, 8, 10, 12, 6]
the longest ascending sequence is of length 4 - [-1, 3, 5, 2, 5, 3, 9, "4, 8, 10, 12", 6] is the longest set of
numbers that is continuously increasing.
"""
def countLongestAscending(number_array):
# Write your code here
  ascending = 1
  longest = 0
  for i in range(1, len(number_array)):
    if number_array[i] > number_array[i-1]:
      ascending = ascending + 1
    if ascending > longest:
      longest = ascending
    elif not number_array[i] > number_array[i-1]:
      ascending = 1
  return longest

# Complete the 'isPowerOfThree' function below.
#
# This function checks if n is a power of 3 and
# returns true if it is and false if it is not.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
#
def isPowerOfThree(n):
# Write your code here
  if n == 0:
    return 0;
  while n%3 == 0:
    n = n/3
  if n/3 == 1:
    return 1
  return 0



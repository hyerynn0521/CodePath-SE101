#
# Complete the 'FizzBuzz' function below.
#
# This function takes in integer n as a parameter
# and prints out its value, fizz if n is divisible
# by 3, buzz if n divisible by 5, and fizzbuzz
# if n is divisible by 3 and 5.
#
def FizzBuzz(n):
# Write your code here
  for i in range(1, n+1):
    if i%3 == 0 and i%5 == 0:
      print("fizzbuzz")
    elif i%3 == 0:
      print("fizz")
    elif i%5 == 0:
      print("buzz")
    else:
      print(i)

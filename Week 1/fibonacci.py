#
# Complete the 'fibonacci' function below.
#
# The function accepts INTEGER n as parameter.
# and prints out the nth value of the fibonacci
# sequence
#
def fibonacci(n):
# Write your code here
  fib_array = [0, 1, 1]
  fibonacci = 0;
  length = len(fib_array) - 1
  if n < len(fib_array):
    print(fib_array[n])
    return
  while len(fib_array) - 1 <= n:
    length = len(fib_array) - 1
    fib_array.append(fib_array[length] + fib_array[length - 1])
  print(fib_array[n])
  return

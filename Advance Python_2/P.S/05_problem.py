from functools import reduce
# Write a program to find the maximum of the numbers in a list using the reduce
# function.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,77]
def greater(x, y):
  if x > y:
    return x
  else:
    return y

final = reduce(greater, l)
print(final)
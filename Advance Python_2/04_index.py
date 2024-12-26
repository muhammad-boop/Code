from functools import reduce
# MAP, FILTER & REDUCE
# ! Map
l = [1,2,4,5]
square = lambda x:x*x
sqList = map(square,l)
print(list(sqList))

# ! Filter Example
def even(n):
  if n%2==0:
    return True
  else:
    return False
evenList = filter(even,l)
print(list(evenList))
# ! Reduce
def sum(a,b):
  return a+b
print(reduce(sum,l))
# ! Another example
def multi(a,b):
  return a*b
print(reduce(multi,l)) 
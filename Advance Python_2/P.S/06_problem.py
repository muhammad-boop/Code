'''
Write a Python code snippet to filter out all odd numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9].
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def odd(n):
  if(n%2!=0):
    print(f"{n} is odd")
  else:
    print(f"{n} is even")
final = filter(odd,l)
print(list(final))
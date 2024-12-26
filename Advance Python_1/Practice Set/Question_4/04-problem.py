"""
Write a program to display a/b where a and b are integers. If b=0, display infinite by
handling the ‘ZeroDivisionError’.
"""
try:
  a = int(input("Enter a Number: "))
  b = int(input("Enter a Number: "))
  print(a/b)
except ZeroDivisionError as e:
    e = "Can't divide by zero"
    print(e)
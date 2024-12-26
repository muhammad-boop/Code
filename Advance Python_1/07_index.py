# RAISING EXCEPTIONS
a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
if(b==0):
  raise ZeroDivisionError("Cannot divide by zero")
else:
  print(f"The division of {a} and {b} is {a/b} ")
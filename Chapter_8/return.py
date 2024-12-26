# ! Return_Value_in_Python
def greet(name,end):
  print(f"Good Day {name}")
  print(end)
  return "Done"
a = greet("Muhammad","ThankYou")
print(a)
# ! Professional_Use
def sum():
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))
  c = int(input("Enter a number: "))
  result = a+b+c
  return result
a = sum()
print(a)
# Write a python function which converts inches to cms
def inches_to_cms(inches):
  result = inches *2.54
  return result
inches = int(input("Enter the value of inches: "))
print(f"{inches} inches to cm is {inches_to_cms(inches)}")
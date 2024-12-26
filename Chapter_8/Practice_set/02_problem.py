# Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c():
  f = int(input("Enter the value of Fahrenheit: "))
  c = (f-32)*5/9
  print(f"{f} Fahrenheit is equal to {c} Celsius")
f_to_c()
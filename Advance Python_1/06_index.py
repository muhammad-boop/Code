# EXCEPTION HANDLING IN PYTHON
# try:
#     data = int(input("Enter a number: "))
#     print(data)
# except Exception as e:
#     e = "Please entered a Valid Number"
#     print(e)
# print("Thanks!")
# ! Program Using Exception
try:
   number = int(input("Enter a Number: "))
   number1 = int(input("Enter a second Number: "))
   print(f"The sum of {number} and {number1} is {number+number1} ")
except Exception as e:
  e = "Please enter a Valid Number"
  print(e)
# We use Exception To protect our program from errors
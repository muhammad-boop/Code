# TRY WITH ELSE CLAUSE
try:
  a = int(input("Enter a Number: "))
  print(a)
except Exception as e:
  e = "Please enter a Valid Number"
  print(e)
else: # If try block run successfully then the code goes in else block...
  print("The code Run Successfully Congragulations")
# CHAPTER 6 – CONDITIONAL EXPRESSION
age = int(input("Enter Your age: "))
if(age>18):
  print("You are above the age of concent")
elif(age<0):
  print("You are entering a negative age")
elif(age==0):
  print("You are entering 0 and its not a valid age")
elif(age<10):
  print("You are a kid")
else:
  print("You are below the age of concent")
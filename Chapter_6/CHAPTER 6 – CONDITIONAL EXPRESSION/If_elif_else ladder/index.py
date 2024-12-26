# if_elif_else Ladder
age = int(input("Enter your age: "))
if(age>=18):
  print("You are eligible to vote") 
elif(age<0):
  print("You are entering a negative age: ")
elif(age==0):
  print("You are entering 0 ")
elif(age<10):
  print("You are a kid")
else:
  print("You are not eligible to vote")

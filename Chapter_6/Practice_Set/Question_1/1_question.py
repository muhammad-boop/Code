# Write a program to find the greatest of four numbers entered by the user.
n1 = int(input("Enter the first number1: "))
n2 = int(input("Enter the second number2: "))
n3 = int(input("Enter the second number3: "))
n4 = int(input("Enter the second number4: "))
if(n1>n2 and n1>n3 and n1>n4):
  print(f"{n1} is greater than {n2}, {n3} and {n4}")
elif(n2>n1 and n2>n3 and n2>n4):
  print(f"{n2} is greater than {n1}, {n3} and {n4}")
elif(n3>n1 and n3>n2 and n3>n4):
  print(f"{n3} is greater than {n1}, {n2} and {n4}")
elif(n4>n1 and n4>n2 and n4>n3):
  print(f"{n4} is greater than {n1}, {n2} and {n3}")
else:
  print("You enterted a wrong number")
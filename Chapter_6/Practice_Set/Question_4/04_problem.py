# ! Write a program to find whether a given username contains less than 10
# characters or not.

username = input("Enter your username: ")
if(len(username)<10):
  print("Username has less than 10 characters")
else:
  print("Username has more than 10 characters")
print("End of program")
# Quick Quiz: Write a program to print yes when the age entered by the user is greater
# than or equal to 18.
age = int(input("Enter your age: "))
if(age>=18):
  print("Yes")
else:
  print("No")
# ! IMPORTANT NOTES:
# There can be any number of elif statements.
#  Last else is executed only if all the conditions inside elifs fail.
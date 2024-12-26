"""
write a Program using Exceptiosn Handling to get the following result

"""
try:
 age = int(input("Enter a number: "))
 if((n:=age)>18):
  print("You are eligiable to vote ")
 else:
  print("Not Eligiable to vote")
except ValueError:
 print("Enter a Valid age Please")
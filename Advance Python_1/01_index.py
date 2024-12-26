# CHAPTER 12 – ADVANCED PYTHON 1
# ! WALRUS OPERATOR
if(n:=len([1,2,3,56,612]))>2: #The Walrus Operator (:=) in Python, introduced in Python 3.8, allows you to assign a value to a variable as part of an expression. This is also known as the assignment expression.
# The main benefit of the walrus operator is that it simplifies code by combining assignment and expression evaluation into a single step.
  print(f"There are {n} elements")
else:
  print("List is too short")
# ! Example of Walrus Operator
while(number:=int(input("Enter a number"))!=0):
  print(f"You endered {number}")
  break
# ! Example of Walrus Operator
list = [1,2,3,4,5]
if(n:=len(list))>2:
  print(f"List contain {n} elements")
else:
  print("List is too short")
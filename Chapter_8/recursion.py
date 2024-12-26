# RECURSION
def factorial(n):
  if(n==1 or n==0):
    return 1
  else:
    return n*factorial(n-1)
n  = int(input("Enter a number: "))
print(f"The factorial of given number is {factorial(n)}")
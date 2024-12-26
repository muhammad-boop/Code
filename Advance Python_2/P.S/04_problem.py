# Write a program to filter a list of numbers which are divisible by 5
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def divide(n):
  if(n%5==0):
    print("This number is divide by 5")
  else:
    print("This number is not divide by 5")
final = filter(divide, l)
print(list(final))
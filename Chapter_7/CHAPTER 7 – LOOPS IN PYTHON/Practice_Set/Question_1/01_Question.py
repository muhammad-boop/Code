#  Write a program to print multiplication table of a given number using for loop.
#  Example : Input : 2 Output : 2 4 6 8 10 12 14 16 18 20
number = int(input("Enter a number: "))
for i in range(1,11):
  print(f"{number}X{i} is {number*i}")

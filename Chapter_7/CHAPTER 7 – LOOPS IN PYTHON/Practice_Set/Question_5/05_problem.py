# Write a program to find the sum of first n natural numbers using while loop.
number = int(input("Enter a number: "))
i = 1
sum = 0
while(i<=number):
  sum+=i
  i+=1
print(sum)
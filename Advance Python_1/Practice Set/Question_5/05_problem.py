"""
Store the multiplication tables generated in problem 3 in a file named Tables.txt.
"""
n = int(input("Enter a number: "))
table = [n*i for i in range(1,11)]
print(table)


file = open("Tables.txt", "a")
file.write(str(table) + "\n")
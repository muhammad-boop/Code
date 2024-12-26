'''
Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
present, a message without exiting the program must be printed prompting the same.

'''
try:
  f1 = open("1.txt")
  print(f1.read())
  f1.close()

  f2 = open("2.txt")
  print(f2.read())
  f2.close()

  f3 = open("3.txt")
  print(f3.read())
  f3.close()
except Exception as e:
  print(e)
print("Thanks for using our service")
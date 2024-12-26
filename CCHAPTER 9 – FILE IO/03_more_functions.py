# ! ReadLines()
# f = open("file.txt")

# lines = f.readlines() # If we want to read all the lines then we use readlines()
# print(lines,type(lines))
# f.close()
# ReadLine()
f = open("file.txt")

# line1 = f.readline() # if we want to read a single line then we use readline()
# print(line1,type(line1))
# line2 = f.readline() # if we want to read a single line then we use readline()
# print(line2,type(line2))
# line3 = f.readline() # if we want to read a single line then we use readline()
# print(line3,type(line3))
# line4 = f.readline() # if we want to read a single line then we use readline()
# print(line4,type(line4))

line = f.readline()
while(line!=""):
  print(line)
  line = f.readline()
# How to write in a file
st = "Muhammad is a very good boy"
st2 = "He is a good student"
f = open("myFile.txt", "w")
f.write(st)
f.write("\n"+st2)
f.close()
print("Done!")
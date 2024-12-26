# ! append Mode
st = "Good morning"
f = open("myFile.txt", "a") # we use append methood to write in a file at the end of lines
f.write("\n" + st)
f.close()
print('Done')
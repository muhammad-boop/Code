# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
text1 = input("Enter your text: ")
if(text1=="Make a lot of money"):
  print("This is a spam comment")
elif(text1=="buy now"):
  print("This is a spam comment")
elif(text1=="subscribe this"):
  print("This is a spam comment")
elif(text1=="click this"):
  print("This is a spam comment")
else:
  print("This is not a spam comment")
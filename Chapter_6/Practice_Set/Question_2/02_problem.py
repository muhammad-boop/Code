# ! Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
marks = int(input("Enter marks: "))
if(marks>40):
  print("Passed")
elif(marks==33):
  print("Remedial")
else:
  print("Failed")
# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
name = ["Harry", "Soham", "Sachin", "Rahul"]

for i in name:
  if(i.startswith("S")):
    print(f"Good afternoon {i}")
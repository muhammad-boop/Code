# Label the program written in problem 4 with comments. 
# ! Importing the OS Modules
import os

# ! Specifcing the path 

directory_path = '/'

# ! Listing the entries
entries = os.listdir(directory_path)
# ! Printing the entries
for entry in entries:
    print(entry)


import os

# Specify the directory path
directory_path = '/'

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print the entries
for entry in entries:
    print(entry)

# ! DICTIONARY METHODS
students = {
  "Muhammad" : 77,
  "Touheed" : 66,
  "Sufyan" : 90,
  "Ali" : 100
}
# ! Items
print(students.items()) # items() method is used to get a dictionary's (key, value) tuple pairs.
# ! Keys
print(students.keys()) # keys() method is used to get a dictionary's keys.
# ! Values
print(students.values()) # value () is used to get a dictionary's values.
# ! Update
students.update({"Muhammad":98})
print(students)
print(students.get("Muhammad8")) # Prints None
print(students["Muhammad8"]) # Returns an error

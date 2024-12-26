# STRING FUNCTIONS
a = "hello"
print(len(a)) #!  len() is used to find the length of a string
print(a.endswith("llo")) #! endswith() is used to check if a string ends with a certain character and returns a boolean value
print(a.startswith("he")) #! startswith() is used to check if a string starts with a certain character and returns a boolean value
print(a.capitalize())
print(a.upper())
print(a.count('l')) # ! – counts the total number of occurrences of any character.
name = "Muhammad Raza"
print(name.find("Raza")) # ! find() is used to find the index of a character in a string
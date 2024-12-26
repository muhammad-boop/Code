# ! Type Defination
n: int = 8 # The data type of n is an integer
print(n) 
name:str = "Muhammad" # The data type of name is a string
print(name)

# ! Using in Functions
def sum(a:int,b:int)->int:
  return a+b
add = sum(1,2)
print(add)
def student(name:str,grade:str)->str:
  return f"{name} is in {grade} grade"
student1 = student("Muhammad","A+")
print(student1)
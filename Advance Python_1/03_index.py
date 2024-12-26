# ADVANCED TYPE HINTS
from typing import List,Tuple,Dict,Union

# ! List

list1:List[int] = [1,2,455,77,121,122]
print(list1)
name:List[str] = ["Muhammad","Raza","Khan","Baloch"]
print(name)
roll_numbers:List[int] = [90,66,87,33]
print(roll_numbers)
# ! Dict
student1:Dict[str,int] = {
  "Muhammad" : 12,
  "age":18
}
print(student1)
programer:Dict[str,str] = {"Name":"Muhammad","Class":"12th"}
print(programer)
# ! Tuple
data:Tuple[int,str] = (1,"Muhammad")
print(data)

# ! Uninion
data:Union[int,str] = "Muhammad"
print(data)
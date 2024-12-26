# Encapsulation in Python 
class Student:
  def __init__(self):
    self.name = ""
    self.age = ""
  def getName(self):
    return self.name
  def getAge(self):
    return self.age
  def setAge(self,age):
    self.age = age
  def setName(self,name):
    self.name = name
obj = Student()
obj.setName("Jhon")
obj.setAge(77)
age = obj.getAge()
name = obj.getName()
print(name)
print(age)
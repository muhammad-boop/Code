# ! _init_constructor
class Employee:
  language = "Python"
  company = "Google"
  def __init__(self,name,salary,language):
    self.name = name
    self.salary = salary
    self.language = language

    
Employe1 = Employee("Muhammad",1300000,"Java")
print(Employe1.name)
print(Employe1.salary)
print(Employe1.language)
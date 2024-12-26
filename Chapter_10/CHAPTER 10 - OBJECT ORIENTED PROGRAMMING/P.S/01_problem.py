# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class Programmer:
  company = "Microsoft"
  def __init__(self,name,salary,language):
    self.name = name
    self.salary = salary
    self.language = language
programer1 = Programmer("Muhammad",13000,"Python")
print(programer1.name,programer1.salary,programer1.language)
programer2 = Programmer("Ali",880000,"Java")
print(programer2.name,programer2.salary,programer2.language)
programer3 = Programmer("Hassan",13000,"C++")
print(programer3.name,programer3.salary,programer3.language)
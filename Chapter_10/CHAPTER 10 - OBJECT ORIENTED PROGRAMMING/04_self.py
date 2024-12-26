# ! Self 
class Employee:
  company = "Google"
  language = "Python"
  def Info(self):
    print(f"The language is {self.language} and company is {self.company}")
client1 = Employee()
client1.Info()
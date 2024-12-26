# # ! Multipel Inheritance
class student1:
  def st1(self):
    print("This is Student 1")
class student2:
  def st2(self):
    print("This is Student 2")
class student3(student1,student2):
  def st3(self):
    print("This is Student 3")
obj = student3()
obj.st1()
obj.st2()
obj.st3()
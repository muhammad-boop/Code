# Inheritance in Python
class A:
  def showValue(self):
    print("This is class A")
class B(A): # ! This is a single level Inheritance B(A)
  def showValue2(self):
    print("This is class B")
obj = B()
obj.showValue()
obj.showValue2()

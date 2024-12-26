# ! MultiLevel Inheritance
class A:
  def displayA(self):
    print("This is class A")
class B(A):
  def displayB(self):
    print("This is class B")
class C(B):
  def displayC(self):
    print("This is class C")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
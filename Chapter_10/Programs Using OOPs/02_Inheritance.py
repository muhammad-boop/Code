# ! Inheritance
class A:
  def sum(self):
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    c = a+b
    print(f"The Sum of {a} and {b} is {c}")
class B:
  def multiply(self):
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    c = a*b
    print(f"The Multiply of {a} and {b} is {c}")
class C(A,B):
  def divide(self):
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    c = a/b
    print(f"The Divide of {a} and {b} is {c}")
obj = C()
obj.sum()
obj.multiply()
obj.divide()
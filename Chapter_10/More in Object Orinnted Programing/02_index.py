class Demo():
  a = 10 
  def showValue(self):
    print(self.a)
  def square(self,n):
    result = n*n
    print(f"The square of {n} is {result}")
  # ! Cinstructor
  def __init__(self):
    print("This is constructor") # Constructor is called when object is created
obj = Demo()
obj.showValue()
obj.square(int(input("Enter a number: ")))
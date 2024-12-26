class circle:
  def raduis(self,raduis):
    self.raduis = raduis
  def area(self):
    area = 3.14 * self.raduis * self.raduis
    print(f"The area of circle is {area}")
obj = circle()
obj.raduis(int(input("Enter raduis: ")))
obj.area()

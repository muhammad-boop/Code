'''
Create a class Car with attributes make, model, and year.
Define a method display_info() to print these details.
'''
class car:
  def display_info(self,make,model,year):
    self.make  = make
    self.model = model
    self.year  = year
    print(self.make)
    print(self.model)
    print(self.year)
obj=car()
obj.display_info("BMW",2006,2006)
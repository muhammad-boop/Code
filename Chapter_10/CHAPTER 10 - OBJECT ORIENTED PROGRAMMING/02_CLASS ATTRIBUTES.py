# CLASS ATTRIBUTES
class Employee:
  compnay = "Google" # This is a class atribuite
  language = "Python"
client1 = Employee()
client1.name = input("Enter your name: ") # This is a instance  atribuite
print(client1.name,client1.compnay,client1.language)
client2 = Employee()
client2.name = input("Enter your name: ")
print(client2.name,client2.compnay,client2.language)
'''
Here company and salary are class attributes.name is object atribute as they directly belong to class
'''
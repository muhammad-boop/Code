# Instance Atributes vs Class Atributes
class employee:
  company = "Google"
  language = "Python"
client1 = employee()
client1.name = input("Enter your name: ")
client1.language = "JavaScript"
print(client1.name,client1.language)
client1.info()
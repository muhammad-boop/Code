# STATIC METHOD
class students:
  grade = "2nd Year I.C.S Physcis Math"
  college = "GCMT"
  @staticmethod
  def greet():
    print("Good Morning")
student1 = students()
student1.greet()
student1.name = input("Enter your name: ")
print(student1.name,student1.grade,student1.college)
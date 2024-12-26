def myFunc():
  try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    print(f"The division of {a} and {b} is {a/b} ")
    return
  except Exception as e:
    e = "Please enter a Valid Number"
    print(e)
    return
  finally:
    print("Thanks!")
if(__name__ == "__main__"):
   # This line is used to check if the program is being run as the main program or being imported as a module into another program
   print("We are running The code directly..")
   myFunc()
   print(__name__)
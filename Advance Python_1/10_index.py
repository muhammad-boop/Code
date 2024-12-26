# ! Using Finally in Functions
def main():
  try:
    number1 = int(input("Enter Your Number: "))
    number2 = int(input("Enter another Number: "))
    print(f"The sum of {number1} and {number2} is {number1+number2}")
    return
  except Exception as e:
    e = "Please enter a Valid Number"
    print(e)
    return
  finally:
    print("Thanks!")
main()
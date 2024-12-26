# ! Finally
def main():
  try:
    number = int(input("Enter a number: "))
    print(f"Your entered number is {number}")
    return
  except Exception as e:
    e = "Please enter a Valid Number"
    print(e)
    return
  finally: # Finally is used to execute a block of code, regardless of whether the try block raises an exception or not
    print("Thanks!")
main()
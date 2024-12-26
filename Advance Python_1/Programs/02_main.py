# ! Program using match case
def rollNum(rollNum):
  match rollNum:
    case 1:
      return ("Free")
    case 2:
      return ("OK")
    case 3:
      return("Great")
    case 4:
     return ("Not present")
print(rollNum(4))

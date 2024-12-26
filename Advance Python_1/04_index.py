def status(status):
  match status:
    case 200:
      return("Success")
    case 404:
      return("Not Found")
    case 500:
      return("OK")
    case _:
      return("Unknown")
print(status(200))
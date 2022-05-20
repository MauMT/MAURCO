def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def checkintOrFloat(num):
  if(isint(num)):
      return "int"
  elif (isfloat(num)):
      return "float"
  else:
      return "unknown"

def isConstant(num):
  if checkintOrFloat(num) != "unknown":
    return True
  return False

# print(checkintOrFloat("2.3"))
# print(isConstant("5"))
# print(isConstant("b"))
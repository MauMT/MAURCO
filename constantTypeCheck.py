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

print(checkintOrFloat("2.3"))
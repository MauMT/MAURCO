'''
    MÓDULO ENCARGADO DE RECONOCER EL TIPO DE LAS CONSTANTES
'''

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


# Función para revisar si algo es casteable a string
def is_string(s):
    try:
        s + ""
        return True
    except TypeError:
        return False

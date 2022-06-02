# Inicio de direcciones para variables globales
Gi = 5000
Gf = 8000

# Inicio de direcciones para variables locales
Li = 11000
Lf = 13000

# Inicio de direcciones para variables temporales globales
Tgi = 15000
Tgf = 17000

# Inicio de direcciones para constantes
Ci = 23000
Cf = 24000 #hasta 25,000

def restarDireccionBase(direccion, tipoDireccion):
  tipoDireccion = tipoDireccion.lower()
  if tipoDireccion == "gi":
    return direccion-5000
  elif tipoDireccion == "gf":
    return direccion-8000
  elif tipoDireccion == "li":
    return direccion-11000
  elif tipoDireccion == "lf":
    return direccion-13000
  elif tipoDireccion == "tgi":
    return direccion-15000
  elif tipoDireccion == "tgf":
    return direccion-17000
  elif tipoDireccion == "ci":
    return direccion-23000
  elif tipoDireccion == "cf":
    return direccion-24000
  else:
    return None

### FUNCIONES PARA OBTENER EL CONTADOR ACTUAL DE CADA TIPO DE DIRECCIÓN
# getAddress de cualquier tipo mueve el contador a una dirección después de la última asignada
# Num variables de cierto tipo = contador - dirección inicial
# si contador = 5001, dirección inicial = 5000, entonces num variables = 5001 - 5000 = 1 
def getCurrentGlobalAddressInt():
  return Gi

def getCurrentGlobalAddressFloat():
  return Gf

def getCurrentLocalAddressInt():
  return Li

def getCurrentLocalAddressFloat():
  return Lf

def getCurrentTempAddresInt():
  return Tgi

def getCurrentTempAddresFloat():
  return Tgf

def getCurrentConstantAddressInt():
  return Ci

def getCurrentConstantAddressFloat():
  return Cf

#---------------------------------------------------------------------------------

### FUNCIONES PARA OBTENER UNA DIRECCIÓN DEPENDIENDO EL TIPO Y SCOPE
def getGlobalAddressInt(size=1):
  global Gi
  aux = Gi
  Gi = Gi+size
  return aux

def getGlobalAddressFloat(size=1):
  global Gf
  aux = Gf
  Gf = Gf+size
  return aux

def setGlobalAddressInt(x):
  global Gi
  Gi = x

def setGlobalAddressFloat(x):
  global Gf
  Gf = x
  
### Están asociadas a una función
def getLocalAddressInt(size=1):
  global Li
  aux = Li
  Li = Li+size
  return aux

def getLocalAddressFloat(size=1):
  global Lf
  aux = Lf
  Lf = Lf+size
  return aux
##################################

# TEMPORALES GLOBALES
def getGlobalTempAddressInt():
  global Tgi
  aux = Tgi
  Tgi = Tgi+1
  return aux

def getGlobalTempAddressFloat():
  global Tgf
  aux = Tgf
  Tgf = Tgf+1
  return aux


def getConstantAddressInt():
  global Ci
  aux = Ci
  Ci = Ci+1
  return aux

def getConstantAddressFloat():
  global Cf
  aux = Cf
  Cf = Cf+1
  return aux


### FUNCIONES PARA REINICIAR LOS COUNTERS DE LAS VARIABLES LOCALES Y LAS VARIABLES TEMPORALES
def reiniciarCountersLocales():
  global Li
  global Lf
  global Tli
  global Tlf
  Li = 11000
  Lf = 13000
  Tli = 19000
  Tlf = 21000

def reiniciarTemporalesLocales():
  global Tli
  global Tlf
  Tli = 19000
  Tlf = 21000
#---------------------------------------------------------------------------------


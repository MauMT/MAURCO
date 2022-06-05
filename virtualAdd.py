
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

Tp = 69000

GLOBAL_INT_START = 5000
GLOBAL_FLOAT_START = 8000

LOCAL_INT_START = 11000
LOCAL_FLOAT_START = 13000

TEMPORAL_INT_START = 15000
TEMPORAL_FLOAT_START = 17000

CONSTANT_INT_START = 23000
CONSTANT_FLOAT_START = 24000

TEMPORAL_POINTER_START = 69000

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

def getCurrentTempAddressInt():
  return Tgi

def getCurrentTempAddressFloat():
  return Tgf

def getCurrentConstantAddressInt():
  return Ci

def getCurrentConstantAddressFloat():
  return Cf

def getCurrentTempPointer():
  return Tp

#---------------------------------------------------------------------------------

### FUNCIONES PARA OBTENER UNA DIRECCIÓN DEPENDIENDO EL TIPO Y SCOPE
def getTempPointerAddress():
  global Tp
  aux = Tp
  Tp = Tp+1
  return aux

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
  global Tp
  Li = 11000
  Lf = 13000
  Tli = 19000
  Tlf = 21000
  Tp = 69000

def reiniciarTemporalesLocales():
  global Tli
  global Tlf
  global Tp
  Tli = 19000
  Tlf = 21000
  Tp = 69000
#---------------------------------------------------------------------------------


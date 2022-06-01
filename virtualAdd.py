
# Inicio de direcciones para variables globales
Gi = 5000
Gf = 8000

# Inicio de direcciones para variables locales
Li = 11000
Lf = 13000

# Inicio de direcciones para variables temporales globales
Tgi = 15000
Tgf = 17000

# Inicio de direcciones para variables temporales locales
Tli = 19000
Tlf = 21000


# Inicio de direcciones para constantes
Ci = 23000
Cf = 24000


def getGlobalAddressInt():
  global Gi
  aux = Gi
  Gi = Gi+1
  return aux

def getGlobalAddressFloat():
  global Gf
  aux = Gf
  Gf = Gf+1
  return aux

def setGlobalAddressInt(x):
  global Gi
  Gi = x

def setGlobalAddressFloat(x):
  global Gf
  Gf = x
  
### deben ir asociadas a una función o algo así
def getLocalAddressInt():
  global Li
  aux = Li
  Li = Li+1
  return aux

def getLocalAddressFloat():
  global Lf
  aux = Lf
  Lf = Lf+1
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


# TEMPORALES LOCALES
def getLocalTempAddressInt():
  global Tli
  aux = Tli
  Tli = Tli+1
  return aux

def getLocalTempAddressFloat():
  global Tlf
  aux = Tlf
  Tlf = Tlf+1
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



def reiniciarCountersLocales():
  global Li
  global Lf
  global Tli
  global Tlf
  Li = 11000
  Lf = 13000
  Tli = 19000
  Tlf = 21000
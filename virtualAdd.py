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
Cf = 24000

def getCurrentGlobalAddressInt():
  return Gi

def getCurrentGlobalAddressFloat():
  return Gf

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
  
### deben ir asociadas a una función o algo así
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


""" x = getLocalAddressInt()
print("1", x)
y = getLocalAddressInt(size=12)
print("2", y)
z = getLocalAddressInt()
print("3", z)
 """
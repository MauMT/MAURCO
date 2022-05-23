import dirVar
# Inicio de direcciones para variables globales
Gi = 5000
Gf = 8000

# Inicio de direcciones para variables locales
Li = 11000
Lf = 13000

# Inicio de direcciones para variables temporales
# 
Ti = 15000
Tf = 17000

# Inicio de direcciones para constantes
Ci = 20000
Cf = 21000

def intOrFloatAddress(tipo):
  if tipo == "int":
    return getGlobalAddInt()
  elif tipo == "float":
    return getGlobalAddFloat()
  return None

def intOrFloatConstant(tipo):
  if tipo == "int":
    return getConstantAddInt()
  elif tipo == "float":
    return getConstantAddFloat()
  return None

def getGlobalAddInt():
  global Gi
  aux = Gi
  Gi = Gi+1
  return aux

def getGlobalAddFloat():
  global Gf
  aux = Gf
  Gf = Gf+1
  return aux

  
### deben ir asociadas a una función o algo así
def getLocalAddFloat():
  global Lf
  aux = Lf
  Lf = Lf+1
  return aux
  
def getLocalAddInt():
  global Li
  aux = Li
  Li = Li+1
  return aux
##################################

def getConstantAddInt():
  global Ci
  aux = Ci
  Ci = Ci+1
  return aux

def getConstantAddFloat():
  global Cf
  aux = Cf
  Cf = Cf+1
  return aux


def buscarDireccionVirtual(nombreVariable):
  if nombreVariable in dirVar.dirglobalVar:
    return dirVar.dirglobalVar[nombreVariable].direccion


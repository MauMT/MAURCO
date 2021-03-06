'''
    MÓDULO DE CUÁDRUPLOS
    Es el encargado de generar los cuádruplos dependiendo del tipo de estatuto que el parser obtiene,
    además contiene la lista actual de cuádruplos y una función para imprimirlos en consola.
    - Hace uso del directorio de constantes en el módulo 'dirVar' para reausar las direcciones de memoria cuando
    algún operando es una constante.
    - Hace uso del módulo 'virtualAdd' para asignar direcciones de memoria a los reusltados de las expresiones.
    - Hace uso del diccionario 'semantic' para validar la semántica de las expresiones que s enecuentra en el módulo 'semanticCube'.
'''

import dirVar
import virtualAdd
from semanticCube import semantic
import queue
#pOperandos
pOperandos = []

#POPER
pOperadores = []


pTipos = []
psaltos = []




cuads=[("goto","1","","")]

tempcounter = 0

'''
Funciones de control de la pila de tipos, pila de operadores y pila de operandos
'''

def agregarID(id):
  pOperandos.append(id)

def agregarConst(const):
  pOperandos.append(const)

def agregarTipo(tipo):
  pTipos.append(tipo)

def agregarOperador(operador):
  if operador != None:
    pOperadores.append(operador)



def validar():
    '''
    Función validar(), es usada por todas las expresiones aritméticas, 
    de comparación y de operadores lógicos para la generación de cuádruplos.
    '''    
    global tempcounter
    #right operando
    #left operando
    right = pOperandos.pop()
    left = pOperandos.pop()
    

    #right type
    #left type
    rightType = pTipos.pop()
    #print("ltype", rightType)

    leftType = pTipos.pop()
    #print("rtype", leftType)
    
    #operador
    oper = pOperadores.pop()
    #print(oper)

    #result type, checa la semántica usando el cubo semántico
    result_type = semantic[leftType][oper][rightType]
    #print(result_type)

    agregarTipo(result_type)

    #agregar un valor a temp counter
    #generar cuadruplo

    if result_type == "int":
      result_addr = virtualAdd.getGlobalTempAddressInt()
    elif result_type == "float":
      result_addr = virtualAdd.getGlobalTempAddressFloat()
    else:
      pass
      #print("errorvalidar")
    


    cuads.append((oper, left, right, result_addr))
    

    #agregar resultado en pOperandos
    agregarID(result_addr)
    
    dirVar.agregarglobalVariable(result_addr, [] ,result_type)
    



def cuadssumsub():
  
  if not pOperadores:
    pass
    #print("empty")
  else:
    if(( pOperadores[-1] == "+") or ( pOperadores[-1] == "-")):
      validar()
    else:
      #print(pOperandos)
      pass
      #print("no-summin")

def cuadsmuldiv():
  if not pOperadores:
    #print("empty")
    pass
  else:
    if(( pOperadores[-1] == "*") or ( pOperadores[-1] == "/")):
      validar()
    else:
      #print("no-multdiv")
      pass

def cuadscomparation():
  if not pOperadores:
    #print("empty")
    pass
  else:
    if(( pOperadores[-1] == "<") or ( pOperadores[-1] == "==") 
      or (pOperadores[-1] == ">") or (pOperadores[-1] == "!=")):
      
      validar()
    else:
      #print(pOperandos)
      #print("no-compar")
      pass

def cuadsand():
  if not pOperadores:
    #print("empty")
    pass
  else:
    if(( pOperadores[-1] == "&")):
      #print("yes")
      validar()
    else:
      #print("no-and")
      pass

def cuadsor():
  if not pOperadores:
    #print("empty")
    pass
  else:
    if(( pOperadores[-1] == "|")):
      #print("yes")
      validar()
    else:
      #print("no-or")
      pass


def auxAsignacion(): 
    '''
    Función auxiliar para la generación de cuádruplos de asignación.
    Es similar a validar()
    '''
    right = ''

    left = pOperandos.pop()
    leftType = pTipos.pop()
    

    result = pOperandos.pop()
    resultType = pTipos.pop()
    
    
  
    #operador
    oper = pOperadores.pop()

    result_type = semantic[resultType][oper][leftType]

    if result_type == "error":
      print("Type Error: No se puede asignar un tipo '{}' a un tipo '{}'".format(leftType, resultType))
      raise Exception("No se puede asignar un tipo '{}' a un tipo '{}'".format(leftType, resultType))
    
    cuads.append((oper, left, right, result))



'''----------------------------------------------'''

def cuadsasignacion():
  if not pOperadores:
    pass
  else:
    if(( pOperadores[-1] == "=")):
      
      global tempcounter
      
      auxAsignacion()
    


######################################################
#CONDICIONES Y CICLOS
######################################################
#pOperandos
#pOperandos = []

#POPER
#pOperadores = []



#1
#la ultima direccion de memoria validando el tipo de expresion
#if lasttemp != int ERROR
#generar cuadruplo falso sin saber el resultado
def condicion1():
  
  result = pOperandos.pop()
  pTipos.pop()
  cuads.append(("GOTOF", result, " ", "fill"))
  #print(len(cuads))
  psaltos.append(len(cuads)-1)
  
    
    
#2
#rellenar end
#end = psaltos.pop
#fill(end, cont)
def condicion2():
  end = psaltos.pop()
  fill(end, len(cuads))


#3
#generar quad GOTO_
#false = psaltos.pop()
#psaltos.push(cont-1)
#fill(falso, cont)
def condicion3():
  cuads.append(("GOTO", " ", " ", "fill"))
  false = psaltos.pop()
  psaltos.append(len(cuads)-1)
  fill(false, len(cuads))



def fill(x, y):
  auxfill = (cuads[x])
  v = list(auxfill)
  v[3] = str(y)
  cuads[x] = tuple(v)



def ciclowhile1():
  psaltos.append(len(cuads))

def ciclowhile2():
  checktype = pTipos.pop()
  
  #implementar la tabla de variables y funciones
  #if checktype != bool:
  #  print("TYPE MISMATCH")
  #else:
  result = pOperandos.pop()
  cuads.append(("GOTOF", result, " ", "fill"))
  psaltos.append(len(cuads)-1)


def ciclowhile3():
  end = psaltos.pop()
  returns = psaltos.pop()
  cuads.append(("GOTO", " ", " ", returns))
  fill(end, len(cuads))



def ciclofrom1(x):
 
  agregarID(x)
  agregarTipo("int")


def ciclofrom2():
  checktype = pTipos.pop()
  
  
  result = pOperandos.pop()
  
  #VControl = pOperandos[-1]
    #LLAMADA A CUBO SEMANTICO
    #if Tipo Res ERROR
    # SEMANTICA
  cuads.append(("=", result, " ", "VControl"))

def ciclofrom3():
  
  checktype = pTipos.pop()
  #implementar la tabla de variables y funciones
  #if checktype != bool:
    #print("TYPE MISMATCH")
  #else:
  result = pOperandos.pop()
  #VFinal = result
  cuads.append(("=", result, " ", "VFinal"))
  cuads.append(("<", "VControl", "VFinal", "Tx"))
  psaltos.append(len(cuads)-1)
  cuads.append(("GOTOF", "Tx", " ", "fill"))
  psaltos.append(len(cuads)-1)


def ciclofrom4():
  
  global tempcounter
  result = "t" + str(tempcounter)
  tempcounter = tempcounter +1
  cuads.append(("+", "VControl", 1, result))
  cuads.append(("=", result, " ", "VControl"))

  cuads.append(("=", result, " ",pOperandos.pop()))
  pTipos.pop()
  FIN = psaltos.pop()
  RET = psaltos.pop()
  cuads.append(("GOTO", " ", " ", RET))
  fill(FIN, len(cuads))

  #pTipos.pop()



######################################################
#CUADS FUNCIONES
######################################################

def fincuads():
  cuads.append(("END", " ", " ", " "))

def lectInp():
  cuads.append(("INPUT", " ", " ", pOperandos.pop()))
  pTipos.pop()

def escPri():
  cuads.append(("PRINT", " ", " ",  pOperandos.pop()))
  pTipos.pop()



######################################################

def endfunc():
  cuads.append(("ENDFUNC", " ", " ", " "))


def createERA(nombre):
  cuads.append(("ERA", nombre, " ", " "))
  global conttipos
  conttipos = 0
  

def valparams(params):
  
  global conttipos
  if(params):
    if pTipos[-1] == params[conttipos]:
      conttipos += 1
      
      #print(pOperandos[-1])
      vfin = (conttipos)
      #print(vfin)
      cuads.append(("PARAM", pOperandos.pop() ," ", vfin))
      pTipos.pop()
      
    else:
      pass
      #print("errorparam")
  else:
    pass
    #print("There are no params")

def valnull(params):
  #global conttipos
  if(len(params) == conttipos):
    return True
  else:
    return False

def createGOSUB(nombre):
  cuads.append(("GOSUB", nombre, " ", " "))


def valMain():
  cumain = (("GOTO", " ", " ", len(cuads)))
  cuads[0] = cumain


def cReturn():
  valret = pOperandos[-1]
  cuads.append(("RETURN", " ", " ", valret))
  

def asignval(callfunc, tipo):

  if tipo == "int":
    result_addr = virtualAdd.getGlobalTempAddressInt()
  elif tipo == "float":
    result_addr = virtualAdd.getGlobalTempAddressFloat()
  else:
    #print("errorASSIGN")
    pass
  agregarID(result_addr)
  agregarTipo(tipo)
  cuads.append(("=", callfunc, " ", result_addr))


def getConstantAddressbyValue(currVal, currTipo):
  if currVal in dirVar.dirConstantes:
    auxDir = dirVar.dirConstantes[currVal]
  else:
    if currTipo == "int":
      auxDir = virtualAdd.getConstantAddressInt()
    elif currTipo == "float":
      auxDir = virtualAdd.getConstantAddressFloat()
    dirVar.dirConstantes[currVal] = auxDir
  return auxDir


######################################################
#ARREGLOS
######################################################
def arrVerifica(val, rango):
  
  cero = getConstantAddressbyValue(0, "int")
  limite = getConstantAddressbyValue(rango-1, "int")
  cuads.append(("VER", val, cero, limite))


def arrMult(s1, m1):
  result = virtualAdd.getGlobalTempAddressInt()
  dir_m1 = getConstantAddressbyValue(m1, "int")
  cuads.append(("*", s1, dir_m1, result))
  agregarID(result)
  agregarTipo("int")

def arrSumaMult(s2):
  result = virtualAdd.getGlobalTempAddressInt()
  val = pOperandos.pop()
  pTipos.pop()
  cuads.append(("+", s2, val, result))
  agregarID(result)
  agregarTipo("int")



def sumaDirBase(direccion):
  dir_base = getConstantAddressbyValue(direccion, "int")
  result = virtualAdd.getTempPointerAddress()
  cuads.append(("+", dir_base, pOperandos.pop(), result))
  pTipos.pop()
  agregarID(result)
  agregarTipo("int")

def sumaDirBasearr(temp, direccion):
  result = virtualAdd.getTempPointerAddress()
  dir_base = getConstantAddressbyValue(direccion, "int")
  cuads.append(("+", dir_base, temp, result))
  agregarID(result)
  agregarTipo("int")

######################################################
# GENERACIÓN DE TABLA CON CUADS FORMATEADA
######################################################
def getCurrCounter():
  return len(cuads)


#add counter to each element in cuads
def addCounter():
  cuadCounter = 0
  for el1, el2, el3, el4 in cuads:
      cuads[cuadCounter] = (cuadCounter, el1, el2, el3, el4)
      cuadCounter+=1

# prints cuads as a formatted table
def printCuads():
  print ("\n\n\n")
  print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format("cuad","op","v1","v2","vf"))
  print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format("----","--","---","---","---"))
  for cuadCounter, el1, el2, el3, el4 in cuads:
      print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format(cuadCounter,el1,el2,el3,el4))


def escChar(char):
  #remove first and last char from char string
  char = char[1:-1]
  cuads.append(("PRINT", " ", " ", char))

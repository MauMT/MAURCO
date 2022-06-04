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

####### NUMERAR LÍNEAS E IMPRIMIR EN TABLA BONITA

#funcion de array cuadruplos
cuads=[("goto","1","","")]

tempcounter = 0

#funcion de agregar ID 
#validaciones de ID con tipo

## ESTO ES MÁS UN AGREGAR TEMPORAL
def agregarID(id):
  #if nomFuncion in dirFunciones:
  #validacion de tipo y si esta en varstable
  #if id not in dirVar.dirglobalVar:
    pOperandos.append(id)
  #else:
  #  raise NameError('Variable no declarada')
  #  print("variable no declarada")

def agregarConst(const):
  pOperandos.append(const)

def agregarTipo(tipo):
  pTipos.append(tipo)

def agregarOperador(operador):
  if operador != None:
    pOperadores.append(operador)


def validar():
    print("validar")
    global tempcounter
    #right operando
    #left operando
    right = pOperandos.pop()
    print(right)

    left = pOperandos.pop()
    print(left)

    #right type
    #left type
    rightType = pTipos.pop()
    print("ltype", rightType)

    leftType = pTipos.pop()
    print("rtype", leftType)
    
    #operador
    oper = pOperadores.pop()
    print(oper)

    #result type checar semantica con cubo
    result_type = semantic[leftType][oper][rightType]
    print(result_type)

    agregarTipo(result_type)

    #agregar un valor a temp counter
    #generar cuadruplo

    if result_type == "int":
      result_addr = virtualAdd.getGlobalTempAddressInt()
    elif result_type == "float":
      result_addr = virtualAdd.getGlobalTempAddressFloat()
    else:
      print("errorvalidar")
    


    cuads.append((oper, left, right, result_addr))
    print(cuads)

    #agregar resultado en pOperandos
    agregarID(result_addr)
    print("agreegarid")
    dirVar.agregarglobalVariable(result_addr, [] ,result_type)
    
    #agregar resultadotipo en pTipospo



def cuadssumsub():
  print("entrasumsub")
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "+") or ( pOperadores[-1] == "-")):
      print("op1sumsub")
      validar()
    else:
      #print(pOperandos)
      print("no-summin")

def cuadsmuldiv():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "*") or ( pOperadores[-1] == "/")):
      print("yes")
      validar()
    else:
      #print(pOperandos)
      print("no-multdiv")

def cuadscomparation():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "<") or ( pOperadores[-1] == "==") 
      or (pOperadores[-1] == ">") or (pOperadores[-1] == "!=")):
      print("yes")
      validar()
    else:
      #print(pOperandos)
      print("no-compar")

def cuadsand():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "&")):
      print("yes")
      validar()
    else:
      #print(pOperandos)
      print("no-and")

def cuadsor():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "|")):
      print("yes")
      validar()
    else:
      #print(pOperandos)
      print("no-or")



'''
REVISAR ESTO
'''
def auxAsignacion(): 

    right = ''
    #print("rOp assign ", right)

    left = pOperandos.pop()
    leftType = pTipos.pop()
    print("leftType", leftType)

    result = pOperandos.pop()
    resultType = pTipos.pop()
    print("resOp assign ", result)
    print("rtype -", resultType)

    print("tamaño pTipos", len(pTipos))
    print("tamaño pOperandos", len(pOperandos))

    print("lOp assign ", left)
    
  
    #operador
    oper = pOperadores.pop()
    print(oper)

    result_type = semantic[resultType][oper][leftType]
    print(result_type)
    print("sensual")

    if result_type == "error":
      print("No se puede asignar un tipo '{}' a un tipo '{}'".format(leftType, resultType))
      raise Exception("No se puede asignar un tipo '{}' a un tipo '{}'".format(leftType, resultType))
    #agregarTipo(result_type)

    #agregar un valor a temp counter
    #generar cuadruplo
    """
    myAddress = None
    if dirVar.getlocalVariable(currFuncion, result) == None:
      if dirVar.getglobalVariable(result) == None:
        print("error en la busqueda")
        raise Exception("variable no existe we")
      else:
       myAddress = dirVar.getglobalVariable(result).direccion
    else:
      myAddress = dirVar.getlocalVariable(currFuncion, result).direccion
    """
    cuads.append((oper, left, right, result))
    print(cuads)

    #######################################################
#######NO SE DIRECCION
    #######################################################

    
    #agregar resultado en pOperandos
    #agrsegarID(result)
    #agregar resultadotipo en pTipospo
'''----------------------------------------------'''

def cuadsasignacion():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "=")):
      print("yes-assign")
      global tempcounter
      #tempcounter = tempcounter + 1
      auxAsignacion()
    else:
      #print(pOperandos)
      print("no-assign")


######################################################
#CONDICIONES Y CICLOS
######################################################
#pOperandos
#pOperandos = []

#POPER
#pOperadores = []



#1
#la ultima direccion de memoria validando el tipo de expresion
#if lasttemp != bool ERROR
#generar cuadruplo falso sin saber el resultado
def condicion1():
  #checktype = pTipos.pop()
  #implementar la tabla de variables y funciones
  #if checktype != bool:
    #print("TYPE MISMATCH")
  #else:
  result = pOperandos.pop()
  pTipos.pop()
  cuads.append(("GOTOF", result, " ", "fill"))
  print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
  print(len(cuads))
  psaltos.append(len(cuads)-1)
  print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
    
#2
#rellenar end
#end = psaltos.pop
#fill(end, cont)
def condicion2():
  #rint("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
  end = psaltos.pop()
  print(end)
  #print("No se logra establecer el fill")
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
  print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  print("No se logra establecer el fill")
  print(x)
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
  
  #implementar la tabla de variables y funciones
  print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2")
  #if checktype != bool:
  #  print("TYPE MISMATCH")
  #else:
  print("SS")
  result = pOperandos.pop()
  print("SS")
  #VControl = pOperandos[-1]
    #LLAMADA A CUBO SEMANTICO
    #if Tipo Res ERROR
    # SEMANTICA
  cuads.append(("=", result, " ", "VControl"))

def ciclofrom3():
  print("3333333333333333333333333333333333333333333333333333333333333")
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
  print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASSSSSS")
  global tempcounter
  result = "t" + str(tempcounter)
  tempcounter = tempcounter +1
  cuads.append(("+", "VControl", 1, result))
  cuads.append(("=", result, " ", "VControl"))

  cuads.append(("=", result, " ",pOperandos.pop()))
  pTipos.pop()
  print("2222222222222222222222222222222222222222222222222222222222222")
  FIN = psaltos.pop()
  RET = psaltos.pop()
  print("3333333333333333333333333333333333333333333333333333333333333")
  cuads.append(("GOTO", " ", " ", RET))
  fill(FIN, len(cuads))
  print("44444444444444444444444444444444444444444444444444444444444444")

  print("55555555555555555555555555555555555555555555555555555555555555")
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
  print("ERAAAAAAA")

def valparams(params):
  print("dentrodepilatipos")
  #validar tipo
  global conttipos
  print(pTipos[-1])
  if(params):
    if pTipos[-1] == params[conttipos]:
      conttipos += 1
      print("sientra")
      print(pOperandos[-1])
      vfin = ("param"+str(conttipos))
      print(vfin)
      cuads.append(("PARAM", pOperandos.pop() ," ", vfin))
      pTipos.pop()
      print("finaliza")
    else:
      print("errorparam")
  else:
    print("There are no params")

def valnull(params):
  #global conttipos
  if(len(params) == conttipos):
    return True
  else:
    return False

def createGOSUB(nombre):
  print(nombre)
  print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
  cuads.append(("GOSUB", nombre, " ", " "))


def valMain():
  print("maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaani")
  cumain = (("GOTO", " ", " ", len(cuads)))
  cuads[0] = cumain


def cReturn():
  print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
  valret = pOperandos[-1]
  cuads.append(("RETURN", " ", " ", valret))
  #return valret

def asignval(callfunc, tipo):

  if tipo == "int":
    result_addr = virtualAdd.getGlobalTempAddressInt()
  elif tipo == "float":
    result_addr = virtualAdd.getGlobalTempAddressFloat()
  else:
    print("errorASSIGN")
    
  cuads.append(("=", callfunc, " ", result_addr))


"""
  if tipo == "int":
    result_addr = virtualAdd.getGlobalTempAddressInt()
  elif tipo == "float":
    result_addr = virtualAdd.getGlobalTempAddressFloat()
  else:
    print("error")
  """

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
  print("tamaño pTipos", len(pTipos))
  print("tamaño pOperandos", len(pOperandos))
  print("la dir base es", direccion)
  dir_base = getConstantAddressbyValue(direccion, "int")
  result = virtualAdd.getGlobalTempAddressInt()
  cuads.append(("+", dir_base, pOperandos.pop(), result))
  pTipos.pop()
  agregarID(result)
  agregarTipo("int")

def sumaDirBasearr(temp, direccion):
  print(direccion)
  result = virtualAdd.getGlobalTempAddressInt()
  cuads.append(("+", direccion, temp, result))
  agregarID(result)
  agregarTipo("int")

######################################################
#PRINT
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


'''
myAddress = None
result = 'f'
currFuncion = 'helloWorld2'

dirVar.agregarFuncion('helloWorld2', "int")
dirVar.agregarlocalVariable('helloWorld2', result, [], "int", False)
dirVar.getlocalVariable(currFuncion, result).direccion = 9999


dirVar.agregarglobalVariable(result, [], "int")
dirVar.getglobalVariable(result).direccion = 1111

if dirVar.getlocalVariable(currFuncion, result) == None:
  if dirVar.getglobalVariable(result) == None:
    print("error en la busqueda")
    raise Exception("variable no existe we")
  else:
   print("global")
   myAddress = dirVar.getglobalVariable(result).direccion
else:
  print("local")
  myAddress = dirVar.getlocalVariable(currFuncion, result).direccion

print(myAddress)
'''
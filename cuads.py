import dirVar
import virtualAdd
import constantTypeCheck
pOperandos = []
pOperadores = []
pTipos = []

#cuadruplos
cuads=[("goto","1","","")]

tempcounter = 0
'''
def checarExistenciaGlobaloConstante(operandoIzq, operandoDer):
  if not constantTypeCheck.isConstant(operandoIzq) and not constantTypeCheck.isConstant(operandoDer):
    if operandoIzq not in dirVar.dirglobalVar:
      raise NameError('Variable ', operandoIzq,' no declarada')
      print('Variable ', operandoIzq,' no declarada')
    elif operandoDer not in dirVar.dirglobalVar:
      raise NameError('Variable ', operandoDer,' no declarada')
      print('Variable ', operandoDer,' no declarada')
'''

#funcion de agregar ID 
#validaciones de ID con tipo

## ESTO ES MÁS UN AGREGAR TEMPORAL EN CUADS Y CONSTANT O 
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
    
    #right operando
    #left operando
    right = pOperandos.pop()
    print(right)

    left = pOperandos.pop()
    print(left)
    
  #right type
    #left type
    #llenar con el tipo de los cuads

    #operador
    oper = pOperadores.pop()
    print(oper)

    #result type checar semantica con cubo

    #generar cuadruplo
    result = "t" + str(tempcounter)


    cuads.append((oper, left, right, result))
    print(cuads)

    #agregar resultado en pilaop
    agregarID(result)
    dirVar.agregarglobalVariable(result,"float")
    
    #agregar resultadotipo en pilatipo


def cuadssumsub():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "+") or ( pOperadores[-1] == "-")):
      global tempcounter
      tempcounter = tempcounter + 1
      validar()
    else:
      #print(pilaOp)
      print("no-summin")

def cuadsmuldiv():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "*") or ( pOperadores[-1] == "/")):
      print("yes")
      global tempcounter
      tempcounter = tempcounter + 1
      validar()
    else:
      #print(pilaOp)
      print("no-multdiv")

def cuadscomparation():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "<") or ( pOperadores[-1] == "==") 
      or (pOperadores[-1] == ">") or (pOperadores[-1] == "!=")):
      print("yes")
      global tempcounter
      tempcounter = tempcounter + 1
      validar()
    else:
      #print(pilaOp)
      print("no-compar")

def cuadsand():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "&")):
      print("yes")
      global tempcounter
      tempcounter = tempcounter + 1
      validar()
    else:
      #print(pilaOp)
      print("no-and")

def cuadsor():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "|")):
      print("yes")
      global tempcounter
      tempcounter = tempcounter + 1
      validar()
    else:
      #print(pilaOp)
      print("no-or")

'''
REVISAR ESTO
'''
def auxAsignacion(): 

    right = ''
    print(right)

    left = pOperandos.pop()
    print("lOp assign ", left)
    result = pOperandos.pop()
    print("lOp assign ", result)
  
    #operador
    oper = pOperadores.pop()
    print(oper)

    cuads.append((oper, left, right, result))
    print(cuads)
    
    dirVar.agregarglobalVariable(result,"float")
    print(dirVar.dirglobalVar)
    #agregar resultado en pilaop
    #agregarID(result)
    #agregar resultadotipo en pilatipo
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
      #print(pilaOp)
      print("no-assign")


def printCuads():
  cuadCounter = 0
  # print cuads as a formatted table
  print ("\n\n\n")
  print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format("cuad","op","v1","v2","vf"))
  print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format("----","--","---","---","---"))
  for el1, el2, el3, el4 in cuads:
      print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format(cuadCounter,el1,el2,el3,el4))
      cuadCounter+=1
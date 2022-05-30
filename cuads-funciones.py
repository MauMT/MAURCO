import dirVar
import virtualAdd
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
    
    #right operando
    #left operando
    right = pOperandos.pop()
    print(right)

    left = pOperandos.pop()
    print(left)

    #right type
    #left type
    #llenar con el tipo de os cuads

    #operador
    oper = pOperadores.pop()
    print(oper)

    #result type checar semantica con cubo

    #generar cuadruplo
    result = "t" + str(tempcounter)


    cuads.append((oper, left, right, result))
    print(cuads)

    #agregar resultado en pOperandos
    agregarID(result)
    dirVar.agregarglobalVariable(result,"float")
    
    #agregar resultadotipo en pTipospo


def cuadssumsub():
  if not pOperadores:
    print("empty")
  else:
    if(( pOperadores[-1] == "+") or ( pOperadores[-1] == "-")):
      global tempcounter
      tempcounter = tempcounter + 1
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
      global tempcounter
      tempcounter = tempcounter + 1
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
      global tempcounter
      tempcounter = tempcounter + 1
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
      global tempcounter
      tempcounter = tempcounter + 1
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
      global tempcounter
      tempcounter = tempcounter + 1
      validar()
    else:
      #print(pOperandos)
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
    #agregar resultado en pOperandos
    #agregarID(result)
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
  fill(false, len(cuads)+1)



def fill(x, y):
  print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  print("No se logra establecer el fill")
  print(x)
  auxfill = (cuads[x])
  v = list(auxfill)
  v[3] = str(y)
  cuads[x] = tuple(v)



def ciclowhile1():
  psaltos.append(len(cuads)-1)

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
  fill(end, len(cuads)-1)



def ciclofrom1(x):
  agregarID(x)
  #validar que el tipo de ID sea numerico
  #pTipos

def ciclofrom2():
  checktype = pTipos.pop()
  
  #implementar la tabla de variables y funciones
  if checktype != bool:
    print("TYPE MISMATCH")
  else:
    result = pOperandos.pop()
    VControl = pOperandos.top()
    tipControl = pOperandos.top()

    #LLAMADA A CUBO SEMANTICO
    #if Tipo Res ERROR
    # SEMANTICA
    cuads.append(("=", result, " ", VControl))

def ciclofrom3():
  checktype = pTipos.pop()
  #implementar la tabla de variables y funciones
  if checktype != bool:
    print("TYPE MISMATCH")
  else:
    result = pOperandos.pop()
    #VFinal = result
    cuads.append(("=", result, " ", "VFinal"))
    cuads.append(("<", "VControl", "VFinal", "Tx"))
    psaltos.append(len(cuads)-1)
    cuads.append(("GOTOF", "Tx", " ", "fill"))
    psaltos.append(len(cuads)-1)


def ciclofrom4():
  cuads.append(("+", "VControl", 1, "Ty"))
  cuads.append(("=", "Ty", " ", "VControl"))
  cuads.append(("=", "Ty", " ",pOperandos.top()))
  FIN = psaltos.pop()
  RET = psaltos.pop()
  cuads.append(("GOTO", " ", " ", RET))
  fill(FIN, len(cuads)-1)
  pOperandos.pop()
  pTipos.pop()



######################################################
#PRINT
######################################################
def printCuads():
  cuadCounter = 0
  # print cuads as a formatted table
  print ("\n\n\n")
  print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format("cuad","op","v1","v2","vf"))
  print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format("----","--","---","---","---"))
  for el1, el2, el3, el4 in cuads:
      print ("{:<10}{:<10}{:<10}{:<10}{:<10}".format(cuadCounter,el1,el2,el3,el4))
      cuadCounter+=1
import ply.lex as lex
import ply.yacc as yacc
import dirVar
import queue
import constantTypeCheck
import cuads
import virtualAdd
from functools import reduce

tokens = [
#
  'ID',
  'PROGRAM',
  'MAIN',
  'VARS',
# 
  'FUNCTION',
  'OBJECT',
#
  'INT',
  'FLOAT',
  'CHAR',
  'VOID',
#
  'SEP_COMMA',
  'SEP_SEMICOLON',
  'SEP_COLON',
  'SEP_LBRACE',
  'SEP_RBRACE',
  'SEP_LPAREN',
  'SEP_RPAREN',
  'SEP_LBRACKET',
  'SEP_RBRACKET',

#
  'OP_MULT',
  'OP_DIV',
  'OP_PLUS',
  'OP_MINUS',
  'OP_DOT',
  
#
  'OP_ASSIGN',
#
  'IF',
  'THEN',
  'ELSE',
#
  'WHILE',
  'DO',
  'FROM',
  'TO',
#
  'RETURN',
  'INPUT',
  'PRINT',
  'PRINTA',
  'MAP',
#
  'OP_GT',
  'OP_LT',
  'OP_NOTEQ',
  'OP_EQUAL',
  'REL_AND',
  'REL_OR',
#

  'CTE_INT',
  'CTE_CHAR',
  'CTE_FLOAT',
  
  'END',
  'CLASS',
  'INHERITS',
  'ATTRIBUTES',
  'METHODS',

]
#t_ID =#t_PROGRAMA =#t_VAR =  #tipos de datos#t_INT =#t_FLOAT =#t_STRING =#t_CTEINT =#t_CTEFLOAT =#comandos#t_IF =#t_ELSE = #t_PRINT =

#VOID FUNCTION ID SEP_LPAREN paramsmv SEP_RPAREN voidvarsmet
  
reservadas = {
  
  'program': 'PROGRAM',
  'main' : 'MAIN',
  'vars': 'VARS',

  'func': 'FUNCTION',
  'object': 'OBJECT',
  'if':'IF',
  'then' : 'THEN',
  'else':'ELSE',

  'while' : 'WHILE',
  'do' : 'DO',
  'from' : 'FROM',
  'to' : 'TO',

  'int': 'INT',
  'float': 'FLOAT',
  'char' : 'CHAR',
  'void' : 'VOID',
  'end': 'END',

  'return' : 'RETURN',
  'input' : 'INPUT',
  'print' : 'PRINT',
  'printA' : 'PRINTA',
  'map': 'MAP',
  'class': 'CLASS',
  'inherits': 'INHERITS',
  'attributes': 'ATTRIBUTES',
  'methods': 'METHODS',
  
  }

t_SEP_COMMA = r'\,'
t_SEP_SEMICOLON = r';'
t_SEP_COLON = r':'
t_SEP_LBRACE = r'\{'
t_SEP_RBRACE = r'\}'
t_SEP_LPAREN = r'\('
t_SEP_RPAREN = r'\)'
t_SEP_LBRACKET = r'\['
t_SEP_RBRACKET = r'\]'
t_OP_MULT = r'\*'
t_OP_DIV = r'/'
t_OP_PLUS = r'\+'
t_OP_MINUS = r'-' 
#signo del numero

t_OP_DOT = r'\.'
t_OP_ASSIGN = r'='
t_REL_AND = r'&'
t_REL_OR = r'\|'

t_OP_GT = r'\>'
t_OP_LT = r'\<'
t_OP_NOTEQ = r'\!='
t_OP_EQUAL = r'\=\='

# Caracteres ignorados
t_ignore = " \t"


# DEFINICIONES REGULARES

def t_CTE_FLOAT(t):
  r'\d\.\d+'
  t.value = float(t.value)
  return t

def t_CTE_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t 


def t_CTE_CHAR(t):
  r'\"[a-zA-Z0-9_]*\"'
  t.value = str(t.value)
  return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
  print ("caracter ilegal '%s'" % t.value[0])
  t.lexer.skip(1)

# REGLAS 

print("CALL INITIAL")

currID = queue.Queue()
currVars = queue.Queue()
currMet = queue.Queue()
currTypeID = queue.Queue()
arrLength = []
currFuncion = None

""" if(currFuncion == None):
    print("es none")
    arrVar = dirVar.getglobalVariable(currentID)
    if(arrVar == None):
        print("ERROR NO EXISTE LA VARIABLE")
else:
    arrVar = dirVar.getlocalVariable(currFuncion, currentID)
    if(arrVar == None):
      arrVar = dirVar.getglobalVariable(currentID)
      if(arrVar == None):
          #NO EXISTE
          print("ERROR NO EXISTE LA VARIABLE") """

def p_programa(p):
  '''
  programa : PROGRAM ID SEP_SEMICOLON proaux
  '''
  p[0] = "Success"

def p_ini(p):
  '''
  ini :
  '''
  print("CALL INITIAL")
  global currFuncion
  global currClass
  global currID
  global currTypeID
  global currMet
  global currVars
  global currTipo
  global isArr
  global isMat
  global arrExp
  isArr = False
  isMat = False
  arrExp = []
  arrLength = []
  currID = queue.Queue()
  currVars = queue.Queue()
  currMet = queue.Queue()
  currTypeID = queue.Queue()
  #currTipo = queue.Queue()
#####################################


def p_proaux(p):
  '''
  proaux : clase proaux
         | provarsaux 
  '''

#variables globales o funciones
def p_provarsaux(p):
  '''
  provarsaux : varsGlobal profunctions
             | profunctions
  '''

def p_varsGlobal(p):
    '''
    varsGlobal : VARS SEP_LBRACE varsauxGlobal SEP_RBRACE
    '''

def p_varsauxGlobal(p):
    '''
    varsauxGlobal : idvarsglobal
                  | objectsvarsglobal
                  | empty
     '''

def p_objectsvarsglobal(p):
    '''
    objectsvarsglobal : OBJECT ID lista_objetos varsauxGlobal
    '''
    print("call objectsvarsglobal")
    global currTipo
    currTipo = p[2]
    while not(currID.empty()) :
      curr = currID.get()
      print("Algo no se")
      dirVar.agregarglobalVariable(curr[0], curr[1], currTipo)

def p_idvarsglobal(p):
    '''
    idvarsglobal : typeVarsGlobal lista_ids stepid varsauxGlobal
     '''

def p_stepid(p):
    '''
    stepid : empty
    '''
    print("Empty")
    print(currID.empty())
    while not(currID.empty()) :
      curr = currID.get()
      print("gloubal ", curr[0], curr[1], currTipo)
      

      if len(curr[1]) == 0:
        print("not array")
        dirVar.agregarglobalVariable(curr[0], [], currTipo)
        print("not 1ssssss")
        if currTipo == "int":
          print("not 1aaaaaa")
          auxDir = virtualAdd.getGlobalAddressInt()
          print(auxDir)
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        elif currTipo == "float":
          print("not 123123")
          auxDir = virtualAdd.getGlobalAddressFloat()
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        else:
          print("tipo desconocido")
      else:
        print("array")
        dirVar.agregarglobalVariable(curr[0], curr[1], currTipo)
        arrSize = reduce(lambda x, y: x * y, curr[1])
        if currTipo == "int":
          auxDir = virtualAdd.getGlobalAddressInt(size=arrSize)
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        elif currTipo == "float":
          auxDir = virtualAdd.getGlobalAddressFloat(size=arrSize)
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        else:
          print("tipo desconocido")

def p_typeVarsGlobal(p):
  '''
  typeVarsGlobal : INT
                 | FLOAT
                 | CHAR
    '''
  print("call varsGlobal")
  global currTipo
  currTipo = p[1]
 


#funciones del programa

def p_profunctions(p):
  '''
  profunctions : functions profunctions
               | principal END
  '''

def p_principal(p):
  '''
  principal : MAIN maini SEP_LPAREN SEP_RPAREN bloque
  '''
  ############################
  ############################
  currTipo = "VOID"
  currFuncion = p[1]
  dirVar.agregarFuncion(currFuncion, currTipo)
  ############################
  ############################

def p_maini(p):
  '''
  maini : empty
  '''
  print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooa")
  cuads.valMain()

def p_bloque(p):
  '''
  bloque : SEP_LBRACE estatuto bloqueaux
  '''

def p_bloqueaux(p):
  '''
  bloqueaux : estatuto bloqueaux
            | SEP_RBRACE
  '''

#####################################
#clases
#####################################

def p_clase(p):
    '''
    clase : CLASS ID inheritsaux SEP_LBRACE ATTRIBUTES OP_LT atributos OP_GT metaux SEP_RBRACE
    '''
  #################################
    print("call clase")
    currClass = p[2]
    dirVar.crearClase(currClass)
    print("CLASSSSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

    #METODO QUE QUITA LAS VARIABLES Y PARAMETROS CON TIPO
    #currMet.put(currFuncion, currTipo)
    while not(currMet.empty()) :
      metup = currMet.get()
      print(metup)
      dirVar.agregarMetodosClase(currClass, metup[0], metup[1])
      
    #METODO QUE AGREGA LAS FUNCIONES
    while not(currTypeID.empty()) :
      tup = currTypeID.get()
      print(tup)
      #currID.put(p[1], isMat, isArr, arrLength) Tipo
      dirVar.agregarAtributosClase(currClass,tup[0], tup[1],tup[2])

def p_inheritsaux(p):
    '''
    inheritsaux : OP_LT INHERITS ID OP_GT
    | empty
    '''

def p_atributos(p):
  '''
  atributos : varsclass
            | empty
  '''

#######

def p_varsclass(p):
    '''
    varsclass : VARS varsauxclass
    '''

#111111111111111111111111111111
def p_varsauxclass(p):
    '''
    varsauxclass : idvarsclass
                  | objectsvarsclass
                  | empty
     '''

def p_objectsvarsclass(p):
    '''
    objectsvarsclass : OBJECT ID lista_objetos varsauxclass
    '''
    print("call objectsvarsclass")
    global currTipo
    currTipo = p[2]
    while not(currID.empty()) :
      curr = currID.get()
      currTypeID.put((curr[0], curr[1], currTipo))

def p_stepidvarsclass(p):
    '''
    stepidvarsclass : 
    '''
    while not(currID.empty()) :
      curr = currID.get()
      currTypeID.put((curr[0], curr[1], currTipo))

def p_idvarsclass(p):
    '''
    idvarsclass : typevarsclass lista_ids stepidvarsclass varsauxclass
    '''


def p_typevarsclass(p):
    '''
    typevarsclass : INT
            | FLOAT
            | CHAR
    '''
    print("call typevarsclass")
    global currTipo
    
    currTipo = p[1]
    print(currTipo)

def p_metaux(p):
    '''
    metaux : METHODS OP_LT metodos OP_GT
    | empty
    '''

################################################
# REVISAR
def p_metodos(p):
    '''
    metodos : metodo_void metodosaux
            | metodo_no_void metodosaux
    '''
def p_metodosaux(p):
    '''
    metodosaux : metodo_void metodosaux
               | metodo_no_void metodosaux
               | empty
    '''

def p_metodo_no_void(p):
    '''
    metodo_no_void : typemet SEP_LPAREN paramsmet SEP_RPAREN varsmet SEP_LBRACE estmet mnvaux 
    '''
    print("call metodo_no_void")


def p_metodo_void(p):
    '''
    metodo_void : typemet SEP_LPAREN paramsmet SEP_RPAREN voidvarsmet
    '''

def p_typemet(p):
    '''
    typemet : INT FUNCTION ID
            | FLOAT FUNCTION ID
            | CHAR FUNCTION ID
            | VOID FUNCTION ID
    '''
    currTipo = p[1]
    currFuncion = p[3]
    currMet.put((currFuncion, currTipo))
    #dirVar.agregarMetodosClase(currClass, currFuncion, currTipo)


def p_paramsmet(p):
    '''
    paramsmet : paramsmetcreate
              | empty
    '''


def p_paramsmetcreate(p):
    '''
    paramsmetcreate : typeparamet ID paramsauxmet
    '''
    print("paramsmnv")
    print(p[2])
    global arrLength
    currID.put((p[2], arrLength))
    curr = currID.get()
    currTypeID.put((curr[0], curr[1], currTipo))

def p_typeparamet(p):
    '''
    typeparamet : INT
                  | FLOAT
                  | CHAR
    '''
    print("call typeparammv")
    global currTipo
    currTipo = p[1]


def p_paramsauxmet(p):
    '''
    paramsauxmet : paramsauxmetcreate
                 | empty
    '''


def p_paramsauxmetcreate(p):
    '''
    paramsauxmetcreate : SEP_COMMA typeparamet ID paramsauxmet
    '''
    print("paramsmnv")
    print(p[3])
    global arrLength
    currID.put((p[3], arrLength))
    curr = currID.get()
    currTypeID.put((curr[0], curr[1], currTipo))


def p_voidvarsmet(p):
    '''
    voidvarsmet : varsmet SEP_LBRACE estmet RETURN SEP_SEMICOLON SEP_RBRACE
    '''


def p_varsmet(p):
    '''
    varsmet : metvarsm
                | empty
    '''

def p_varsmnv(p):
    '''
    metvarsm : VARS varsauxmet
    '''


def p_varsauxmet(p):
    '''
    varsauxmet : idvarsmet
              | objectsvarsmet
              | empty
    '''

def p_objectsvarsmet(p):
    '''
    objectsvarsmet : OBJECT ID lista_objetos varsauxmet
    '''
    print("call objectsvarsmet")
    currTipo = p[2]
    while not(currID.empty()) :
      curr = currID.get()
      currTypeID.put((curr[0], curr[1], currTipo))

def p_idvarsmet(p):
    '''
    idvarsmet : typemetp lista_ids stepidvarsmet varsauxmet
    '''

def p_stepidvarsmet(p):
    '''
    stepidvarsmet : 
    '''
    print("Empty")
    print(currID.empty())
    while not(currID.empty()) :
      curr = currID.get()
      currTypeID.put((curr[0], curr[1], currTipo))

def p_typemetp(p):
  '''
  typemetp : INT
                 | FLOAT
                 | CHAR
  '''
  print("call typemv")
  global currTipo
  currTipo = p[1]

def p_estmet(p):
    '''
    estmet : estatuto estmet
            | empty
    '''

def p_mnvaux(p):
    '''
    mnvaux : RETURN SEP_LPAREN hyper_exp SEP_RPAREN SEP_SEMICOLON SEP_RBRACE
    '''
#####################################
#General
#####################################
################################
def p_lista_ids(p):
  '''
  lista_ids : idlistval listaidaux
  '''

def p_idlistval(p):
    '''
    idlistval : ID 
    '''
    global currArrvalue
    currArrvalue = p[1]


def p_listaidaux(p):
    '''
    listaidaux : decarr pasarr decaraux
               | pasarr decaraux
    '''
    #print("ccccccccooooooooooooooooooooomo")
    

def p_pasarr(p):
    '''
    pasarr : empty
    '''
    global arrLength
    global currArrvalue
    
    print("OLISTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(currArrvalue)
    print(arrLength)
    print("next")
    if len(arrLength)==0:
      print("hey")
      currID.put((currArrvalue, []))
    else:
      print("hey1")
      currID.put((currArrvalue, arrLength))
        
    arrLength = []

    

def p_decaraux(p):
    '''
    decaraux : SEP_COMMA lista_ids
             | SEP_SEMICOLON
    '''
    #print("estaaaaaaaaaaaaaaaaaaaaaaaaaas")


def p_lista_objetos(p):
  '''
  lista_objetos : ID listaobjaux
  '''
  global arrLength
  currID.put((p[1], arrLength))
  print("lista_objetos")
  print(p[1])

def p_listaobjetosaux(p):
    '''
    listaobjaux : SEP_COMMA lista_objetos
                | SEP_SEMICOLON
    '''
  #######################################################
#ARRAYS
  #######################################################
def p_decarr(p):
    '''
    decarr : arrdecprime
           | matdecprime
    '''
    

def p_arrdecprime(p):
    '''
    arrdecprime : SEP_LBRACKET CTE_INT SEP_RBRACKET
    '''
    global arrLength
    arrLength = []
    arrLength.append(p[2])
    

def p_matdecprime(p):
    '''
    matdecprime : SEP_LBRACKET CTE_INT SEP_RBRACKET SEP_LBRACKET CTE_INT SEP_RBRACKET
    '''
    global arrLength
    arrLength = []
    arrLength.append(p[2])
    arrLength.append(p[5])



def p_acceso_array(p):
    '''
    acceso_array : mataccarraux
                 | arraccarraux
    '''

def p_it(p):
    '''
    it : empty
               
    '''
    print("NOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMMMMMMMMMMMS")


def p_arraccarraux(p):
    '''
    arraccarraux : SEP_LBRACKET hyper_exp SEP_RBRACKET
    '''
    global isArr
    global arrExp
    isArr = True
    val = cuads.pOperandos.pop()
    print(val)
    print("ATTTTTTTTTTTTTTTTTTTAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    arrExp.append(val)


def p_mataccarraux(p):
    '''
    mataccarraux : SEP_LBRACKET  hyper_exp SEP_RBRACKET SEP_LBRACKET  hyper_exp SEP_RBRACKET
    '''
    global isMat
    global arrExp
    isMat = True
    val = cuads.pOperandos.pop()
    print("ATTTTTTTTTTTTTTTTTTTAYYYYÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ")
    arrExp.append(val)
    val = cuads.pOperandos.pop()
    arrExp.append(val)

    
"""
def p_matvalue(p):
    '''
    matvalue : 
    '''
"""




####################################################################################
#PROBABLEMENTE QUITAR ARRAY INSIDE PORQUE ES MAS FUNCIONALIDAD CON PUNTOS
####################################################################################

def p_array_inside(p):
    '''
    array_inside : SEP_LBRACKET hyper_exp insideaux
    '''

def p_insideaux(p):
    '''
    insideaux : SEP_COMMA hyper_exp insideaux
              | SEP_RBRACKET matrixaux
    '''

def p_matrixaux(p):
    '''
    matrixaux : SEP_LBRACKET CTE_INT matrixinside
    '''

def p_matrixinside(p):
    '''
    matrixinside : SEP_COMMA CTE_INT matrixinside
                 | SEP_RBRACKET
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
             | decision
             | escritura
             | llamadavoid
             | repeticion
             | lectura
    '''
################################################

def p_asignacion(p):
    '''
    asignacion : valasigaux OP_ASSIGN asign_opciones SEP_SEMICOLON
    '''
    
    currOper = p[2]
    cuads.agregarOperador(currOper)
    cuads.cuadsasignacion()
    
  
def p_valasigaux(p):
  '''
  valasigaux : ID valasign_aux2
  '''

  global isArr
  global arrExp
  global isMat
  currentID = p[1]
  print("prueba ID --- ", currentID)
  print("tipo id --- ", currTipo)
  cuads.agregarID(currentID)

  #verificar que ID tiene dimensiones y tipo
  print("1")
  #currentID = cuads.pOperandos.top()
  #currTID = cuads.pTipos.pop()
  print("2")
  #print(currentID)
  if(currFuncion == None):
    print("es none")
    arrVar = dirVar.getglobalVariable(currentID)
    if(arrVar == None):
        print("ERROR NO EXISTE LA VARIABLE")
  else:
      arrVar = dirVar.getlocalVariable(currFuncion, currentID)
      if(arrVar == None):
        arrVar = dirVar.getglobalVariable(currentID)
        if(arrVar == None):
            #NO EXISTE
            print("ERROR NO EXISTE LA VARIABLE")

  print("3")
  #verificar si es un arreglo o matriz
  if(len(arrVar.length)==0):
    #ES UNA VARIABLE NORMAL
    print("normal")
  else:
    cuads.pOperandos.pop()
    #arr por ahora
    print("lengths Exp")
    print(len(arrExp))
    print(arrExp)
    print(len(arrVar.length))
    print("lengths arrvar")
    if(len(arrExp)==len(arrVar.length)):
        if(len(arrVar.length)==1):
            print("aqui entra arrvar1")
            #arreglo
            #verificar pilatop con arrexp
            #cuadruplo de suma
            print("arrExp en 0")
            print(arrExp[0])
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            print("verify")

            ##############AQUI HAY UNA DIRECCION FALSA HAY QUE CAMBIARLA 27/05

            cuads.sumaDirBasearr(arrExp[0], 3)
            print("no hay 4")

        else:
            print("aqui entra arrvar2")
            #matriz
            print("3")
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            print("4")
            cuads.arrMult(arrExp[0], arrVar.length[1])
            #verificar pilatop con arrexp
            print("5")
            cuads.arrVerifica(arrExp[1], arrVar.length[1])
            print("6")
            cuads.arrSumaMult(arrExp[1])
            print("7")
            cuads.sumaDirBase(3)
            print("8")
            #crear cuadruplo de multiplicacion
    else:
        #ERROR LAS DIMENSIONES NO COINCIDEN
        print("Las dimensiones no coinciden")
  print("4")


  isArr = False
  isMat = False
  arrExp = []



def p_valasign_aux2(p):
  '''
  valasign_aux2 :  asatr
                |  acceso_array
  '''



#agrgar el code para leer asignaciocompleja cteidcall creo
def p_asign_opciones(p):
  '''
  asign_opciones : asignacion_simple
               
  '''
  


def p_asignacion_simple(p):
  '''
  asignacion_simple : hyper_exp
                    | array_inside
  '''
  #cuads.cuadsasignacion()

def p_asatr(p):
      '''
      asatr : OP_DOT ID
           | empty
      '''

def p_asignacion_compleja(p):
    '''
    asignacion_compleja : usfunc asatr asignacion_funcion
    '''

def p_usfunc(p):
    '''
    usfunc : ID
    '''
    global callfunc
    callfunc = p[1]
    bex = dirVar.verify(p[1])
    if (bex):
        cuads.createERA(p[1])


##### NO USADA EN ESTA VERSIÓN
def p_asignacion_compleja_aux(p):
    '''
    asignacion_compleja_aux : asignacion_funcion
                            | asignacion_metodo
    '''
####

def p_asignacion_funcion(p):
    '''
    asignacion_funcion : SEP_LPAREN args SEP_RPAREN valnull
    '''

def p_valnull(p):
    '''
    valnull : empty
    '''
    global callfunc
    par = dirVar.getParametersfunc(callfunc)
    if(cuads.valnull(par)):
        print("Todo bien")
        cuads.createGOSUB(callfunc)
    else:
        print("break")


    if(dirVar.getfunctype(callfunc) == "void"):
        print("ES VOID")
        print("1 No todo bien")
    else:
        print("2 No todo bien")
        cuads.asignval(callfunc)

### cambié SEP_LPAREN arg SEP_RPAREN por asignacion_funcion
def p_asignacion_metodo(p):
    '''
    asignacion_metodo : OP_DOT ID asignacion_funcion
    '''

def p_args(p):
    '''
    args : hyper_exp validateparam argsaux
         | empty
    '''

def p_validateparam(p):
    '''
    validateparam : empty
    '''
    global callfunc
    par = dirVar.getParametersfunc(callfunc)
    cuads.valparams(par)




def p_argsaux(p):
    '''
    argsaux : SEP_COMMA hyper_exp validateparam argsaux
            | empty
    '''

def p_lectura(p):
    '''
    lectura : INPUT SEP_LPAREN ID lectaux SEP_RPAREN SEP_SEMICOLON
    '''

def p_lectaux(p):
    '''
    lectaux : SEP_COMMA ID lectaux
            | empty
    '''

def p_escritura(p):
    '''
    escritura : PRINT SEP_LPAREN escrituraaux
    '''

def p_escrituraaux(p):
    '''
    escrituraaux : letrero escaux2
                 | hyper_exp escaux2
    '''

def p_escaux2(p):
    '''
    escaux2 : SEP_COMMA escrituraaux
            | SEP_RPAREN
    '''

def p_letrero(p):
    '''
    letrero : CTE_CHAR letaux
    '''

def p_letaux(p):
    '''
    letaux : CTE_CHAR letaux
           | empty
    '''

#### NO SE USAN 😬#######
def p_llamadavoid(p):
    '''
    llamadavoid : usfunc asatr SEP_LPAREN args SEP_RPAREN valnull SEP_SEMICOLON
    '''

def p_voididt(p):
    '''
    voididt : ID
            | ID OP_DOT ID
    '''
#########################
  
def p_decision(p):
    '''
    decision : IF SEP_LPAREN hyper_exp SEP_RPAREN ifcond1 THEN bloque decisionaux ifcond2
    '''

def p_ifcond1(p):
  '''
  ifcond1 : empty
  '''
  cuads.condicion1()

def p_ifcond2(p):
  '''
  ifcond2 : empty
  '''
  cuads.condicion2()
  

def p_decisionaux(p):
    '''
    decisionaux : ifcond3 ELSE bloque
                | empty
    '''
  
def p_ifcond3(p):
  '''
  ifcond3 :
  '''
  cuads.condicion3()

def p_repeticion(p):
    '''
    repeticion : repeticioncondicional
                | repeticionnocondicional
    '''

def p_repeticioncondicional(p):
    '''
    repeticioncondicional : WHILE cicwh1 SEP_LPAREN hyper_exp SEP_RPAREN cicwh2 DO bloque cicwh3
    '''
  
def p_cicwh1(p):
  '''
  cicwh1 :
  '''
  cuads.ciclowhile1()

def p_cicwh2(p):
  '''
  cicwh2 :
  '''
  cuads.ciclowhile2()

def p_cicwh3(p):
  '''
  cicwh3 :
  '''
  cuads.ciclowhile3()

def p_repeticionnocondicional(p):
    '''
    repeticionnocondicional : FROM cicfr1 OP_ASSIGN hyper_exp cicfr2 TO hyper_exp cicfr3 DO bloque cicfr4
    '''

def p_cicfr1(p):
  '''
  cicfr1 : ID
  '''
  cuads.ciclofrom1(p[1])

def p_cicfr2(p):
  '''
  cicfr2 : 
  '''
  cuads.ciclofrom2()

def p_cicfr3(p):
  '''
  cicfr3 : 
  '''
  cuads.ciclofrom3()

def p_cicfr4(p):
  '''
  cicfr4 : 
  '''
  cuads.ciclofrom4()

###########################################################################
def p_valueid(p):
    '''
    valueid : ID
            | CTE_INT
    '''
#### REGLAS NO USADAS:  ####################################################
def p_llamadafuncionmetodo(p):
    '''
    llamadafuncionmetodo : funcidt SEP_LPAREN args SEP_RPAREN
    '''

def p_funcidt(p):
    '''
    funcidt : ID asatr
            
    '''

def p_funcidt_aux(p):
  '''
  funcidt_aux : OP_DOT ID
                | empty
  '''
####################################################
  
def p_map(p):
    '''
    map : MAP SEP_LPAREN ID SEP_COMMA operator SEP_COMMA intof SEP_RPAREN SEP_SEMICOLON
    '''

def p_operator(p):
    '''
    operator : OP_MULT
             | OP_DIV
             | OP_PLUS
             | OP_MINUS
    '''

def p_intof(p):
    '''
    intof : CTE_INT
          | CTE_FLOAT
    '''

def p_printA(p):
    '''
    printA : PRINTA SEP_LPAREN ID SEP_RPAREN SEP_SEMICOLON
    '''

################################################
# REVISAR la hyperexpresion para uso de AND y OR, falta modificar las reglas que usen expresion para que usen hyperexp
def p_hyper_exp(p):
    '''
    hyper_exp : and_exp hyper_aux
    '''

def p_hyper_aux(p):
    '''
    hyper_aux : REL_OR hyper_exp
              | empty
    '''
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
    cuads.cuadsor()

def p_and_exp(p):
    '''
    and_exp : expresion andexpaux
    '''
def p_andexpaux(p):
    '''
    andexpaux : REL_AND and_exp
              | empty
    '''
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
    cuads.cuadsand()

def p_expresion(p):
  '''
  expresion : exp expresionaux
  '''
  
def p_expresionaux(p):
  '''
  expresionaux : evaluators exp
               | empty
  '''
  ############################################################
  cuads.cuadscomparation()

def p_evaluators(p):
    '''
    evaluators : OP_LT
                | OP_GT
                | OP_EQUAL
                | OP_NOTEQ
    '''
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
  
def p_exp(p):
    '''
    exp : termino expaux
    '''
    print("exp")

  
def p_expaux(p):
    '''
    expaux : gensumres expaux
           | empty
    '''
    print("expaux")
    currOperador = p[1]
    cuads.agregarOperador(currOperador)

def p_gensumres(p):
    '''
    gensumres : OP_PLUS termino
              | OP_MINUS termino
    '''
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
    print("operador -|-|-|- ", currOperador)
    cuads.cuadssumsub()
    
def p_termino(p):
    '''
    termino : factor terminoaux
    '''
    print("term")
    ############################################################
    
  
def p_terminoaux(p):
    '''
    terminoaux :  genmuldiv terminoaux
               |  empty
    '''

def p_genmuldiv(p):
    '''
    genmuldiv : OP_MULT factor
              | OP_DIV factor
    '''
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
    print("operador -|-|-|- ", currOperador)
    cuads.cuadsmuldiv()
  
def p_factor(p):
    '''
    factor : SEP_LPAREN hyper_exp SEP_RPAREN
           | cteidcall
           | cteidcall_atributo_metodo
    '''


  #QUITE sign antes de cteidcall  
"""
def p_sign(p):
    '''
    sign : OP_PLUS
         | OP_MINUS
         | empty
    '''
    print("555555555555555555555555555555")
    print(p[0])
"""


###### CHECAR SI AGREGAR CTE_CHAR 
def p_cteidcall(p):
    '''
    cteidcall : CTE_INT
              | CTE_FLOAT
              
              
    '''
    currVal = p[1]
    print("mau ", currVal)
    currTipo = constantTypeCheck.checkintOrFloat(str(currVal))
    print("mmmm ", currTipo)

    if currVal in dirVar.dirConstantes:
        auxDir = dirVar.dirConstantes[currVal]
    else:
        if currTipo == "int":
          auxDir = virtualAdd.getConstantAddressInt()
        elif currTipo == "float":
          auxDir = virtualAdd.getConstantAddressFloat()
        dirVar.dirConstantes[currVal] = auxDir
    #cuads.agregarConst(currVal)
    cuads.agregarConst(auxDir)
    cuads.agregarTipo(currTipo)
    print("fffffffffffffffffffffffffffffffffffffffffffffffffffff")
    print(currVal)
    print(currTipo)
    
    
  #print("SSSSSSSSSSSSSSSSS")
    #print(p[1])

#Factorización por la izq de ID asatr y llamadafuncionmetodo
def p_cteidcall_atributo_metodo(p):
  '''
  cteidcall_atributo_metodo : ID var_id_aux
  '''
  global isArr
  global arrExp
  global isMat
  currentID = p[1]
  print("prueba ID --- ", currentID)
  print("tipo id --- ", currTipo)
  cuads.agregarID(currentID)
  cuads.agregarTipo(currTipo)
  #verificar que ID tiene dimensiones y tipo
  print("1")
  #currentID = cuads.pOperandos.top()
  #currTID = cuads.pTipos.pop()
  print("2")
  #print(currentID)
  if(currFuncion == None):
    print("es none")
    arrVar = dirVar.getglobalVariable(currentID)
    if(arrVar == None):
        print("ERROR NO EXISTE LA VARIABLE")
  else:
      arrVar = dirVar.getlocalVariable(currFuncion, currentID)
      if(arrVar == None):
        arrVar = dirVar.getglobalVariable(currentID)
        if(arrVar == None):
            #NO EXISTE
            print("ERROR NO EXISTE LA VARIABLE")

  print("3")
  #verificar si es un arreglo o matriz
  if(len(arrVar.length)==0):
    #ES UNA VARIABLE NORMAL
    print("normal")
  else:
    cuads.pOperandos.pop()
    #arr por ahora
    print("lengths Exp")
    print(len(arrExp))
    print(arrExp)
    print(len(arrVar.length))
    print("lengths arrvar")
    if(len(arrExp)==len(arrVar.length)):
        if(len(arrVar.length)==1):
            print("aqui entra arrvar1")
            #arreglo
            #verificar pilatop con arrexp
            #cuadruplo de suma
            print("arrExp en 0")
            print(arrExp[0])
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            print("verify")

            ##############AQUI HAY UNA DIRECCION FALSA HAY QUE CAMBIARLA 27/05

            cuads.sumaDirBasearr(arrExp[0], 3)
            print("no hay 4")

        else:
            print("aqui entra arrvar2")
            #matriz
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            cuads.arrMult(arrExp[0], arrVar.length[1])
            #verificar pilatop con arrexp
            cuads.arrVerifica(arrExp[1], arrVar.length[1])
            cuads.arrSumaMult(arrExp[1])

            cuads.sumaDirBase()
            #crear cuadruplo de multiplicacion
    else:
        #ERROR LAS DIMENSIONES NO COINCIDEN
        print("Las dimensiones no coinciden")
  print("4")


  isArr = False
  isMat = False
  arrExp = []


def p_var_id_aux(p):
  '''
  var_id_aux : aux_accesoarray
             | empty
  '''

def p_aux_accesoarray(p):
  '''
  aux_accesoarray : asatr cteidcall_am_aux
                  | acceso_array
  '''

# asignacion_funcion ---> SEP_LPAREN  SEP_RPAREN
def p_cteidcall_am_aux(p):
  '''
  cteidcall_am_aux : asignacion_funcion
                    | empty
  '''
################### NO SE USA
#def p_typeidf(p):
'''
typeidf : OP_DOT ID 
        | empty
'''
###################

def p_empty(p):
    'empty :'
    pass

def p_error(p):
  print("Error de parser en", p)
  raise Exception("Error al parsear ", p)


#####################################
#funciones
#####################################

def p_functions(p):
    '''
    functions : reini typefun
    '''

'''
def p_funcion_no_void(p):
    ''
    funcion_no_void : typefun 

    ''

def p_funcion_void(p):
    ''
    funcion_void : typefun 
    ''
'''

def p_typefun(p):
  '''
    typefun : INT FUNCTION ID novoidnext
                  | FLOAT FUNCTION ID novoidnext
                  | CHAR FUNCTION ID novoidnext
                  | VOID FUNCTION ID voidnext
  '''
  currTipo = p[1]
  currFuncion = p[3]
  dirVar.agregarFuncion(currFuncion, currTipo)
  dirVar.initFunction(currFuncion, insContcuad, primtempcont)
  dirVar.agregartemp(currFuncion, finaltemp)

  if(p[1] == "VOID"):
    print("hola")
    #valred
  else:
    dirVar.agregarglobalVariable(currFuncion, [], currTipo)

  #AGREGAR VARIABLES LOCALES
  while not(currTypeID.empty()) :
      tup = currTypeID.get()
      #(nomFuncion, nomVariable, arrLength, tipoVariable, isParam)
      #dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1], tup[2], tup[3])
      print("curr0:", tup[0], tup[1], tup[2], tup[3])
      
      tipo = tup[2]
      if len(tup[1]) == 0:
        print("not array")
        dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1], tup[2], tup[3])
        print("la variable es", tup[0], virtualAdd.Li)
        if tipo == "int":
          auxDir = virtualAdd.getLocalAddressInt()
          #setLocalVarAddress(func, nombreVar, dir)
          dirVar.setLocalVarAddress(currFuncion, tup[0], auxDir)
        elif tipo == "float":
          auxDir = virtualAdd.getLocalAddressFloat()
          dirVar.setLocalVarAddress(currFuncion, tup[0], auxDir)
        else:
          print("tipo desconocido")
        
      else:
        
        print(currFuncion)
        dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1], tup[2], tup[3])
        arrSize = reduce(lambda x, y: x * y, tup[1])
        
        print("arrSize", arrSize)
        if tipo == "int":
          auxDir = virtualAdd.getLocalAddressInt(size=arrSize)
          dirVar.setLocalVarAddress(currFuncion, tup[0], auxDir)
        elif tipo == "float":
          auxDir = virtualAdd.getLocalAddressFloat(size=arrSize)
          dirVar.setLocalVarAddress(currFuncion, tup[0], auxDir)
        else:
          print("tipo desconocido") 
      

def p_reini(p):
  '''
    reini : 
  '''
  virtualAdd.reiniciarCountersLocales()
  virtualAdd.reiniciarTemporalesLocales()

def p_voidnext(p):
  '''
  voidnext : SEP_LPAREN paramsfun SEP_RPAREN voidvars
  '''

def p_novoidnext(p):
  '''
  novoidnext : SEP_LPAREN paramsfun insCont SEP_RPAREN varsfun SEP_LBRACE estfun nvaux
  '''

  def p_cureturn(p):
    '''
    cureturn : empty
    '''
    cuads.cReturn()


def p_paramsfun(p):
    '''
    paramsfun : paramsfuncreate
              | empty
    '''


def p_paramsfuncreate(p):
    '''
    paramsfuncreate : typeparamfun ID paramsauxfun
    '''
    print("paramsmnv")
    print(p[2])
    global arrLength
    currID.put((p[2], arrLength))

    curr = currID.get()
    currTypeID.put((curr[0], curr[1], currTipo, True))


def p_typeparamfun(p):
    '''
    typeparamfun : INT
                  | FLOAT
                  | CHAR
    '''
    print("call typeparammnv")
    global currTipo
    currTipo = p[1]
      

def p_paramsauxfun(p):
    '''
    paramsauxfun : paramsauxfuncreate
                 | empty
    '''


def p_paramsauxfuncreate(p):
    '''
    paramsauxfuncreate : SEP_COMMA typeparamfun ID paramsauxfun
    '''
    print("paramsmnv")
    print(p[3])
    global arrLength
    currID.put((p[3], arrLength))

    curr = currID.get()
    currTypeID.put((curr[0], curr[1], currTipo, True))

def p_voidvars(p):
    '''
    voidvars : varsfun insCont SEP_LBRACE estfun RETURN SEP_SEMICOLON relCurr SEP_RBRACE
    '''


def p_insCont(p):
    '''
    insCont : empty
    '''
    global insContcuad
    global primtempcont
    insContcuad = cuads.getCurrCounter()
    primtempcont = cuads.getTempCounter()


def p_varsfun(p):
    '''
    varsfun : varsnfun
               | empty
    '''

def p_varsnfun(p):
    '''
    varsnfun : VARS varsauxfun
    '''

def p_varsauxfun(p):
    '''
    varsauxfun : idvarsfun
            | objectvarsfun
            | empty
     '''

def p_objectsvarsfun(p):
    '''
    objectvarsfun : OBJECT ID lista_objetos varsauxfun
    '''
    print("call objectsvarsmet")
    currTipo = p[2]
    while not(currID.empty()) :
      while not(currID.empty()) :
        curr = currID.get()
        currTypeID.put((curr[0], curr[1], currTipo, False))

def p_idvarsfun(p):
    '''
    idvarsfun : typefunp lista_ids stepidvarsfun varsauxfun
     '''

def p_stepidvarsfun(p):
    '''
    stepidvarsfun : 
    '''

    #currID.pust(p[1], isMat, isArr, arrLength)

    print("Empty")
    print(currID.empty())
    while not(currID.empty()) :
      curr = currID.get()
      currTypeID.put((curr[0], curr[1], currTipo, False))

def p_typefunp(p):
  '''
  typefunp : INT
                 | FLOAT
                 | CHAR
  '''
  print("call typemv")
  global currTipo
  currTipo = p[1]

def p_estfun(p):
    '''
    estfun : estatuto estfun
              | empty
    '''


def p_nvaux(p):
    '''
    nvaux : RETURN SEP_LPAREN hyper_exp cureturn SEP_RPAREN SEP_SEMICOLON relCurr SEP_RBRACE
    '''

def p_cureturn(p):
    '''
    cureturn : empty
    '''
    cuads.cReturn()

def p_relCurr(p):
    '''
    relCurr : empty
    '''
    #release current varTable
    #funcion para borrar toda la tabla de la funcion
    cuads.endfunc()
    global finaltemp
    finaltemp = cuads.getTempCounter()




file = open("basic_test.txt", 'r')

#lexer.input("program primero ")

lines = file.read()
file.close()

# Build the lexer.
lexer = lex.lex()
lexer.input(lines)

# Build the parser.
parser = yacc.yacc()
try:
    print('Parsing...')
    parser.parse(lines, debug=1)
    print("DIRGLOB")
    print(dirVar.dirglobalVar)
    print("dirFunc")
    print(dirVar.dirFunciones)
    print("Dirclases")
    print(dirVar.dirClases)
    
    print("\nvars hw2:\n")
    for key in dirVar.dirFunciones["helloWorld2"].localVar:
      print(key, dirVar.dirFunciones["helloWorld2"].localVar[key].__dict__)

    print("\nvars globales:\n")
    for key in dirVar.dirglobalVar:
      print(key, dirVar.dirglobalVar[key].__dict__)
    #a = (dirVar.getFuncion("helloWorld"))
    #print(a._dict_)
    #b = a["localVar"]
    #print(b._dict_)
    #clase
    #libro = (dirVar.dirClases["Libro"])
    #print(libro._dict_)
    #print("pOperandos\n", cuads.pOperandos)
    #print("pTipos\n", cuads.pTipos)
    #print("pOperadores\n", cuads.pOperadores)
    print("Correct syntax")
except:
    print(f'Syntax error')
    

cuads.printCuads()
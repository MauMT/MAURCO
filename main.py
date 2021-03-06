'''
  MÓDULO PRINCIPAL
  Contiene el parser y hace el guardado de las variables, funciones y expresiones
  para su posterior manejo y ejecución 
  
  - Hace uso del módulo 'cuads' para llamar a cada uno delos métodos que generan los cuádruplos
  - Hace uso del módulo 'dirVar' para guardar y verificar la existencia de las variables, constantes y funciones
  - Usa el módulo 'virtualAdd' para aignar una dirección virtual a cada una de las variables, constantes y funciones
  - Usa el módulo constantTypeCheck para verificar cuál es el tipo de una constante y si es válido
  - Utiliza la función reduce del módulo 'functool' para hacer el cálculo del tamaño de un arreglo con base en sus dimensiones
'''
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
  'class': 'CLASS',
  'inherits': 'INHERITS',
  'attributes': 'ATTRIBUTES',
  'methods': 'METHODS',
  
  }

t_SEP_COMMA = r'\,'
t_SEP_SEMICOLON = r';'
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
  r'\d*\.\d+'
  t.value = float(t.value)
  return t

def t_CTE_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t 



def t_CTE_CHAR(t):
  #r'\"[a-zA-Z0-9_ .,-]*\"'
  r'\".*\"'
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
  print("Lexical Error: El caracter '%s' no es válido" % t.value[0])
  raise Exception("Caracter ilegal '%s'" % t.value[0])
  t.lexer.skip(1)

# REGLAS 

#print("CALL INITIAL")

currID = queue.Queue()
currMet = queue.Queue()
currTypeID = queue.Queue()
arrLength = []
currFuncion = None
isCallFun = False


def p_programa(p):
  '''
  programa : PROGRAM ID SEP_SEMICOLON proaux
  '''
  p[0] = "Success"



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
    #print("call objectsvarsglobal")
    global currTipo
    currTipo = p[2]
    while not(currID.empty()) :
      curr = currID.get()
      dirVar.agregarglobalVariable(curr[0], curr[1], currTipo)

def p_idvarsglobal(p):
    '''
    idvarsglobal : typeVarsGlobal lista_ids stepid varsauxGlobal
     '''

def p_stepid(p):
    '''
    stepid : empty
    '''
    
    #print(currID.empty())
    while not(currID.empty()) :
      curr = currID.get()
      
      if len(curr[1]) == 0:
        #print("not array")
        
        dirVar.agregarglobalVariable(curr[0], [], currTipo)
        
        #print("not 1ssssss")
        if currTipo == "int":
          auxDir = virtualAdd.getGlobalAddressInt()
          #print(auxDir)
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        elif currTipo == "float":
          
          auxDir = virtualAdd.getGlobalAddressFloat()
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        else:
          pass
      else:
        # Es un array
        dirVar.agregarglobalVariable(curr[0], curr[1], currTipo)
        arrSize = reduce(lambda x, y: x * y, curr[1])
        if currTipo == "int":
          auxDir = virtualAdd.getGlobalAddressInt(size=arrSize)
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        elif currTipo == "float":
          auxDir = virtualAdd.getGlobalAddressFloat(size=arrSize)
          dirVar.setGlobalVarAddress(curr[0], auxDir)
        else:
          pass

def p_typeVarsGlobal(p):
  '''
  typeVarsGlobal : INT
                 | FLOAT
                 | CHAR
    '''
  global currTipo
  currTipo = p[1]
 



# REGLAS DE LAS FUNCIONES

def p_profunctions(p):
  '''
  profunctions : functions profunctions
               | principal END endcuads
  '''

def p_endcuads(p):
    '''
    endcuads : empty
    '''
    cuads.fincuads()

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
    #print("call clase")
    currClass = p[2]
    dirVar.crearClase(currClass)
    

    #METODO QUE QUITA LAS VARIABLES Y PARAMETROS CON TIPO
    #currMet.put(currFuncion, currTipo)
    while not(currMet.empty()) :
      metup = currMet.get()
      #print(metup)
      dirVar.agregarMetodosClase(currClass, metup[0], metup[1])
      
    #METODO QUE AGREGA LAS FUNCIONES
    while not(currTypeID.empty()) :
      tup = currTypeID.get()
      #print(tup)
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
    #print("call objectsvarsclass")
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
    #print("call typevarsclass")
    global currTipo
    
    currTipo = p[1]
    #print(currTipo)

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
    #print("call metodo_no_void")
    pass


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
    #print("paramsmnv")
    #print(p[2])
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
    #print("call typeparammv")
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
    #print("paramsmnv")
    #print(p[3])
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
    #print("call objectsvarsmet")
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
    
    #print(currID.empty())
    while not(currID.empty()) :
      curr = currID.get()
      currTypeID.put((curr[0], curr[1], currTipo))

def p_typemetp(p):
  '''
  typemetp : INT
                 | FLOAT
                 | CHAR
  '''
  #print("call typemv")
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
    
    

def p_pasarr(p):
    '''
    pasarr : empty
    '''
    global arrLength
    global currArrvalue
    
    if len(arrLength)==0:
      currID.put((currArrvalue, []))
    else:
      currID.put((currArrvalue, arrLength))
        
    arrLength = []

    

def p_decaraux(p):
    '''
    decaraux : SEP_COMMA lista_ids
             | SEP_SEMICOLON
    '''
    


def p_lista_objetos(p):
  '''
  lista_objetos : ID listaobjaux
  '''
  global arrLength
  currID.put((p[1], arrLength))
  

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
    #print("Verificación de acceso a la regla")


def p_arraccarraux(p):
    '''
    arraccarraux : SEP_LBRACKET hyper_exp SEP_RBRACKET
    '''
    global isArr
    global arrExp
    isArr = True
    val = cuads.pOperandos.pop()
    arrExp.append(val)


def p_mataccarraux(p):
    '''
    mataccarraux : SEP_LBRACKET  hyper_exp SEP_RBRACKET SEP_LBRACKET  hyper_exp SEP_RBRACKET
    '''
    global isMat
    global arrExp
    isMat = True
    val = cuads.pOperandos.pop()
    arrExp.insert(0, val)
    val = cuads.pOperandos.pop()
    arrExp.insert(0, val)


def p_estatuto(p):
    '''
    estatuto : asignacion
             | decision
             | escritura
             | llamadavoid
             | repeticion
             | lectura
    '''


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
  if(currFuncion == "main" or currFuncion == None):
    var = dirVar.getglobalVariable(currentID)
    if(var == None):
      print("Name Error: Variable '{}' no declarada".format(currentID))
      sys.exit()
    tipo = var.tipoVariable()
  else:
      if(dirVar.getlocalVariable(currFuncion, currentID) == None):
        var = dirVar.getglobalVariable(currentID)
        if(var == None):
          print("Name Error: Variable '{}' no declarada".format(currentID))
          sys.exit()
        tipo = dirVar.getglobalVariable(currentID).tipoVariable()

      else:

        tipo = dirVar.getlocalVariable(currFuncion, currentID).tipoVariable()

  cuads.agregarID(currentID)
  cuads.agregarTipo(tipo)
  
  if(currFuncion == "main" or currFuncion == None):
    arrVar = dirVar.getglobalVariable(currentID)
    if(arrVar == None):
        print("No existe la variable global", currentID)
        raise Exception("No existe la variable global", currentID)
    auxDir = arrVar.direccion

  else:
    
    if(dirVar.getlocalVariable(currFuncion, currentID) == None):
        arrVar = dirVar.getglobalVariable(currentID)
        auxDir = arrVar.direccion
    else:
        
        arrVar = dirVar.getlocalVariable(currFuncion, currentID)
        if(arrVar == None):
            print("No existe la variable global", currentID)
            raise Exception("No existe la variable global", currentID)
        auxDir = arrVar.direccion

  #print("3")
  #verificar si es un arreglo o matriz
  if(len(arrVar.length)==0):
    #print("arrvarlength0")
    cuads.pOperandos[-1] = auxDir
  else:
    cuads.pOperandos.pop()
    #arr por ahora
    #print("lengths Exp")
    #print(len(arrExp))
    #print(arrExp)
    #print(len(arrVar.length))
    #print("lengths arrvar")


    myAddress = None
    if dirVar.getlocalVariable(currFuncion, currentID) == None:
        if dirVar.getglobalVariable(currentID) == None:
            print("Name Error: Variable '{}' no declarada".format(currentID))
            raise Exception("No existe la variable global", currentID)
        else:
            myAddress = dirVar.getglobalVariable(currentID).direccion
    else:
        myAddress = dirVar.getlocalVariable(currFuncion, currentID).direccion

    if(len(arrExp)==len(arrVar.length)):
        if(len(arrVar.length)==1):
            
            #arreglo
            #verificar pilatop con arrexp
            #cuadruplo de suma
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            

            cuads.sumaDirBasearr(arrExp[0], myAddress)
            

        else:
            #print("aqui entra arrvar2")
            #matriz
            #print("3")
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            #print("4")
            cuads.arrMult(arrExp[0], arrVar.length[1])
            #verificar pilatop con arrexp
            #print("5")
            cuads.arrVerifica(arrExp[1], arrVar.length[1])
            #print("6")
            cuads.arrSumaMult(arrExp[1])
            #print("7")
            cuads.sumaDirBase(myAddress)
            #print("8")
            #crear cuadruplo de multiplicacion
    else:
        #ERROR LAS DIMENSIONES NO COINCIDEN
        print("Dimension Error: Las dimensiones no coinciden")
        raise Exception("Las dimensiones no coinciden")
  #print("4")


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
  asignacion_simple : it hyper_exp
  '''


def p_asatr(p):
      '''
      asatr : OP_DOT ID
           | empty
      '''

def p_asignacion_compleja(p):
    '''
    asignacion_compleja : usfunc asignacion_funcion
    '''

def p_usfunc(p):
    '''
    usfunc : ID
    '''
    #print("IDGLOBALCURRFUNC")
    #print(p[1])
    global callfunc
    callfunc = p[1]
    bex = dirVar.verify(p[1])
    if (bex):
        cuads.createERA(p[1])



def p_asignacion_funcion(p):
    '''
    asignacion_funcion : SEP_LPAREN args SEP_RPAREN valnull
    '''
    pass

def p_valnull(p):
    '''
    valnull : empty
    '''
    global callfunc
    par = dirVar.getParametersfunc(callfunc)
    
    if(cuads.valnull(par)):
        
        cuads.createGOSUB(callfunc)
    else:
        pass
        #print("break")


    if(dirVar.getfunctype(callfunc) == "void"):
        #print("ES VOID")
        pass
    else:
        
        dirFuncion = dirVar.getglobalVariable(callfunc).direccion
        cuads.asignval(dirFuncion, dirVar.getfunctype(callfunc))


""" def p_asignacion_metodo(p):
    '''
    asignacion_metodo : OP_DOT ID asignacion_funcion
    ''' """

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
    lectura : INPUT SEP_LPAREN valasigaux cuadsinput lectaux  SEP_RPAREN SEP_SEMICOLON
    '''
    #print("LECTURA")

def p_lectaux(p):
    '''
    lectaux : SEP_COMMA valasigaux cuadsinput lectaux
            | empty
    '''

def p_cuadsinput(p):
    '''
    cuadsinput : empty
    '''
    cuads.lectInp()

def p_escritura(p):
    '''
    escritura : PRINT SEP_LPAREN escrituraaux
    '''

def p_escrituraaux(p):
    '''
    escrituraaux : letrero escaux2
                 | hyper_exp cuadprint escaux2
    '''

def p_escaux2(p):
    '''
    escaux2 : SEP_COMMA escrituraaux
            | SEP_RPAREN SEP_SEMICOLON
    '''

def p_cuadprint(p):
    '''
    cuadprint : empty
    '''
    cuads.escPri()


def p_letrero(p):
    '''
    letrero : CTE_CHAR 
    '''
    cuads.escChar(p[1])
 


def p_llamadavoid(p):
    '''
    llamadavoid : usfunc asatr SEP_LPAREN args SEP_RPAREN valnull SEP_SEMICOLON
    '''


  
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
  expresionaux : evaluators exp cuadcomp
               | empty
  '''
  ############################################################


def p_cuadcomp(p):
  '''
  cuadcomp : empty
  '''
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

  
def p_expaux(p):
    '''
    expaux : gensumres expaux
           | empty
    '''
    """ currOperador = p[1]
    cuads.agregarOperador(currOperador) """

def p_gensumres(p):
    '''
    gensumres : OP_PLUS termino
              | OP_MINUS termino
    '''
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
    cuads.cuadssumsub()
    
def p_termino(p):
    '''
    termino : it factor terminoaux
    '''
    
    
  
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
    cuads.cuadsmuldiv()
  
def p_factor(p):
    '''
    factor : SEP_LPAREN hyper_exp SEP_RPAREN
           | cteidcall
           | separadorarrfunc
    '''


def p_cteidcall(p):
    '''
    cteidcall : CTE_INT
              | CTE_FLOAT
              
              
    '''
    currVal = p[1]
    currTipo = constantTypeCheck.checkintOrFloat(str(currVal))

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
    
 

def p_separadorarrfunc(p):
    '''
    separadorarrfunc : asignacion_compleja
                     | cteidcall_atributo_metodo
    '''


#Factorización por la izq de ID asatr y llamadafuncionmetodo
def p_cteidcall_atributo_metodo(p):
  '''
  cteidcall_atributo_metodo : ID var_id_aux
  '''
  global isArr
  global arrExp
  global isMat
  currentID = p[1]
  

  if(currFuncion == "main" or currFuncion == None):
    var = dirVar.getglobalVariable(currentID)
    if var == None:
      print("Name Error: variable '{}' no declarada".format(currentID))
      sys.exit()
    tipo = var.tipoVariable()
  else:
      
      if(dirVar.getlocalVariable(currFuncion, currentID) == None):
        var = dirVar.getglobalVariable(currentID)
        if var == None:
          print("Name Error: variable '{}' no declarada".format(currentID))
          sys.exit()
        tipo = dirVar.getglobalVariable(currentID).tipoVariable()

      else:
        tipo = dirVar.getlocalVariable(currFuncion, currentID).tipoVariable()


  cuads.agregarID(currentID)
  cuads.agregarTipo(tipo)
  
  if(currFuncion == "main" or currFuncion == None):
    arrVar = dirVar.getglobalVariable(currentID)
    if(arrVar == None):
        print("No existe la variable global", currentID)
        raise NameError("No existe la variable global", currentID)
    auxDir = arrVar.direccion

  else:

    if(dirVar.getlocalVariable(currFuncion, currentID) == None):
        arrVar = dirVar.getglobalVariable(currentID)
        auxDir = arrVar.direccion
    else:
        
        arrVar = dirVar.getlocalVariable(currFuncion, currentID)
        if(arrVar == None):
            print("No existe la variable local", currentID)
            raise NameError("No existe la variable local", currentID)
        auxDir = arrVar.direccion

  
  #verificar si es un arreglo o matriz
  if(len(arrVar.length)==0):
    
    cuads.pOperandos[-1] = auxDir
  else:
    cuads.pOperandos.pop()
    #arr por ahora
    """ print("lengths Exp")
    print(len(arrExp))
    print(arrExp)
    print(len(arrVar.length))
    print("lengths arrvar") """


    myAddress = None
    if dirVar.getlocalVariable(currFuncion, currentID) == None:
        if dirVar.getglobalVariable(currentID) == None:
            print("Name Error: variable '{}' no declarada".format(currentID))
            raise Exception("variable no declarada")
        else:
            myAddress = dirVar.getglobalVariable(currentID).direccion
    else:
        myAddress = dirVar.getlocalVariable(currFuncion, currentID).direccion

    if(len(arrExp)==len(arrVar.length)):
        if(len(arrVar.length)==1):
            
            #arreglo
            #verificar pilatop con arrexp
            #cuadruplo de suma
            
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            cuads.sumaDirBasearr(arrExp[0], myAddress)
            

        else:
            
            #matriz
            #print("3")
            cuads.arrVerifica(arrExp[0], arrVar.length[0])
            #print("4")
            cuads.arrMult(arrExp[0], arrVar.length[1])
            #verificar pilatop con arrexp
            #print("5")
            cuads.arrVerifica(arrExp[1], arrVar.length[1])
            #print("6")
            cuads.arrSumaMult(arrExp[1])
            #print("7")
            cuads.sumaDirBase(myAddress)
            #print("8")
            #crear cuadruplo de multiplicacion
    else:
        #ERROR LAS DIMENSIONES NO COINCIDEN
        print("Dimension Error: Las dimensiones no coinciden")
        raise Exception("Dimension Error: Las dimensiones no coinciden")
  #print("4")


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
  aux_accesoarray : acceso_array
                  | asatr cteidcall_am_aux
  '''


def p_cteidcall_am_aux(p):
  '''
  cteidcall_am_aux : asignacion_funcion
                | empty
  '''



def p_empty(p):
    'empty :'
    pass

def p_error(p):
  print("Syntax Error: Expresión o token no válido", p)
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
    typefun : nvfuntipid novoidnext
            | vfuntipid voidnext
  '''
  

def p_nvfuntipid(p):
    '''
    nvfuntipid : INT FUNCTION ID
               | FLOAT FUNCTION ID
               | CHAR FUNCTION ID
    '''
    global currTipo
    global currFuncion
    currTipo = p[1]
    currFuncion = p[3]
    
    dirVar.agregarFuncion(currFuncion, currTipo)
    #dirVar.initFunction(currFuncion, insContcuad, primtempcont)
    if(currTipo == "void"):
        pass
    else:
        dirVar.agregarglobalVariable(currFuncion, [], currTipo)
        if currTipo == "int":
          auxDir = virtualAdd.getGlobalAddressInt()
          dirVar.setGlobalVarAddress(currFuncion, auxDir)
          dirVar.dirFunciones[currFuncion].direccion = auxDir
        elif currTipo == "float":
          auxDir = virtualAdd.getGlobalAddressFloat()
          dirVar.setGlobalVarAddress(currFuncion, auxDir)
          dirVar.dirFunciones[currFuncion].direccion = auxDir
        else:
          pass
          #print("tipo desconocido")



def p_vfuntipid(p):
    '''
    vfuntipid : VOID FUNCTION ID
    '''
    global currTipo
    global currFuncion
    currTipo = p[1]
    currFuncion = p[3]
    dirVar.agregarFuncion(currFuncion, currTipo)
    
    if(currTipo != "void"):
        dirVar.agregarglobalVariable(currFuncion, [], currTipo)

   
def p_genLoc(p):
      '''
      genLoc : empty
      '''
      
      #dirVar.agregartemp(currFuncion, finaltemp)
      #AGREGAR VARIABLES LOCALES
      while not(currTypeID.empty()) :
          tup = currTypeID.get()
          #(nomFuncion, nomVariable, arrLength, tipoVariable, isParam)
          #dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1], tup[2], tup[3])
          
          #print("curr0:", tup[0], tup[1], tup[2], tup[3])
          
          tipo = tup[2]
          if len(tup[1]) == 0:
            #print("not array")
            dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1], tup[2], tup[3])
            
            if tipo == "int":
              auxDir = virtualAdd.getLocalAddressInt()
              #setLocalVarAddress(func, nombreVar, dir)
              dirVar.setLocalVarAddress(currFuncion, tup[0], auxDir)
            elif tipo == "float":
              auxDir = virtualAdd.getLocalAddressFloat()
              dirVar.setLocalVarAddress(currFuncion, tup[0], auxDir)
            else:
              raise TypeError("tipo desconocido")
            
          else:
            
            dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1], tup[2], tup[3])
            arrSize = reduce(lambda x, y: x * y, tup[1])
            
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
  novoidnext : SEP_LPAREN paramsfun insCont SEP_RPAREN varsfun SEP_LBRACE genLoc estfun nvaux
  '''

  """ def p_cureturn(p):
    '''
    cureturn : empty
    '''
    cuads.cReturn() """


def p_paramsfun(p):
    '''
    paramsfun : paramsfuncreate
              | empty
    '''


def p_paramsfuncreate(p):
    '''
    paramsfuncreate : typeparamfun ID paramsauxfun
    '''
    
    global arrLength
    global currTipo
    currID.put((p[2], arrLength))

    curr = currID.get()
    currTypeID.put((curr[0], curr[1], currTipo, True))


def p_typeparamfun(p):
    '''
    typeparamfun : INT
                  | FLOAT
                  | CHAR
    '''
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
    
    global arrLength
    currID.put((p[3], arrLength))

    curr = currID.get()
    currTypeID.put((curr[0], curr[1], currTipo, True))

def p_voidvars(p):
    '''
    voidvars : varsfun insCont SEP_LBRACE genLoc estfun RETURN SEP_SEMICOLON relCurr SEP_RBRACE
    '''


def p_insCont(p):
    '''
    insCont : empty
    '''
    global insContcuad
    global primtempcont
    insContcuad = cuads.getCurrCounter()
    dirVar.initFunction(currFuncion, insContcuad)


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

    #print(currID.empty())
    while not(currID.empty()) :
      curr = currID.get()
      
      currTypeID.put((curr[0], curr[1], currTipo, False))

def p_typefunp(p):
  '''
  typefunp : INT
                 | FLOAT
                 | CHAR
  '''
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
    #print(currFuncion)
    cuads.endfunc()
    global finaltemp
    #finaltemp = cuads.getTempCounter()


def printDirVarValues():
  print("DIRGLOB")
  print(dirVar.dirglobalVar)
  print("dirFunc")
  print(dirVar.dirFunciones)
  print("Dirclases")
  print(dirVar.dirClases)
  
  print("\nvars globales:\n")
  for key in dirVar.dirglobalVar:
    print(key, dirVar.dirglobalVar[key].__dict__)

  print("\ndirConstantes\n")
  for key in dirVar.dirConstantes:
    print(dirVar.dirConstantes[key], key)



def run(name, flag):
  file = open("Testing files/"+name, 'r')

  lines = file.read()
  file.close()
  # Build the lexer.
  lexer = lex.lex()
  lexer.input(lines)

  # Build the parser.
  parser = yacc.yacc()
  try:
      
      parser.parse(lines, debug=0)
      #print("flag", flag)
      cuads.addCounter()
      if flag == "1":
        cuads.printCuads()
      import vm
      

  except:
      print(f'Syntax error')

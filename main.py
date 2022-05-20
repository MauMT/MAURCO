import ply.lex as lex
import ply.yacc as yacc
import dirVar
import queue
import constantTypeCheck
import cuads

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
'''global currFuncion
global currClass
global currID
global currTypeID
global currMet
global currVars
global currTipo'''
currID = queue.Queue()
currVars = queue.Queue()
currMet = queue.Queue()
currTypeID = queue.Queue()
currFuncion = ""
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
      cul = currID.get()
      print("VARGLOBAAAAAAAAAAAAAAAAAAAAL")
      print(cul)
      dirVar.agregarglobalVariable(cul, currTipo)

def p_idvarsglobal(p):
    '''
    idvarsglobal : typeVarsGlobal lista_ids stepid varsauxGlobal
     '''
  
def p_stepid(p):
    '''
    stepid : 
    '''
    print("Empty")
    print(currID.empty())
    while not(currID.empty()) :
      dirVar.agregarglobalVariable(currID.get(), currTipo)
    

def p_typeVarsGlobal(p):
  '''
  typeVarsGlobal : INT
                 | FLOAT
                 | CHAR
    '''
  print("call varsGlobal")
  global currTipo
  currTipo = p[1]
  #print("Empty")
  #print(currID.empty())
  #while not(currID.empty()) :
    #dirVar.agregarglobalVariable(currID.get(), currTipo)


#funciones del programa

def p_profunctions(p):
  '''
  profunctions : functions profunctions
               | principal END
  '''

def p_principal(p):
  '''
  principal : MAIN SEP_LPAREN SEP_RPAREN bloque
  '''
  ############################
  ############################
  currTipo = "VOID"
  currFuncion = p[1]
  
  dirVar.agregarFuncion(currFuncion, currTipo)
  ############################
  ############################

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
      #currTypeID.put(currID.get(), currTipo)
      tup = currTypeID.get()
      print(tup)
      dirVar.agregarAtributosClase(currClass,tup[0], tup[1])

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
      currTypeID.put((currID.get(), currTipo))
      #dirVar.agregarAtributosClase(currClass,currID.get(), currTipo)

def p_stepidvarsclass(p):
    '''
    stepidvarsclass : 
    '''
    #print("Empty")
    #print(currID.empty())
    #print(currTipo)
    while not(currID.empty()) :
      currTypeID.put((currID.get(), currTipo))

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
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    #while not(currID.empty()) :
      #currTypeID.put(currID.get(), currTipo)
      #objcur = (currID.get(), currTipo)
      #print(objcur)
      #print("objcur")
      #currTypeID.put(objcur)

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
    print("4588888 -", currFuncion)
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
    currID.put(p[2])
    currTypeID.put((currID.get(), currTipo))

def p_typeparamet(p):
    '''
    typeparamet : INT
                  | FLOAT
                  | CHAR
    '''
    print("call typeparammv")
    global currTipo
    currTipo = p[1]
    #while not(currID.empty()) :
      #currTypeID.put(currID.get(), currTipo)


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
    currID.put(p[3])
    currTypeID.put((currID.get(), currTipo))


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
      currTypeID.put((currID.get(), currTipo))

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
      currTypeID.put((currID.get(), currTipo))

def p_typemetp(p):
  '''
  typemetp : INT
                 | FLOAT
                 | CHAR
  '''
  print("call typemv")
  global currTipo
  currTipo = p[1]
  #while not(currID.empty()) :
      #currTypeID.put(currID.get(), currTipo)

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
  lista_ids : ID listaidaux
  '''
  print("listaids")
  print(p[1])
  currID.put(p[1])

def p_listaidaux(p):
    '''
    listaidaux : decarr decaraux
               | decaraux
    '''
    

def p_decaraux(p):
    '''
    decaraux : SEP_COMMA lista_ids
             | SEP_SEMICOLON
    '''

def p_lista_objetos(p):
  '''
  lista_objetos : ID listaobjaux
  '''

  print("lista_objetos")
  print(p[1])
  currID.put(p[1])

def p_listaobjetosaux(p):
    '''
    listaobjaux : SEP_COMMA lista_objetos
                | SEP_SEMICOLON
    '''
  ######################################
#FALTAN ARRAYS
  ######################################
def p_decarr(p):
    '''
    decarr : SEP_LBRACKET CTE_INT SEP_RBRACKET auxdec
    '''

def p_auxdec(p):
    '''
    auxdec : SEP_LBRACKET CTE_INT SEP_RBRACKET
           | empty
    '''

def p_acceso_array(p):
    '''
    acceso_array : SEP_LBRACKET hyper_exp SEP_RBRACKET accarraux
    '''

def p_accarraux(p):
  '''
    accarraux : SEP_LBRACKET hyper_exp SEP_RBRACKET
              | empty
    '''

def p_array_inside(p):
    '''
    array_inside : SEP_COMMA CTE_INT insideaux
    '''

def p_insideaux(p):
    '''
    insideaux : SEP_COMMA CTE_INT insideaux
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
    print("valasigaux--- ", p[1])
    currID = p[1]
    print(type(currID))
    if currID in dirVar.dirglobalVar:
      cuads.agregarID(currID)
      print('entra|')
    else:
      raise NameError('Variable no declarada')
      print('Variable', currID, 'no declarada')
    #cuads.agregarID(currID)
    print("pipipipipiop", cuads.pOperandos)
    #  print("AAAAAAAAAAAAAAAAAAAAAAAA")

def p_valasign_aux2(p):
  '''
  valasign_aux2 : asatr
                | acceso_array
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
    asignacion_compleja : ID asatr asignacion_funcion
    '''
##### NO USADA EN ESTA VERSIÓN
def p_asignacion_compleja_aux(p):
    '''
    asignacion_compleja_aux : asignacion_funcion
                            | asignacion_metodo
    '''
####

def p_asignacion_funcion(p):
    '''
    asignacion_funcion : SEP_LPAREN args SEP_RPAREN
    '''

### cambié SEP_LPAREN args SEP_RPAREN por asignacion_funcion
def p_asignacion_metodo(p):
    '''
    asignacion_metodo : OP_DOT ID asignacion_funcion
    '''

def p_args(p):
    '''
    args : hyper_exp argsaux
         | empty
    '''

def p_argsaux(p):
    '''
    argsaux : SEP_COMMA hyper_exp argsaux
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
##### ESTE PRINT DEBERÍA INCLUIR STRINGS como print("hola")
## actualmente lo toma como id al parecer
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
    llamadavoid : ID asatr SEP_LPAREN args SEP_RPAREN SEP_SEMICOLON
    '''

def p_voididt(p):
    '''
    voididt : ID
            | ID OP_DOT ID
    '''

#########################
  
def p_decision(p):
    '''
    decision : IF SEP_LPAREN hyper_exp SEP_RPAREN THEN bloque decisionaux
    '''

def p_decisionaux(p):
    '''
    decisionaux : ELSE bloque
                | empty
    '''

def p_repeticion(p):
    '''
    repeticion : repeticioncondicional
                | repeticionnocondicional
    '''

def p_repeticioncondicional(p):
    '''
    repeticioncondicional : WHILE SEP_LPAREN hyper_exp SEP_RPAREN DO bloque
    '''

def p_repeticionnocondicional(p):
    '''
    repeticionnocondicional : FROM ID OP_ASSIGN valueid TO valueid DO bloque
    '''

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
    cuads.cuadssumsub()
  
def p_expaux(p):
    '''
    expaux : OP_PLUS termino expaux
           | OP_MINUS termino expaux
           | empty
    '''
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
    
def p_termino(p):
    '''
    termino : factor terminoaux
    '''
    cuads.cuadsmuldiv()
  
def p_terminoaux(p):
    '''
    terminoaux : OP_MULT factor terminoaux
               | OP_DIV factor terminoaux
               | empty
    '''
    
    currOperador = p[1]
    cuads.agregarOperador(currOperador)
    print("operador -|-|-|- ", currOperador)
  
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
    cuads.agregarConst(currVal)
    cuads.agregarTipo(currTipo)
    
  #print("SSSSSSSSSSSSSSSSS")
    #print(p[1])

#Factorización por la izq de ID asatr y llamadafuncionmetodo
def p_cteidcall_atributo_metodo(p):
  '''
  cteidcall_atributo_metodo : ID var_id_aux
  '''
  currID = p[1]
  print("prueba ID --- ", currID)
  #currTipo = dirVar.getglobalVariable(currID).tipoVariable()
  print("tipo id --- ", currTipo)
  #cuads.agregarTipo(currTipo)

  if currID in dirVar.dirglobalVar:
    cuads.agregarID(currID)
    print('entra|')
  else:
    raise NameError('Variable no declarada')
    print('Variable', currID, 'no declarada')

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

# asignacion_funcion ---> SEP_LPAREN args SEP_RPAREN
def p_cteidcall_am_aux(p):
  '''
  cteidcall_am_aux : asignacion_funcion
                    | empty
  '''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
  print("Error de parser en!")
  print(p)


#####################################
#funciones
#####################################

def p_functions(p):
    '''
    functions : typefun
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
  global currFuncion
  currFuncion = p[3]
  dirVar.agregarFuncion(currFuncion, currTipo)
  print("dirkun ", dirVar.dirFunciones)
  #AGREGAR VARIABLES LOCALES
  #while not(currTypeID.empty()) :
      #currTypeID.put(currID.get(), currTipo)
  #    tup = currTypeID.get() 
  #    dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1])


def p_voidnext(p):
  '''
  voidnext : SEP_LPAREN paramsfun SEP_RPAREN voidvars
  '''
  

def p_novoidnext(p):
  '''
  novoidnext : SEP_LPAREN paramsfun SEP_RPAREN varsfun SEP_LBRACE estfun nvaux
  '''
  


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
    currID.put(p[2])
    currTypeID.put((currID.get(), currTipo))


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
    currID.put(p[3])
    currTypeID.put((currID.get(), currTipo))

def p_voidvars(p):
    '''
    voidvars : varsfun SEP_LBRACE estfun RETURN SEP_SEMICOLON SEP_RBRACE
    '''

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
      currTypeID.put((currID.get(), currTipo))


def p_idvarsfun(p):
    '''
    idvarsfun : typefunp lista_ids stepidvarsfun varsauxfun
     '''

def p_stepidvarsfun(p):
    '''
    stepidvarsfun : 
    '''
    #print("Empty")
    #print(currID.empty())
    #while not(currID.empty()) :
    #  currTypeID.put((currID.get(), currTipo))
    #agregarlocalVariable(nomFuncion, nomVariable, tipoVariable)
    print("mi id cu", currID)
    global currFuncion
    print(dirVar.dirFunciones)
    print("jejeje- ", currID.get())
    while not(currID.empty()) :
      dirVar.agregarlocalVariable(currFuncion, currID.get(), currTipo)

def p_typefunp(p):
  '''
  typefunp : INT
                 | FLOAT
                 | CHAR
  '''
  print("call typemv")
  global currTipo
  currTipo = p[1]
  #while not(currID.empty()) :
      #currTypeID.put(currID.get(), currTipo)

def p_estfun(p):
    '''
    estfun : estatuto estfun
              | empty
    '''


def p_nvaux(p):
    '''
    nvaux : RETURN SEP_LPAREN hyper_exp SEP_RPAREN SEP_SEMICOLON SEP_RBRACE
    '''

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
    a = (dirVar.getFuncion("helloWorld"))
    print("a - helloWorld()", a.__dict__)
    libro = (dirVar.dirClases["Libro"])
    print(libro.__dict__)
    print("pOperandos\n", cuads.pOperandos)
    print("pTipos\n", cuads.pTipos)
    print("pOperadores\n", cuads.pOperadores)
    print("Correct syntax")
except:
    print(f'Syntax error')
    print("DIRGLOB")
    print(dirVar.dirglobalVar)
    

cuads.printCuads()
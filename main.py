from ply.lex import lex
from ply.yacc import yacc
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

def p_provarsaux(p):
  '''
  provarsaux : vars profunctions
             | profunctions
  '''
def p_profunctions(p):
  '''
  profunctions : functions profunctions
               | principal END
  '''

def p_principal(p):
  '''
  principal : MAIN SEP_LPAREN SEP_RPAREN bloque
  '''

def p_bloque(p):
  '''
  bloque : SEP_LBRACE estatuto bloqueaux
  '''

def p_bloqueaux(p):
  '''
  bloqueaux : estatuto bloqueaux
            | SEP_RBRACE
  '''

def p_clase(p):
    '''
    clase : CLASS ID inheritsaux SEP_LBRACE claseaux
    '''
def p_inheritsaux(p):
    '''
    inheritsaux : OP_LT INHERITS ID OP_GT
    | empty
    '''
def p_claseaux(p):
    '''
    claseaux : ATTRIBUTES OP_LT atributos OP_GT metaux SEP_RBRACE
    '''
def p_atributos(p):
  '''
  atributos : vars
  '''
  
#functions y methods son prácticamente iguales en los diagramas
def p_metaux(p):
    '''
    metaux : METHODS OP_LT metodos OP_GT
    | empty
    '''

################################################
# REVISAR
def p_metodos(p):
    '''
    metodos : funcion_void metodosaux
            | funcion_no_void metodosaux 
    '''
def p_metodosaux(p):
    '''
    metodosaux : funcion_void metodosaux
               | funcion_no_void metodosaux
               | empty
    '''
################################################

def p_functions(p):
    '''
    functions : funcion_void
              | funcion_no_void
    '''

def p_vars(p):
    '''
    vars : VARS varsaux
    '''

def p_varsaux(p):
    '''
    varsaux : type lista_ids varsaux
            | OBJECT ID lista_objetos varsaux
            | empty
     '''

def p_lista_ids(p):
  '''
  lista_ids : ID listaidaux
  '''

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

def p_listaobjetosaux(p):
    '''
    listaobjaux : SEP_COMMA lista_objetos
                | SEP_SEMICOLON
    '''
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
    acceso_array : ID SEP_LBRACKET expresion SEP_RBRACKET accarraux
    '''

def p_accarraux(p):
  '''
    accarraux : SEP_LBRACKET expresion SEP_RBRACKET
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

def p_type(p):
    '''
    type : INT
         | FLOAT
         | CHAR
    '''

def p_params(p):
    '''
    params : type ID paramsaux
           | paramsaux
    '''

def p_paramsaux(p):
    '''
    paramsaux : SEP_COMMA params
              | empty
    '''
################################################ 
# REVISAR LO DE LECTURA
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

def p_valasigaux(p):
    '''
    valasigaux : ID asatr
               | acceso_array
    '''

def p_asign_opciones(p):
  '''
  asign_opciones : asignacion_simple
                | asignacion_funcion
                | asignacion_metodo
  '''

def p_asignacion_simple(p):
  '''
  asignacion_simple : expresion
                   | array_inside
  '''

def p_asatr(p):
    '''
    asatr : OP_DOT ID
         | empty
    '''

def p_asignacion_funcion(p):
    '''
    asignacion_funcion : ID SEP_LPAREN args SEP_RPAREN
    '''

def p_asignacion_metodo(p):
    '''
    asignacion_metodo : ID OP_DOT ID SEP_LPAREN args SEP_RPAREN
    '''

def p_args(p):
    '''
    args : expresion argsaux
         | empty
    '''

def p_argsaux(p):
    '''
    argsaux : SEP_COMMA expresion argsaux
            | empty
    '''

def p_funcion_no_void(p):
    '''
    funcion_no_void : type FUNCTION ID SEP_LPAREN params SEP_RPAREN varsnovoid SEP_LBRACE estnovoid nvaux 
    '''

def p_varsnovoid(p):
    '''
    varsnovoid : vars
               | empty
    '''

################################################
# REVISAR este |empty
################################################
def p_estnovoid(p):
    '''
    estnovoid : estatuto estnvaux
              | empty
    '''

def p_estnvaux(p):
    '''
    estnvaux : estatuto estnvaux
             | empty
    '''

def p_nvaux(p):
    '''
    nvaux : RETURN SEP_LPAREN expresion SEP_RPAREN SEP_SEMICOLON SEP_RBRACE
    '''

def p_funcion_void(p):
    '''
    funcion_void : VOID FUNCTION ID SEP_LPAREN params SEP_RPAREN voidvars
    '''
################################################
# return obligatorio en todas las funciones
def p_voidvars(p):
    '''
    voidvars : vars SEP_LBRACE voidest RETURN SEP_SEMICOLON SEP_RBRACE
             | SEP_LBRACE voidest RETURN SEP_SEMICOLON SEP_RBRACE
    '''

def p_voidest(p):
    '''
    voidest : estatuto voidestaux
            | empty
    '''

def p_voidestaux(p):
    '''
    voidestaux : estatuto voidestaux
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
                 | expresion escaux2
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

def p_llamadavoid(p):
    '''
    llamadavoid : voididt SEP_LPAREN args SEP_RPAREN SEP_SEMICOLON
    '''

def p_voididt(p):
    '''
    voididt : ID
            | ID OP_DOT ID
    '''

def p_decision(p):
    '''
    decision : IF SEP_LPAREN expresion SEP_RPAREN THEN bloque decisionaux
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
    repeticioncondicional : WHILE SEP_LPAREN expresion SEP_RPAREN DO bloque
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

def p_llamadafuncionmetodo(p):
    '''
    llamadafuncionmetodo : funcidt SEP_LPAREN args SEP_RPAREN
    '''

def p_funcidt(p):
    '''
    funcidt : ID
            | ID OP_DOT ID
    '''

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
""" def p_hyper_exp(p):
    '''
    hyper_exp : and_exp hyper_aux
    '''

def p_hyper_aux(p):
    '''
    hyper_aux : REL_OR hyper_exp
              | empty
    '''

def p_and_exp(p):
    '''
    and_exp : expresion andexpaux
    '''
def p_andexpaux(p):
    '''
    andexpaux : REL_AND and_exp
              | empty
    ''' """

def p_expresion(p):
  '''
  expresion : exp expresionaux
  '''
  
def p_expresionaux(p):
  '''
  expresionaux : evaluators exp
               | empty
  ''' 

def p_evaluators(p):
    '''
    evaluators : OP_LT
                | OP_GT
                | OP_EQUAL
                | OP_NOTEQ
    '''

def p_exp(p):
    '''
    exp : termino expaux
    '''

def p_expaux(p):
    '''
    expaux : OP_PLUS termino expaux
           | OP_MINUS termino expaux
           | empty
    '''

def p_termino(p):
    '''
    termino : factor terminoaux
    '''

def p_terminoaux(p):
    '''
    terminoaux : OP_MULT factor terminoaux
               | OP_DIV factor terminoaux
               | empty
    '''

def p_factor(p):
    '''
    factor : SEP_LPAREN expresion SEP_RPAREN
           | sign cteidcall
    '''

def p_sign(p):
    '''
    sign : OP_PLUS
         | OP_MINUS
         | empty
    '''

def p_cteidcall(p):
    '''
    cteidcall : CTE_INT
              | CTE_FLOAT
              | ID typeidf
              | llamadafuncionmetodo
              | acceso_array
    '''

def p_typeidf(p):
    '''
    typeidf : OP_DOT ID 
            | empty
    '''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
  print("Error de parser en!")
  print(p)

import sys
lexer = lex()
parser = yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            archEnt = open(file, 'r')
            text = archEnt.read()
            archEnt.close()
            if parser.parse(text) == "Success":
                print("Compilación exitosa")
        except EOFError:
            print(EOFError)
    else:
        print("No se ingresó el nombre de un archivo")
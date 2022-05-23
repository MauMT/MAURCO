import cuads
import virtualAdd

class variable:
    def __init__(self, tipovar):
        self.tipovar = tipovar
        self.valor = None
        self.direccion = None
    def tipoVariable(self):
        return self.tipovar

    def valorVariable(self):
        return self.valor
    
    def direccionVariable(self):
        return self.direccion

#-----------------------------------------------------------
class funcion:
    def __init__(self, tipoFuncion):
        self.tipoFuncion = tipoFuncion
        self.parameters = []
        self.cantVar = 0
        self.tempcount = 0
        self.direccion = 0
        self.localVar = {}

    def gettipoFuncion(self):
        return self.tipoFuncion
    
    def gettableFuncion(self):
        return self.localVar

#-----------------------------------------------------------
class objeto:
    def __init__(self, tipoObjeto):
        self.tipoObjeto = tipoObjeto
        self.atributos = {}
        self.metodos = {}
    
    def getTipoObjeto(self):
        return self.tipoObjeto

    def getAtributosClase(self):
        return self.atributos
    
    def getMetodosClase(self):
        return self.metodos


#-----------------------------------------------------------
     
def getFuncion(nomFuncion):
    if nomFuncion in dirFunciones:
        return dirFunciones[nomFuncion]
    return None

def getlocalVariable(nomFuncion, nomVariable):
    if nomFuncion in dirFunciones:
        if nomVariable in dirFunciones[nomFuncion].gettableFuncion():
            return dirFunciones[nomFuncion].gettableFuncion()[nomVariable]
        return None
    return None

def getglobalVariable(nomVariable):
    if nomVariable in dirglobalVar:
        return dirglobalVar[nomVariable]
    return None


def agregarFuncion(nomFuncion, tipoFuncion):
  print("dirFunciones actualmente: ", dirFunciones)
  if nomFuncion in dirFunciones:
    print("Error, ya existe")
    raise NameError("Error: la función", nomFuncion,"ya existe")
  else:
    dirFunciones[nomFuncion] = funcion(tipoFuncion)


def agregarlocalVariable(nomFuncion, nomVariable, tipoVariable, isParam):
  if nomFuncion in dirFunciones:
    if nomVariable in dirFunciones[nomFuncion].gettableFuncion():
      print("ya existe esta variable local")
    else:
      if(isParam):
        dirFunciones[nomFuncion].parameters.append(tipoVariable)
      dirFunciones[nomFuncion].gettableFuncion()[nomVariable]= variable(tipoVariable)
      dirFunciones[nomFuncion].cantVar = len(dirFunciones[nomFuncion].gettableFuncion())
  else:
    print("no existe esta funcion")


def initFunction(nomFuncion, dir, cant):
    if nomFuncion in dirFunciones:
        dirFunciones[nomFuncion].direccion = dir
        dirFunciones[nomFuncion].tempcount = cant
    else:
        print("no existe la funcion")

def agregartemp(nomFuncion, cant):
    if nomFuncion in dirFunciones:
        dirFunciones[nomFuncion].cantVar += (cant - dirFunciones[nomFuncion].tempcount)
    else:
        print("no existe la funcion")


def verify(nomFuncion):
    if nomFuncion in dirFunciones:
        return True
    else:
        return False

def getParametersfunc(nomFuncion):
    if nomFuncion in dirFunciones:
        return dirFunciones[nomFuncion].parameters
    else:
        print("no existe la funcion")

#######################################################################################
#FUNCION ELIMINAR TODAS LAS VARIABLES EN SCOPE
#######################################################################################

    

def agregarglobalVariable(nomVariable, tipoVariable):
  if nomVariable in dirglobalVar:
    print("Error ya existe la variable global: ", nomVariable)
    #raise NameError("Error: la variable ", nomVariable," ya existe")
  else:
    dirglobalVar[nomVariable] = variable(tipoVariable)

##checar si usar objeto(), o cambiar objeto() a clase()
def crearClase(nombreClase):
  if nombreClase in dirClases:
    print("Error, esa clase ya existe")
  else:
    dirClases[nombreClase] = objeto(nombreClase)

def getClase(nombreClase):
    if nombreClase in dirClases:
        return dirClases[nombreClase]
    return None

#-----------------------

def agregarAtributosClase(nombreClase, nomVariable, tipoVariable):
  if nombreClase in dirClases:
    if nomVariable in dirClases[nombreClase].getAtributosClase():
      print("ya existe esta variable local")
    else:
      dirClases[nombreClase].getAtributosClase()[nomVariable]= variable(tipoVariable)
  
  else:
    print("no existe esa clase")

def agregarMetodosClase(nombreClase, nomMetodo, tipoRetorno):
  if nombreClase in dirClases:
    if nomMetodo in dirClases[nombreClase].getMetodosClase():
      print("ya existe este método")
    else:
      dirClases[nombreClase].getMetodosClase()[nombreClase] = funcion(tipoRetorno)
  else:
    print("no existe esa clase")

# primero se busca en la tabla de variables de la función actual y luego en la global
# Y si es una constante se busca en la tabla de constantes, y se declara si no está declarada
def agregarDireccionVariable(nombre, direccion):
    if nombre in dirglobalVar:
        dirglobalVar[nombre].direccion = direccion
    else:
        print("no existe la variable")

dirglobalVar = {}
#adentro puede haber objetos de la clase que esten instanciados
#agregarobjeto

dirFunciones = {}
#adentro puede haber objetos de la clase que esten instanciados
#agregarobjeto

dirClases = {}
#dirClases (atributos y metodos)
#Crear clase
#checar si ya existe
#agregar clase

dirConstantes = {}

# {valor: dirección}
# ejemplo {'2.3': 5000, '1': 5001}
def obtener_o_agregar_constante(valor, tipo):
    if valor in dirConstantes:
        return dirConstantes[valor]
    else:
        dirConstantes[valor] = virtualAdd.intOrFloatConstant(tipo)
        return dirConstantes[valor]



'''
agregarFuncion("hola", "int")
agregarFuncion("adios", "float")
agregarFuncion("si", "str")
agregarFuncion("no", "int")
#agregarFuncion("no", "int")
agregarglobalVariable("alex", "int")
agregarglobalVariable("luis", "int")
agregarlocalVariable("hola", "estrella", "float")
agregarlocalVariable("hola","andy", "int")
#agregarlocalVariable("hola","andy", "int")
print(dirFunciones)
print(dirFunciones["hola"].localVar)
print(dir)
'''



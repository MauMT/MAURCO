class variable:
    def __init__(self, tipovar):
        self.tipovar = tipovar
        self.valor = None

    def tipoVariable(self):
        return self.tipovar

    def valorVariable(self):
        return self.valor

#-----------------------------------------------------------
class funcion:
    def __init__(self, tipoFuncion):
        self.tipoFuncion = tipoFuncion
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
    if nomVariable in nomVariable:
        return nomVariable[nomVariable]
    return None


def agregarFuncion(nomFuncion, tipoFuncion):
  if nomFuncion in dirFunciones:
    print("Error, ya existe")
  else:
    dirFunciones[nomFuncion] = funcion(tipoFuncion)

def agregarlocalVariable(nomFuncion, nomVariable, tipoVariable):
  if nomFuncion in dirFunciones:
    if nomVariable in dirFunciones[nomFuncion].gettableFuncion():
      print("ya existe esta variable local")
    else:
      dirFunciones[nomFuncion].gettableFuncion()[nomVariable]= variable(tipoVariable)
  
  else:
    print("no existe esta funcion")
    

def agregarglobalVariable(nomVariable, tipoVariable):
  if nomVariable in dirglobalVar:
    print("Error ya existe esta variable global")
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
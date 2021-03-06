'''
    MÓDULO DE LOS DIRECTORIOS
    Contiene las funciones para manejar el directorio de variables, de funciones,y de constantes
    Es el responsable de búsqueda y escritura de los nombres de funciones, constantes y variables
    en los diccionarios correspondientes.
    Además, contiene la definición de los objetos 'variable' y 'funcion'
    - La máquina virtual en el módulo 'vm' hace uso del directorio de funciones y de constantes que están en este módulo
    - El módulo 'cuads' hace uso de este módulo para agregar variables temporales a los directorios
    
'''

from functools import reduce

class variable:
    def __init__(self, tipovar, length):
        self.tipovar = tipovar
        self.length = length
        self.direccion = None

    def tipoVariable(self):
        return self.tipovar

    def lengthVariable(self):
        return self.length

    def direccionVariable(self):
        return self.direccion
    
    def __str__(self):
        return str(self.tipovar) + " " + str(self.length) + " " + str(self.direccion)

#-----------------------------------------------------------
class funcion:
    def __init__(self, tipoFuncion):
        self.tipoFuncion = tipoFuncion
        self.parameters = []
        self.cuadcount = 0
        self.intcant = 0
        self.floatcant = 0
        self.tempintcant = 10
        self.tempfloatcant = 10
        self.charcant = 0
        self.direccion = 0
        self.localVar = {}

    def gettipoFuncion(self):
        return self.tipoFuncion
    
    def gettableFuncion(self):
        return self.localVar

    def setintcant(self, value):
        self.intcant = value

    def getintcant(self):
        return self.intcant

    def setfloatcant(self, value):
        self.floatcant = value

    def getfloatcant(self):
        return self.floatcant

    def setcharcant(self, value):
        self.floatcant = value

    def getcharcant(self):
        return self.charcant
    
    def gettempintcant(self):
        return self.tempintcant
    
    def gettempfloatcant(self):
        return self.tempfloatcant
    
    def settempintcant(self, value):
        self.tempintcant = value
    
    def settempfloatcant(self, value):
        self.tempfloatcant = value

    

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
  if nomFuncion in dirFunciones:
    print("Error ya existe la función", nomFuncion)
    raise NameError("Error ya existe la función", nomFuncion)
  else:
    dirFunciones[nomFuncion] = funcion(tipoFuncion)


def agregarlocalVariable(nomFuncion, nomVariable, arrLength, tipoVariable, isParam):
  
  if nomFuncion in dirFunciones:
    
    if nomVariable in dirFunciones[nomFuncion].gettableFuncion():
      print("Ya existe la variable local", nomVariable, "en la función", nomFuncion)
      raise NameError("Ya existe la variable local", nomVariable, "en la función", nomFuncion)
    else:
      
      if(isParam):
        dirFunciones[nomFuncion].parameters.append(tipoVariable)
      #es correcta la identacion por param
      if len(arrLength) == 0:
        indsum = 1
      else:
        indsum = reduce(lambda x, y: x * y, arrLength)

      if(tipoVariable == "int"):
        dirFunciones[nomFuncion].setintcant(dirFunciones[nomFuncion].getintcant()+indsum)
      elif(tipoVariable == "float"):
        dirFunciones[nomFuncion].setfloatcant(dirFunciones[nomFuncion].getfloatcant()+indsum)
        #dirFunciones[nomFuncion].floatcant = indsum+floatcant
      elif(tipoVariable == "char"):
        dirFunciones[nomFuncion].setcharcant(dirFunciones[nomFuncion].getcharcant()+indsum)
        #dirFunciones[nomFuncion].charcant = indsum+charcant
      
      dirFunciones[nomFuncion].gettableFuncion()[nomVariable]= variable(tipoVariable, arrLength)
      
      
  else:
    print("no existe esta función")


def getfunctype(nomFuncion):
    if nomFuncion in dirFunciones:
        return dirFunciones[nomFuncion].tipoFuncion
    else:
        print("functype no existe la funcion")

"""
#currID.put(p[1], isMat, isArr, arrLength) Tipo
      dirVar.agregarAtributosClase(currClass,tup[0], tup[1], tup[2], tup[3],tup[4])


tup = currTypeID.get()
#currID.put(p[1], isMat, isArr, arrLength) Tipo, TrueParam
      dirVar.agregarlocalVariable(currFuncion,tup[0], tup[1], tup[2], tup[3], tup[4], tup[5])
"""

def initFunction(nomFuncion, currcuadcounter):
    if nomFuncion in dirFunciones:
        dirFunciones[nomFuncion].cuadcount = currcuadcounter
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
        #print(dirFunciones[nomFuncion].parameters)
        return dirFunciones[nomFuncion].parameters
    else:
        print("no existe la funcion")

#######################################################################################
#FUNCION ELIMINAR TODAS LAS VARIABLES EN SCOPE
#######################################################################################

    

def agregarglobalVariable(nomVariable, arrLength, tipoVariable):
  
  #print(nomVariable)
  if nomVariable in dirglobalVar:
    print("Name Error: Error ya existe la variable global", nomVariable)
    raise NameError("Error ya existe la variable global", nomVariable)
  else:
    #print(tipoVariable)
    #print(nomVariable)
    #print(type(nomVariable))
    #print(arrLength)
    dirglobalVar[nomVariable] = variable(tipoVariable, arrLength)
    #print(arrLength)


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

"""
#currID.put(p[1], isMat, isArr, arrLength) Tipo
      dirVar.agregarAtributosClase(currClass,tup[0], tup[1], tup[2], tup[3],tup[4])
"""

def agregarAtributosClase(nombreClase, nomVariable, arrLength, tipoVariable):
  if nombreClase in dirClases:
    if nomVariable in dirClases[nombreClase].getAtributosClase():
      print("ya existe esta variable local")
    else:
      dirClases[nombreClase].getAtributosClase()[nomVariable]= variable(tipoVariable, arrLength)

  
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


def setLocalVarAddress(func, nombre, dir):
    if func in dirFunciones:
        dirFunciones[func].localVar[nombre].direccion = dir
    else:
        print("no existe la funcion")

def setGlobalVarAddress(nombre, dir):
    if nombre in dirglobalVar:
        dirglobalVar[nombre].direccion = dir
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


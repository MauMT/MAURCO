from cuads import cuads
import dirVar
import virtualAdd

class Memoria:
    def __init__(self):
        self.globalesFloat = []
        self.globalesInt = []
        self.localesFloat = []
        self.localesInt = []
        self.temporalesInt = []
        self.temporalesFloat = []
        self.constantesInt = []
        self.constantesFloat = []
    
    def getGlobalesFloat(self):
        return self.globalesFloat

    def getGlobalesInt(self):
        return self.globalesInt
    
    def getLocalesFloat(self):
        return self.localesFloat

    def getLocalesInt(self):
        return self.localesInt

    def getTemporalesFloat(self):
        return self.temporalesFloat
    
    def getTemporalesInt(self):
        return self.temporalesInt
    
    # mejorar ese print
    def __str__(self):
        aux = "Memoria: \n\tglobalesFloat: " + str(self.globalesFloat)
        aux += "\n\tglobalesInt: " + str(self.globalesInt)
        aux += "\n\tlocalesFloat: " + str(self.localesFloat)
        aux += "\n\tlocalesInt: " + str(self.localesInt)
        aux += "\n\ttemporalesFloat: " + str(self.temporalesFloat)
        aux += "\n\ttemporalesInt: " + str(self.temporalesInt)
        aux += "\n\tconstantesFloat: " + str(self.constantesFloat)
        aux += "\n\tconstantesInt: " + str(self.constantesInt)
        return aux

#-----------------------------------------------------------
#SETTERS PARA NO HACER UN CONSTRUCTOR DE MÚLTIPLES ARGUMENTOS
    def setGlobalesFloatSize(self, size):
        self.globalesFloat = [0] * size
        

    def setGlobalesIntSize(self, size):
        self.globalesInt = [0] * size
        
    
    def setLocalesFloatSize(self, size):
        self.localesFloat = [0] * size
        
    
    def setLocalesIntSize(self, size):
        self.localesInt = [0] * size
        
    
    def setTemporalesFloatSize(self, size):
        self.temporalesFloat = [0] * size
        

    def setTemporalesIntSize(self, size):
        self.temporalesInt = [0] * size
        
    
    def setConstantesIntSize(self, size):
        self.constantesInt = [0] * size
        
    
    def setConstantesFloatSize(self, size):
        self.constantesFloat = [0] * size
        

    #-----------------------------------------------------------

""" print("num casillas int global", virtualAdd.restarDireccionBase(virtualAdd.getCurrentGlobalAddressInt(), 'gi') )
print("num casillas float global", virtualAdd.restarDireccionBase(virtualAdd.getCurrentGlobalAddressFloat(), 'gf') )
print("num casillas constante int", virtualAdd.restarDireccionBase(virtualAdd.getCurrentConstantAddressInt(), 'ci') )
print("num casillas constante float", virtualAdd.restarDireccionBase(virtualAdd.getCurrentConstantAddressFloat(), 'cf') ) """

casillasGlobalInt = virtualAdd.restarDireccionBase(virtualAdd.getCurrentGlobalAddressInt(), 'gi')
casillasGlobalFloat = virtualAdd.restarDireccionBase(virtualAdd.getCurrentGlobalAddressFloat(), 'gf')
casillasConstantInt = virtualAdd.restarDireccionBase(virtualAdd.getCurrentConstantAddressInt(), 'ci')
casillasConstantFloat = virtualAdd.restarDireccionBase(virtualAdd.getCurrentConstantAddressFloat(), 'cf')

x = Memoria()
x.setGlobalesFloatSize(casillasGlobalFloat)
x.setGlobalesIntSize(casillasGlobalInt)
x.setConstantesFloatSize(casillasConstantFloat)
x.setConstantesIntSize(casillasConstantInt)

print(x)

instruction_pointer = 0


#myCuads = [(0, 'GOTO', ' ', ' ', 1), (1, '+', 23000, 23001, 15000), (2, '+', 15000, 23002, 15001), (3, '+', 15001, 23003, 15002), (4, '+', 15002, 23004, 15003), (5, '=', 15003, '', 'x'), (6, '+', 5001, 23004, 15004), (7, '=', 15004, '', 'a'), (8, '+', 23004, 24000, 17000), (9, '*', 5003, 17000, 17001), (10, '=', 17001, '', 'y'), (11, '*', 23005, 23006, 15005), (12, '=', 15005, '', 'z'), (13, '/', 23002, 23004, 17002), (14, '+', 5004, 17002, 17003), (15, '=', 23007, '', 'a'), (16, 'END', ' ', ' ', ' ')]

""" class Cuadruplo:
    def __init__(self, op, operandoIzq, operandoDer, res):
        self.op = op
        self.operandoIzq = operandoIzq
        self.operandoDer = operandoDer
        self.res = res """

print("Num cuadruplos: ", cuads.__len__())

while cuads[instruction_pointer][1] != 'END': 
    
    cuad = cuads[instruction_pointer]
    operacion = cuad[1]
    operandoIzq = cuad[2]
    operandoDer = cuad[3]
    res = cuad[4]

    if operacion == 'GOTO':
        print("GOTO")
        instruction_pointer = res

    elif operacion == '+':
        print("+")
        #Memoria[operandoIzq] = Memoria[operandoIzq] + Memoria[operandoDer]
        instruction_pointer += 1
    
    elif operacion == '-':
        print("-")
        #Memoria[operandoIzq] = Memoria[operandoIzq] - Memoria[operandoDer]
        instruction_pointer += 1
    
    elif operacion == '*':
        print("*")
        #Memoria[operandoIzq] = Memoria[operandoIzq] * Memoria[operandoDer]
        instruction_pointer += 1
    elif operacion == '/':
        print("/")
        #Memoria[operandoIzq] = Memoria[operandoIzq] / Memoria[operandoDer]
        instruction_pointer += 1

    elif operacion == '=':
        print("=")
        #Memoria[res] = Memoria[operandoIzq]
        instruction_pointer += 1
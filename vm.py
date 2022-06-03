from cuads import cuads
from dirVar import dirFunciones
from dirVar import dirConstantes
import virtualAdd


# 0 globales int 5000
# 1 globales float 8000

# 2 locales int 11000
# 3 locales float 13000

# 4 temporales int 15000
# 5 temporales float 17000
MemoriaGlobal = [[],[],[],[],[],[],[],[]]

class MemoriaLocal:
    def __init__(self):
        self.MemoriaLocal = [[],[]]



### STACK DE MEMORIAS ####
memoryStack = []

def getFuncionContext(funcion):
    return dirFunciones[funcion]


### RESTAR VALOR DE LA DIRECCIÓN BASE DEPERENDIENDO EL TIPO Y SCOPE
casillasGlobalInt = virtualAdd.getCurrentGlobalAddressInt() - 5000
casillasGlobalFloat = virtualAdd.getCurrentGlobalAddressFloat() - 8000
casillasTemporalesInt = virtualAdd.getCurrentTempAddressInt() - 15000
casillasTemporalesFloat = virtualAdd.getCurrentTempAddressFloat() - 17000
#-----------------------------------------------------------

MemoriaGlobal[0] = [0] * casillasGlobalInt
MemoriaGlobal[1] = [0] * casillasGlobalFloat

""" MemoriaGlobal[2] = [0] * 
MemoriaGlobal[3] = [0] * """

MemoriaGlobal[4] = [0] * casillasTemporalesInt
MemoriaGlobal[5] = [0] * casillasTemporalesFloat



dictConstantesMemoriaGlobal = dict((v,k) for k,v in dirConstantes.items())
print(dictConstantesMemoriaGlobal)
print("--")
print(MemoriaGlobal)

instruction_pointer = 1

#myCuads = [(0, 'GOTO', ' ', ' ', 1), (1, '+', 23000, 23001, 15000), (2, '+', 15000, 23002, 15001), (3, '+', 15001, 23003, 15002), (4, '+', 15002, 23004, 15003), (5, '=', 15003, '', 'x'), (6, '+', 5001, 23004, 15004), (7, '=', 15004, '', 'a'), (8, '+', 23004, 24000, 17000), (9, '*', 5003, 17000, 17001), (10, '=', 17001, '', 'y'), (11, '*', 23005, 23006, 15005), (12, '=', 15005, '', 'z'), (13, '/', 23002, 23004, 17002), (14, '+', 5004, 17002, 17003), (15, '=', 23007, '', 'a'), (16, 'END', ' ', ' ', ' ')]


print("Num cuadruplos: ", cuads.__len__())

def getTypeScopeByAddress(num):
    '''
    Devuelve un string con el tipo y scope de la variable en la dirección num
    '''
    if num >= 5000 and num < 8000:
        return 'gi'
    elif num >= 8000 and num < 11000:
        return 'gf'
    elif num >= 11000 and num < 13000:
        return 'li'
    elif num >= 13000 and num < 15000:
        return 'lf'
    elif num >= 15000 and num < 17000:
        return 'tgi'
    elif num >= 17000 and num < 19000:
        return 'tgf'
    elif num >= 23000 and num < 24000:
        return 'ci'
    elif num >= 24000 and num < 25000:
        return 'cf'


def getConstant(key):
    return dictConstantesMemoriaGlobal[key]

def readMemory(num):
    aux = getTypeScopeByAddress(num)
    if aux == 'gi':
        return MemoriaGlobal[0][num - 5000]
    elif aux == 'gf':
        return MemoriaGlobal[1][num - 8000]
    elif aux == 'li':
        return MemoriaGlobal[2][num - 11000]
    elif aux == 'lf':
        return MemoriaGlobal[3][num - 13000]
    elif aux == 'tgi':
        return MemoriaGlobal[4][num - 15000]
    elif aux == 'tgf':
        return MemoriaGlobal[5][num - 17000]
    elif aux == 'ci':
        return getConstant(num)
    elif aux == 'cf':
        return getConstant(num)

# 'value' is an actual value that will assigned to 'addr' 
def writeOnMemory(value, addr):
    aux = getTypeScopeByAddress(addr)
    print("aux: ", aux)
    if aux == 'gi':
        MemoriaGlobal[0][addr - 5000] = value
    elif aux == 'gf':
        MemoriaGlobal[1][addr - 8000] = value
    elif aux == 'li':
        MemoriaGlobal[2][addr - 11000] = value
    elif aux == 'lf':
        MemoriaGlobal[3][addr - 13000] = value
    elif aux == 'tgi':
        MemoriaGlobal[4][addr - 15000] = value
    elif aux == 'tgf':
        MemoriaGlobal[5][addr - 17000] = value

def incrementInstructionPointer():
    global instruction_pointer
    instruction_pointer += 1

def printHelper(operador, izq, der, res, newRes):
    print(operador)
    print(izq, operador, der, "en", res)
    print("-- newResult", newRes)



while cuads[instruction_pointer][1] != 'END': 
    
    cuad = cuads[instruction_pointer]
    operacion = cuad[1]
    operandoIzq = cuad[2]
    operandoDer = cuad[3]
    res = cuad[4]

    if operacion == 'GOTO':
        print("GOTO")
        incrementInstructionPointer()

    elif operacion == '+':
        newResult = readMemory(operandoIzq) + readMemory(operandoDer)
        printHelper('+', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()
    
    elif operacion == '-':
        newResult = readMemory(operandoIzq) - readMemory(operandoDer)
        printHelper('-', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()
    
    elif operacion == '*':
        print("*")
        print(operandoIzq, '*', operandoDer, "en", res)
        newResult = readMemory(operandoIzq) * readMemory(operandoDer)
        print("-- newResult", newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '/':
        print("/")
        print(operandoIzq, '/', operandoDer, "en", res)
        newResult = readMemory(operandoIzq) / readMemory(operandoDer)
        print("-- newResult", newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '<':
        print("<")
        print(operandoIzq, '<', operandoDer, "en", res)
        newResult = readMemory(operandoIzq) < readMemory(operandoDer)
        print("-- newResult", newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '>':
        print(">")
        print(operandoIzq, '>', operandoDer, "en", res)
        newResult = readMemory(operandoIzq) > readMemory(operandoDer)
        print("-- newResult", newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '!=':
        print("!=")
        print(operandoIzq, '!=', operandoDer, "en", res)
        newResult = readMemory(operandoIzq) != readMemory(operandoDer)
        print("-- newResult", newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '&':
        print("&")
        incrementInstructionPointer()

    elif operacion == '|':
        print("|")
        incrementInstructionPointer()

    elif operacion == 'INPUT':
        print("INPUT")
        incrementInstructionPointer()

    elif operacion == '=':
        print("=")
        print("operandoIzq: ", operandoIzq)
        print("res: ", res)
        writeOnMemory(readMemory(operandoIzq), res)
        incrementInstructionPointer()

    elif operacion == 'VER':
        print("VER")
        incrementInstructionPointer()

    elif operacion == 'GOTOF':
        print("GOTOF")
        incrementInstructionPointer()

    elif operacion == 'PRINT':
        print("PRINT")
        print(readMemory(res))
        incrementInstructionPointer()
    
    elif operacion == 'ERA':
        print("ERA")
        incrementInstructionPointer()
    
    elif operacion == 'PARAM':
        print("PARAM")
        incrementInstructionPointer()
    
    elif operacion == 'GOSUB':
        print("GOSUB")
        incrementInstructionPointer()
    
    elif operacion == 'RETURN':
        print("RETURN")
        incrementInstructionPointer()
    
    elif operacion == 'ENDFUNC':
        print("ENDFUNC")
        incrementInstructionPointer()
    

    
    
print(MemoriaGlobal)

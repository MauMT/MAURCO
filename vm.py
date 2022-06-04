from cuads import cuads
from dirVar import dirFunciones
from dirVar import dirConstantes
import virtualAdd

from virtualAdd import GLOBAL_INT_START, GLOBAL_FLOAT_START, LOCAL_INT_START, LOCAL_FLOAT_START, TEMPORAL_INT_START, TEMPORAL_FLOAT_START, CONSTANT_INT_START, CONSTANT_FLOAT_START

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
casillasGlobalInt = virtualAdd.getCurrentGlobalAddressInt() - virtualAdd.GLOBAL_INT_START
casillasGlobalFloat = virtualAdd.getCurrentGlobalAddressFloat() - virtualAdd.GLOBAL_FLOAT_START
casillasTemporalesInt = virtualAdd.getCurrentTempAddressInt() - virtualAdd.TEMPORAL_INT_START
casillasTemporalesFloat = virtualAdd.getCurrentTempAddressFloat() - virtualAdd.TEMPORAL_FLOAT_START
#-----------------------------------------------------------

MemoriaGlobal[0] = [0] * casillasGlobalInt
MemoriaGlobal[1] = [0] * casillasGlobalFloat

""" MemoriaGlobal[2] = [0] * 
MemoriaGlobal[3] = [0] * """

MemoriaGlobal[4] = [0] * casillasTemporalesInt
MemoriaGlobal[5] = [0] * casillasTemporalesFloat



dictConstantesMemoriaGlobal = dict((v,k) for k,v in dirConstantes.items())

print(MemoriaGlobal)

instruction_pointer = 1


print("Num cuadruplos: ", cuads.__len__())
print("-----------------------------------------------------")
def getTypeScopeByAddress(num):
    '''
    Devuelve un string con el tipo y scope de la variable en la dirección num
    '''
    if num >= GLOBAL_INT_START and num < GLOBAL_FLOAT_START:
        return 'gi'
    elif num >= GLOBAL_FLOAT_START and num < LOCAL_INT_START:
        return 'gf'
    elif num >= LOCAL_INT_START and num < LOCAL_FLOAT_START:
        return 'li'
    elif num >= LOCAL_FLOAT_START and num < TEMPORAL_INT_START:
        return 'lf'
    elif num >= TEMPORAL_INT_START and num < TEMPORAL_FLOAT_START:
        return 'tgi'
    elif num >= TEMPORAL_FLOAT_START and num < 19000:
        return 'tgf'
    elif num >= CONSTANT_INT_START and num < CONSTANT_FLOAT_START:
        return 'ci'
    elif num >= CONSTANT_FLOAT_START and num < 25000:
        return 'cf'


def getConstant(key):
    return dictConstantesMemoriaGlobal[key]

def readMemory(num):
    aux = getTypeScopeByAddress(num)
    if aux == 'gi':
        return MemoriaGlobal[0][num - GLOBAL_INT_START]
    elif aux == 'gf':
        return MemoriaGlobal[1][num - GLOBAL_FLOAT_START]
    elif aux == 'li':
        return MemoriaGlobal[2][num - LOCAL_INT_START]
    elif aux == 'lf':
        return MemoriaGlobal[3][num - LOCAL_FLOATT_START]
    elif aux == 'tgi':
        return MemoriaGlobal[4][num - TEMPORAL_INT_START]
    elif aux == 'tgf':
        return MemoriaGlobal[5][num - TEMPORAL_FLOAT_START]
    elif aux == 'ci':
        return getConstant(num)
    elif aux == 'cf':
        return getConstant(num)

# 'value' is an actual value that will assigned to 'addr' 
def writeOnMemory(value, addr):
    aux = getTypeScopeByAddress(addr)
    if aux == 'gi':
        MemoriaGlobal[0][addr - GLOBAL_INT_START] = value
    elif aux == 'gf':
        MemoriaGlobal[1][addr - GLOBAL_FLOAT_START] = value
    elif aux == 'li':
        MemoriaGlobal[2][addr - LOCAL_INT_START] = value
    elif aux == 'lf':
        MemoriaGlobal[3][addr - LOCAL_FLOATT_START] = value
    elif aux == 'tgi':
        MemoriaGlobal[4][addr - TEMPORAL_INT_START] = value
    elif aux == 'tgf':
        MemoriaGlobal[5][addr - TEMPORAL_FLOAT_START] = value

def isTemporalAddress(addr):
    return is_between(TEMPORAL_INT_START, addr, 19000)

def incrementInstructionPointer():
    global instruction_pointer
    instruction_pointer += 1

def printHelper(operador, izq, der, res, newRes):
    print(operador)
    print(izq, operador, der, "en", res)
    print("-- newResult", newRes)

def boolean_to_num(val):
    if val:
        return 1
    else:
        return 0

def getTypeByAddres(addr):
    if (addr >= GLOBAL_INT_START and addr < GLOBAL_FLOAT_START) or (addr >= TEMPORAL_INT_START and addr < TEMPORAL_FLOAT_START) or (addr >= LOCAL_INT_START and addr < LOCAL_FLOATT_START):
        return 'int'
    elif (addr >= GLOBAL_FLOAT_START and addr < LOCAL_INT_START) or (addr >= LOCAL_FLOAT_START and addr < TEMPORAL_INT_START) or (addr >= TEMPORAL_FLOAT_START and addr < CONSTANT_INT_START):
        return 'float'

def is_between(x, y, z):
    return x <= y <= z

inside_array_flag = False

while cuads[instruction_pointer][1] != 'END': 
    
    cuad = cuads[instruction_pointer]
    operacion = cuad[1]
    operandoIzq = cuad[2]
    operandoDer = cuad[3]
    res = cuad[4]
    
    if operacion == 'GOTO':
        print("GOTO")
        #incrementInstructionPointer()
        instruction_pointer = int(res)
    elif operacion == '+':
        newResult = readMemory(operandoIzq) + readMemory(operandoDer)
        #printHelper('+', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()
    
    elif operacion == '-':
        newResult = readMemory(operandoIzq) - readMemory(operandoDer)
        #printHelper('-', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()
    
    elif operacion == '*':
        newResult = readMemory(operandoIzq) * readMemory(operandoDer)
        #printHelper('*', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '/':
        newResult = readMemory(operandoIzq) / readMemory(operandoDer)
        #printHelper('/', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '<':
        newResult = readMemory(operandoIzq) < readMemory(operandoDer)
        #printHelper('<', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == '>':
        newResult = readMemory(operandoIzq) > readMemory(operandoDer)
        #printHelper('>', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == '!=':
        newResult = readMemory(operandoIzq) != readMemory(operandoDer)
        #printHelper('!=', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == '&':
        newResult = readMemory(operandoIzq) and readMemory(operandoDer)
        #printHelper('&', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == '|':
        newResult = readMemory(operandoIzq) or readMemory(operandoDer)
        printHelper('|', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == 'INPUT':
        tipo = getTypeByAddres(res)

        if tipo == 'int':
            newResult = int(input())
        elif tipo == 'float':
            newResult = float(input())
            
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '=':
        """ print("=")
        print("operandoIzq: ", operandoIzq)
        print("res: ", res) """
        if inside_array_flag:
            writeOnMemory(readMemory(operandoIzq), readMemory(res))
        else:
            writeOnMemory(readMemory(operandoIzq), res)
        incrementInstructionPointer()

    elif operacion == 'VER':
        print("VER")
        
        if is_between(readMemory(operandoDer), readMemory(operandoIzq), readMemory(res)):
            incrementInstructionPointer()
            inside_array_flag = True
        else:
            raise IndexError("Index out of range")

    elif operacion == 'GOTOF':
        if readMemory(operandoIzq) == 0:
            instruction_pointer = int(res)
        else:
            incrementInstructionPointer()

    elif operacion == 'PRINT':
        if isTemporalAddress(res):
            print(readMemory(readMemory(res)))
        else:
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
    

print("-----------------------------------------------------")
print(MemoriaGlobal)

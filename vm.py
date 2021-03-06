'''
    MÓDULO DE LA MÁQUINA VIRTUAL
    Contiene la memoria global y el stack de memorias locales
    Lee los cuádruplos y ejecuta las operaciones indicadas y necesarias
    para manejo de valores en la memoria
    - Lee las losta de cuádruplos del módulo 'cuads'
    -  Importa el directiorio de funciones y constantes de 'dirVar'
    - Hace uso dela función is_string quer verifica si un argumento es un string o una dirección
    - Hace uso de las contantes de 'virtualAdd' que indican los inicios de memoria por cada tipo y scope
'''

from cuads import cuads
from dirVar import dirFunciones, dirConstantes
import virtualAdd
from constantTypeCheck import is_string
from virtualAdd import GLOBAL_INT_START, GLOBAL_FLOAT_START, LOCAL_INT_START, LOCAL_FLOAT_START, TEMPORAL_INT_START, TEMPORAL_FLOAT_START, CONSTANT_INT_START, CONSTANT_FLOAT_START, TEMPORAL_POINTER_START

# 0 globales int 5000
# 1 globales float 8000

# 2 locales int 11000
# 3 locales float 13000

# 4 temporales int 15000
# 5 temporales float 17000

MemoriaGlobal = [[],[],[],[],[],[],[]]


### crear direcciones para el char
casillasGlobalInt = virtualAdd.getCurrentGlobalAddressInt() - virtualAdd.GLOBAL_INT_START
casillasGlobalFloat = virtualAdd.getCurrentGlobalAddressFloat() - virtualAdd.GLOBAL_FLOAT_START

casillasTemporalesInt = virtualAdd.getCurrentTempAddressInt() - virtualAdd.TEMPORAL_INT_START
casillasTemporalesFloat = virtualAdd.getCurrentTempAddressFloat() - virtualAdd.TEMPORAL_FLOAT_START
casillasTemporalesPointer = virtualAdd.getCurrentTempPointer() - virtualAdd.TEMPORAL_POINTER_START
#-----------------------------------------------------------

MemoriaGlobal[0] = [0] * casillasGlobalInt
MemoriaGlobal[1] = [0] * casillasGlobalFloat


MemoriaGlobal[4] = [0] * casillasTemporalesInt
MemoriaGlobal[5] = [0] * casillasTemporalesFloat
MemoriaGlobal[6] = [0] * casillasTemporalesPointer


# Se revierten las keys y values del diccionario para obtener un valor a partir de una dirección de memoria
dictConstantesMemoriaGlobal = dict((v,k) for k,v in dirConstantes.items())

# Stack de memorias locales usado en la recursividad
memoryStack = []
memoriaLocal = [[], []]

instruction_pointer = 0


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
    elif num >= TEMPORAL_POINTER_START and num < 70000:
        return 'tp'


def getConstant(key):
    return dictConstantesMemoriaGlobal[key]

def readMemory(num):
    aux = getTypeScopeByAddress(num)
    
    if aux == 'gi':
        return MemoriaGlobal[0][num - GLOBAL_INT_START]
    elif aux == 'gf':
        return MemoriaGlobal[1][num - GLOBAL_FLOAT_START]
    elif aux == 'li':
        if memoryStack:
            return memoryStack[-1][0][num - LOCAL_INT_START]
    elif aux == 'lf':
        if memoryStack:
            return memoryStack[-1][1][num - LOCAL_FLOAT_START]
    elif aux == 'tgi':
        return MemoriaGlobal[4][num - TEMPORAL_INT_START]
    elif aux == 'tgf':
        return MemoriaGlobal[5][num - TEMPORAL_FLOAT_START]
    elif aux == 'ci':
        return getConstant(num)
    elif aux == 'cf':
        return getConstant(num)
    elif aux == 'tp':
        return MemoriaGlobal[6][num - TEMPORAL_POINTER_START]

# 'value' is an actual value that will assigned to 'addr' 
def writeOnMemory(value, addr):
    
    aux = getTypeScopeByAddress(addr)
    if aux == 'gi':
        MemoriaGlobal[0][addr - GLOBAL_INT_START] = value
    elif aux == 'gf':
        MemoriaGlobal[1][addr - GLOBAL_FLOAT_START] = value
    elif aux == 'li':
        if memoryStack:
            memoryStack[-1][0][addr - LOCAL_INT_START] = value
    elif aux == 'lf':
        if memoryStack:
            memoryStack[-1][1][addr - LOCAL_FLOAT_START] = value
    elif aux == 'tgi':
        MemoriaGlobal[4][addr - TEMPORAL_INT_START] = value
    elif aux == 'tgf':
        MemoriaGlobal[5][addr - TEMPORAL_FLOAT_START] = value
    elif aux == 'tp':
        MemoriaGlobal[6][addr - TEMPORAL_POINTER_START] = value

def isTemporalAddress(addr):
    return is_between(TEMPORAL_POINTER_START, addr, 70000)

def incrementInstructionPointer():
    global instruction_pointer
    cuad = cuads[instruction_pointer]
    operacion = cuad[1]
    operandoIzq = cuad[2]
    operandoDer = cuad[3]
    res = cuad[4]
    #print(operacion, operandoIzq, operandoDer, "en", res)
    instruction_pointer += 1


def printHelper(operador, izq, der, res, newRes):
    print("********************************************************")
    print(operador)
    print(izq, operador, der, "en", res)
    print("-- newResult", newRes)
    print("********************************************************")

def boolean_to_num(val):
    if val:
        return 1
    else:
        return 0

def getTypeByAddress(addr):
    if (addr >= GLOBAL_INT_START and addr < GLOBAL_FLOAT_START) or (addr >= TEMPORAL_INT_START and addr < TEMPORAL_FLOAT_START) or (addr >= LOCAL_INT_START and addr < LOCAL_FLOAT_START) or (addr >= CONSTANT_INT_START and addr < CONSTANT_FLOAT_START):
        return 'int'
    elif (addr >= GLOBAL_FLOAT_START and addr < LOCAL_INT_START) or (addr >= LOCAL_FLOAT_START and addr < TEMPORAL_INT_START) or (addr >= TEMPORAL_FLOAT_START and addr < CONSTANT_INT_START) or (addr >= CONSTANT_FLOAT_START and addr < 25000):
        return 'float'
    else:
        return 'erro'

def is_between(x, y, z):
    return x <= y <= z

inside_array_flag = False

#cuads[instruction_pointer][1] != 'END'
pFunciones = []
pPointersFuncion = []

while cuads[instruction_pointer][1] != 'END': 
    paramCounter = 0
    cuad = cuads[instruction_pointer]
    operacion = cuad[1]
    operandoIzq = cuad[2]
    operandoDer = cuad[3]
    res = cuad[4]
    
    
    if operacion == 'GOTO':
        instruction_pointer = int(res)

    elif operacion == '+':
        newResult = readMemory(operandoIzq) + readMemory(operandoDer)
        
        #printHelper('+', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        #print(readMemory(res))
        incrementInstructionPointer()
    
    elif operacion == '-':
        newResult = readMemory(operandoIzq) - readMemory(operandoDer)
        #printHelper('-', operandoIzq, operandoDer, res, newResult)
        #print("hola", readMemory(operandoIzq))
        writeOnMemory(newResult, res)
        incrementInstructionPointer()
    
    elif operacion == '*':
        newResult = readMemory(operandoIzq) * readMemory(operandoDer)
        #printHelper('*', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '/':
        if readMemory(operandoDer) == 0:
            print("Value Error: Division by zero")
            exit()
        newResult = readMemory(operandoIzq) / readMemory(operandoDer)
        #printHelper('/', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '<':
        if operandoDer >= 69000 and operandoIzq >= 69000:
            operandoDer = readMemory(operandoDer)
            operandoIzq = readMemory(operandoIzq)
        elif operandoIzq >= 69000:
            operandoIzq = readMemory(operandoIzq)
        elif operandoDer >= 69000:
            operandoDer = readMemory(operandoDer) 

        newResult = readMemory(operandoIzq) < readMemory(operandoDer)
        #printHelper('<', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == '>':
        if operandoDer >= 69000 and operandoIzq >= 69000:
            operandoDer = readMemory(operandoDer)
            operandoIzq = readMemory(operandoIzq)
        elif operandoIzq >= 69000:
            operandoIzq = readMemory(operandoIzq)
        elif operandoDer >= 69000:
            operandoDer = readMemory(operandoDer) 
        
        
        newResult = readMemory(operandoIzq) > readMemory(operandoDer)
        #printHelper('>', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()


    elif operacion == '==':
        
        if operandoDer >= 69000 and operandoIzq >= 69000:
            operandoDer = readMemory(operandoDer)
            operandoIzq = readMemory(operandoIzq)
        elif operandoIzq >= 69000:
            operandoIzq = readMemory(operandoIzq)
        elif operandoDer >= 69000:
            operandoDer = readMemory(operandoDer) 
        
        newResult = readMemory(operandoIzq) == readMemory(operandoDer)
        #printHelper('==', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == '!=':
        
        if operandoDer >= 69000 and operandoIzq >= 69000:
            operandoDer = readMemory(operandoDer)
            operandoIzq = readMemory(operandoIzq)
        elif operandoIzq >= 69000:
            operandoIzq = readMemory(operandoIzq)
        elif operandoDer >= 69000:
            operandoDer = readMemory(operandoDer) 
            
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
        #printHelper('|', operandoIzq, operandoDer, res, newResult)
        writeOnMemory(value=boolean_to_num(newResult), addr=res)
        incrementInstructionPointer()

    elif operacion == 'INPUT':
        tipo = getTypeByAddress(res)

        if tipo == 'int':
            try:
                newResult = int(input())
            except ValueError:
                print('Input Error: El valor ingresado no es asignable a esa variable')
                exit()
            
        elif tipo == 'float':
            try:
                newResult = float(input())
            except ValueError:
                print('Input Error: El valor ingresado no es asignable a esa variable')
                exit()
        
        
            
        writeOnMemory(newResult, res)
        incrementInstructionPointer()

    elif operacion == '=':

        if res >= 69000 and operandoIzq >= 69000:
            writeOnMemory(readMemory(readMemory(operandoIzq)), readMemory(res))
        elif operandoIzq >= 69000:
            writeOnMemory(readMemory(readMemory(operandoIzq)), res)  
        elif res >= 69000:
            writeOnMemory(readMemory(operandoIzq), readMemory(res))  
        else:
            writeOnMemory(readMemory(operandoIzq), res)

        incrementInstructionPointer()

    elif operacion == 'VER':
        
        if is_between(readMemory(operandoDer), readMemory(operandoIzq), readMemory(res)):
            incrementInstructionPointer()
            
        else:
            print("Index Error: '{}' no se encuentra entre '{}' y '{}'".format(readMemory(operandoIzq), readMemory(operandoDer), readMemory(res)))
            raise IndexError("Index out of range")
            

    elif operacion == 'GOTOF':
        if readMemory(operandoIzq) == 0:
            instruction_pointer = int(res)
        else:
            incrementInstructionPointer()

    elif operacion == 'PRINT':
        
        if is_string(res):
            print(res)
        else:
            if isTemporalAddress(res):
                print(readMemory(readMemory(res)))
            else:
                print(readMemory(res))
        incrementInstructionPointer()
    
    elif operacion == 'ERA':
        #print("ERA")
        cantIntLocales = dirFunciones[operandoIzq].intcant
        cantFloatLocales = dirFunciones[operandoIzq].floatcant
        cantTempIntLocales = dirFunciones[operandoIzq].tempintcant
        cantTempFloatLocales = dirFunciones[operandoIzq].tempfloatcant
        pFunciones.append(operandoIzq)
        
        memoriaLocal[0] = [0]*cantIntLocales
        memoriaLocal[1] = [0]*cantFloatLocales
        """ memoriaLocal[2] = [0]*cantTempIntLocales
        memoriaLocal[3] = [0]*cantTempFloatLocales """
        #memoryStack.append(x)
        
        incrementInstructionPointer()
    
    elif operacion == 'PARAM':
        #print("PARAM")
        #print("tatata", readMemory(operandoIzq))
        tipo = getTypeByAddress(operandoIzq)
        #print("operandoIzq:", operandoIzq, "tipo:", tipo)
        #print(memoryStack)
        #print("read memory --", readMemory(operandoIzq))
        
        if memoryStack:
            if tipo == 'int':
                #print("read memory", readMemory(operandoIzq))
                memoriaLocal[0][res-1] = readMemory(operandoIzq)
            elif tipo == 'float':
                memoriaLocal[1][res-1] = readMemory(operandoIzq) 
        else:
            if tipo == 'int':
                #print("read memory", readMemory(operandoIzq))
                memoriaLocal[0][res-1] = readMemory(operandoIzq)
            elif tipo == 'float':
                memoriaLocal[1][res-1] = readMemory(operandoIzq)     
        #print("mem actual ---", memoryStack[-1].MemoriaLocal)
        incrementInstructionPointer()
    
    elif operacion == 'GOSUB':
        #print("GOSUB")
        # se mete el pointer hacia el sig cuadruplo en una pila para saber a dónde regresar al terminar de ejecutar la función
        #print("GOSUB", operandoIzq)
        memoryStack.append(memoriaLocal.copy())
        pPointersFuncion.append(instruction_pointer+1)
        instruction_pointer = dirFunciones[operandoIzq].cuadcount
        # incrementInstructionPointer()
    
    elif operacion == 'RETURN':
        #print("RETURN")
        funcActual = pFunciones[-1]
        #print(res, readMemory(res))
        dirFuncionActual = dirFunciones[funcActual].direccion
        writeOnMemory(readMemory(res), dirFuncionActual)
        incrementInstructionPointer()
    
    elif operacion == 'ENDFUNC':
        #print("ENDFUNC")
        #pop de una emptu list menso
        #print("endfunc pPointers", pPointersFuncion)
        memoryStack.pop()
        pFunciones.pop()
        instruction_pointer = pPointersFuncion.pop()
        


from cuads import cuads
import dirVar

class Memoria:
    def __init__(self, size):
        
        self.lst = [0]*size
        self.size = size
    
    def getLst(self):
        return self.lst
    
    def getSize(self):
        return self.size

x = Memoria(size=10)
print(x.getLst())

print("Directorio de constantes:")
print(dirVar.dirConstantes)

print("Directorio de variables globales:")
print(dirVar.dirglobalVar)

instruction_pointer = 0


myCuads = [(0, 'GOTO', ' ', ' ', 1), (1, '+', 23000, 23001, 15000), (2, '+', 15000, 23002, 15001), (3, '+', 15001, 23003, 15002), (4, '+', 15002, 23004, 15003), (5, '=', 15003, '', 'x'), (6, '+', 5001, 23004, 15004), (7, '=', 15004, '', 'a'), (8, '+', 23004, 24000, 17000), (9, '*', 5003, 17000, 17001), (10, '=', 17001, '', 'y'), (11, '*', 23005, 23006, 15005), (12, '=', 15005, '', 'z'), (13, '/', 23002, 23004, 17002), (14, '+', 5004, 17002, 17003), (15, '=', 23007, '', 'a'), (16, 'END', ' ', ' ', ' ')]

class Cuadruplo:
    def __init__(self, op, operandoIzq, operandoDer, res):
        self.op = op
        self.operandoIzq = operandoIzq
        self.operandoDer = operandoDer
        self.res = res

print("Num cuadruplos: ", myCuads.__len__())

while myCuads[instruction_pointer][1] != 'END': 
    
    cuad = myCuads[instruction_pointer]
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
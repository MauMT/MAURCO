'''
    MÓDULO DE LECTURA DE ARCHIVOS
    Es el encargado de recibir el nombre del archivo que se ejecutará
    Usa el módulo 'main' para ejecutar el archivo
    Posee una flag que indica si se desea que se impriman los cuadruplos o no
'''
import sys
from main import run


if __name__ == '__main__':

    if len(sys.argv) == 2:
        file = sys.argv[1]
        try:
            run(file, False)
        except EOFError:
            print(EOFError)
    elif len(sys.argv) == 3:
        file = sys.argv[1]
        flag = sys.argv[2]
        
        try:
            run(file, flag)
        except EOFError:
            print(EOFError)

    else:
        print("Número incorrecto de argumentos") 
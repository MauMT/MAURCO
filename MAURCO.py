################ 
# File Reader, checar posible futura implementación para lectura de archivos
################
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
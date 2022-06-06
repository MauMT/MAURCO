################ 
# File Reader, checar posible futura implementación para lectura de archivos
################
import sys
from main import run


if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            run(file)
        except EOFError:
            print(EOFError)
    else:
        print("No se ingresó el nombre de un archivo") 
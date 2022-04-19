# MAURCO
Final project for Compiler Design 

### Primer avance
---
Esta entrega consiste un lexer y parser hecho usando PLY (Python lex() y yacc()).
- Ejecución del programa:
``` 
python main.py ejemplo.txt
```


### Features
---
- Declaración de clases, variables locales y globales y funciones.
- Estatutos de lectura, escritura, asignación, decisión y repetición.
- Tres tipos básicos (char, int y float), arreglos de los tipos y objetos basados en los tipos. 

### Requerimientos
---
- Python 3.6 o superior
- PLY 4.0: [Repositorio de PLY](https://github.com/dabeaz/ply)

### Bugs conocidos
---
- La asignación con variables seguidas no funciona sin paréntesis:\
❌ x = y + 1\
✅ x = (y + 1)
- No funciona la instanciación de los objetos
- Los methods de un objeto no pueden ser de un tipo diferente a void 
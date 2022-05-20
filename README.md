# MAURCO
## Proyecto final para la clase de Diseño de Compiladores

### Primer avance

Esta entrega consiste un lexer y parser hecho usando PLY (Python lex() y yacc()).
- Declaración de clases, variables locales y globales y funciones.
- Estatutos de lectura, escritura, asignación, decisión y repetición.
- Tres tipos básicos (char, int y float), arreglos de los tipos y objetos basados en los tipos. 

- Ejecución del programa:
``` 
python main.py ejemplo.txt
```
---
### Segundo avance

- Correción de conflictos en la sintaxis
- creación de directorio de variables(globales y locales), funciones y clases

---
### Tercer avance
- Generación de cuádruplos para expresiones lineales

---
### Cuarto avance
- Generación de cuádruplos para expresiones no lineales: _while_, _if-else_ y _from-to_

---
### Quinto avance
- Validación semántica de existencia de variables
- Impresión de cuádruplos formateadas y con número

---
### Requerimientos
- Python 3.6 o superior
- PLY 4.0: [Repositorio de PLY](https://github.com/dabeaz/ply)

---
### Bugs conocidos
- El directorio de funciones sale vacío después de la regla
- Aún no se reconocen variables locales de las funciones o clases
- No funciona aún la obtención de atributos o métodos como variables, solamente se leen IDs  
- ~~Los methods de un objeto no pueden ser de un tipo diferente a void~~ _En corrección_
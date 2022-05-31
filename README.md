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

### Avance siete
- Se agregaron Funciones, arreglos y matrices

---
### Requerimientos
- Python 3.6 o superior
- PLY 4.0: [Repositorio de PLY](https://github.com/dabeaz/ply)

---
### Bugs conocidos
- La asignación, que es asociativa por derecha genera cuádruplos en orden erróneo
- No funciona aún la obtención de atributos o métodos como variables, solamente se leen IDs  
- ~~Los methods de un objeto no pueden ser de un tipo diferente a void~~ _En corrección_

### Pendientes
Tabla de variables (metodos)
9   ################################## 	

Tipos aritmeticos con memoria
1  ################################ Importante

Maquina virtual
7 ################################ Despues de memoria

version de documentacion
8   ################################ Despues de maquina virtual

- type mismatch (no a fuerzas) ints
3  ##################################

- return statement
5  #################################Funciones valor global

- arreglar count de goto
4  #################################Contadores erroneos

- asignar direcciones virtuales locales y globales
2  #################################tipos primero y hay pedos

- asociativdad izquierda con el mismo operador
6  ##################################no tan importante
# MAURCO
## Proyecto final para la clase de Diseño de Compiladores
<br></br>
### Primer avance
---
Esta entrega consiste un lexer y parser hecho usando PLY (Python lex() y yacc()).
- Declaración de clases, variables locales y globales y funciones.
- Estatutos de lectura, escritura, asignación, decisión y repetición.
- Tres tipos básicos (char, int y float), arreglos de los tipos y objetos basados en los tipos. 

- Ejecución del programa:
``` 
python main.py ejemplo.txt
```

### Segundo avance
---
- Correción de conflictos en la sintaxis
- creación de directorio de variables(globales y locales), funciones y clases

### Tercer avance
---
- Generación de cuádruplos para expresiones lineales

### Requerimientos
---
- Python 3.6 o superior
- PLY 4.0: [Repositorio de PLY](https://github.com/dabeaz/ply)

### Bugs conocidos
---
- Existe un warning de shift-reduce en la regla para las funciones
- ~~Los methods de un objeto no pueden ser de un tipo diferente a void~~ En correción
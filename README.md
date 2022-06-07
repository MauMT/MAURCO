# MAURCO
## Proyecto final para la clase de Diseño de Compiladores

### Program execution:
``` 
python MAURCO.py ejemplo.m
```
### Program execution with ```flag```:
Program can be executed using a third argument ```flag```. If ```flag``` is 1, then the quadruples will be shown before program execution.

Any other valor in the ```flag``` argument won't print quadruples and a number of arguments different from 2 or 3 will raise an error.
```
python MAURCO.py ejemplo.m 1
```

---
### Requirements
- Python 3.6 or higher
- PLY 4.0: [PLY repository](https://github.com/dabeaz/ply)

## Quick Reference Manual
---
Maurco compiles in a linear fashion, so everything that will be used must be declared before using it in the next order: program name, global variables, functions, local variables for the functions and finally the main module and its end. Some parts can be empty but they must have the keyword in order to work.

## Steps for for compiling and running a MAURCO file:
---
1. Add a file.m to the Testing files directory.
2. Open a terminal
3. Run ```python MAURCO file.m```
4. The terminal will run the ```file.m``` and if the syntax is correct it will be executed and the generated quadruples will be shown.

## Initial declarations:
---
All programs must have the keyword “program” and a name that represents the program (ID) and a semicolon after it.
```
program Ejemplo;
```
Global variable declaration must have first the keyword “vars” then “{“ and at the end “}”.
Global variable declaration is optional and it can also be empty.

```
vars{ ... }
```

Functions declaration also must have keywords first should be the type of function that is declared ```int```, ```float```, ```char``` or ```void``` then the keyword ```func``` and then the ID followed by '```(```' then the parameters (in the next section) and '```)```'.

Example:

```
void func helloWorld(params)
```

Local variables must be declared with the keyword ```vars``` followed by any quantity of variables, then '```{```' , any number of statements and at the end of the function '```}```'.
```
vars
int msg; { statements and return }
```
Parameters must be declared with the type of variable, then the name followed by a comma if necessary repeating type and ID. Parameters can be empty.
```
int i, float s, int f
```
### Returns for functions

Functions of type ```int``` and ```float``` must have a keyword ```return``` followed by '```(```' a hyper expression and '```)```' ending with '```;```'. Returns can not have another function called in them due to memory calculations, only arithmetic expressions. 

```int```, ```float``` --> ```return(f);```

```void``` --> ```return;```

Variable declarations in all sections must have a type followed by any number of id with commas '```,```' between them ending with '```;```'.
```
int i, j , p;
```
Array and matrix declarations can be placed in normal variable declarations. After the id in brackets there must be the size of the array or matrix. 

Only one and two dimensional arrays are accepted. 

```
int arr[3], matrix[2][4]
```
After the declaration of program name, global variables and functions, there must be a main program that executes statements.

The keyword ```main``` followed by '```()``` ```{```' any number of statements and '```}``` ```end```'.

```
main () {
	…statements…
} end
```

## Statements
---
Assignment is used for assigning a value to a variable.

This value can be an expression, another variable, a constant or the return of a function (```float``` or ```int``` only).

The types must match in order to work. Assignments for arrays must have the ID and in the brackets of the size there must be an index between 0 and the size of the array or matrix - 1.

Every assignment must end with '```;```'
```
f = hw1(3);
mat[0][1] = i * 3;
x = 2;
```
Function calling for ```void``` type does not return a value, so it must be placed only by the function name, parameters and at the end of the function '```;```'.

Functions with a return value can not be placed like this:
```
printThis(8);
```
Input statements must also be declared in a specific way. It must be the ```input``` keyword next to '```(```' and the name of the variable you want the user to enter. If there's more than one variable '```,```' must be placed between ids, at the end there must be '```);```'

```
input(x, y, j);
```
```print``` statements write in the terminal an specific value or set of values that the user decides.

It functions similarly to input, first the ```print``` statement '```(```' id or a ```char``` constant.

For multiple prints in the same call commas '```,```' have to be placed followed by a ```char``` constant or id ending with '```;```'.
```
print(“hola”, h);
```

Conditional statements ```if else``` work based on a hyper expression. 

First the keyword ```if``` must be placed, right after in parenthesis ```(...)``` a condition must be placed.

The keyword ```then``` must follow with '```{```' ```statements``` '```}```'. If there is no alternative path the conditional ```if``` ends with the last '```}```', if there is an alternative path the keyword ```else``` must also have '```{ ... }```' and statements between the braces.
```
if(i < 3) then {
      i = i+1;
}
else {
      a = (x+5);
}
```
Lastly, the while cycle evaluates a condition and repeats the statements in the while cycle until it stops being true

First, the “while” keyword must appear then the condition in parenthesis '```(```' condition '```)```' then the keyword ```do``` and '```{ ... }```' with statements between the braces. For the cycle to work properly the condition must change. 
```
while(i<3) do {
    i = (i+1);
}
```

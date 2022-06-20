# Python

Lenguaje de programación:

- Tipado dinámico (vs tipado estático). 
  Al definir una variable no hay que predefinir un tipo de datos
- Interpretado (vs compilado). Distribuimos el fuente "as it is".
    Cuál es el intérprete de python? Hay muchos!!!!
        - Cuando "instalamos python" o eso decimos, lo que estamos haciendo es
          montar 1 interprete: CYTHON. Intérperete de python escrito en C... 
                                       CON LIMITACIONES IMPORTANTES!!!!
                                            Solo es capaz de usar un core de la máquina
        - PYPY
        - JYTHON
- Paradigmas de programación:
    √ Programación imperativa: El ir dando órdenes al computador que se procesan secuencialmente
        Instrucciones típicas: GOTO, if, for, while
    √ Programación procedural: Capacidad de definir funciones/procedimientos/método
        Instrucciones: def
    √ Programación funcional: Capacidad de asignar / referenciar desde una variable a una función.
                              Ya que las funciones tambiñen se guardan en memoria:
                                - Podemos pasar a una función otra función como argumento
                                - Podemos devolver una función desde otra
    √ Programación Orientada a Objetos

## Variable

Referencia a una posición de memoria en la que meto un dato

numero=7
# Poner un 7 en memoria RAM
# Crear una variable (POSTIT, en el que escribo la palabra numero)
# Referencio al 7 desde la variable: Pego el postit al lado del 7

numero=8
# Poner un 8 en memoria RAM, en un nuevo sitio... Y que pasa con el 7? 
    Ahí sigue... hasta que el garbage collector se lo pule
# La variable numero, varia su posición, para apuntar al 8.

numero="Hola"

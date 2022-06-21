Python es capaz de hacer uso de varios cores, o no?
Para python, tenemos varios interpretes:
- Cython: Solo hace uso de un core
- Pypy
- Jython


Python es un lenguaje de programación: Igual que C, JAVA
- Syntaxis
- Gramática
- Semantica


Java es capaz de hacer uso de varios cores? Será el interprete, no JAVA,... Java es un lenguaje, igual que python


Merece la pena abrir varios hilos si estoy usando cython, que es el interprete más habitual?
Un hilo solo usa CPU? Tambien accede a memoria, o a disco, o a red, o a un gpu, o espera.

Respuesta 1: Dependiendo de la naturaleza del programa.. de lo que haga y que recursos utilice.
             Si solo es CPU... no... o eso parece...
Respuesta 2: 
    Cuales son los grandes usos de python a dia de hoy:
        - ** Machine learning, deep learning, data mining ** Cuentas matemáticas por un tubo -> CPU
        - Testers
        - Scripts sysadmins (bash)
    
    Muchas librerias de las que hay desarooladas en python... realmente no estan desarrolladas en python, sino en C
        Pandas, numpy -> estan escritas en C
    Tan solo hay una capa de comunicacion (API) expuesto en python
    
    
---

# Orientación a objetos es otro paradigma de programación

Es decir, otra forma de usar el lenguaje para conseguir una finalidad

La orientación a objetos me permite definir mis propios tipos de variables.

Tipos que conocemos en python:
int
str
float
bool
tuple
dict
list

Yo voy a conseguir un tipo nuevo de datos, que tendrá:
    - Sus propias caracteristicas (atributos)
    - Sus propias funciones
    
str.... tiene sus propias funciones? upper, lower
list .. tiene sus propias funciones: append, insert, sort


Servidor
    Un servidor es algo que tiene una IP, un nombre, cpus, memoria
    Además a un servidor le puedo pedir que se arranque, que se detenga
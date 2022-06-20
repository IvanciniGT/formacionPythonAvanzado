# Comentarios, con el cuadradito.  //

# Comentario en bloque. 
# NO EXISTE. En python hay una chapuza muy grande que hacemos para poner comentarios en bloque

numero=7

texto="Hola"

""" Esto en python, re considera documentación del código
Hola 
amigos !!!!
y amigas !!!!
"""

# Documentar:   Detallar lo que hace y que necesita el código
# Comentar:     Explicar cómo hace lo que hace

# Tipos de datos:
# Números
7
19
-19
1.98

# Lógicos:
True
False

# Textos
"Hola soy un texto"
'Hola soy un texto'
"""
Texto multilinea
con comillas dobles
"""
'''
Textos multilinea con 
comillas simples
'''

# Tipos compuestos

## Colecciones

### Tupla: Conjunto secuencial/ordenado de datos, inmutables
# Ambas 2 tuplas tienen los mismos elementos: 4
( 1, 2 ,3 ,4 )
( 1, 2 ,3 ,4, )

# En python, los parentesis los usamos para muchas cosas:
# - Definir tuplas
# - Ejecutar funciones
# - Definir argumentos de funciones
# - Cambiar la prioridad/precedencia de operadores:
#     3 + 4 * 5 = 23
#     ( 3 + 4 ) * 5 = 35

# Qué es esto en python? Es un caso ambiguo
(24)  # En python es un entero
(24, ) # Una tupla de un elemento
3*(-17)

# A los elementos de una tupla accedemos mediante su posición en la tupla 
    #(comenzando a contar en 0)

### Listas: Conjunto secuencial/ordenado de datos, mutables
# Ambas 2 listas tienen los mismos elementos: 4
[ 1, 2 ,3 ,4 ]
lista=[ 1, 2 ,3 ,4, ]

# Puedo cambiar los elementos de la lista, añadir nuevos, borrarlos, ...

valor="1991"
lista.append(valor)

# Mezclar tipos de datos

(1,2,True, "Si")
[1,2,True, "Si"]

[1,2,(12,14)] # Os suena esta sintaxis. 
              # Existe un lenguaje de marcado/estructuración de información
              # Con una sintaxis similar? JSON

### Diccionarios: Conjunto secuencial/ordenado de datos, mutables.
                  # A cada elemento de esa colección, accedo a través de una clave, 
                  # y no de su posición
# Antes de python 3.6.? los diccionarios no garantizaban orden. Hoy en día si, desde esa versión
{"clave1": 1, "clave2":2 ,"clave 3": True,"otra clave": "Si"}

## Operadores de python
### Operadores numéricos: Devuelven un valor numérico y susu argumentos deben ser numéricos
1 + 3 - 5 * 1 / 9
2 ** 3
8/3  # 2.6666667
8//3  # 2
8%3   # 2

# Operadores relaciones: Devuelven un valor lógico
# ==   Igual
# !=   Distinto
# >   
# <   
# >=  
# <=  

# Operados lógicos: Devuelven un valor lógico, 
# pero sus argumentos también son valores lógicos

#   and
#   or
#   not

# Operadores sobre textos
"hola" + " amigo" # concatenación
print("hola" * 4)

# Operadores de asignación
numero=8

# Incremento
numero-=2
numero*=2
numero/=2
numero//=2

# Programación imperativa
## Condicionales
EXPRESION_LOGICA=True
if EXPRESION_LOGICA: 
    pass
elif not EXPRESION_LOGICA:
    pass
else:
    # Aqui hago algo
    pass

# Que otros condicional tenemos... COMO EXPERSION
# Lo que en otros lenguajes es el operador ternario
CONDICION=True
numero=7 if CONDICION else 18
#   VALOR-SI-TRUE   if   CONDICION      else    VALOR_SI_FALSE
#   CONDICION ? VALOR_SI_TRUE : VALOR_SI_FALSE
print(numero)

# Switch/case . Existe esto en python??? desde 3.10, que es muy reciente
# variable=7
# match variable:
#    case 3:
#        pass
#    case 14:
#        pass
#    case _:
#        pass

# Bucles
## Basados en colección
coleccion=[1,2,3,4,5,6]
for dato in coleccion:
    print(dato)

for dato in range(1,100,5):
    print(dato)
    
for dato in range(100,1, -1):
    print(dato)
    if dato % 5 == 0: # Si es un múltiplo de 5
        continue
    if dato % 11 == 0: # Si es un múltiplo de 11
        break
    print("a por otro")


lista=[1,2,3,4,5,6]
print(lista)
print(     [ valor*3 if valor%2 == 0 else valor*2  for valor in lista if valor>3 ]      )


lista=[]
for valor in (1,2,3,4,5,6):
    if valor>3: break
    lista.append(valor*3)


## Basados en condición
numero=10
while numero>0 : # CONDICION
    print("Hago algo")
    numero-=1
    
## UNTIL... do while... No existe en python
## Como lo implemento

numero=10
while True:
    print("hago algo")
    numero-=1
    if (numero==0):
        break
    
# Destructuración de tuplas
tupla = (1,2,3)
valor1, valor2, valor3= (1, 2, 3 )
print(int("3") + valor2 )


(_, _ , valor)=(1,2,3)
print(valor)

## Funciones de conversión de tipos de datos
str(4)
int("3")
float("3.28")
bool("True")
print(list( (1,2,3) ))

# En python3, toda función debe ejecutarse mediante unos parentesis detras coladitos. 
# Si no peta.

print
7
"hola"
max(1,2)
max

numero=17; print("Si quiero poner varias cosas en la misma linea...")
# Aunque esto es una cagada grande y no lo haria en la vida

# Definir Funciones

def saluda(efusivo, nombre = "Compañer@"):
    if efusivo:
        print("Holaaa "+ nombre + "!!!!!")
    else:
        print("Buenos dias "+ nombre)

saluda( True, "Ivan" )
saluda( False, "Alexander")
saluda( True, "Virginia")
saluda( False, "Omar" )
saluda( True)

def componerSaludos(efusivo, nombre = "Compañer@"):
    if efusivo:
        return "Holaaa "+ nombre + "!!!!!",  nombre + "!!!!!"
    else:
        return ("Buenos dias "+ nombre, "Hola "+ nombre)
        

(opcion1, opcion2)=componerSaludos( True, "Ivan" )

opcion1, opcion2=componerSaludos( False, "Alexander")

print(componerSaludos( True, "Virginia"))
print(componerSaludos( False, "Omar" ))
print(componerSaludos( True))


# Python permite DAR PISTAS . Desde python 3.5
def componerSaludosNuevos(efusivo: bool, nombre:str = "Compañer@") -> tuple:
    if efusivo:
        return "Holaaa "+ nombre + "!!!!!",  nombre + "!!!!!"
    else:
        return ("Buenos dias "+ nombre, "Hola "+ nombre)



def componerDespedida(efusivo: bool=True, nombre = "Compañer@"):
    if efusivo: # Si es true
                # si tiene un valor no lógico asignado (No None)
        return "Adios "+ nombre
    else: # si es false
          # Si está desasignado (None)
        return "Buenos noches "+ nombre

componerDespedida(False,"Ivan")
componerDespedida(False) # Buenas noches compañer@
print(componerDespedida("Berta") ) # Adios compañer@ # El valor se asigna a efusivo
print(componerDespedida(nombre="Berta") ) # Adios compañer@
print(componerDespedida("Berta") ) # Adios compañer@


# En los cindicionales: IF, si la condición no es un valor lógico, tiene una 
# interpretación distinta el if:
#   - si el valor está asignado: TRUE
#   - si el valor no está asignado: FALSE

# String nombre=null; En python es None

print(componerSaludosNuevos( None , "Virginia"))

# Colleciones
mitupla=(1,2,3,4,5,)
        #0,1,2,3,4
print( len(mitupla) )
print( mitupla[2] )
print( "ultimo " + str(   mitupla[ len(mitupla) - 1 ] )    )
print( "ultimo " + str(   mitupla[ -1 ] )    )

print(  mitupla[-3]  ) # Antepenultimo

# Slicing: Subcoleccion
print( mitupla[1:4] )
print( mitupla[2:] ) # Del tercero en adelante
print( mitupla[:-2] ) # Hasta el antepenultimo incluido

for item in mitupla:
    print(item)

# Fijaros en estos operadores.... que curiosos
print( (1,2,3,) * 5 )
print( (1,2,3,) + ("a", "b", "c") )

# Hemos visto uncompartamiento similar por ahi ya? SIIII : TEXTOS
# Y es que un texto no es sino una tupla de caracteres en python
# Todo lo anterior vale para textos
mi_texto="Hola" # En python usamos snake Case. En java usamos CamelCase

print( len(mi_texto) )
print( texto[3] )
print( texto[-1] )
print( texto[:-2] )
for caracter in mi_texto:
    print(caracter)

# Listas
mi_lista = [1,2,3,4,5]
# Puedo hacer lo mismo que con las tuplas
# Pero ademas: puedo hacer modificaciones de diversos tipos

mi_lista[1]="A"
print(mi_lista)

# Añadir cosas a la lista
mi_lista.append("ultimo")
print(mi_lista)
mi_lista+=("hola",)
mi_lista+=("hola","adios")
print(mi_lista)
mi_lista.insert(0, "primero")
print(mi_lista)

# Borrar cosas
mi_lista.remove(3) # Esto me borra el elemento 3. Solo la primera ocurrencia
print(mi_lista)
borrado=mi_lista.pop(3) # Esto me borra el elemento en la posicion 3.
print(mi_lista)
print(borrado)

# append + pop: Me permiten usar unalista como si fuera una : PILA (stack)
# push, pop

mi_lista=[1,2,3,4,6,8,7,6]
mi_lista.sort(reverse=True)
mi_lista.reverse()
print(mi_lista.count(6))
print(mi_lista)

# Programación funcional: poder referenciar una funcion desde una variable
funcion_a_utilizar=print

funcion_a_utilizar("HOLA")

def imprime(texto, transformacion):
    print(transformacion(texto))

def minusculas(texto):
    return texto.lower()
    
    
def mayusculas(texto):
    return texto.upper()
    
imprime("Hola Amigo", minusculas)
imprime("Hola Amigo", mayusculas)


# Funciones que devuelven funciones


def minusculas2(texto):
    return texto.lower
    
    
def mayusculas2(texto):
    return texto.upper
    
def super_transformacion_virgina(texto):
    return texto.upper().lower()

def imprime2(funcion):
    print(funcion())
    
imprime2(minusculas2("Hola Amigo"))
imprime2(mayusculas2("Hola Amigo"))
una_funcion=minusculas2("Hola Amigo")

#imprime2(super_transformacion_virgina)

print( una_funcion )
print( una_funcion() )

# Funciones lambda: Funcion anonima, cutre que cagas, con solo una expresion de codigo

#def doble(numero):
#    return numero * 2
#funcion=doble
funcion=lambda numero: numero * 2

print (funcion (2))

def funcion_que_llama_a_la_funcion_de_transformacion_de_virginia():
    return super_transformacion_virgina("Hola")

imprime2(funcion_que_llama_a_la_funcion_de_transformacion_de_virginia)
imprime2(lambda:super_transformacion_virgina("Hola"))

def funcion_que_devuelve_la_funcion_de_transformacion_de_virginia(texto):
    def funcion_de_transformacion_de_virginia():
        return texto.upper().lower()
    return funcion_de_transformacion_de_virginia
    
imprime2(funcion_que_devuelve_la_funcion_de_transformacion_de_virginia("Hola"))

# Modo tradicional
coleccion=(1,2,3,4,5,6)
filtrada=[]
for elemento in coleccion:
    if elemento%2==0 : 
        pass
    else:
        filtrada.append(elemento)
print(filtrada)
        
# Modo ahorro on!
filtrada=[ elemento for elemento in coleccion if elemento %2!=0 ]
print(filtrada)

# Modo programación funcional
filtrada=filter(lambda elemento: elemento%2!=0, coleccion)
                # Al aplicar la funcion sobre cada elemento: Un valor lógico: True o False
                # Filter deja solo los elementos originales cuya transformación valga True
print(list(filtrada))

# Montar vuestra propia fiuncion filter... llamemosla:
def mi_propia_funcion_filter(funcion_de_filtro, coleccion):
    return None

filtrada=mi_propia_funcion_filter(lambda elemento: elemento%2!=0, coleccion)
                # Al aplicar la funcion sobre cada elemento: Un valor lógico: True o False
                # Filter deja solo los elementos originales cuya transformación valga True
print(list(filtrada))

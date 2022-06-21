
## contar: Una funcion que recibe NOMBRE, CANTIDAD, LAPSO_TIEMPO
### Soy NOMBRE: Voy por el 1
#### Esperamos el lapso indicado
### Soy NOMBRE: Voy por el 2

# Libreria:
# Coleccion de funciones y/o clases que ya ha escrito alguien
# Para hacer uso de una libreria que necesito:
# - Tenerla / Instalarla                        pip      pip3      python -m pip install 
# - Decirle a python que la quiero usar         import

import time
#import threading # Clase Thread
from threading import Thread

def contar(nombre, cantidad, lapso):
    for numero in range(1, cantidad+1):
        print("Soy " + nombre + ": Voy por el " + str(numero) )
        time.sleep(lapso) # Pausa... Retrasa la ejecuación del hilo que está corriendo esta linea. 

hilo_a=Thread( target = lambda: contar("CONTADOR A" , 0, 1) )
hilo_a.start()

hilo_b=Thread( target = lambda: contar("CONTADOR B" , 0, 2) )
hilo_b.start()

hilo_b.join() # Esperar en este punto a que el hilo b acabe . Punto de sincronización
hilo_a.join() # Esperar en este punto a que el hilo b acabe . Punto de sincronización

print("YA ACABE")
# Qué es un hilo? Thread
#  Es una ejecución paralela a otras ejecuaciones del código 
# No es un proceso. Los procesos de SO ejecutan su código mediante hilos

# Al solicitar al SO la ejecución de un programa, el SO abre un proceso para controlar su ejecución
# Lo primero que hace el SO es reservar una zona en memoria:
# Colocar el programa en esa zona de memoria (el código)
# A parte se reserva otra zona para colocar los datos del programa
# El SO arranca un hilo asociado al proceso (principal)

# Los hilos de un proceso comparten la memoria RAM del proceso. 

class Contador (Thread):
    
    # Constructor
    def __init__(self, nombre, cantidad, lapso ):
        super().__init__()
        self.nombre=nombre
        self.cantidad=cantidad
        self.lapso=lapso

    def run(self):
        for numero in range(1, self.cantidad+1):
            print("Soy " + self.nombre + ": Voy por el " + str(numero) )
            time.sleep(self.lapso) # Pausa... Retrasa la ejecuación del hilo que está corriendo esta linea. 

contadorA = Contador("CONTADOR A" , 10, 1 )
contadorB = Contador("CONTADOR B" ,  5, 2 )

contadorA.start()
contadorB.start()

contadorA.join()
contadorB.join()

print("YA HE VUELTO A ACABAR")

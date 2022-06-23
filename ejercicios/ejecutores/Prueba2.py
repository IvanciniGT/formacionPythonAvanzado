from PoolDeEjecutores import PoolDeEjecutores
from Promesa import Estado
import time 

def tareaSimple(numero):
    def funcion():
        time.sleep(2)
        # Hago llamada a servicio Web
        return numero*2
    return funcion


def trabajoProcesado( numero ):
    def callback (dato):
    # Necesito saber de que trabajo es este dato
        print("Valor devuelto: " + str(dato) +" para el numero: " + str(numero) )
    return callback




pool_de_ejecutores1 = PoolDeEjecutores(3, 1)
lista_promesas={}
for numero in range(5):
    # Sincrona
    pool_de_ejecutores1.nuevoTrabajo( tareaSimple(numero) , trabajoProcesado(numero) )
    # Asincrona
    lista_promesas[numero]=( pool_de_ejecutores1.nuevoTrabajo( tareaSimple(numero) ) )

pool_de_ejecutores1.comienza()
pool_de_ejecutores1.esperarFinalizacionDeTrabajos()

#HAGO OTRAS COSAS ANTES
pendientes={}
while len(lista_promesas) > 0:
    for clave,promesa in lista_promesas.items(): # item tendría la clave
        if promesa.estado == Estado.RESULETA:
            print( "Para el numero " + str(clave) +" tengo el valor "+ str(promesa.valor ))
        else:
            pendientes[clave]= promesa
    # LAs no acabadas la muevo a un diccionario temporal que reasigno
    lista_promesas = pendientes
    #del lista_promesas[clave]
    
    time.sleep(1)

# Dentro de la lista de promesas será una Promesa
# - Estado: Pendiente, Resuelta, Error
# - Valor
# - Error

print("Acabado")
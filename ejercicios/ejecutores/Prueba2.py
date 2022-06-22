from PoolDeEjecutores import PoolDeEjecutores
import time 

def tareaSimple(numero):
    def funcion():
        time.sleep(2)
        # Hago llamada a servicio Web
        return numero*2
    return funcion


def trabajoProcesado( dato ):
    # Necesito saber de que trabajo es este dato
    print("Valor devuelto: " + dato)




pool_de_ejecutores1 = PoolDeEjecutores(3, 1)
lista_promesas=[]
for numero in range(10):
    # Sincrona
    pool_de_ejecutores1.nuevoTrabajo( tareaSimple(numero) , trabajoProcesado )
    # Asincrona
    lista_promesas.append( pool_de_ejecutores1.nuevoTrabajo( tareaSimple(numero) ) )

pool_de_ejecutores1.comienza()
pool_de_ejecutores1.esperarFinalizacionDeTrabajos()

#HAGO OTRAS COSAS ANTES

while len(lista_promesas) > 0
    for item in lista_promesas:
        if item.estado == EstadoPromomesa.Resuelta:
            print( item.valor )
            lista_promesas.remove(item)
    time.sleep(1)

# Dentro de la lista de promesas será una Promesa
# - Estado: Pendiente, Resuelta, Error
# - Valor
# - Error

print("Acabado")
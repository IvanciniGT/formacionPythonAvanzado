from PoolDeEjecutores import PoolDeEjecutores
import time 

def tareaSimple(numero):
    return lambda: print("Trabajo " + str(numero))

def tareaSimple2(numero):
    def imprimir():
        print("Trabajo " + str(numero))
        time.sleep(3)
    return imprimir

pool_de_ejecutores1 = PoolDeEjecutores(3, 1)
 
for numero in range(10):
    pool_de_ejecutores1.nuevoTrabajo( tareaSimple(numero) )

pool_de_ejecutores1.comienza()

for numero in range(10,20):
    pool_de_ejecutores1.nuevoTrabajo( (lambda numero: lambda: print("Trabajo " + str(numero)))(numero) )

#pool_de_ejecutores1.para() # Los trabajos que no estén ejecución
                           # Que sean descartados
print("Espero un poco")
time.sleep(5)
print("Tiro más tareas")

for numero in range(20,30):
    pool_de_ejecutores1.nuevoTrabajo( tareaSimple2(numero) )

pool_de_ejecutores1.esperarFinalizacionDeTrabajos()

print("Acabado")
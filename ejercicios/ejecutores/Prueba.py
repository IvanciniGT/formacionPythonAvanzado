from PoolDeEjecutores import PoolDeEjecutores

pool_de_ejecutores1 = PoolDeEjecutores(3, 1)
 
for numero in range(100):
    pool_de_ejecutores1.nuevoTrabajo( lambda: print("Trabajo " + str(numero)) )

pool_de_ejecutores1.comienza()

for numero in range(100,200):
    pool_de_ejecutores1.nuevoTrabajo( lambda: print("Trabajo " + str(numero)) )

pool_de_ejecutores1.para() # Los trabajos que no estén ejecución
                           # Que sean descartados

for numero in range(200,300):
    pool_de_ejecutores1.nuevoTrabajo( lambda: print("Trabajo " + str(numero)) )

pool_de_ejecutores1.esperarFinalizacionDeTrabajos()

print("Acabado")
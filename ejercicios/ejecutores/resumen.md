Queremos tener un pool de ejecutores que podamos usar para ejecutar tareas


```py

pool_ejecutores = PoolEjecutores( NUMERO_DE_EJECUTORES , TIEMPO DE ESPERA )

pool_ejecutores.comienza()

pool_ejecutores.nuevoTrabajo( referencia_a_una_funcion )

pool_ejecutores.pausa()

pool_ejecutores.para(): Vaciar la cola

pool_ejecutores.esperarFinalizacionDeTrabajos()



---

Cola de trabajos pendientes: FIFO
T4 > T3 > T2 > T1.    Los ejecutores leen trabajo de esta cola

```

Clase: PoolDeEjecutores
Clase: Ejecutor

Programa para proabr que esto funciona

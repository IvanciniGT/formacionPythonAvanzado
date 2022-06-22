from threading import Thread
from Estados import Estado
import time

class Ejecutor( Thread ):

    __ESTADOS_DE_TRABAJO=[ Estado.INICIADO , Estado.PAUSADO, Estado.PENDIENTE_FINALIZACION ]

    def __init__(self, pool_de_ejecutores ):
        super().__init__()
        self.pool_de_ejecutores = pool_de_ejecutores

    def run(self):
   
        # Asegurar que el hilo sigue corriendo
        while self.pool_de_ejecutores.estado_pool_ejecutores in Ejecutor.__ESTADOS_DE_TRABAJO:
            # Si no estoy pausado
            if self.pool_de_ejecutores.estado_pool_ejecutores != Estado.PAUSADO:
                # Saco curro
                proximo_trabajo = self.pool_de_ejecutores.recuperarTrabajo()
                if  proximo_trabajo: # Si hay curro
                    # hacerTrabajo
                    proximo_trabajo()
                    continue # Evitar la siesta
                if self.pool_de_ejecutores.estado_pool_ejecutores == Estado.PENDIENTE_FINALIZACION:
                    break
                    #else:
                        #Si no hay trabajo y estoy iniciado
            #else:
                # Estoy en pausa
            # Si no hay trabajo y estoy iniciado
            # O si estoy en pausa
            time.sleep( self.pool_de_ejecutores.tiempo_espera )

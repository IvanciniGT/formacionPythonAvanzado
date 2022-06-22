from enum import Enum

class Estado(Enum):
    PENDIENTE = 0
    INICIADO  = 1
    PAUSADO   = 2
    PARADO    = 3

__TRANSICIONES_DE_ESTADO={                                          \
    Estado.PENDIENTE: [ Estado.INICIADO ],                          \
    Estado.INICIADO:  [ Estado.PAUSADO, Estado.PARADO ],            \
    Estado.PAUSADO:   [ Estado.INICIADO, Estado.PARADO ],           \
    Estado.PARADO:    [ ],                                          \
}

class StateTransitionException(Exception):
    
    def __init__(self, source_state , target_state):
        super().__init__( "Transición no permitida" )
        self.source_state = source_state
        self.target_state = target_state

class PoolDeEjecutores:
    
    def __init__(self, numero_ejecutores, tiempo_espera ):
        self.__numero_ejecutores      = numero_ejecutores
        self.__tiempo_espera          = tiempo_espera
        self.__trabajos_pendientes    = []
        self.__ejecutores             = []
        self.__estado_pool_ejecutores = None
        self.__cambiarEstado( Estado.PENDIENTE )
        # Creamos ejecutores
        Ejecutor(.     )
    
    @property
    def estado_pool_ejecutores(self):
        return self.__estado_pool_ejecutores
        
    def __cambiarEstado(self, nuevoEstado):
        if nuevoEstado not in __TRANSICIONES_DE_ESTADO[ self.__estado_pool_ejecutores ]:
            raise StateTransitionException(self.__estado_pool_ejecutores, nuevoEstado)
        self.__estado_pool_ejecutores = Estado.PENDIENTE
        
    def comienza(self):
        self.__cambiarEstado( Estado.INICIADO )
        # Al arrancar, los hilos:
        # Miran con una periodicidad a una COLA
        #   trabajos pendientes
        #   - Si hay trabajo, toman 1 trabajo y lo ejecutan
        #                     y vuelven a mirar de inmediato en la cola
        #   - Si no hay trabajo, siguen esperando y mirando

    def nuevoTrabajo( self, funcion_a_ejecutar ):
        if self.__estado_pool_ejecutores == Estado.PARADO:
            raise ValueError("No se admiten más trabajos")
        self.__trabajos_pendientes.insert( 0 , funcion_a_ejecutar)
    
    def pausa(self):
        self.__cambiarEstado( Estado.PAUSADO )

    
    def para(self):
        self.__cambiarEstado( Estado.PARADO )
        self.__trabajos_pendientes.clear()
    
    def esperarFinalizacionDeTrabajos(self):
        pass

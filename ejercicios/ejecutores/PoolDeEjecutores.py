from enum import Enum

class Estado(Enum):
    PENDIENTE_INICIO        = 0
    INICIADO                = 1
    PAUSADO                 = 2
    PARADO                  = 3
    PENDIENTE_FINALIZACION  = 4
    ACABADO                 = 5

__TRANSICIONES_DE_ESTADO={                                                                              \
    Estado.PENDIENTE_INICIO: [ Estado.INICIADO ],                                                       \
    Estado.INICIADO:         [ Estado.PAUSADO, Estado.PARADO, Estado.PENDIENTE_FINALIZACION ],          \
    Estado.PAUSADO:          [ Estado.INICIADO, Estado.PARADO, Estado.PENDIENTE_FINALIZACION ],         \
    Estado.PARADO:           [ ],                                                                       \
    Estado.PENDIENTE_FINALIZACION:  [ Estado.ACABADO ],                                                 \
    Estado.ACABADO:          [ ]                                                                        \
}

class StateTransitionException(Exception):
    
    def __init__(self, source_state , target_state):
        super().__init__( "Transición no permitida" )
        self.source_state = source_state
        self.target_state = target_state

class PoolDeEjecutores:
    
    def __init__(self, numero_ejecutores, tiempo_espera ):
        self.__numero_ejecutores      = numero_ejecutores
        self.tiempo_espera          = tiempo_espera
        self.__trabajos_pendientes    = []
        self.__estado_pool_ejecutores = None
        self.__cambiarEstado( Estado.PENDIENTE_INICIO )
        
        # Creamos ejecutores
        # self.__ejecutores             = []
        # for numero in range (self.__numero_ejecutores):
        #    self.__ejecutores.append(Ejecutor(self))
        self.__ejecutores = [ Ejecutor(self) for n in range (self.__numero_ejecutores) ]
            
    
    @property
    def estado_pool_ejecutores(self):
        return self.__estado_pool_ejecutores
        
    def __cambiarEstado(self, nuevoEstado):
        if nuevoEstado not in __TRANSICIONES_DE_ESTADO[ self.__estado_pool_ejecutores ]:
            raise StateTransitionException(self.__estado_pool_ejecutores, nuevoEstado)
        self.__estado_pool_ejecutores = nuevoEstado
        
    def comienza(self):
        estado_anterior = self.__estado_pool_ejecutores
        self.__cambiarEstado( Estado.INICIADO )
        if estado_anterior == Estado.PENDIENTE_INICIO:
            for ejecutor in self.__ejecutores:
                ejecutor.start()
    
    def recuperarTrabajo(self):
        # Sincronizado
        # Asegurarnos que solo 1 hilo hace esto
        return None
    
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
        self.__cambiarEstado( Estado.PENDIENTE_FINALIZACION )
        for ejecutor in self.__ejecutores:
            ejecutor.join()
        self.__cambiarEstado( Estado.ACABADO )


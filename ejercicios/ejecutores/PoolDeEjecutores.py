from threading import Semaphore
from Estados import Estado, StateTransitionException, _TRANSICIONES_DE_ESTADO
from Ejecutor import Ejecutor

class PoolDeEjecutores:
    
    def __init__(self, numero_ejecutores, tiempo_espera ):
        self.__numero_ejecutores      = numero_ejecutores
        self.tiempo_espera            = tiempo_espera
        self.__trabajos_pendientes    = []
        self.__estado_pool_ejecutores = Estado.PENDIENTE_INICIO
        #self.__cambiarEstado( Estado.PENDIENTE_INICIO )
        self.__llaves                 = Semaphore()
        # Creamos ejecutores
        # self.__ejecutores             = []
        # for numero in range (self.__numero_ejecutores):
        #    self.__ejecutores.append(Ejecutor(self))
        self.__ejecutores = [ Ejecutor(self) for n in range (self.__numero_ejecutores) ]
            
    
    @property
    def estado_pool_ejecutores(self):
        return self.__estado_pool_ejecutores
        
    def __cambiarEstado(self, nuevoEstado):
        if nuevoEstado not in _TRANSICIONES_DE_ESTADO[ self.__estado_pool_ejecutores ]:
            raise StateTransitionException(self.__estado_pool_ejecutores, nuevoEstado)
        self.__estado_pool_ejecutores = nuevoEstado
        
    def comienza(self):
        estado_anterior = self.__estado_pool_ejecutores
        self.__cambiarEstado( Estado.INICIADO )
        if estado_anterior == Estado.PENDIENTE_INICIO:
            for ejecutor in self.__ejecutores:
                ejecutor.start()
    
    def recuperarTrabajo(self):
        trabajo_a_devolver = None
        self.__llaves.acquire()    # Coje las llaves y cuando las tengas entra
                                   # Si no estan las llaves en su sitio, espera
        if len( self.__trabajos_pendientes ) > 0:   
            trabajo_a_devolver = self.__trabajos_pendientes.pop()
        self.__llaves.release()    # Deja las llaves en su sitiop, para el proximo
        return trabajo_a_devolver

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


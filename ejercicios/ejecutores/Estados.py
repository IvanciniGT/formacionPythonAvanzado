from enum import Enum

class Estado(Enum):
    PENDIENTE_INICIO        = 0
    INICIADO                = 1
    PAUSADO                 = 2
    PARADO                  = 3
    PENDIENTE_FINALIZACION  = 4
    ACABADO                 = 5

_TRANSICIONES_DE_ESTADO={                                                                              \
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

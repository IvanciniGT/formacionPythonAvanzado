from enum import Enum

class Estado(Enum):
    PENDIENTE        = 0
    RESULETA         = 1
    ERROR            = 2
    
class Promesa:
    
    def __init__(self):
        self.estado = Estado.PENDIENTE
        self.valor  = None
        self.error  = None
        
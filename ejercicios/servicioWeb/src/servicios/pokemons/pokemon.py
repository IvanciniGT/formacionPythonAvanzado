from comun.objetopersistente import ObjetoPersistente
from servicios.inicializador import base_datos

class Pokemon(ObjetoPersistente, base_datos.Model):
                                # Va a controlar la BBDD para este tipo de objeto
    # Por ser esto un modelo de SQLAlchemy:
    # Necesito unas variables a nivel de clase
    # Que indiquen los campos que tienen persistencia
    # Y los tipos de datos
    id              = base_datos.Column(base_datos.Integer, primary_key=True)
    nombre          = base_datos.Column(base_datos.String)
    clase           = base_datos.Column(base_datos.String)
    evolucion       = base_datos.Column(base_datos.String)
    ataque_estrella = base_datos.Column(base_datos.String)
    
    def __init__(self, nombre, clase , evolucion, ataque_estrella):
        self.nombre = nombre
        self.clase = clase
        self.evolucion = evolucion
        self.ataque_estrella = ataque_estrella
 
    @staticmethod
    def instanciarDesdeDiccionario(dict):
        return Pokemon(dict["nombre"], dict["clase"] , dict["evolucion"], dict["ataque_estrella"])
 
# Tener una tabla en una BBDD con un monton de Pokemons

#pikachu = Pokemon("Pikachu", "Electrico", "Raichu", "Impactrueno")
#pikachu.guardar()
#pikachu.borrar()

#pikachu = Pokemon.recuperar("pikachu")
#pokemons = Pokemon.recuperarTodos()

class Pokemon:
    
    def __init__(self, nombre, clase , evolucion, ataque_estrella):
        self.nombre = nombre
        self.clase = clase
        self.evolucion = evolucion
        self.ataque_estrella = ataque_estrella


# Tener una tabla en una BBDD con un monton de Pokemons

# Montar un api Restful para hacer operaciones con los pokemons

# Alta de pokemon
# Baja de pokemon
# Listar pokemons
# Recuperar datos de un pokemon
# Buscar pokemons
# 
# Api rest:
# http://SERVIDOR:PUERTO/api/v1/pokemons
#   Metodos HTTP                        GET >   Listado de todos los pokemons
#   Metodos HTTP                        POST>   Alta de un pokemon
# http://SERVIDOR:PUERTO/api/v1/pokemons/picachu
#   Metodos HTTP                        DELETE> Baja de un pokemon
#   Metodos HTTP                        GET >   Detalle de picachu

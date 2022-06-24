
# Api rest:

from flask_restful import Resource, Api         # Definición de un ENDPOINT

from servicios.pokemons.pokemon import Pokemon  # MODELO concreto

from esquema import esquema_para_pokemons       # Serializados/desserializados a JSON del modelo concreto

from flask import request                       # Datos de la peticion que nos han hecho por HTTP

# http://SERVIDOR:PUERTO/api/v1/pokemons
class EndpointsPokemons (Resource):
    
#   Metodo HTTP GET >   Listado de todos los pokemons
    def get(self):
        codigo_respuesta = 200
        try:
            pokemons = Pokemon.recuperarTodos()                                   # Lista de pokemons
            json_a_devolver = esquema_para_pokemons.dump(pokemons , many=True )   # Serializar la lista -> JSON
        except:
            codigo_respuesta = 500
            json_a_devolver = "{}"
        return json_a_devolver, codigo_respuesta

#   Metodos HTTP                        POST>   Alta de un pokemon
    def post(self):
        codigo_respuesta = 201
        json_a_devolver = "{}"

        try:
            datos_enviados = request.get_json()  # Recupero el JSON que me envian con el post
            pokemon_datos = esquema_para_pokemons.load( datos_enviados )   # Transformando el texto en DICCIONARIO
            # Controlar que ese pokemon no existe ya
        except:
            codigo_respuesta = 401          #4XX.    Error de cliente
        else:
            nuevo_pokemon = Pokemon.instanciarDesdeDiccionario( pokemon_datos )
            try:
                nuevo_pokemon.guardar()
            except:
                codigo_respuesta = 500
            else:
                json_a_devolver = esquema_para_pokemons.dump( nuevo_pokemon )   # Serializar la lista -> JSON
                
        return json_a_devolver, codigo_respuesta


def registrarAPIPokemons(blueprint):            # flask: Coleccion de API servicios que ofrecemos
    api_pokemons_v1 = Api(blueprint)    # Creamos un API que es una coleccion de endpoints
    api_pokemons_v1.add_resource( EndpointsPokemons , '/api/v1/pokemons' )  # añadir endpoints

















# http://SERVIDOR:PUERTO/api/v1/pokemons/picachu
#   Metodos HTTP                        DELETE> Baja de un pokemon.   CODIGO ESTADO 200, 400
#   Metodos HTTP                        GET >   Detalle de picachu


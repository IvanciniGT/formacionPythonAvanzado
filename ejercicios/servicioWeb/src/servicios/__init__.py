
from inicializador import base_datos, serializador_json, gestor_estructura_base_datos, mi_blueprint
from servicios.pokemons.api_v1.endpoints import registrarAPIPokemons

def configurarServicios(servidor_flask):
    
    # Damos de alta e inicialziamos el marshmallow en nuestro servidor concreto de flask
    serializador_json.init_app( servidor_flask )
    
    # Damos de alta e inicialziamos la BBDD en nuestro servidor concreto de flask
    base_datos.init_app( servidor_flask )
    # Tengo una BBDD... pero tiene la estructura adecuada? Usamos migrate para asegurarlo
    gestor_estructura_base_datos.init_app( servidor_flask, base_datos)
    
    # Dar de alta las apis
    registrarAPIPokemons(mi_blueprint)
    
    # Añado el blueprint a flask
    servidor_flask.register_blueprint( mi_blueprint )
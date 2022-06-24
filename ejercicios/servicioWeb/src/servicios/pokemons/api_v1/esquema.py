# a marshmallow le vamos a crear esquemas
# Cuando le pidamos que serialice un objeto, usará un determinado esquema
# JSON v1

from marshmallow import fields
from servicios.inicializador import serializador_json        # ruta absoluta
#from ...inicializador import serializador_json              # ruta relativa

class EsquemaPokemon(serializador_json.Schema):
    
    # Mashmallow va a usar las variables de clase que defina aqui para serializar el objeto
    # Son los campos que deben ser serializados
    id              = fields.Integer( dump_only=True )
    nombre          = fields.String()
    clase           = fields.String()
    evolucion       = fields.String()
    ataque_estrella = fields.String()

# Esta libreria Marshmallow, serializará y desserializará los pokemons en función de este esquema
# El esquema tiene una doble finalidad:
# - Identificar tipos de campos
# - Validar en entrada, que lleguen todos los datos que estamos 

esquema_para_pokemons = EsquemaPokemon()
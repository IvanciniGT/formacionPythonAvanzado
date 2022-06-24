# a marshmallow le vamos a crear esquemas
# Cuando le pidamos que serialice un objeto, usará un determinado esquema
# JSON v1

from marshallow import fields
from servicios.inicializador import serializador_json        # ruta absoluta
#from ...inicializador import serializador_json              # ruta relativa

class EsquemaPokemon(serializador_json.Schema):
    
    # Mashmallow va a usar las variables de clase que defina aqui para serializar el objeto
    # Son los campos que deben ser serializados
    id              = fields.Integer()
    nombre          = fields.String()
    clase           = fields.String()
    evolucion       = fields.String()
    ataque_estrella = fields.String()
    

import requests

SERVICIO_WEB = "http://127.0.0.1:5000/api/v1/pokemons"

def recuperarPokemons():
    respuesta = requests.get( SERVICIO_WEB )
    print( respuesta.status_code )
    print( respuesta.json() )
    return len( respuesta.json() )

def altaPokemon(datos ):
    respuesta = requests.post( SERVICIO_WEB, json=datos )
    print( respuesta.status_code )
    print( respuesta.json() )
    return len( respuesta.json() )
    
print( recuperarPokemons() )

rainchu={
         "nombre": "Rainchu" ,
         "clase": "Electrico" ,
         "evolucion": "Rainchu salvaje" ,
         "ataque_estrella": "Puño certero" 
}
print( altaPokemon(rainchu) )

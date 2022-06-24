curl -X POST http://127.0.0.1:5000/api/v1/pokemons \
    -H 'Content-Type: application/json' \
    -d '{ "nombre": "Pikachu" ,"clase": "Electrico" ,"evolucion": "Rainchu" ,"ataque_estrella": "Impactrueno" }'
    
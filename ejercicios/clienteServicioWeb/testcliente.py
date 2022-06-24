from cliente import recuperarPokemons

import requests_mock
import unittest 

class TestServicios(unittest.TestCase):

    def setUp(self):
        self.mi_mock=requests_mock.Mocker()
        self.mi_mock.register_uri(
            'GET',
            "/api/v1/pokemons",
            json=[
                {
                     "nombre": "Rainchu" ,
                     "clase": "Electrico" ,
                     "evolucion": "Rainchu salvaje" ,
                     "ataque_estrella": "Puño certero" 
                }
                ],
            status_code=200
        )

    def test_recuperarPokemons(self):
        with self.mi_mock:
            cantidad = recuperarPokemons()
            self.assertTrue( cantidad > 0 )

if __name__ == '__main__':
    unittest.main()
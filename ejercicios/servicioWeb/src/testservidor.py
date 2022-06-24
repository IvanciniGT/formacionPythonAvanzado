from programa import servidor_flask
import unittest 

class TestServicios(unittest.TestCase):

    SERVICIO_WEB = "/api/v1/pokemons"

    def setUp(self):
        # Arrancar servidor
        servidor_flask.config['TESTING'] = True
        self.cliente=servidor_flask.test_client()
         
    def test_get_all(self):
        # Cliente servidor donde hacer un get al endpoint adecuado
        respuesta = self.cliente.get( TestServicios.SERVICIO_WEB )
        self.assertEqual( respuesta.status_code , 200 )
        self.assertTrue( len(respuesta.json) > 0 )
        # Comprobar que devuelve una lista
        # Y un codigo 200

if __name__ == '__main__':
    unittest.main()
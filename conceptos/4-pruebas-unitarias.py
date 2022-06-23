import unittest

# Definir casos de prueba -> 3 resultados: OK, FALLO, EXPLOSION CATASTROFICA 

class LibreriaOperacionesMatematicas:
    
    @staticmethod
    def suma(numero1, numero2):
        return numero1 + numero2
    
    @staticmethod
    def resta(numero1, numero2):
        return numero1 - numero2
    
# Llamada de prueba

class Test_LibreriaOperacionesMatematicas(unittest.TestCase):
    
    def test_sumar2positivos(self):
        resultado= LibreriaOperacionesMatematicas.suma(3,5)
        self.assertEqual(resultado, 8)

    def test_sumar2negativos(self):
        resultado= LibreriaOperacionesMatematicas.suma(-3,-5)
        self.assertEqual(resultado, -8)

    def test_sumar_positivo_negativo(self):
        resultado= LibreriaOperacionesMatematicas.suma(-3,5)
        self.assertEqual(resultado, 2)

    def test_sumar_cero(self):
        resultado= LibreriaOperacionesMatematicas.suma(3,0)
        self.assertEqual(resultado, 3)

#####

    def test_restar2positivos(self):
        resultado= LibreriaOperacionesMatematicas.resta(3,5)
        self.assertEqual(resultado, -2)

    def test_restar2negativos(self):
        resultado= LibreriaOperacionesMatematicas.resta(-3,-5)
        self.assertEqual(resultado, 2)

    def test_restar_positivo_negativo(self):
        resultado= LibreriaOperacionesMatematicas.resta(-3,5)
        self.assertEqual(resultado, -8)

    def test_restar_cero(self):
        resultado= LibreriaOperacionesMatematicas.resta(3,0)
        self.assertEqual(resultado, 3)

if __name__ == '__main__': # Ejecuta solo ese código, si estan llamando directamente a este fichero
    unittest.main()
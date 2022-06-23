import unittest

from pruebasunitarias import Test_LibreriaOperacionesMatematicas

suite=unittest.TestSuite()
suite.addTest(Test_LibreriaOperacionesMatematicas())

if __name__ == '__main__': # Ejecuta solo ese código, si estan llamando directamente a este fichero
    runner = unittest.TextTestRunner()
    runner.run(suite)
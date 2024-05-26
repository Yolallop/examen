import unittest
from Kata import Kata

class KataTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Kata()

    def test_esPalindromo_true(self):
        palabra = "ana"
        self.assertTrue(self.p1.esPalindromo(palabra))

    def test_esPalindromo_false(self):
        palabra = "hola"
        self.assertFalse(self.p1.esPalindromo(palabra))

    def test_esVocal(self):
        cadena = "hola"
        self.assertEqual(self.p1.esVocal(cadena), 2)

    def test_esPalindromo_method_exists(self):
        self.assertTrue(hasattr(Kata, "esPalindromo"))

    def test_esVocal_method_exists(self):
        self.assertTrue(hasattr(Kata, "esVocal"))

    def test_startsWithA_true(self):
        cadena = "Amanda"
        self.assertTrue(self.p1.startsWithA(cadena))

    def test_startsWithA_false(self):
        cadena = "tuyaaya"
        self.assertFalse(self.p1.startsWithA(cadena))

    def test_palabrasConVocalesImpares_true(self):
        cadena = "maria"
        self.assertEqual(self.p1.palabrasConVocalesImpares(cadena), "maria")

    def test_palabrasConVocalesImpares_false(self):
        cadena = "raul"
        self.assertFalse(self.p1.palabrasConVocalesImpares(cadena))

    def test_palabrasQueTenganTamañoMayorQue7_true(self):
        cadena = "mamaguevo"
        self.assertEqual(self.p1.palabrasQueTenganTamañoMayorQue7(cadena), "mamaguevo")

    def test_palabrasQueTenganTamañoMayorQue7_false(self):
        cadena = "d3"
        self.assertFalse(self.p1.palabrasQueTenganTamañoMayorQue7(cadena))

    def test_deletarVocalesDeUnaCadena(self):
        cadena = "keloke"
        self.assertEqual(self.p1.deletarVocalesDeUnaCadena(cadena), "klk")

    def test_annadirZDespuesDeUnaA_false(self):
        cadena = "orco"
        self.assertEqual(self.p1.annadirZDespuesDeUnaA(cadena), "orco")

    def test_annadirXTresPosicionesMasDeUnaJ(self):
        cadena = "joder"
        self.assertEqual(self.p1.annadirXTresPosicionesMasDeUnaJ(cadena), "jodxer")

    def test_entero_a_romano(self):
        numero = 2021
        self.assertEqual(self.p1.entero_a_romano(numero), "MMXXI")

    def test_entero_a_romano_2(self):
        numero = 1094
        self.assertEqual(self.p1.entero_a_romano(numero), "MXCIV")

    def test_entero_a_romano_3(self):
        numero = 47
        self.assertEqual(self.p1.entero_a_romano(numero), "XLVII")

if __name__ == '__main__':
    unittest.main()

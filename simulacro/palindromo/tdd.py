import unittest
from palindromo_capicua import Cliserv

class CliservTest(unittest.TestCase):

    # Comprueba que la palabra introducida es un palíndromo
    def test_palindromo(self):
        cliserv = Cliserv()
        palabra = "ana"
        es_valido = cliserv.esPalindromo(palabra)
        self.assertTrue(es_valido)

    # Comprueba que la palabra no es un palíndromo
    def test_no_palindromo(self):
        cliserv = Cliserv()
        palabra = "hola"
        es_valido = cliserv.esPalindromo(palabra)
        self.assertFalse(es_valido)

    # Comprueba que el número es capicúa
    def test_capicua(self):
        cliserv = Cliserv()
        numero = "2002"
        es_valido = cliserv.esCapicua(numero)
        self.assertTrue(es_valido)

    # Comprueba que el número no es capicúa
    def test_no_capicua(self):
        cliserv = Cliserv()
        numero = "428"
        es_valido = cliserv.esCapicua(numero)
        self.assertFalse(es_valido)

    # Comprueba que no es un número natural
    def test_no_natural(self):
        cliserv = Cliserv()
        cadena = "hola"
        es_valido = cliserv.esNatural(cadena)
        self.assertFalse(es_valido)

    # Comprueba que es un número natural
    def test_natural(self):
        cliserv = Cliserv()
        cadena = "AA"
        es_valido = cliserv.esNatural(cadena)
        self.assertTrue(es_valido)

    # Comprueba que contiene caracteres especiales
    def test_contiene_caracteres_especiales(self):
        cliserv = Cliserv()
        self.assertFalse(cliserv.contieneCaracteresEspeciales("raul"))
        self.assertTrue(cliserv.contieneCaracteresEspeciales("??"))
        self.assertFalse(cliserv.contieneCaracteresEspeciales("12"))

if __name__ == '__main__':
    unittest.main()

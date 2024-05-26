class Kata:

    def esPalindromo(self, cadena):
        cadena = cadena.lower()
        return cadena == cadena[::-1]

    def esVocal(self, cadena):
        contador = sum(1 for caracter in cadena if caracter.lower() in "aeiou")
        return contador

    def startsWithA(self, cadena):
        return cadena.startswith("a") or cadena.startswith("A")

    def palabrasConVocalesImpares(self, cadena):
        contador = sum(1 for vocal in cadena if vocal.lower() in "aeiouAEIOU")
        return cadena if contador % 2 == 1 else False

    def palabrasQueTenganTamañoMayorQue7(self, cadena):
        return cadena if len(cadena) >= 7 else False

    def deletarVocalesDeUnaCadena(self, cadena):
        cadenaConsonantes = ''.join(caracter for caracter in cadena if caracter.lower() not in "aeiou")
        return cadenaConsonantes

    def annadirZDespuesDeUnaA(self, cadena):
        cadena_nueva = cadena.replace("a", "az").replace("A", "Az")
        return cadena_nueva

    def annadirXTresPosicionesMasDeUnaJ(self, cadena):
        posicion_j = cadena.lower().find("j")
        if posicion_j != -1:
            cadena_nueva = cadena[:posicion_j + 3] + "x" + cadena[posicion_j + 3:]
            return cadena_nueva
        else:
            return cadena

    def entero_a_romano(self, numero):
        valores = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
            90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        resultado = ''
        for valor, simbolo in valores.items():
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado

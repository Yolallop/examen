class Cliserv:

    def pide(self):
        peticion = input("Introduzca una palabra o un número natural: ")
        return peticion

    def esNatural(self, peticion):
        
        try:
            int(peticion)
            return True
        except ValueError:
            return False

    def esPalindromo(self, peticion):
      
        peticion = peticion.lower().replace(" ", "")
        return peticion == peticion[::-1]

    def esCapicua(self, peticion):
       
        return str(peticion) == str(peticion)[::-1]
    
    def contieneCaracteresEspeciales(self, peticion):
        for c in peticion:
            if not c.isalnum():
                return True
        return False

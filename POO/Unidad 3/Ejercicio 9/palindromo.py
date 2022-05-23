class Palindromo:
    __palabra: str

    def __init__(self, palabra: str):
        self.__palabra = palabra

    def setPalabra(self, nuevaPalabra: str):
        self.__palabra = nuevaPalabra

    def esPalindromo(self):
        i = 0
        j = -len(self.__palabra)

        bandera = True

        while i < -j and bandera:
           if self.__palabra[i] != self.__palabra[i]:
               bandera = False
           else:
               i += 1
               j += 1
		
        return bandera
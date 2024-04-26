class Palindromo:
    __palabra: str # = None
    def __init__(self, palabra):
        self.__palabra = palabra
	
    def esPalindromo(self):
        if self.__palabra == '':
            return True

        i = 0
        j = len(self.__palabra) - 1 #

        bandera = True

        while i < abs(j) and bandera:
            if self.__palabra[i] != self.__palabra[j]: #
                bandera=False
            else:
                i += 1
                j -= 1

        return bandera

    def setPalabra(self, nuevaPalabra):
        if type(nuevaPalabra) != str:
            raise TypeError("La palabra debe ser un string")
		
        self.__palabra = nuevaPalabra
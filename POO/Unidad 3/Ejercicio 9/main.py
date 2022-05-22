"""
Testing

Dada la Clase Palindromo, que tiene como atributo una palabra y una función para chequear que la palabra es palíndromo o no, dicha función devuelve True si la palabra es palíndromo, False en caso contrario.

Regla de Negocio: una palabra es palíndromo si se puede chequear que se escribe igual de adelante hacia atrás y de atrás hacia adelante. Ejemplos: ana, ANA, anana, MENEM.

La implementación provista por una empresa subcontratista, “Mi Softw@re siempre @nda”, es la siguiente:

class Palindromo:
    __palabra = None
    def __init__(self, palabra):
        self.__palabra = palabra
    def esPalindromo(self):
        i=0
        j=-len(self.palabra)
        bandera = True
        while i<abs(j) and bandera:
           if self.__palabra[i] != self.__palabra[i]:
               bandera=False
           else:
               i += 1
               j += 1
        return bandera
    def setPalabra(self, nuevaPalabra):
        self.__palabra = nuevaPalabra

 Su tarea consiste en diseñar los tests para probar la implementación realizada por la empresa, en caso de que alguno no funcione, deberá corregir la función correspondiente.
"""
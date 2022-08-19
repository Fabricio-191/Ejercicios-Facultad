import numpy as np

class PilaDoble: # lifo
    __elementos: np.ndarray
    __tope1: int = -1
    __tope2: int
    __tamañoTotal: int

    def __init__(self, tamaño, tipo):
        self.__tamañoTotal = tamaño
        self.__tope2 = tamaño
        self.__elementos = np.empty(tamaño, dtype=tipo)
        for i in range(tamaño):
            self.__elementos[i] = 0
    
    def espacioLibre(self):
        return self.__tope2 - self.__tope1 - 1

    def add1(self, obj):
        if self.espacioLibre() == 0:
            raise Exception('No queda espacio en la pila')

        self.__tope1 += 1
        self.__elementos[self.__tope1] = obj

    def get1(self):
        if self.__tope1 == 0:
            raise Exception('No quedan elementos en la pila 1')

        self.__tope1 -= 1
        return self.__elementos[self.__tope1 + 1]

    def getTamaño1(self):
        return self.__tope1 + 1

    def getTamaño2(self):
        return self.__tamañoTotal - self.__tope2

    def add2(self, obj):
        if self.espacioLibre() == 0:
            raise Exception('No queda espacio en la pila')

        self.__tope2 -= 1
        self.__elementos[self.__tope2] = obj

    def get2(self):
        if self.__tope2 == self.__tamañoTotal:
            raise Exception('No quedan elementos en la pila 1')

        self.__tope2 += 1
        return self.__elementos[self.__tope2 + 1]

    def __str__(self):
        return str(list(self.__elementos))

pila = PilaDoble(15, int)

for i in range(5):
    pila.add1(i)

for i in range(5):
    pila.add2(-i)

print(pila.espacioLibre())
print(pila)
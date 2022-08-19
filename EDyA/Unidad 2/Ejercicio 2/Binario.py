from typing import Any

class Pila: # lifo
    __elementos: list[Any]

    def __init__(self):
        self.__elementos = []
    
    def getTamaño(self):
        return len(self.__elementos)

    def add(self, obj):
        self.__elementos.append(obj)

    def get(self):
        if self.getTamaño() == 0:
            raise Exception('No quedan elementos en la pila')

        return self.__elementos.pop()

def pasarABinario(num: int):
    pila = Pila()

    while num != 0:
        resto = num % 2
        pila.add(resto)
        num //= 2

    string: str = ''

    while pila.getTamaño() != 0:
        string += str(pila.get())

    return string

print(pasarABinario(120)) # 1111000
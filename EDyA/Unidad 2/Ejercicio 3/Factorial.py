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

def factorial(num: int):
    pila = Pila()

    while num != 0:
        pila.add(num)
        num -= 1

    resultado: int = 1

    while pila.getTamaño() != 0:
        resultado *= pila.get()

    return resultado

print(factorial(6))
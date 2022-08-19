from __future__ import annotations
from typing import Any

class Nodo:
    __dato: Any
    __next: Nodo | None

    def __init__(self, dato, next: Nodo | None = None):
        self.__dato = dato
        self.__next = next

    def getDato(self):
        return self.__dato

    def getNext(self) -> Nodo | None:
        return self.__next

    def setNext(self, next: Nodo | None):
        self.__next = next

class Pila: # lifo
    __cabeza: Nodo | None
    __tamaño: int

    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0
    
    def getTamaño(self):
        return self.__tamaño

    def add(self, dato):
        self.__cabeza = Nodo(dato, self.__cabeza)

    def get(self):
        nodo = self.__cabeza

        if nodo is None:
            raise Exception('No hay elementos en la lista')

        self.__cabeza = nodo.getNext()

        return nodo.getDato()


pila = Pila()

pila.add(4)
pila.add(5)
pila.add(6)

print(pila.get())
print(pila.get())
print(pila.get())
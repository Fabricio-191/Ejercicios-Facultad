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


class PilaConTipo: # lifo
    __elementos: list[Any]
    __tipo: Any

    def __init__(self, tipo):
        self.__elementos = []
        self.__tipo = tipo
    
    def getTamaño(self):
        return len(self.__elementos)

    def add(self, obj):
        if not isinstance(obj, self.__tipo):
            raise Exception('El objeto introducido no es del tipo correcto')

        self.__elementos.append(obj)

    def get(self):
        if self.getTamaño() == 0:
            raise Exception('No quedan elementos en la pila')

        return self.__elementos.pop()

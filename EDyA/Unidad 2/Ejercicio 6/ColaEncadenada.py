class Nodo:
    __elem = None
    __next = None

    def __init__(self, elem, next = None):
        self.__elem = elem
        self.__next = next

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def getDato(self):
        return self.__elem

class ColaEnlazada:
    __cabeza = None
    __cola = None

    def __init__(self):
        self.__cabeza = None
        self.__cola = None

    def add(self, elem):
        nuevo = Nodo(elem)
        
        if self.__cola == None:
            self.__cabeza = nuevo
        else:
            self.__cola.setNext(nuevo)

        self.__cola = nuevo

    def get(self):
        if self.__cabeza == None:
            raise Exception('La cola no tiene elementos')

        nodo = self.__cabeza
        self.__cabeza = nodo.getNext()

        return nodo
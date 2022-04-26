from math import sqrt
class Punto:
    __x = -1
    __y = 0
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    def __str__(self):
        return '({}, {})'.format(self.__x, self.__y)
    def setX(self, v):
        self.__x = v
    def getX(self):
        return self.__x
    def setY(self, v):
        self.__y = v
    def getY(self):
        return self.__y
    def mostrarDatos(self):
        print("(x,y) = (",self.__x,',', self.__y,")")
        print('Dirección de memoria de self en mostrarDatos:{}'.format(hex(id(self))))
    def mover(self, x, y):
        self.setX(x)
        self.setY(y)
    def distanciaEuclidea(self, otroPunto):
        distancia = sqrt((otroPunto.__x-self.__x)**2+(otroPunto.__y-self.__y)**2)
        return distancia
if __name__=='__main__':
    unPunto = Punto(3,4)
    print('Direccion de memoria de instancia unPunto: {}'.format(hex(id(unPunto))))
    unPunto.mostrarDatos()
    otroPunto = Punto(4,7)
    unPunto.mostrarDatos()
    otroPunto.mostrarDatos()
    tercerPunto = Punto()
    tercerPunto.mostrarDatos()
    unPunto.mover(8, -17)
    unPunto.mostrarDatos()

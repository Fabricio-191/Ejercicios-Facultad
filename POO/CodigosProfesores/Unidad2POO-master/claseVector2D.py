# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:14:59 2020

@author: morte
"""

class Vector2D:
    __x=0.0
    __y=0.0
    def __init__(self, x=-1, y=-1):
        self.__x=x
        self.__y=y
    def __str__(self):
        return '<x, y>=<{},{}>'.format(self.__x, self.__y)
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def __add__(self, otroVector):
        if type(self) == type(otroVector):
            return Vector2D(self.__x+otroVector.getX(), self.__y+otroVector.getY())
        else:
            if type(otroVector)==int or type(otroVector)==float:
                return Vector2D(self.__x+otroVector, self.__y)
    def __sub__(self, otroVector):
        return Vector2D(self.__x-otroVector.getX(), self.__y-otroVector.getY())
    def __mul__(self, escalar):
        return Vector2D(self.__x*escalar, self.__y*escalar)
    def __rmul__(self, escalar):
        return Vector2D(self.__x*escalar, self.__y*escalar)
    
if __name__=='__main__':
    a = Vector2D(4, 5)
    b = Vector2D(2, 7)
    suma = a + b
    resta = a - b
    s = a + 5
    productoEscalar =  1.5 * a
    print(a)
    print(b)
    print('Suma a+b:',suma)
    print('Suma a+5:',s)
    print('Resta a-b',resta)
    print('Producto por un escalar  1.5 * a',productoEscalar)
    pe = b * 3
    print('Producto escalar de a * 3', pe)

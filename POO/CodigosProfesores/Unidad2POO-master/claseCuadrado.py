# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 08:02:09 2020

@author: morte
"""
import numpy as np
class Cuadrado:
    __lado = 0.0
    def __init__(self, lado):
        self.__lado = lado
    def __str__(self):
        return  "%4d   %6.2f   %8.2f" % (self.__lado, self.perimetro(), self.superficie())
    def setLado(self, lado):
        self.__lado = lado
    def getLado(self):
        return self.__lado
    def perimetro(self):
        return self.__lado * 4
    def superficie(self):
        return self.__lado**2
    
class ManejadorCuadrados:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=5):
        self.__cuadrados = np.empty(dimension, dtype=Cuadrado)
        self.__cantidad = 0
        self.__dimension = dimension
    def __str__(self):
        s = "Cuadrado lado perímetro superficie\n"
        for i in range(self.__cantidad):
            unCuadrado = self.__cuadrados[i]
            s += '{0:8}'.format(i+1)+str(unCuadrado) + '\n'
        return s
    def agregarCuadrado(self, unCuadrado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__cuadrados.resize(self.__dimension)
        self.__cuadrados[self.__cantidad]=unCuadrado
        self.__cantidad += 1
    def getCuadrado(self, indice):
        return self.__cuadrados[indice]
    def perimetroPromedio(self):
        promedio = 0.0
        for i in range(self.__cantidad):
            promedio += self.getCuadrado(i).perimetro()
        return promedio/self.__cantidad
    def cantidadCuadrados(self):
        cantidad = 0
        promedio = self.perimetroPromedio()
        for i in range(self.__cantidad):
            if self.getCuadrado(i).perimetro()>promedio:
                cantidad+=1
        return cantidad        
    def testManejadorCuadrados(self):
        unCuadrado = Cuadrado(4)
        self.agregarCuadrado(unCuadrado)
        otroCuadrado = Cuadrado(7.5)
        self.agregarCuadrado(otroCuadrado)
        unCuadrado = Cuadrado(9.97)
        self.agregarCuadrado(unCuadrado)
        
if __name__ == '__main__':
    mCuadrados = ManejadorCuadrados(3,5)
    mCuadrados.testManejadorCuadrados()
    print(mCuadrados)
    print('Cantidad de Cuadrados con perímetro > que perímetro promedio: {}'.format(mCuadrados.cantidadCuadrados()))
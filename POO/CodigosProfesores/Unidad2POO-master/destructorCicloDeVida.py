# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 07:35:11 2020

@author: morte
"""
class A:
    __b=None
    def __init__(self, unObjetoB):
        self.__b=unObjetoB
    def __del__(self):
        print('Chau objeto A')

class B:
    __a=None
    def __init__(self):
        self.__a=A(self)
    def __del__(self):
        print('Chau Objeto B')
     
def funcionCreaB():
    b = B()
    del b
    
class CicloDeVida:
    __nombre=None
    def __init__(self, nombre):
        print('Hola: ',nombre)
        self.__nombre = nombre
    def vida(self):
        print(self.__nombre)
    def __del__(self):
        print('Chau... ',self.nombre)
def funcion():
    o = CicloDeVida('Violeta')
    o.vida()
if __name__=='__main__':
    objeto = CicloDeVida('Carlos')
    objeto.vida()
    del objeto
    funcion()
    funcionCreaB()
  

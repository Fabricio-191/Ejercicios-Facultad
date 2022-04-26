# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:58:31 2020

@author: morte
"""
class Libro:
    def __init__(self, idLibro, titulo, autor, edicion,  editorial, anio):
        self.__idLibro = idLibro
        self.__titulo = titulo
        self.__autor = autor
        self.__edicion = edicion
        self.__editorial = editorial
        self.__anio = anio
    def __str__(self):
        return "%s %s %s %s %s %s" % (self.__idLibro, self.__titulo, self.__autor, self.__edicion, self.__editorial, self.__anio)
    def getIdLibro(self):
        return self.__idLibro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getEdicion(self): 
        return self.__edicion
    def getEditorial(self):
        return self.__editorial
    

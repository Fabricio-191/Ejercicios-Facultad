# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:59:57 2020

@author: morte
"""
import csv
from claseLibro import Libro
class ManejadorLibros:
    def __init__(self):
        self.__listaLibros = []
    def __str__(self):
        s = ""
        for libro in self.__listaLibros:
            s += str(libro) + '\n'
        return s
    def agregarLibro(self,unLibro):
        self.__listaLibros.append(unLibro)
    def buscarLibro(self, clave):
        for indice, libro in enumerate(self.__listaLibros):
            if libro.getIdLibro() == clave:
                return indice
    def borrarLibro(self, clave):
        indice = self.buscarLibro(clave)
        if indice != None:
            self.__listaLibros.pop(indice)
            return indice
    def getLibro(self, indice):
        return self.__listaLibros[indice]
    def testLibros(self):
        archivo = open('librosPOO.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
              idLibro = int(fila[0])
              titulo = fila[1]
              autor = fila[2]
              edicion = fila[3]
              editorial = fila[4]
              anio = int(fila[5])
              unLibro = Libro(idLibro,titulo,autor,edicion, editorial,anio)
              self.agregarLibro(unLibro)
        archivo.close()
if __name__=='__main__':
    ml = ManejadorLibros()
    ml.testLibros()
    print('Colección de libros inicial')
    print(ml)
    idLibro = int(input('Ingrese idLibro a Buscar: '))
    indice=ml.buscarLibro(idLibro)
    if indice == None:
        print('El idLibro {} no corresponde a un libro de la colección'.format(idLibro))
    else:
        libro = ml.getLibro(indice)
        print ('idLibro: {}, título: {}, autor: {}'.format(idLibro, libro.getTitulo(),libro.getAutor()))
    idLibro = int(input('Ingrese idLibro a Borrar: '))
    indice = ml.borrarLibro(idLibro)
    if indice != None:
        libro = ml.getLibro(indice)
        print('El libro {} se borró de la colección'.format(libro.getTitulo()))
    else:
        print('El idLibro {}, no corresponde a un libro de la colección'.format(idLibro))
    print('Colección de libros final')
    print (ml)
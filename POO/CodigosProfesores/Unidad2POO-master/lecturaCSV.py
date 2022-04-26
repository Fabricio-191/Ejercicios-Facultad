# -*- coding: utf-8 -*-

"""
Created on Sun Jan 19 18:25:01 2020

@author: morte
"""


import csv
total = 0
lineaCompleta = []
archivo = open('compras.csv')
reader = csv.reader(archivo,delimiter=';')
for fila in reader:
    '''
    fila[0] es la descripción, fila[1] es la cantidad, fila[2] es el precio unitario
    el precio unitario viene con coma decimal, Python trabaja con punto decimal,
    por eso se reemplaza
    '''
    costo = float(fila[1]) * float(fila[2].replace(",","."))
    total += costo
    lineaCompleta = fila + [round(costo,2)]
    print(lineaCompleta)
print('Total de compra: {0:.2f}'.format(total))
archivo.close()
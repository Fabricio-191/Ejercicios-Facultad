"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones encadenamiento, utilizando como función de transformación de claves el método de plegado, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand.

Se pide informar:

1.    La longitud de cada una de las listas de claves sinónimas.
2.    La cantidad de esas listas que registran una longitud que varía en hasta 3 unidades, por exceso o por defecto, respecto al promedio de las longitudes de dichas listas.

Considerando:

1.    La cantidad de listas de claves sinónimas no es un número primo.
2.    La cantidad de listas de claves sinónimas sí es un número primo.
"""
from TablaHash import TablaHash
import random

def datasetWithoutDuplicates(dataset):
	yielded = []

	for key, value in reversed(dataset):
		if key not in yielded:
			yielded.append(key)
			yield key, value

def test(dataset, size, usarPrimo):
	table = TablaHash(size, usarPrimo)

	for key, value in dataset:
		table.insertar(key, value)

	for key, value in datasetWithoutDuplicates(dataset):
		assert table.buscar(key) == value

	prom = 0
	print(f'Tamaño {size} (tamaño real {table.getSize()})')
	for lista in table:
		prom += lista.getSize()
		print(lista.getSize(), end = ' ')

	prom /= table.getSize()

	cont = 0
	for lista in table:
		if abs(lista.getSize() - prom) >= 3:
			cont += 1
	print()
	print(f'Promedio de longitud de las listas: {prom}')
	print(f'Listas con longitud que varía en hasta 3 unidades respecto al promedio: {cont}')

if __name__ == '__main__':
	tamañoInicial = 1000
	dataset = [(random.randint(0, 1000000), i) for i in range(tamañoInicial)]

	print('Tabla Hash con tamaño no primo')
	test(dataset, tamañoInicial, False)
	print()
	print()
	print('Tabla Hash con tamaño primo')
	test(dataset, tamañoInicial, True)
	print()
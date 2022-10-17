"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones direccionamiento abierto, utilizando como función de transformación de claves el método de la división, procesando las claves sinónimas a través de la secuencia de Prueba Pseudo Random y considerando trabajar con 1000 claves numéricas que serán generadas pseudoaleatoriamente a través de la función rand.

Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en cuenta:

1.    El tamaño de la tabla Hash no es un número primo.
2.    El tamaño de la tabla Hash sí es un número primo.
"""
import random
from TablaHash import TablaHash

def getPrimeNumber(size):
	for i in range(size, 2 * size):
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			return i

	raise ValueError('No se encontró un número primo')

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

	table.getProbeLength()

	for key, value in datasetWithoutDuplicates(dataset):
		assert table.buscar(key) == value

	print(f'Tamaño {size} (tamaño real {table.getSize()})')
	print(f'Factor de carga: {table.calcularFactorCarga() * 100:.2f}%')
	print('Longitud de la secuencia de prueba:', table.getProbeLength())

if __name__ == '__main__':
	tamañoInicial = 1000
	dataset = [(random.randint(0, 1000000), i) for i in range(tamañoInicial)]

	print('Tabla Hash con tamaño no primo')
	test(dataset, tamañoInicial, False)
	print()
	print('Tabla Hash con tamaño primo')
	test(dataset, tamañoInicial, True)
"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones direccionamiento abierto, utilizando como función de transformación de claves el método de la división, procesando las claves sinónimas a través de la secuencia de Prueba Pseudo Random y considerando trabajar con 1000 claves numéricas que serán generadas pseudoaleatoriamente a través de la función rand.

Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en cuenta:

1.    El tamaño de la tabla Hash no es un número primo.
2.    El tamaño de la tabla Hash sí es un número primo.
"""
import random
from TablaHash import TablaHash

def test(dataset, size, usarPrimo):
	table = TablaHash(size, usarPrimo)

	for key, value in dataset:
		table.insertar(key, value)

	table.probeLength = 0

	for key, value in dataset:
		table.buscar(key)

	print(f'  Tamaño {size} (tamaño real {table.getSize()})')
	print(f'  Factor de carga: {table.calcularFactorCarga() * 100 :.2f}%')
	print(f'  Longitud promedio de la secuencia de prueba: {table.probeLength / 1000 :.2f}')

if __name__ == '__main__':
	tamañoInicial = 1000
	random.seed(111)
	dataset = [(random.randint(0, 1000000), i) for i in range(tamañoInicial)]

	print('Tabla Hash con tamaño no primo')
	test(dataset, tamañoInicial, False)
	print()
	print('Tabla Hash con tamaño primo')
	test(dataset, tamañoInicial, True)
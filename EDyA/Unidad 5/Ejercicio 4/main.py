"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones usando Buckets, utilizando como función de transformación de claves el método de extracción, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand; teniendo en cuenta:

Se pide informar:

1.    La cantidad de Buckets desbordados; esto es, todas sus componentes ocupadas.
2.    La cantidad de Buckets subocupados; esto es, menos de la tercera parte ocupada.

Considerando:

1.    La cantidad de Buckets del Área Primaria no es un número primo.          
2.    La cantidad de Buckets del Área Primaria sí es un número primo.
"""
from TablaHash import TablaHash
import string, random

def randomString(stringLength = 10):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

def test(dataset, size: int, bucketSize: int, usarPrimo: bool):
	table = TablaHash(size, bucketSize, usarPrimo)

	for key, value in dataset:
		table.insertar(key, value)

	print(f'Tamaño {size} (tamaño real {table.getSize()})')
	bucketsDesbordados = 0
	bucketsSubocupados = 0

	for bucket in table:
		if bucket.estaLleno():
			bucketsDesbordados += 1
		elif bucket.estaSubocupado():
			bucketsSubocupados += 1

	print(f'Buckets desbordados: {bucketsDesbordados}')
	print(f'Buckets subocupados: {bucketsSubocupados}')

if __name__ == '__main__':
	tamañoInicial = 100
	tamañoBucket = 15
	# random.seed(30)
	dataset = [(random.randint(0, 1000000), i) for i in range(tamañoInicial * 10)]

	print('Tabla Hash con tamaño no primo')
	test(dataset, tamañoInicial, tamañoBucket, False)
	print()
	print()
	print('Tabla Hash con tamaño primo')
	test(dataset, tamañoInicial, tamañoBucket, True)
	print()
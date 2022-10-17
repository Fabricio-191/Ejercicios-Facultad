"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones usando Buckets, utilizando como función de transformación de claves el método de extracción, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand; teniendo en cuenta:

Se pide informar:

1.    La cantidad de Buckets desbordados; esto es, todas sus componentes ocupadas.
2.    La cantidad de Buckets subocupados; esto es, menos de la tercera parte ocupada.

Considerando:

1.    La cantidad de Buckets del Área Primaria no es un número primo.          
2.    La cantidad de Buckets del Área Primaria sí es un número primo.
"""
import string, random

def randomString(stringLength = 10):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

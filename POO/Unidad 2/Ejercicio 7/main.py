
"""
EJERCICIO 7
Sobrecarga por derecha (reverse operators)
Dada la clase ViajeroFrecuente definida en el ejercicio 2 con las sobrecargas de operadores solicitadas en el ejercicio 6, resolver lo siguiente:
1-    Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero a través de la sobrecarga del operador igual (== o __eq__). Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar tanto v ==  100 como 100 == v.
2-    Acumular millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 + v.
3-    Canjear millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 - v.

"""

from Viajero import Viajero
from os import path

def test():
	viajero = Viajero(1, "0", "Juan", "Lendro", 23)

	assert viajero.cantidadTotaldeMillas() == 23
	assert viajero.obtenerNumero() == 1

	assert viajero > Viajero(0, "", "", "", 22)
	assert (viajero + 100).cantidadTotaldeMillas() == 123
	assert (viajero - 50).cantidadTotaldeMillas() == 73

	assert viajero == 73
	assert (100 + viajero).cantidadTotaldeMillas() == 173
	assert (50 - viajero).cantidadTotaldeMillas() == 123
	assert viajero == Viajero(1, "0", "Juan", "Lendro", 123)



if __name__ == '__main__':
	test()
	viajeros = Viajero.leerArchivo(path.dirname(__file__) + "/viajeros.csv")
	
	viajero = viajeros[0]

	print(viajero == viajeros[0])
	print(viajero == viajeros[1])
	print(viajero == 100)
	print(viajero == 200)

	viajero = 100 + viajero
	viajero.mostrar()

	viajero = 100 - viajero
	viajero.mostrar()
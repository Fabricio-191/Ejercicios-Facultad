
"""
Sobrecarga de operadores
Dada la clase ViajeroFrecuente definida en el ejercicio 2, resolver lo siguiente:
1-    Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).
2-    Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente forma v = v + 100.
3-    Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente forma v = v - 100.
"""

from Viajero import Viajero
from os import path

def test():
	viajero = Viajero(1, "0", "Juan", "Lendro", 23)

	assert viajero.cantidadTotaldeMillas() == 23
	assert viajero.obtenerNumero() == 1

	viajero.acumularMillas(7)
	assert viajero.cantidadTotaldeMillas() == 30

	viajero.canjearMillas(10)
	assert viajero.cantidadTotaldeMillas() == 20
	
	assert viajero > Viajero(0, "", "", "", 15)
	assert (viajero + 100).cantidadTotaldeMillas() == 120
	assert (viajero - 50).cantidadTotaldeMillas() == 70


if __name__ == '__main__':
	test()
	viajeros: list[Viajero] = Viajero.leerArchivo(path.dirname(__file__) + "/viajeros.csv")

	masMillas = max(viajeros).cantidadTotaldeMillas()
	for viajero in viajeros:
		if viajero.cantidadTotaldeMillas() == masMillas:
			viajero.mostrar()

	print('sobrecargas')

	viajero = viajeros[0]
	viajero.mostrar()
	viajero += 100
	viajero.mostrar()
	viajero -= 100
	viajero.mostrar()
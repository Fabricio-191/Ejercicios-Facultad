"""
b) Leer y procesar el archivo “aparatoselectronicos.json” para almacenar en la lista los aparatos  de la empresa.    
c) Implemente un programa que a través de un menú de opciones permita:

    * Insertar un aparato en la colección en una posición determinada.
    * Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).
    * Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.
	* Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.
    * Mostrar la marca de todos los lavarropas que tienen carga superior .
    * Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.
    * Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.
"""

from Menu import Menu

if __name__ == '__main__':
	menu = Menu('Menu principal')
	menu.iniciar()
	
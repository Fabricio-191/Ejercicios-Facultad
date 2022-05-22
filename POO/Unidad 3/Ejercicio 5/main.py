"""
Defina una interface con los siguientes métodos:

a- insertarElemento: para insertar un objeto en una posición determinada en una colección, teniendo en cuenta el manejo de excepciones cuando la posición donde se vaya a insertar no sea válida.

b- agregarElemento: para agregar un elemento al final de una colección.

c- mostrarElemento: dada una posición de la colección, mostrar los datos del elemento almacenado en dicha posición si esa posición es válida, en caso de que no sea válida lanzar una excepción que controle el error.
"""

from zope.interface import Interface, implementer

'''Declaración de interface ICajero
El Cajero solo puede buscar productos por descripción
el método declarado es
buscarProductoPorDescripcion(descripcion)
'''

class ICajero(Interface):
	def buscarProductoPorDescripcion(descripcion):
		pass

'''Declaración de interface ISupervisor
El Supervisor modificar el precio de un producto, que busca por código
Los métodos que declara la intereface es
buscarProductoPorCodigo(codigo)
modificarPrecioProducto(codigo, precio)
'''
class ISupervisor(Interface):
	def buscarProductoPorCodigo(codigo):
		pass

	def modificarPrecioProducto(codigo, precio):
		pass
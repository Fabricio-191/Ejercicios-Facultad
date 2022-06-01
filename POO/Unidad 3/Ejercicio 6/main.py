"""   
    * Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.
    * Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.
"""
from Menu import Menu
from src.GestorAparatos import GestorAparatos
from os import path


from src.Aparatos.Aparato import Aparato
from src.Aparatos.Heladera import Heladera
from src.Aparatos.Lavarropa import Lavarropa
from src.Aparatos.Televisor import Televisor

def leerAparato() -> Aparato:
	tipo = input('Ingrese el tipo de aparato: ')
	marca = input('Ingrese la marca: ')
	modelo = input('Ingrese el modelo: ')
	color = input('Ingrese el color: ')
	pais = input('Ingrese el pais: ')
	precio = float(input('Ingrese el precio: '))

	if tipo == 'Heladera':
		capacidad = float(input('Ingrese la capacidad: '))
		freezer = input('Tiene freezer? (Si/No): ') == 'Si'
		cyclica = input('Tiene cyclica? (Si/No): ') == 'Si'
		return Heladera(marca, modelo, color, pais, precio, capacidad, freezer, cyclica)
	elif tipo == 'Lavarropa':
		capacidad = float(input('Ingrese la capacidad: '))
		velocidad = int(input('Ingrese la velocidad: '))
		carga = input('Ingrese la carga: ')
		programas = int(input('Ingrese la cantidad de programas: '))
		return Lavarropa(marca, modelo, color, pais, precio, capacidad, velocidad, carga, programas)
	elif tipo == 'Televisor':
		resolucion = input('Ingrese la resolucion: ')
		sintonizador = input('Tiene sintonizador? (Si/No): ') == 'Si'
		tipoDefinicion = input('Ingrese el tipo de definicion: ')
		internet = input('Tiene internet? (Si/No): ') == 'Si'
		return Televisor(marca, modelo, color, pais, precio, resolucion, sintonizador, tipoDefinicion, internet)
	else:
		raise ValueError('Tipo de aparato invalido')

def opcion1(gestor: GestorAparatos):
	pos = int(input('Ingrese la posicion: '))
	aparato = leerAparato()
	gestor.insertarAparato(pos, aparato)

def opcion2(gestor: GestorAparatos):
	aparato = leerAparato()
	gestor.agregarAparato(aparato)

def opcion3(gestor: GestorAparatos):
	pos = int(input('Ingrese la posicion: '))

	print(gestor.obtenerAparato(pos).__class__.__name__)

def opcion4(gestor: GestorAparatos):
	print(gestor.conteoMarca('Philips'))

def opcion5(gestor: GestorAparatos):
	for elem in gestor.getLista():
		if isinstance(elem, Lavarropa):
			if elem.cargaSuperior():
				print(elem.getMarca())

def opcion6(gestor: GestorAparatos):
	for elem in gestor.getLista():
		print(elem.getMarca(), elem.getPais(), elem.cacularPrecioVenta())

def opcion7(gestor: GestorAparatos):
	gestor.guardar(path.dirname(__file__) + '/aparatos.json')

if __name__ == '__main__':
	gestorAparatos = GestorAparatos(path.dirname(__file__) + '/aparatos.json')
	menu = Menu('Menu principal')
	menu.registrarOpcion('1', 'Insertar un aparato', opcion1, gestorAparatos)
	menu.registrarOpcion('2', 'Agregar un aparato', opcion2, gestorAparatos)
	menu.registrarOpcion('3', 'Obtener un aparato', opcion3, gestorAparatos)
	menu.registrarOpcion('4', 'Contar aparatos de una marca', opcion4, gestorAparatos)
	menu.registrarOpcion('5', 'Listar aparatos de lavarropas que superen la carga', opcion5, gestorAparatos)
	menu.registrarOpcion('6', 'Listar aparatos con su precio de venta', opcion6, gestorAparatos)
	menu.registrarOpcion('7', 'Guardar aparatos', opcion7, gestorAparatos)
	menu.iniciar()

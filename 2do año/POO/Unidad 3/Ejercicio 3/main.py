from Menu import Menu
from src.GestorEquipos import GestorEquipos
from src.GestorJugadores import GestorJugadores
from src.GestorContratos import GestorContratos
from os import path

def pathRelativo(p: str) -> str:
	return path.join(path.dirname(__file__), p)

def crearContrato(gestorContratos: GestorContratos):
	dni = input("Ingrese el DNI del jugador: ")
	equipo = input("Ingrese el nombre del equipo: ")
	fechaInicio = input("Ingrese la fecha de inicio del contrato: ")
	fechaFin = input("Ingrese la fecha de finalización del contrato: ")
	pagoMensual = input("Ingrese el pago mensual: ")

	gestorContratos.crearContrato(fechaInicio, fechaFin, pagoMensual, dni, equipo)

def consultarContratosJugador(gestorContratos: GestorContratos):
	dni = input("Ingrese el DNI del jugador: ")
	contratos = gestorContratos.encontrarContratos(dni)

	if len(contratos) == 0:
		print("El jugador no está contratado")
	else:
		for contrato in contratos:
			print(f'Equipo: {contrato.getEquipo().getNombre()}')
			print(f'Fecha de finalización: {contrato.getFechaFinalizacion()}')

def contratosPorVencer(gestorContratos: GestorContratos):
	equipo = input("Ingrese el nobre del equipo: ")

	contratos = gestorContratos.encontrarContratosPorVencer(equipo)

	if len(contratos) == 0:
		print("No hay contratos por vencer")
	else:
		for contrato in contratos:
			print(f'DNI: {contrato.getJugador().getDNI()}')

def obtenerImporteContratos(gestorContratos: GestorContratos):
	nombreEquipo = input("Ingrese el nombre del equipo: ")
	importe = gestorContratos.getImporteContratos(nombreEquipo)

	print(f'El importe total de los contratos es: {importe}')

def guardarContratos(gestorContratos: GestorContratos):
	gestorContratos.guardarEn(pathRelativo('contratosNuevo.txt'))

if __name__ == '__main__':
	gestorEquipos = GestorEquipos(pathRelativo('equipos.csv'))
	gestorJugadores = GestorJugadores(pathRelativo('jugadores.csv'), gestorEquipos)
	gestorContratos = GestorContratos(pathRelativo('contratos.csv'), gestorEquipos, gestorJugadores)

	menu = Menu()
	menu.registrarOpcion('1', "Crear contrato", crearContrato, gestorContratos)
	menu.registrarOpcion('2', "Consultar contratos de jugador", consultarContratosJugador, gestorContratos)
	menu.registrarOpcion('3', "Contratos por vencer", contratosPorVencer, gestorContratos)
	menu.registrarOpcion('4', "Obtener importe de contratos", obtenerImporteContratos, gestorContratos)
	menu.registrarOpcion('5', "Guardar contratos", guardarContratos, gestorContratos)
	menu.iniciar()

"""
1
DNI 1
Equipo a
0/0/0000
0/0/0000
30000
"""
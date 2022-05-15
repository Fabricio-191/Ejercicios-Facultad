from Menu import Menu
from src.GestorEquipos import GestorEquipos
from src.GestorJugadores import GestorJugadores
from src.GestorContratos import GestorContratos
from os import path

"""
2. Crear un contrato para un jugador en un equipo: Se genera un contrato para un jugador en un equipo.
3. Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.
4. Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.
5. Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.
5. Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.
"""

def pathRelativo(p: str) -> str:
	return path.join(path.dirname(__file__), p)

def crearContrato(gestorContratos: GestorContratos):
	dni = input("Ingrese el DNI del jugador: ")
	equipo = input("Ingrese el nombre del equipo: ")
	fechaInicio = input("Ingrese la fecha de inicio del contrato: ")
	fechaFin = input("Ingrese la fecha de finalización del contrato: ")
	pagoMensual = input("Ingrese el pago mensual: ")

	gestorContratos.crearContrato(fechaInicio, fechaFin, pagoMensual, dni, equipo)

def contultarContratosJugador(gestorContratos: GestorContratos):
	dni = input("Ingrese el DNI del jugador: ")
	print(gestorContratos.consultarJugadorContratado(dni))

if __name__ == '__main__':
	gestorEquipos = GestorEquipos(pathRelativo('equipos.csv'))
	gestorJugadores = GestorJugadores(pathRelativo('jugadores.csv'), gestorEquipos)
	gestorContratos = GestorContratos(pathRelativo('contratos.csv'), gestorEquipos, gestorJugadores)

	menu = Menu()
	menu.registrarOpcion('1', "Crear contrato", crearContrato, gestorContratos)
	menu.iniciar()

"""
1
DNI 1
Equipo a
0/0/0000
0/0/0000
30000
"""
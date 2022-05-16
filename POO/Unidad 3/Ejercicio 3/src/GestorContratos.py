from .Contrato import Contrato
from .GestorEquipos import GestorEquipos
from .GestorJugadores import GestorJugadores
from csv import reader
import numpy as np
import datetime

class GestorContratos:
	__gestorEquipos: GestorEquipos
	__gestorJugadores: GestorJugadores
	__contratos: np.ndarray[Contrato, np.dtype[np.object0]]

	def __init__(self, archivo: str, gestorEquipos: GestorEquipos, gestorJugadores: GestorJugadores):
		self.__gestorEquipos = gestorEquipos
		self.__gestorJugadores = gestorJugadores
		self.__contratos = np.array(self.__leerArchivo(archivo)) # type: ignore

	def crearContrato(self, fechaInicio: str, fechaFin: str, pagoMensual: str, DNIjugador: str, nombreEquipo: str):
		jugador = self.__gestorJugadores.getJugador(DNIjugador)
		equipo = self.__gestorEquipos.getEquipo(nombreEquipo)

		self.__contratos = np.append( # type: ignore
			self.__contratos,
			Contrato(float(pagoMensual), fechaInicio, fechaFin, jugador, equipo) # type: ignore
		)

	def encontrarContratos(self, jugadorDNI: str) -> list[Contrato]:
		lista: list[Contrato] = []

		for contrato in self.__contratos:
			if contrato.getJugador().getDNI() == jugadorDNI:
				lista.append(contrato)

		return lista

	def getImporteContratos(self, nombreEquipo: str) -> float:
		importe = 0.0

		for contrato in self.__contratos:
			if contrato.getEquipo().getNombre() == nombreEquipo:
				importe += contrato.getPagoMensual()

		return importe

	"""
	Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.
	"""
	def encontrarContratosPorVencer(self, equipo: str) -> list[Contrato]:
		lista: list[Contrato] = []
		dentroDe6Meses = datetime.timedelta(days=180) + datetime.date.today()

		print(dentroDe6Meses)

		for contrato in self.__contratos:
			if contrato.getEquipo().getNombre() == equipo:
				print(contrato.getFechaFinalizacion())
				if contrato.getFechaFinalizacion() <= dentroDe6Meses:
					lista.append(contrato)

		return lista

	def guardarEn(self, archivo: str) -> None:
		with open(archivo, 'w') as file:
			file.write('PagoMensual;FechaInicio;FechaFin;DNIjugador;NombreEquipo\n')

			for contrato in self.__contratos:
				file.write(
					str(contrato.getPagoMensual()) + ';' +
					contrato.getFechaInicio() + ';' +
					contrato.getFechaFinalizacion() + ';' +
					contrato.getJugador().getDNI() + ';' +
					contrato.getEquipo().getNombre() + '\n'
				)

	def __leerArchivo(self, archivo: str) -> list[Contrato]:
		with open(archivo, 'r') as file:
			lector = reader(file, delimiter=';')
			next(lector, None)

			lista: list[Contrato] = []

			for line in lector:
				jugador = self.__gestorJugadores.getJugador(line[3])
				equipo = self.__gestorEquipos.getEquipo(line[4])

				lista.append(
					Contrato(float(line[0]), line[1], line[2], jugador, equipo)
				)

			return lista
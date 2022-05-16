import numpy as np
from csv import reader
from Cama import Cama
from GestorMedicamentos import GestorMedicamentos

class GestorCamas:
	__camas: np.ndarray[Cama, np.dtype[np.object0]]
	__gestorMedicamentos: GestorMedicamentos
	def __init__(self, camasPath: str, medicamentosPath: str):
		self.__camas = np.array( # type: ignore
			GestorCamas.leerArchivo(camasPath)
		)
		self.__gestorMedicamentos = GestorMedicamentos(medicamentosPath)

	def obtenerPaciente(self, NyA: str) -> Cama | None:
		for cama in self.__camas:
			if cama.obtenerNyA() == NyA:
				return cama
		
		return None

	def listarDatosYMedicamentos(self, NyA: str) -> None:
		cama = self.obtenerPaciente(NyA)
		if cama is None:
			print("Paciente no encontrado")
			return

		print(f"Paciente: {cama.obtenerNyA()}      Cama: {cama.obtenerID()}      Habitación: {cama.obtenerHabitacion()}")
		print(f"Diagnóstico: {cama.obtenerDiagnostico()}      Fecha de internación: {cama.obtenerFechaInternacion()}")

		self.__gestorMedicamentos.indicarMedicamentosADevolver(cama.obtenerID())

	def listarPorDiagnostico(self, diagnostico: str) -> None:
		for cama in self.__camas:
			if cama.obtenerDiagnostico() == diagnostico:
				print(f"Paciente: {cama.obtenerNyA()}      Cama: {cama.obtenerID()}      Habitación: {cama.obtenerHabitacion()}")
				print(f"Diagnóstico: {cama.obtenerDiagnostico()}      Fecha de internación: {cama.obtenerFechaInternacion()}")
				self.__gestorMedicamentos.indicarMedicamentosADevolver(cama.obtenerID())

	@staticmethod
	def leerArchivo(ruta: str) -> list[Cama]:
		with open(ruta, "r") as csv_file:
			csv_reader = reader(csv_file, delimiter=";")
			next(csv_reader, None)

			return list(map(
				lambda line: Cama(
					int(line[0]),
					int(line[1]),
					bool(line[2]),
					line[3],
					line[4],
					line[5],
					line[6]
				),
				csv_reader
			))


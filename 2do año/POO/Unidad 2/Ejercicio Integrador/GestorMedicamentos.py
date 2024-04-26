from Medicamento import Medicamento
from csv import reader

class GestorMedicamentos:
	__medicamentos: list[Medicamento]

	def __init__(self, ruta: str):
		self.__medicamentos = GestorMedicamentos.leerArchivo(ruta)

	def indicarMedicamentosADevolver(self, idCama: int) -> None:
		acum = 0

		print("Medicamento/monodroga           Presentacion          Cantidad    Precio")

		for medicamento in self.__medicamentos:
			if medicamento.getIdCama() == idCama:
				print(
					"{0:<30} {1:<20} {2:<10} {3:<10.2f}".format(
						medicamento.getNombreComercial(),
						medicamento.getPresentacion(),
						medicamento.getCantidadAplicada(),
						medicamento.getPrecio()
					)
				)
				acum += medicamento.getPrecio()

		print(f"Total: {acum}")

	@staticmethod
	def leerArchivo(rutaArchivo: str) -> list[Medicamento]:
		with open(rutaArchivo, "r") as csv_file:
			csv_reader = reader(csv_file, delimiter=";")
			next(csv_reader, None)

			return list(map(
				lambda line: Medicamento(
					int(line[0]),
					int(line[1]),
					line[2],
					line[3],
					line[4],
					int(line[5]),
					float(line[6])
				),
				csv_reader
			))


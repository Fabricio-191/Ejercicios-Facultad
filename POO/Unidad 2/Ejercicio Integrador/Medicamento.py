from __future__ import annotations

"""
A cada paciente internado, se le aplican medicamentos, los datos de los medicamentos se almacenan en un archivo “medicamentos.csv”, que guarda la siguiente información: idCama, idMedicamento (1 a 100),nombre comercial, monodroga, presentación, cantidad aplicada, precio total (este archivo se genera sin un orden particular). 
"""

class Medicamento:
	__idCama: int
	__idMedicamento: int
	__nombreComercial: str
	__monodroga: str
	__presentacion: str
	__cantidadAplicada: int
	__precioTotal: float

	def __init__(
		self,
		idCama: int,
		idMedicamento: int,
		nombreComercial: str,
		monodroga: str,
		presentacion: str,
		cantidadAplicada: int,
		precioTotal: float
	):
		self.__idCama = idCama
		
		if(idMedicamento > 100 or idMedicamento < 1):
			raise ValueError("El id de medicamento debe estar entre 1 y 100")

		self.__idMedicamento = idMedicamento
		self.__nombreComercial = nombreComercial
		self.__monodroga = monodroga
		self.__presentacion = presentacion
		self.__cantidadAplicada = cantidadAplicada
		self.__precioTotal = precioTotal

	def getNombreComercial(self) -> str:
		return self.__nombreComercial

	def getMonodroga(self) -> str:
		return self.__monodroga

	def getPresentacion(self) -> str:
		return self.__presentacion

	def getCantidadAplicada(self) -> int:
		return self.__cantidadAplicada

	def getPrecio(self) -> float:
		return self.__precioTotal

	def getIdCama(self) -> int:
		return self.__idCama

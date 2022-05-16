from __future__ import annotations

class Repartidor:
	__idRepartidor: int
	__apellido: str
	__nombre: str
	__telefono: str
	__tipoMovilidad: str # (‘B’ Bicicleta, ‘M’ Moto, ‘A’ Auto),
	__comision: float

	def __init__(self, linea: list[str]):
		self.__idRepartidor = int(linea[0])
		self.__apellido = linea[1]
		self.__nombre = linea[2]
		self.__telefono = linea[3]
		self.__tipoMovilidad = linea[4]
		self.__comision = float(linea[5])

	def getIdRepartidor(self) -> int:
		return self.__idRepartidor

	def getApellido(self) -> str:
		return self.__apellido

	def getNombre(self) -> str:
		return self.__nombre

	def getTelefono(self) -> str:
		return self.__telefono
	
	def getTipoMovilidad(self) -> str:
		return self.__tipoMovilidad

	def setComision(self, comision: float) -> None:
		self.__comision += comision

	def getComision(self) -> float:
		return self.__comision

	def __eq__(self, other: Repartidor) -> bool:
		if(type(other) != Repartidor):
			raise TypeError("No se puede comparar un repartidor con un objeto de otro tipo")

		return (
			self.__nombre == other.getNombre() and
			self.__apellido == other.getApellido() and
			self.__telefono == other.getTelefono()
		)

	def __gt__(self, other: Repartidor) -> bool:
		if(type(other) != Repartidor):
			raise TypeError("No se puede comparar un repartidor con un objeto de otro tipo")

		return (self.__comision > other.getComision())
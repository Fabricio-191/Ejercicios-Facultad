from pyparsing import srange
from .Personal import Personal

porcentajes = {
	"exclusivo": 0.5,
	"semiexclusivo": 0.2,
	"simple": 0.1
}

class Docente(Personal):
	__carrera: str
	__cargo: str
	__catedra: str
	__porcentaje: float

	def __init__(self, data: dict):
		super().__init__(data)
		self.__carrera = data['carrera']
		self.__cargo = data['cargo']		
		self.__catedra = data['catedra']
		self.__porcentaje = porcentajes[self.__cargo]

	def getCarrera(self):
		return self.__carrera

	def calcularSueldo(self):
		return super().calcularSueldo() + self.getSueldoBasico() * self.__porcentaje
		
	def setPorcentaje(self, porcentaje: float):
		self.__porcentaje = porcentaje
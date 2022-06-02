from csv import reader
import numpy as np
from .calefactorAGas import CalefactorAGas
from .calefactorElectrico import CalefactorElectrico
from .calefactor import Calefactor

class ColeccionCalefactores:
	__calefactores: np.ndarray
	__tamaño: int

	def __init__(self, tamaño: int, archivo: str, tipo):
		self.__calefactores = np.empty(tamaño, dtype=tipo)
		self.__tamaño = tamaño
		self.__leerArchivo(archivo, tipo)

	def __iter__(self):
		return iter(self.__calefactores)

	def menorCosto(self) -> Calefactor:
		menor = self.__calefactores[0]
		costo = menor.calcularCosto()

		for calefactor in self.__calefactores:
			if calefactor.calcularCosto() < costo:
				menor = calefactor
				costo = calefactor.calcularCosto()

		return menor

	def __leerArchivo(self, archivo: str, tipo):
		cont = 0

		with open(archivo, 'r') as f:
			for linea in reader(f, delimiter=';'):
				self.__calefactores[cont] = tipo(linea) # type: ignore	
				cont += 1

				if cont == self.__tamaño:
					break

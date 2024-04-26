from __future__ import annotations
from numpy.typing import NDArray
from typing import Any
import numpy as np

class TablaHashParaIPs:
	__size: int
	__table: NDArray[Any]

	def __init__(self, size: int) -> None:
		self.__size = size
		self.__table = np.full(self.__size, None)

	def __hash(self, ip: str) -> int:
		parts = ip.split('.')

		return int(parts[0]) * 2**24 + int(parts[1]) * 2**16 + int(parts[2]) * 2**8 + int(parts[3])

	def insertar(self, key: str, value):
		index = self.__hash(key)

		if self.__table[index] is not None:
			raise ValueError('Espacio en la tabla ya ocupado, hashing imperfecto')

		self.__table[index] = (key, value)

	def buscar(self, key: str):
		index = self.__hash(key)

		if self.__table[index] is None:
			return None
		
		if self.__table[index][0] != key:
			raise ValueError('Espacio en la tabla ya ocupado por otra ip, hashing imperfecto')

		return self.__table[index][1]

	def calcularFactorCarga(self):
		cantidad = sum(1 for i in self.__table if i is not None)

		return cantidad / self.__size

tabla = TablaHashParaIPs(256 ** 3)

for a in range(0, 256):
	print(a)
	for b in range(0, 256):
		for c in range(0, 256):
			tabla.insertar(f'0.{a}.{b}.{c}', 1)

print("Tamaño de la tabla", 256 ** 3)
print("Factor de carga", tabla.calcularFactorCarga())
# https://lite.ip2location.com/argentina-ip-address-ranges?lang=es
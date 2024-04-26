"""
idRepartidor;numeroPeido;Descripcion;Cantidad;PrecioUnitario;Estado
1;333;Medialunas por docena;2;750;N
"""

class Pedido:
	__idRepartidor: int
	__numeroPedido: int
	__descripcion: str
	__cantidad: int
	__precioUnitario: float
	__estado: str # ‘E’ Entregado, ‘N’ No entregado)

	def __init__(self, linea: list[str]):
		self.__idRepartidor = int(linea[0])
		self.__numeroPedido = int(linea[1])
		self.__descripcion = linea[2]
		self.__cantidad = int(linea[3])
		self.__precioUnitario = float(linea[4])
		self.__estado = linea[5]
	
	def getRepartidor(self) -> int:
		return self.__idRepartidor

	def getEstado(self) -> str:
		return self.__estado

	def getNumeroPedido(self) -> int:
		return self.__numeroPedido

	def getDescripcion(self) -> str:
		return self.__descripcion

	def getCantidad(self) -> int:
		return self.__cantidad

	def getPrecioUnitario(self) -> float:
		return self.__precioUnitario

	def getTotal(self) -> float:
		return self.__cantidad * self.__precioUnitario
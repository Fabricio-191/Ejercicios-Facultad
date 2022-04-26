"""
Métodos y Constructores con valores por defecto

Defina una clase Ventana con los siguientes atributos: título, valor de las coordenadas x e y del vértice superior izquierdo y valor de las coordenadas x e y del vértice inferior derecho. Implemente los métodos necesarios, para que pueda ejecutarse el programa dado.

Reglas de negocio:

    El menor valor para las coordenadas del vértice superior izquierdo es 0 para cada una.
    El mayor valor para las coordenadas del vértice inferior derecho es 500 para cada una.
    El desplazamiento por defecto de una ventana es en una unidad en la dirección correspondiente.

    El valor de x del vértice superior izquierdo siempre debe ser menor al valor de x del vértice inferior derecho.
    El valor de y del vértice superior izquierdo siempre debe ser menor al valor de y del vértice inferior derecho.
"""


class Ventana:
	__titulo: str
	__x1: int
	__y1: int
	__x2: int
	__y2: int

	def __init__(
		self,
		titulo: str,
		x1: int = 0, # el punto 1 es el vertice superior izquierdo
		y1: int = 0,
		x2: int = 400, # el punto 2 es el vertice inferior derecho
		y2: int = 400,
	):
		self.__titulo = titulo
		self.__x1 = x1
		self.__y1 = y1
		self.__x2 = x2
		self.__y2 = y2

		self.__validarPuntos()

	def __validarPuntos(self) -> None:
		if (
			self.__x1 < 0 or self.__y1 < 0 or
			self.__x2 > 500 or self.__y2 > 500 or
			self.__x1 > self.__x2 or self.__y1 > self.__y2
		):
			raise ValueError('Las cordenadas de los puntos son incorrectas')

	def getTitulo(self):
		return self.__titulo
	
	def alto(self) -> int:
		return self.__y2 - self.__y1

	def ancho(self):
		return self.__x2 - self.__x1

	def mostrar(self):
		print(f'Punto1: ({self.__x1}, {self.__y1})')
		print(f'Punto2: ({self.__x2}, {self.__y2})')

	def bajar(self, desplazamiento: int = 1):
		self.__y1 += desplazamiento
		self.__y2 += desplazamiento
		self.__validarPuntos()

	def subir(self, desplazamiento: int = 1):
		self.bajar(-desplazamiento)
	
	def moverDerecha(self, desplazamiento: int):
		self.__x1 += desplazamiento
		self.__x2 += desplazamiento
		self.__validarPuntos()
	
	def moverIzquierda(self, desplazamiento: int):
		self.moverDerecha(-desplazamiento)
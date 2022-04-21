"""
Métodos y Constructores con valores por defecto

Defina una clase Ventana con los siguientes atributos: título, valor de las coordenadas x e y del vértice superior izquierdo y valor de las coordenadas x e y del vértice inferior derecho. Implemente los métodos necesarios, para que pueda ejecutarse el programa dado.

Reglas de negocio:

    El menor valor para las coordenadas del vértice superior izquierdo es 0 para cada una.
    El mayor valor para las coordenadas del vértice inferior derecho es 500 para cada una.
    El desplazamiento por defecto de una ventana es en una unidad en la dirección correspondiente.

    El valor de x del vértice superior izquierdo siempre debe ser menor al valor de x del vértice inferior derecho.
    El valor de y del vértice superior izquierdo siempre debe ser menor al valor de y del vértice inferior derecho.

ventana

 Programa a ejecutar

if __name__ ==  '__main__':

    print('==== Ventana Inicio ====')

    ventanaInicio= Ventana('Inicio')

    ventanaInicio.mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))

    print('==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)

    ventanaCargar.mostrar()

    print('*** Mueve a la derecha ***')

    ventanaCargar.moverDerecha(10)

    ventanaCargar.mostrar()

    print('*** Mueve a la izquierda ***')

    ventanaCargar.moverIzquierda(10)

    ventanaCargar.mostrar()

    print('*** Bajar ***')

    ventanaCargar.bajar(10)

    ventanaCargar.mostrar()

    print('==== Ventana Borrar ====')

    ventanaBorrar = Ventana('Borrar', 10,20,100,200)

    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir(5)   

    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir()

    ventanaBorrar.mostrar()

    print('*** Bajar ***')

    ventanaBorrar.bajar()

    ventanaBorrar.mostrar()
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
		x2: int = 0, # el punto 2 es el vertice inferior derecho
		y2: int = 0,
	):
		self.__titulo = titulo
		self.__x1 = x1
		self.__y1 = y1
		self.__x2 = x2
		self.__y2 = y2

		if x1 < 0 or y1 < 0 or x2 > 500 or y2 > 500 or x1 >= x2 or y1 >= y2:
			raise ValueError('Las cordenadas de los puntos son incorrectas')

	def getTitulo(self):
		return self.__titulo
	
	def alto(self):
		return self.__y2 - self.__y1

	def ancho(self):
		return self.__x2 - self.__x1

	def mostrar(self):
		print('Ventana: {} Alto: {} Ancho: {}'.format(self.getTitulo(), self.alto(), self.ancho()))
	
	def moverDerecha(self, desplazamiento: int):
		self.__x1 += desplazamiento
		self.__x2 += desplazamiento
	
	def moverIzquierda(self, desplazamiento: int):
		self.__x1 -= desplazamiento
		self.__x2 -= desplazamiento

	def bajar(self, desplazamiento: int = 1):
		self.__y1 += desplazamiento
		self.__y2 += desplazamiento

	def subir(self, desplazamiento: int = 1):
		self.__y1 -= desplazamiento
		self.__y2 -= desplazamiento

	

	
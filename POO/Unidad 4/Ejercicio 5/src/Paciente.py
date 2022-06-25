def clasificarMCI(mci):
	valor = 0

	if mci < 18.5:
		valor = "Peso inferior al normal"
	elif  18.5 <= mci < 25:
		valor = "Peso normal"
	elif 25 <= mci < 30:
		valor = "Sobrepeso"
	else:
		valor = "Obesidad"

	return valor

class Paciente:
	__nombre: str
	__apellido: str
	__telefono: str
	__altura: float
	__peso: float

	def __init__(self, datos):
		self.__nombre = datos['nombre']
		self.__apellido = datos['apellido']
		self.__telefono = datos['telefono']
		self.__altura = float(datos['altura'])
		self.__peso = float(datos['peso'])
	
	def getApellido(self):
		return self.__apellido
	
	def getNombre(self):
		return self.__nombre

	def getTelefono(self):
		return self.__telefono

	def getAltura(self):
		return self.__altura

	def getPeso(self):
		return self.__peso

	def calcularMCI(self):
		return self.__peso / (self.__altura ** 2 / 100)

	def tipo(self):
		return clasificarMCI(self.calcularMCI())      

	def toJSON(self):
		return  {
			'apellido': self.__apellido,
			'nombre': self.__nombre,
			'telefono': self.__telefono,
			'peso': self.__peso,
			'altura': self.__altura
		}

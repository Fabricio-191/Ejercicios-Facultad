"""
Ejercicio 5
Datos miembro estáticos y Funciones miembro estáticas 

Un concesionario de automóviles ofrece distintos planes de ahorro y se requiere la definición de una clase “PlanAhorro” que represente a cada uno de ellos.

Los datos que es necesario registrar son: código del plan, modelo y versión del vehículo, valor del vehículo, cantidad de cuotas del plan, cantidad de cuotas que debe tener pagas para licitar el vehículo (los últimos dos atributos son los mismos para todos los planes).

El primer día hábil del mes se actualiza el valor del vehículo.
El importe de la cuota se calcula:
valor cuota = (importe vehículo / cantidad de cuotas) + importe vehículo * 0.10
Implemente un programa que: 

1-      Lea desde un archivo separado con “;” los datos de los planes y genere una lista que almacene instancias de la clase “PlanAhorro”.
2-      Presente un menú de opciones permita:

a.       Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente.
b.      Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.
c.       Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota).
d.      Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.
"""

class PlanAhorro:
	__codigo: int
	__modelo: str
	__version: str
	__valor: float
	__valorCuota: float
	__cuotas: int = 0
	__cuotasParaLicitar: int = 0

	def __init__(self, codigo: int, modelo: str, version: str, valor: float):
		self.__codigo = codigo
		self.__modelo = modelo
		self.__version = version
		self.actualizarValor(valor)

	def valorCuota(self) -> float:
		return self.__valorCuota
	
	def actualizarValor(self, valor):
		self.__valor = valor
		self.__valorCuota = (self.__valor / self.__cuotas) + self.__valor * 0.10

	def codigo(self) -> int:
		return self.__codigo

	def montoParaLicitar(self) -> float:
		return self.__cuotasParaLicitar * self.__valorCuota

	def modificarCuotasParaLicitar(self, cuotas: int):
		self.__cuotasParaLicitar = cuotas
	
	def mostrar(self):
		print(f'Código: {self.__codigo} Modelo: {self.__modelo} Versión: {self.__version} Valor: {self.__valor} Cantidad de cuotas: {self.__cuotas} Cantidad de cuotas para licitar: {self.__cuotasParaLicitar} Valor cuota: {self.__valorCuota}')

	@staticmethod
	def leerPlan(line: list[str]):
		cuotas = int(line[4])
		cuotasParaLicitar = int(line[5])

		if cuotas != PlanAhorro.__cuotas:
			PlanAhorro.__cuotas = cuotas
		if cuotasParaLicitar != PlanAhorro.__cuotasParaLicitar:
			PlanAhorro.__cuotasParaLicitar = cuotasParaLicitar

		return PlanAhorro(int(line[0]), line[1], line[2], float(line[3]))
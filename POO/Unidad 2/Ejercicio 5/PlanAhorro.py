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
from csv import reader

class PlanAhorro:
	codigo: int
	modelo: str
	version: str
	valor: float
	valorCuota: float
	cantidadCuotas: int = 0
	cantidadCuotasParaLicitar: int = 0

	def __init__(self, codigo: int, modelo: str, version: str, valor: float, cantidadCuotas: int, cantidadCuotasParaLicitar: int):
		self.codigo = codigo
		self.modelo = modelo
		self.version = version
		self.valor = valor
		self.cantidadCuotas = cantidadCuotas
		self.cantidadCuotasParaLicitar = cantidadCuotasParaLicitar
		self.valorCuota = (self.valor / self.cantidadCuotas) + self.valor * 0.10
	
	def actualizarValor(self, valor):
		self.valor = valor
		self.valorCuota = (self.valor / self.cantidadCuotas) + self.valor * 0.10
	
	def mostrar(self):
		print('Código: {} Modelo: {} Versión: {} Valor: {} Cantidad de cuotas: {} Cantidad de cuotas para licitar: {} Valor cuota: {}'.format(self.codigo, self.modelo, self.version, self.valor, self.cantidadCuotas, self.cantidadCuotasParaLicitar, self.valorCuota))
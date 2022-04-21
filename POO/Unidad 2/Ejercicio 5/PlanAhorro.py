
class PlanAhorro:
	def __init__(self, codigo, modelo, version, valor, cantidadCuotas, cantidadCuotasParaLicitar):
		self.codigo = codigo
		self.modelo = modelo
		self.version = version
		self.valor = valor
		self.cantidadCuotas = cantidadCuotas
		self.cantidadCuotasParaLicitar = cantidadCuotasParaLicitar
		self.valorCuota = 0
		self.valorCuota = (self.valor / self.cantidadCuotas) + self.valor * 0.10
	
	def actualizarValor(self, valor):
		self.valor = valor
		self.valorCuota = (self.valor / self.cantidadCuotas) + self.valor * 0.10
	
	def mostrar(self):
		print('Código: {} Modelo: {} Versión: {} Valor: {} Cantidad de cuotas: {} Cantidad de cuotas para licitar: {} Valor cuota: {}'.format(self.codigo, self.modelo, self.version, self.valor, self.cantidadCuotas, self.cantidadCuotasParaLicitar, self.valorCuota))
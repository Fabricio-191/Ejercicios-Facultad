class Cola:
	__elementos: list

	def __init__(self):
		self.__elementos = []

	def add(self, obj):
		self.__elementos.append(obj)

	def get(self):
		if len(self.__elementos) == 0:
			raise Exception('No quedan elementos en la cola')

		return self.__elementos.pop(0)
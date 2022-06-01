from .Personal import Personal

class PersonalApoyo(Personal):
	__categoria: str

	def __init__(self, categoria: str, **kwargs):
		super().__init__(**kwargs)
		self.__categoria = categoria
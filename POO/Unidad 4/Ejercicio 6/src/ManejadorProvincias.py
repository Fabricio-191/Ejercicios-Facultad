from .Provincia import Provincia
import json
import requests

apiKey = '153b49ce9f575264ee8c1e0880b2e9fe'
class ManejadorProvincias:
	__provincias: list[Provincia]
	__archivo: str

	def __init__(self, archivo: str):
		self.__archivo = archivo
		self.cargar()

	def __iter__(self):
		return iter(self.__provincias)

	def obtener(self, pos: int):
		if len(self.__provincias) > pos:
			return self.__provincias[pos]
		else:
			return None

	def agregar(self, provincia: Provincia):
		self.__provincias.append(provincia)
		self.guardar()
	
	def getDatosTiempo(self, provincia: str):
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={provincia}&appid={apiKey}')
		data = response.json()

		return {
			'temperatura': data['main']['temp'],
			'humedad': data['main']['humidity'],
			'sensacionTermica': data['wind']['feels_like'],
		}

	def cargar(self):
		with open(self.__archivo, 'r') as f:
			data = json.load(f)
			self.__provincias = [Provincia(d) for d in data]

	def guardar(self):
		with open(self.__archivo, 'w') as f:
			json.dump([p.toJSON() for p in self.__provincias], f)
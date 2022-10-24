import math, random

City = tuple[int, int]

class Path:
	__cities: list[City]
	travelledDistance: float

	def __init__(self, path, distance):
		self.__cities = path
		self.travelledDistance = distance

	def length(self):
		return len(self.__cities)

	def __contains__(self, city):
		return city in self.__cities

	def __add__(self, city: City):
		lastCity = self.__cities[-1]
		return Path(
			self.__cities + [city],
			self.travelledDistance + math.sqrt(
				(lastCity[0] - city[0]) ** 2 +
				(lastCity[1] - city[1]) ** 2
			)
		)

	def __repr__(self):
		return "Distance: {:.2f}, Path: {}".format(self.travelledDistance, self.__cities)

class TravellingSalesman:
	__cities: list[City]
	__start: City
	__lessDistance: float
	__solution: Path | None

	def __init__(self, cities: list[City]):
		self.__cities = cities

	def process(self, path: Path):
		if path.length() == len(self.__cities):
			finalPath = path + self.__start

			if finalPath.travelledDistance < self.__lessDistance:
				print(finalPath)
				self.__lessDistance = finalPath.travelledDistance
				self.__solution = finalPath
		elif path.travelledDistance < self.__lessDistance:
			for city in self.__cities:
				if city not in path:
					self.process(path + city)

	def resolve(self, start: City):
		self.__solution = None
		self.__lessDistance = float('inf')
		self.__start = start
		
		self.process(Path([self.__start], 0))

		if self.__solution is None:
			raise Exception('No se encontró solución')

		return self.__solution

	@staticmethod
	def generateCities(n: int = 10) -> list[City]:
		return [
			(random.randint(0, 100), random.randint(0, 100)) for i in range(n)
		]

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(10)
	print('Caminos posibles: ', math.factorial(len(cities) - 1) / 2)
	print('Ciudades: ', cities)

	tsp = TravellingSalesman(cities)

	solution = tsp.resolve(cities[0])
	print('Mejor solución:', solution)

"""
Caminos posibles:  181440.0
Ciudades:  [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (61, 70), (0, 74), (47, 82), (63, 34)]
Distance: 517.56, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (61, 70), (0, 74), (47, 82), (63, 34), (34, 61)]
Distance: 498.89, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (61, 70), (47, 82), (0, 74), (63, 34), (34, 61)]
Distance: 498.59, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (61, 70), (47, 82), (63, 34), (0, 74), (34, 61)]
Distance: 489.26, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (61, 70), (63, 34), (47, 82), (0, 74), (34, 61)]
Distance: 477.41, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (0, 74), (47, 82), (61, 70), (63, 34), (34, 61)]
Distance: 457.23, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (63, 34), (61, 70), (0, 74), (47, 82), (34, 61)]
Distance: 426.24, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (45, 16), (63, 34), (61, 70), (47, 82), (0, 74), (34, 61)]
Distance: 412.42, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (0, 74), (45, 16), (63, 34), (61, 70), (47, 82), (34, 61)]
Distance: 408.31, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (0, 74), (47, 82), (61, 70), (63, 34), (45, 16), (34, 61)]
Distance: 403.92, Path: [(34, 61), (33, 92), (96, 28), (39, 70), (34, 77), (47, 82), (61, 70), (63, 34), (45, 16), (0, 74), (34, 61)]
Distance: 402.48, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (0, 74), (39, 70), (34, 77), (47, 82), (61, 70), (63, 34), (34, 61)]
Distance: 397.90, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (0, 74), (34, 77), (39, 70), (47, 82), (61, 70), (63, 34), (34, 61)]
Distance: 380.95, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (63, 34), (39, 70), (34, 77), (61, 70), (47, 82), (0, 74), (34, 61)]
Distance: 379.25, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (63, 34), (39, 70), (34, 77), (0, 74), (47, 82), (61, 70), (34, 61)]
Distance: 366.84, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (63, 34), (39, 70), (61, 70), (47, 82), (34, 77), (0, 74), (34, 61)]
Distance: 363.33, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (63, 34), (61, 70), (39, 70), (34, 77), (47, 82), (0, 74), (34, 61)]
Distance: 355.61, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (63, 34), (61, 70), (39, 70), (47, 82), (34, 77), (0, 74), (34, 61)]
Distance: 346.72, Path: [(34, 61), (33, 92), (96, 28), (45, 16), (63, 34), (61, 70), (47, 82), (39, 70), (34, 77), (0, 74), (34, 61)]
Distance: 341.43, Path: [(34, 61), (33, 92), (39, 70), (96, 28), (45, 16), (63, 34), (61, 70), (47, 82), (34, 77), (0, 74), (34, 61)]
Distance: 340.59, Path: [(34, 61), (33, 92), (39, 70), (34, 77), (45, 16), (63, 34), (96, 28), (61, 70), (47, 82), (0, 74), (34, 61)]
Distance: 335.09, Path: [(34, 61), (33, 92), (39, 70), (34, 77), (0, 74), (45, 16), (96, 28), (63, 34), (61, 70), (47, 82), (34, 61)]
Distance: 326.77, Path: [(34, 61), (33, 92), (39, 70), (34, 77), (0, 74), (45, 16), (63, 34), (96, 28), (61, 70), (47, 82), (34, 61)]
Distance: 322.66, Path: [(34, 61), (33, 92), (39, 70), (34, 77), (0, 74), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (34, 61)]
Distance: 318.27, Path: [(34, 61), (33, 92), (39, 70), (34, 77), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (0, 74), (34, 61)]
Distance: 310.99, Path: [(34, 61), (33, 92), (34, 77), (39, 70), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (0, 74), (34, 61)]
Distance: 310.42, Path: [(34, 61), (33, 92), (34, 77), (0, 74), (45, 16), (63, 34), (96, 28), (61, 70), (47, 82), (39, 70), (34, 61)]
Distance: 308.77, Path: [(34, 61), (33, 92), (0, 74), (39, 70), (34, 77), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (34, 61)]
Distance: 304.20, Path: [(34, 61), (33, 92), (0, 74), (34, 77), (39, 70), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (34, 61)]
Distance: 303.98, Path: [(34, 61), (39, 70), (33, 92), (34, 77), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (0, 74), (34, 61)]
Distance: 297.18, Path: [(34, 61), (39, 70), (33, 92), (0, 74), (34, 77), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (34, 61)]
Distance: 293.05, Path: [(34, 61), (39, 70), (34, 77), (33, 92), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (0, 74), (34, 61)]
Distance: 286.26, Path: [(34, 61), (39, 70), (34, 77), (0, 74), (33, 92), (47, 82), (61, 70), (96, 28), (63, 34), (45, 16), (34, 61)]
Distance: 286.26, Path: [(34, 61), (45, 16), (63, 34), (96, 28), (61, 70), (47, 82), (33, 92), (0, 74), (34, 77), (39, 70), (34, 61)]
Mejor solución: Distance: 286.26, Path: [(34, 61), (45, 16), (63, 34), (96, 28), (61, 70), (47, 82), (33, 92), (0, 74), (34, 77), (39, 70), (34, 61)]
"""
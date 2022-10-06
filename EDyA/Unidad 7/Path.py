import math

City = tuple[int, int]

class Path:
	travelledDistance: float
	cities: list[City]

	def __init__(self, path, distance):
		self.cities = path
		self.travelledDistance = distance

	def length(self):
		return len(self.cities)

	def lastCity(self):
		return self.cities[-1]

	def __add__(self, city: City):
		lastCity = self.lastCity()
		return Path(
			self.cities + [city],
			self.travelledDistance + math.sqrt(
				(lastCity[0] - city[0]) ** 2 +
				(lastCity[1] - city[1]) ** 2
			)
		)

	def __iter__(self):
		return iter(self.cities)

	def __contains__(self, city: City):
		return city in self.cities

	def __repr__(self):
		return "Distance: {:.2f}, Path: {}".format(self.travelledDistance, self.cities)
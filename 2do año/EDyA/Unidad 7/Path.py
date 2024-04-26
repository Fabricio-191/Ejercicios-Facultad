import math

City = tuple[int, int]

class Path:
	distancesBetweenCities: dict[City, dict[City, float]] = {}
	cities: list[City]
	travelledDistance: float

	def __init__(self, path, distance):
		self.cities = path
		self.travelledDistance = distance

	def length(self):
		return len(self.cities)

	def __add__(self, city: City):
		return Path(
			self.cities + [city],
			self.travelledDistance + self.distancesBetweenCities[self.cities[-1]][city]
		)

	def __repr__(self):
		return "Distance: {:.2f}, Path: {}".format(self.travelledDistance, self.cities)
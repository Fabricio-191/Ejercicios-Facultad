from Path import Path
from TravellingSalesman import TravellingSalesman
from abc import abstractmethod

class Base:
	_problem: TravellingSalesman
	_lessDistance: float
	_solutions: list[Path]

	def __init__(self, problem: TravellingSalesman):
		self._problem = problem

	@abstractmethod
	def _process(self, path: Path):
		pass

	def __baseCase(self):
		start = self._problem.getStart()
		path = Path([start], 0)

		for i in range(len(self._problem.getCities()) - 1):
			closestCity = self._problem.getCities()[0]
			closestDistance = float('inf')

			for city in self._problem.getCities():
				if city not in path:
					distance = self._problem.distanceBetweenCities(path.getCities()[-1], city)

					if distance < closestDistance:
						closestDistance = distance
						closestCity = city

			path = path + closestCity

		baseCase = path + start
		
		self._solutions.append(baseCase)
		self._lessDistance = baseCase.getTravelledDistance()
		print('Caso base', baseCase)

	def resolve(self, baseCase = True):
		self._lessDistance = float('inf')
		self._solutions = []
		if baseCase: self.__baseCase()
		
		self._process(
			Path([self._problem.getStart()], 0)
		)

		return list(
			filter(lambda path: path.getTravelledDistance() == self._lessDistance, self._solutions)
		)
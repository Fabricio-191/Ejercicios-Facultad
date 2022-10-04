from Path import Path
from Graph import Graph
from TravellingSalesman import TravellingSalesman
from abc import abstractmethod

class Base:
	_problem: TravellingSalesman
	_lessDistance: float
	_solution: Path | None
	__graph: Graph | None

	def __init__(self, problem: TravellingSalesman):
		self._problem = problem
		self.__graph = None

	@abstractmethod
	def _process(self, path: Path):
		pass

	def _graph(self, path: Path):
		if path.length() == len(self._problem.getCities()) + 1:
			print(path)
			if self.__graph: self.__graph.updateBestPath(path)
		elif self.__graph: self.__graph.updatePath(path)

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

		self._solution = path + start
		
		self._lessDistance = self._solution.getTravelledDistance()
		self._graph(self._solution)
		print('Caso base')

	def resolve(self, baseCase = True, graph = True):
		self._lessDistance = float('inf')
		self._solution = None
		if graph: self.__graph = Graph(self._problem.getCities())
		if baseCase: self.__baseCase()
		
		self._process(
			Path([self._problem.getStart()], 0)
		)

		if self._solution is None:
			raise Exception('No se encontró solución')

		return self._solution
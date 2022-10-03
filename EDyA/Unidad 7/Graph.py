import matplotlib.pyplot as plt
from Path import Path, City
from time import sleep

class Graph:
	__cities: list[City]

	def __init__(self, cities: list[City]):
		self.__cities = cities
		self.__fig, self.__ax = plt.subplots(1, 2)
		self.__fig.set_size_inches(12, 6)
		self.__fig.show()
	
	def updateBestPath(self, path: Path):
		self.__ax[1].set_title('Mejor camino, distancia: {}'.format(path.getTravelledDistance()))
		self.__draw(self.__ax[1], path, 'blue', 'green')
		self.updatePath(path)
		sleep(1)
	
	__intento = 0
	def updatePath(self, path: Path):
		self.__intento += 1
		self.__ax[0].set_title('Intento: {}, distancia: {:.2f}'.format(self.__intento, path.getTravelledDistance()))
		self.__draw(self.__ax[0], path, 'blue', 'red')
		self.__fig.canvas.draw()
		self.__fig.canvas.flush_events()

	def __draw(self, axes, path: Path, citiesColor: str, plotColor: str):
		axes.clear()

		for city in self.__cities:
			axes.scatter(*city, color=citiesColor)

		x = []
		y = []
		for city in path.getCities():
			x.append(city[0])
			y.append(city[1])

		axes.plot(x, y, color=plotColor)
	
	def __del__(self):
		plt.close(self.__fig)
	
"""
https://upload.wikimedia.org/wikipedia/commons/2/2b/Bruteforce.gif
https://dynetx.readthedocs.io/en/latest/index.html
https://networkx.org/documentation/stable/index.html

import dynetx as dn

class Graph:
	__g: dn.DynGraph
	__currentPath: Path | None
	__currentBestPath: Path | None

	def __init__(self, cities: list[City]):
		self.__g = dn.DynGraph()
		self.__g.add_nodes_from(cities)
		self.__currentPath = None
		self.__currentBestPath = None

	def updateCurrentPath(self, path: Path):
		if self.__currentPath:
			self.__g.remove_edges_from(self.__currentPath.getCities())
		self.__currentPath = path
		self.__g.add_edges_from(path.getCities())

	def updateCurrentBestPath(self, path: Path):
		if self.__currentBestPath:
			self.__g.remove_edges_from(self.__currentBestPath.getCities())
		self.__currentBestPath = path
		self.__g.add_edges_from(path.getCities())
"""

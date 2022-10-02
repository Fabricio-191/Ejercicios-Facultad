from Path import Path, City

"""
https://upload.wikimedia.org/wikipedia/commons/2/2b/Bruteforce.gif
https://dynetx.readthedocs.io/en/latest/index.html
https://networkx.org/documentation/stable/index.html
"""

"""
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
	

import matplotlib.pyplot as plt

class Graph:
	__fig, __ax = plt.subplots()
	__currentBestPath: Path | None = None
	__currentPath: Path | None = None
	__cities: list[City]

	def __init__(self, cities: list[City]):
		self.__cities = cities
		self.__fig, self.__ax = plt.subplots()
		self.__updateGraph()
		self.__fig.show()
	
	def updateCurrentBestPath(self, path: Path):
		self.__currentBestPath = path
		self.__updateGraph()
	
	def updateCurrentPath(self, path: Path):
		self.__currentPath = path
		self.__updateGraph()

	def __updateGraph(self):
		self.__ax.clear()
		plt.title(f"Distance: {self.__currentBestPath.getTravelledDistance() if self.__currentBestPath else 0}")
		self.__drawCities()
		self.__drawCurrentBestPath()
		self.__drawCurrentPath()
		self.__fig.canvas.draw()
		self.__fig.canvas.flush_events()
	
	def __drawCities(self):
		for city in self.__cities:
			self.__ax.scatter(*city, color="black")
		
	def __drawCurrentBestPath(self):
		if self.__currentBestPath is not None:
			self.__drawPath(self.__currentBestPath, "red")
	
	def __drawCurrentPath(self):
		if self.__currentPath is not None:
			self.__drawPath(self.__currentPath, "blue")
		
	def __drawPath(self, path: Path, color: str):
		x = []
		y = []
		for city in path.getCities():
			x.append(city[0])
			y.append(city[1])

		self.__ax.plot(x, y, color=color)
	
	def __del__(self):
		plt.close(self.__fig)
	
def staticGraph(cities: list[City], path: Path):
	fig, ax = plt.subplots()
	ax.set_aspect('equal')

	for city in cities:
		ax.plot(*city, 'bo')
	
	x = []
	y = []
	for city in path.getCities():
		x.append(city[0])
		y.append(city[1])

	ax.plot(x, y, 'r-')

	plt.show()
from TravellingSalesman import TravellingSalesman
from Graph import Graph, staticGraph
from Algoritmos.RamificacionYPoda import ramificacionYPoda
from Algoritmos.BruteForce import bruteForce

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(10)
	print(cities)

	tsp = TravellingSalesman(cities, cities[0])

	bestSolutions = ramificacionYPoda(tsp)
	staticGraph(cities, bestSolutions[-1])

	tsp.restart()

	bestSolutions = bruteForce(tsp)
	staticGraph(cities, bestSolutions[-1])
	
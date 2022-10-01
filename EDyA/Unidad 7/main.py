from TravellingSalesman import TravellingSalesman
from Graph import Graph, staticGraph
from Algoritmos.RamificacionYPoda import RamificacionYPoda
from Algoritmos.BruteForce import BruteForce

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(10)

	tsp = TravellingSalesman(cities, cities[0])
	print(cities)

	bestSolutions = RamificacionYPoda(tsp).resolve()

	staticGraph(cities, bestSolutions[-1])

	
	tsp.restart()
	bestSolutions = BruteForce(tsp).resolve()

	staticGraph(cities, bestSolutions[-1])
	
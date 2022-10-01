from TravellingSalesman import TravellingSalesman
from Graph import Graph, staticGraph
from Algoritmos.RamificacionYPoda import RamificacionYPoda
from Algoritmos.BruteForce import BruteForce

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(10)
	print(len(cities), cities)

	tsp = TravellingSalesman(cities, cities[0])

	bestSolutions = RamificacionYPoda(tsp).resolve()
	staticGraph(cities, bestSolutions[-1])
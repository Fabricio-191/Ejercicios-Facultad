from TravellingSalesman import TravellingSalesman
import math

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(7)
	print('Caminos posibles: ', math.factorial(len(cities) - 1))
	print('Ciudades: ', cities)

	tsp = TravellingSalesman(cities)

	solution = tsp.resolve(cities[0], baseCase=True, graph=False)
	print('Mejor solución:', solution)

# [(64, 46), (38, 36), (0, 74), (95, 65), (19, 13), (3, 12), (91, 10), (78, 74), (45, 50), (58, 70)]
# [(1, 77), (55, 46), (50, 94), (44, 1), (15, 61), (10, 95), (95, 91)]
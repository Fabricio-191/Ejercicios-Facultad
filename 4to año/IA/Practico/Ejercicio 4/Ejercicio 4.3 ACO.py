import random
import numpy as np
import time

# Ejercicio 4.3) (0,8P) Resuelva el mismo problema anterior, pero tratando de que al partir de una ciudad y llegar a la misma en un 
# total de 5000Km recorra la mayor cantidad de ciudades. Encuentre una representación y análisis de la función objetivo que le permita 
# resolver el problema, mediante AG y ACO. Implementarlo en GAlib y ACO en la herramienta que el disponga. 

dirname = 'D:/Programacion/Ejercicios-Facultad/4to año/IA/Practico/Ejercicio 4'
ALPHA = 1
BETA = 2
RHO = 0.2
K = 1
ANTS = 100
ITERATIONS = 100

with open(f'{dirname}/DIST100a.TXT', 'r') as file:
	distances = {}

	data = file.read().strip().split('\n')
	for line in data:
		line = line.strip().split()[1:]
		ciudadA = int(line[0])
		ciudadB = int(line[1])
		distancia = float(line[2])
		distances[(ciudadA - 1, ciudadB - 1)] = distancia
		distances[(ciudadB - 1, ciudadA - 1)] = distancia

with open(f'{dirname}/DIST100.txt', 'r') as file:
	data = file.read().strip().split('\n')
	CITIES = []
	for line in data:
		x = float(line.split()[1])
		y = float(line.split()[2])
		CITIES.append((x, y))
	CITIES_QTY = len(CITIES)

feromones = [[1 for _ in range(CITIES_QTY)] for _ in range(CITIES_QTY)]
probabilities = [[0.0 for _ in range(CITIES_QTY)] for _ in range(CITIES_QTY)]

class Path:
	def __init__(self, path):
		self.path = path
		self.distance = self.__calculate_distance()

	def last_city(self):
		return self.path[-1]
	
	def add_city(self, city):
		self.path.append(city)
		self.distance = self.__calculate_distance()

	def distance_with_city(self, city):
		self.path.append(city)
		distance = self.__calculate_distance()

		self.path.pop()

		return distance

	def __calculate_distance(self):
		total_distance = 0

		for i in range(len(self.path) - 1):
			total_distance += distances[(self.path[i], self.path[i+1])]
			
		total_distance += distances[(self.path[-1], self.path[0])]

		return total_distance

def function_calc_probabilities():
	for i in range(0, CITIES_QTY):
		for j in range(0, CITIES_QTY):
			if i == j: continue
			probabilities[i][j] = (feromones[i][j] ** ALPHA) * ((1 / distances[(i, j)]) ** BETA)

	for i in range(0, CITIES_QTY):
		total = sum(probabilities[i])
		probabilities[i] = [p / total for p in probabilities[i]]

	return probabilities

def probabilites_ant(prob, visited):
	prob = [p if i not in visited.path else 0 for (i, p) in enumerate(prob)]
	total = sum(prob)
	prob = [p / total for p in prob]

	return prob

best_paths = []
for i in range(0, ITERATIONS):
	function_calc_probabilities()

	paths = []
	for ant in range(0, ANTS):
		path = Path([random.randint(0, CITIES_QTY - 1)]) ###

		while True:
			next_city = np.random.choice(
				range(0, CITIES_QTY),
				p=probabilites_ant(
					probabilities[path.last_city()].copy(),
					path
				)
			)
			if path.distance_with_city(next_city) > 5000: break
			path.add_city(next_city)

		paths.append(path)	

	for path in paths:
		for i in range(0, len(path.path) - 1):
			feromones[path.path[i]][path.path[i+1]] += K / path.distance
			feromones[path.path[i+1]][path.path[i]] += K / path.distance

	best_path = max(paths, key=lambda x: len(x.path))			
	best_paths.append(best_path.path)

# best solution
best_path = max(best_paths, key=lambda x: len(x))
print(len(best_path), best_path)

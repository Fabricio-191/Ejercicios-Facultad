CITIES_QTY = 100
distances = {}

with open('D:/Programacion/Ejercicios-Facultad/4to año/IA/Practico/Ejercicio 4/DIST100.TXT', 'r') as file:
	data = file.read().strip().split('\n')
	for line in data:
		line = line.strip().split()[1:]
		ciudadA = int(line[0])
		ciudadB = int(line[1])
		distancia = float(line[2])
		distances[(ciudadA - 1, ciudadB - 1)] = distancia
		distances[(ciudadB - 1, ciudadA - 1)] = distancia

class Solution:
	def __init__(self, path):
		self.path = path
		self.distance = self.calculate_distance()

	def calculate_distance(self):
		total_distance = 0

		for i in range(CITIES_QTY - 1):
			total_distance += distances[(self.path[i], self.path[i+1])]
			
		total_distance += distances[(self.path[-1], self.path[0])]

		return total_distance

class TabuSearch:
	def __init__(self, initial_path):
		self.best_solution = Solution(initial_path)
		self.tabu_list = []
		self.tabu_list_max_size = 100
		self.max_iterations = 300
		self.solutions_track = [self.best_solution]


	def get_neighbourhood(self, solution):
		neighbourhood = []

		for i in range(CITIES_QTY):
			for j in range(i + 1, CITIES_QTY):
				new_path = solution.path.copy()
				new_path[i], new_path[j] = new_path[j], new_path[i]
				neighbourhood.append(Solution(new_path))

		return neighbourhood
	
	def get_best_neighbour(self, neighbourhood):
		best_neighbour = neighbourhood[0]

		for neighbour in neighbourhood:
			if neighbour.distance < best_neighbour.distance and neighbour not in self.tabu_list:
				best_neighbour = neighbour

		return best_neighbour
	
	def solve(self):
		for _ in range(self.max_iterations):
			neighbourhood = self.get_neighbourhood(self.best_solution)
			best_neighbour = self.get_best_neighbour(neighbourhood)

			if best_neighbour.distance < self.best_solution.distance:
				self.best_solution = best_neighbour
				self.solutions_track.append(self.best_solution)

			self.tabu_list.append(best_neighbour)
			if len(self.tabu_list) > self.tabu_list_max_size:
				self.tabu_list.pop(0)

		return self.best_solution

def path_of_nearest_cities():
	path = [0]
	not_visited = list(range(1, CITIES_QTY))
	
	for _ in range(CITIES_QTY - 1):
		not_visited.sort(key=lambda x: distances[(path[-1], x)])
		path.append(not_visited.pop(0))

	return path

initial_solution = list(range(CITIES_QTY))
# initial_solution = path_of_nearest_cities()
# initial_solution = [ 0, 24, 77, 1, 17, 46, 40, 12, 28, 25, 37, 15, 36, 76, 56, 41, 33, 67, 7, 94, 86, 93, 38, 45, 74, 60, 82, 62, 66, 21, 18, 23, 83, 70, 89, 81, 6, 78, 85, 98, 35, 97, 14, 16, 73, 71, 26, 44, 54, 8, 30, 96, 49, 1, 17, 46, 40, 12, 87, 4, 9, 99, 59, 31, 90, 61, 65, 58, 52, 91, 13, 10, 53, 95, 3, 34, 55, 79, 47, 72, 22, 27, 5, 32, 29, 43, 80, 57, 48, 11, 50, 84, 69, 51, 73, 71, 26, 44, 54, 8 ]

ts = TabuSearch(initial_solution)

best_solution = ts.solve()

print(best_solution.path, best_solution.distance)

best_solutions_distances = [int(solution.distance) for solution in ts.solutions_track]

print(best_solutions_distances)
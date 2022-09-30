from TravellingSalesman import TravellingSalesman, City
from Graph import Graph
import json
from os import path

with open(path.dirname(__file__) + '/data.json', 'r') as file:
	data = json.load(file)

	cities = [City(cityData) for cityData in data["cities"]]
	travellingSalesman = TravellingSalesman(cities)

	solutions = travellingSalesman.resolve(cities[0])
	for solution in solutions:
		print(solution)
	
	Graph(data, solutions[-1])

	
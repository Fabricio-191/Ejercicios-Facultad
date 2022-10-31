"""
Actividad 5

Ejercicio Nº 5

Los vértices del siguiente Dígrafo representan ciudades (Almafuerte, Belén, Córdoba, Dar-el-Salam, Estambul y Finisterre) y las aristas indican si existe una ruta aérea entre ellas.

Implemente un algoritmo para averiguar cuál sería la forma en la que una persona podría viajar de una a otra pasando por la menor cantidad de ciudades intermedias posibles.
"""

nodos = ['A', 'B', 'C', 'D', 'E', 'F']
adyacencias = [('A', 'D'), ('B', 'C'), ('B', 'D'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]
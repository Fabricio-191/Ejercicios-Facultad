from __future__ import annotations

class Materia:
	__alumnos: int
	__nombre: str

	def __init__(self, nombre: str, alumnos: int):
		self.__alumnos = alumnos
		self.__nombre = nombre

	def get_alumnos(self) -> int:
		return self.__alumnos

	def get_nombre(self) -> str:
		return self.__nombre

	def __repr__(self) -> str:
		return f"{self.__nombre} ({self.__alumnos} alumnos)"

	def __gt__(self, other: Materia) -> bool:
		if(type(other) != Materia):
			raise TypeError("No se puede comparar una materia con un objeto de otro tipo")

		return self.__alumnos > other.get_alumnos()


lista: list[Materia] = [
	Materia('Algoritmos y resolucion de problemas', 120),
	Materia('Programacion procedural', 90),
	Materia('Programacion orientada a objetos', 70),
]

print('\nResultado:')
print(max(lista))

"""
Resultado:
Algoritmos y resolucion de problemas (120 alumnos)
"""

lista.extend([
	Materia('Estructura de Datos y Algoritmos', 50),
	Materia('Paradigmas de Lenguajes', 45),
	Materia('Algoritmos Numéricos', 40),
])

print('\nResultado:')
for materia in lista:
	print(materia)

"""
Resultado:
Algoritmos y resolucion de problemas (120 alumnos)
Programacion procedural (90 alumnos)
Programacion orientada a objetos (70 alumnos)     
Estructura de Datos y Algoritmos (50 alumnos)     
Paradigmas de Lenguajes (45 alumnos)
Algoritmos Numéricos (40 alumnos)
"""

iterableNombres = map(lambda x: x.get_nombre(), lista)

print('\nResultado: ')
for elemento in iterableNombres:
	print(elemento)

"""
Resultado:
Algoritmos y resolucion de problemas
Programacion procedural
Programacion orientada a objetos
Estructura de Datos y Algoritmos
Paradigmas de Lenguajes
Algoritmos Numéricos
"""

lista.reverse()

print('\nResultado: ')
for elemento in lista:
	print(elemento)

"""
Resultado:
Algoritmos Numéricos (40 alumnos)
Paradigmas de Lenguajes (45 alumnos)
Estructura de Datos y Algoritmos (50 alumnos)     
Programacion orientada a objetos (70 alumnos)     
Programacion procedural (90 alumnos)
Algoritmos y resolucion de problemas (120 alumnos)
"""

def flatList(list):
	return [item for sublist in list for item in sublist]

def removeDuplicates(list):
	return list(set(list))

	"""
	My_list =[‘a’, ’b’, ’c’, ’b’, ’a’]
	Mylist = list(dict.fromkeys(My_List))
	"""

def mostFrequentValue(list):
	return max(set(list), key=list.count)

def hasRepeatedValues(list):
	return len(list) != len(set(list))

"""
Method 	Description
<list>.append()	    Adds an element at the end of the list
<list>.clear()	    Removes all the elements from the list
<list>.copy()	    Returns a copy of the list
<list>.count()	    Returns the number of elements with the specified value
<list>.extend()	    Add the elements of a list (or any iterable), to the end of the current list
<list>.index()	    Returns the index of the first element with the specified value
<list>.insert()	    Adds an element at the specified position
<list>.pop()	    Removes the element at the specified position
<list>.remove()	    Removes the first item with the specified value
<list>.reverse()	Reverses the order of the list
<list>.sort()	    Sorts the list
<string>.join()

slicing
list_1[-1]

in
for in

all()
any()
dict()
enumerate()
filter()
iter()
len()
list()
map()
max()
memoryview()
min()
next()
range()
reversed()
set()
slice()
sorted()
sum()
tuple()
zip()

iterable unpacking
x, y, z = my_list

https://www.programiz.com/python-programming/list-comprehension
https://www.w3schools.com/python/python_lists_comprehension.asp
"""
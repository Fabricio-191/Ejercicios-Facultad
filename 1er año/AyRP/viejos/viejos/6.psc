/*
Construya un algoritmo que usando subprogramas permita:

1. Generar una estructura arreglo que almacene 20 números. Los números se ingresan en forma ordenada de menor a mayor.
2. Ingresar un valor y decir en el algoritmo principal en qué posición (el índice) se encuentra en el arreglo.
3. Generar 2 subarreglos, uno con los números positivos y otro con los negativos.

Mostrar cada uno de los subarreglos generados.
*/

constante N = 20

entero carga(real nums[N])
Comienzo
	entero i
	real num
	
	Escribir "Ingrese 20 numeros"
	Para i desde 0 hasta N - 1
		Leer num

		nums[i] = num
	FinPara

	retorna()
Fin

void mostrar(real nums[N], entero LT, cadena tipo)
Comienzo
	entero i
	Escribir "Los numeros ", tipo,"tivos son los siguientes:"
	Para i desde 0 hasta LT - 1
		Escribir nums[i]
	FinPara
Fin

void positivos(real nums[N])
Comienzo
	entero LT, i
	real npositivos[N]

	LT = 0

	Para i desde 0 hasta N - 1
		Si(nums[i] > 0)
			Entonces
				npositivos[NT] = nums[i]
				NT += 1
		FinSi
	FinPara

	mostrar(npositivos, LT, "posi")
Fin

void negativos(real nums[N])
Comienzo
	entero LT, i
	real nnegativos[N]

	LT = 0

	Para i desde 0 hasta N - 1
		Si(nums[i] < 0)
			Entonces
				nnegativos[NT] = nums[i]
				NT += 1
		FinSi
	FinPara

	mostrar(nnegativos, LT, "nega")
Fin

entero buscar(real nums[N], real num)
Comienzo
	entero i
	booleano encontro

	encontro = falso
	i = 0

	Mientras((i < N) y (!encontro))
		Si(nums[i] == num)
			Entonces encontro = verdadero
			Sino i += 1
		FinSi
	FinMientras

	Si(!encontro)
		Entonces i = -1
	FinSi

	retorna (i)
Fin

void selector(real nums[N])
Comienzo
	entero indice
	real valor

	Escribir "Introduzca el valor a buscar"
	Leer valor

	indice = buscar(nums, valor)

	Si(indice == -1)
		Entonces Escribir "Ese numero no esta en el arreglo"
		Sino Escribir "Ese numero esta en la posicion ", indice
	FinS
Fin

Comienzo
	real nums[N]

	carga(nums)

	positivos(nums)
	negativos(nums)

	selector(nums)
Fin
entero buscar(entero arreglo[N], entero elem) //Busqueda sin bandera
Comienzo
	entero i
	i = 0

	Mientras((i < N) y (arreglo[i] != elem))
		i++
	FinMientras

	retorna (i)
Fin

entero buscar(entero arreglo[N], entero elem) //Busqueda con bandera
Comienzo
	entero i
	booleano encontro

	i=0
	encontro=falso

	Mientras((i < N) y (!encontro))
		Si (arreglo[i] == elem)
			Entonces encontro = verdadero
			Sino i++
		FinSi
	FinMientras

	retorna (i)
Fin

entero buscar(entero arreglo[N+1], entero elem) //Busqueda con elemento sentinela
Comienzo
	entero i = 0
	arreglo[N] = elem

	Mientras (arreglo[i] != elem)
		i++
	FinMientras
	retorna (i)
Fin

entero buscar(entero arreglo[N], entero elem) //Busqueda binaria (no secuencial)
Comienzo
	entero inf , sup , medio
	inf = 0
	sup = N - 1
	medio = (inf + sup) div 2

	Mientras ((inf <= sup) y (elem != arreglo[medio])
		Si (elem < arreglo[medio])
			Entonces sup = medio - 1
			Sino inf = medio + 1
		FinSi
		medio = (inf + sup) div 2
	FinMientras

	Si (inf <= sup)
		Entonces retorna (medio)
		Sino retorna (-1)
	FinSi
Fin


void ordenar(entero arreglo[N]) //metodo burbuja mejorado
Comienzo
	entero k, i, aux, cota

	cota = N - 1
	k = 1

	Mientras(k != -1)
		k = -1

		Para i desde 0 hasta cota - 1
			Si(arreglo[i] > arreglo[i + 1])  //ascendente
				Entonces
					aux = arreglo[i]
					arreglo[i] = arreglo[i + 1]
					arreglo[i + 1] = aux
					k = i
			FinSi
		FinPara

		cota = k
	FinMientras

	retorna()
Fin

void ordenar(entero arreglo[N]) //metodo seleccion
Comienzo
	entero i, j, min, aux
	Para i Desde 0 Hasta N - 2
		min = i
		Para j Desde i+1 hasta N - 1
			Si(arreglo[j] < arreglo[min])  //ascendente
				Entonces min = j
			FinSi
		FinPara

		aux = arreglo[i]
		arreglo[i] = arreglo[min]
		arreglo[min] = aux
	FinPara
	retorna()
Fin

void ordenar(entero arreglo[N]) //metodo insercion
Comienzo
	entero i, j, valor

	Para i Desde 1 Hasta N - 1
		valor = arreglo[i]
		j = i - 1
		Mientras ((j >= 0) y (valor < arreglo[j]))  //ascendente
			arreglo[j + 1] = arreglo[j]
			j = j - 1
		FinMientras
		arreglo[j+1] = valor
	FinPara
	retorna()
Fin
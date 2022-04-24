/*
La policía ha lanzado un operativo para controlar el tránsito durante el verano. 

Se ha dividido a la provincia en 12 zonas. 
Se han clasificado las infracciones en 10 tipos (1: exceso de velocidad, 2: falta de iluminación, … , 10: alcoholemia).

Por cada infracción realizada se tienen los siguientes datos: patente del vehículo, zona y tipo de infracción.

Para evaluar los resultados del Operativo realizar un algoritmo que con subprogramas permita:

1. Realizar un listado ordenado ascendentemente por cantidad de infracciones. (tipo y zona)
2. Mostrar el o los tipos de infracción/es que más se cometen.
3. Decir si algún tipo de infracción no se cometió.
4. Indicar para cada zona la cantidad de infracciones realizadas.
5. Mostrar todas las zonas que tuvieron una cantidad de infracciones inferior al promedio de las infracciones realizadas en las 12 zonas de la provincia.
*/
constante N = 12
constante N1 = 10

void cerearInfracciones(entero infracciones[N1])
Comienzo
	entero i

	Para i desde 0 hasta N1 - 1
		infracciones[i] = 0
	FinPara
	retorna()
Fin
void cerearZonas(entero zonas[N])
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		zonas[i] = 0
	FinPara
	retorna()
Fin

void ordenarInfracciones(entero infracciones[N1])
Comienzo
	entero k, i, aux, cota

	cota = N1 - 1
	k = 1

	Mientras(k != -1)
		k = -1

		Para i desde 0 hasta cota - 1
			Si(arreglo[i] > arreglo[i + 1])
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
void ordenarZonas(entero zonas[N])
Comienzo
	entero k, i, aux, cota

	cota = N - 1
	k = 1

	Mientras(k != -1)
		k = -1

		Para i desde 0 hasta cota - 1
			Si(arreglo[i] > arreglo[i + 1])
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

void mostrarInfracciones(entero infracciones[N1])
Comienzo
	entero i 

	Para i desde 0 hasta N1 - 1
		Escribir "El tipo de infraccion ", i + 1, " se cometio ", infracciones[i], " veces"
	FinPara
	retorna()
Fin
void mostrarZonas(entero zonas[N])
Comienzo
	entero i 

	Para i desde 0 hasta N - 1
		Escribir "En la zona ", i + 1, " se cometieron ", zonas[i], " infracciones"
	FinPara
	retorna()
Fin

void cargar(entero zonas[N], entero infracciones[N1])
Comienzo
	cadena patente
	entero zona, tipo

	Escribir "Introduzca la patente del auto"
	Leer patente

	Mientras(patente != "")
		Escribir "Introduzca la zona y tipo de la infracccion"
		Leer zona, tipo

		zonas[zona - 1]++
		infracciones[tipo - 1]++

		Escribir "Introduzca la patente del auto"
		Leer patente
	FinMientras
	retorna()
Fin

entero encontrarMax(entero infracciones[N1])
Comienzo
	entero i, max

	max = infracciones[0]

	Para i desde 1 hasta N1 - 1
		Si(infracciones[i] > max)
			Entonces max = infracciones[i]
		FinSi
	FinPara

	retorna(max)
Fin
void infraccionesMasCometidas(entero infracciones[N1])
Comienzo
	entero i, max

	max = encontrarMax(infracciones)

	Para i desde 0 hasta N1 - 1
		Si(infracciones[i] == max)
			Entonces Escribir "La infraccion ", i + 1, " es una de las que mas se comete"
		FinSi
	FinPara
	retorna()
Fin

void infraccionesNoCometidas(entero infracciones[N1])
Comienzo
	entero i 
	booleano encontro

	Mientras((i < N1) y !encontro)
		Si(infracciones[i] == 0)
			Entonces encontro = verdadero
			Sino i++
		FinSi
	FinMientras

	Si(encontro)
		Entonces Escribir "Hay un tipo de infraccion que no se cometio"
	FinSi
	retorna()
Fin

real infraccionesPromedio(entero zonas[N])
Comienzo
	entero i, acc

	acc = 0

	Para i desde 0 hasta N - 1
		acc += zonas[i]
	FinPara

	retorna(acc / N)
Fin
void zonasInfraccionesMayorPromedio(entero zonas[N])
Comienzo
	entero i
	real prom

	prom = infraccionesPromedio(zonas)

	Para i desde 0 hasta N - 1
		Si(zonas[i] > prom)
			Entonces Escribir "En la zona ", i + 1, " se cometio una cantidad de infracciones mayor al promedio"
		FinSi
	FinPara
	retorna()
Fin

Comienzo
	entero zonas[N] //arreglo de contadores de infracciones por zona
	entero infracciones[N1] //areglo de contadores de infracciones por tipo

	cerearInfracciones(infracciones)
	cerearZonas(zonas)

	cargar(zonas, infracciones)

	ordenarInfracciones(infracciones) //inciso 1
	mostrarInfracciones(infracciones) //inciso 1
	ordenarZonas(zonas) //inciso 1
	mostrarZonas(zonas) //inciso 4 y 1 a la vez

	infraccionesMasCometidas(infracciones) //inciso 2
	infraccionesNoCometidas(infracciones) //inciso 3

	zonasInfraccionesMayorPromedio(zonas) //inciso 5
Fin
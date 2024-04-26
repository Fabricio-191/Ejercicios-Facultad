/*
Se cuenta con los puntajes de N competidores. Por cada uno se ingresa: número de competidor (valor que varía entre 1 y N) y puntaje obtenido.
Teniendo en cuenta que se han armado dos equipos: A y B, conformados de la siguiente manera: el equipo A, 
por los competidores con número entre 1 y N/2; 
y para B entre (N/2) +1 y N

a)    Informar el equipo que obtuvo el mayor puntaje acumulado.
b)    Indicar cuál es el puntaje promedio en general.

Nota: utilice un mismo subprograma que calcule el puntaje acumulado; esto es, un único subprograma invocado dos veces con distintos parámetros.
*/
Algoritmo competicion
constante N = 20

real sumarPuntajes(caracter equipo, real competidores[N])
Comienzo
	entero inicio, final, i
	real acc

	acc = 0
	inicio = 1
	final = N

	Si(equipo == 'A')
		Entonces final = N / 2
		Sino inicio = (N / 2) + 1
	FinSi

	Para i desde inicio hasta final
		acc += competidores[i - 1]
	FinPara

	retorna(acc)
Fin

void mostrar(real competidores[N])
Comienzo
	real puntajeA, puntajeB, promedioGeneral

	puntajeA = sumarPuntajes('A', competidores)
	puntajeB = sumarPuntajes('B', competidores)
	promedioGeneral = (puntajeA + puntajeB) / N

	Si(puntajeA > puntajeB)
		Entonces Escribir "El equipo A tuvo el mayor puntaje"
		Sino Si(puntajeB > puntajeA)
			Entonces Escribir "El equipo B tuvo el mayor puntaje"
			Sino Escribir "Los equipos tienen el mismo puntaje"
		FinSi
	FinSi

	Escribir "El puntaje promedio es: ", promedioGeneral
Fin

void carga(real competidores[N])
Comienzo
	real puntaje, numero
	entero i

	Para i desde 1 hasta N
		Escribir "Introduzca el numero del competidor"
		Leer numero
		Escribir "Introduzca el puntaje del competidor: ", i
		Leer puntaje

		competidores[numero - 1] = puntaje
	FinPara
Fin

Comienzo
	real competidores[N]

	carga(competidores)
	mostrar(competidores)
Fin
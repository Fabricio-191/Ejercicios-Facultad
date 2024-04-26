/*
En un centro médico se procesa la información de los pacientes que asisten, de cada uno se registra el número de especialidad (1..12) en la que se atiende
Construya un algoritmo que, usando de manera óptima subprogramas (al menos uno por ítem) permita:
1. Indicar la cantidad de pacientes por especialidad.

2. Generar un subarreglo que contenga el Numero de especialidad para aquellas esps donde la cantidad de pacientes atendidos es menor a 10.
3. Muestre la estructura de datos generada en el inciso 2) ordenada descendentemente.
*/

Algoritmo ejercicio2
constante N = 12

void cerear(entero esps[N])
Comienzo
	entero i
	Para i desde 0 hasta N - 1
		esps[i] = 0
	FinPara
	retorna()
Fin

void carga(entero esps[N])
Comienzo
	entero esp
	
	Escribir "Introduzca la especialidad del paciente (0 para terminar)"
	Leer esp
	Mientras(esp != 0)
		esps[esp - 1] += 1
	
		Escribir "Introduzca la especialidad del paciente (0 para terminar)"
		Leer esp
	FinMientras

	retorna()
Fin

void mostrar(entero esps[N])
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		Escribir "En la especialidad ", i + 1, " hay ", esps[i], " pacientes"
	FinPara
	retorna()
Fin

entero sub_arreglo(entero esps[N], entero menor10[N])
Comienzo
	entero i, LT

	LT = 0

	Para i desde 0 hasta N - 1
		Si(esps[i] < 10)
			Entonces
				menor10[LT] = i + 1
				LT += 1
		FinSi
	FinPara

	retorna(LT)
Fin

void ordenar(entero menor10[N], entero LT) //metodo burbuja mejorado
Comienzo
	entero k, i, aux, cota

	cota = LT - 1
	k = 1

	Mientras(k != -1)
		k = -1

		Para i desde 0 hasta cota - 1
			Si(menor10[i] < menor10[i + 1])  //ascendente
				Entonces
					aux = menor10[i]
					menor10[i] = menor10[i + 1]
					menor10[i + 1] = aux
					k = i
			FinSi
		FinPara

		cota = k
	FinMientras

	retorna()
Fin

void mostrarSub(entero menor10[N], entero LT)
Comienzo
	entero i

	Para i desde 0 hasta LT - 1
		Escribir "En la especialidad ", menor10[i], " se atienden menos de 10 personas"
	FinPara
	retorna()
Fin

Comienzo
	entero esps[N], menor10[N], LT

	cerear(esps)
	carga(esps)
	mostrar(esps)
	LT = sub_arreglo(esps, menor10)
	ordenar(menor10, LT)
	mostrarSub(menor10, LT)
Fin
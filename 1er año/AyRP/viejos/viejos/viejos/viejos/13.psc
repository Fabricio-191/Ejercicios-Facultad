/*
ENERGAS ha autorizado en la provincia a 15 talleres para extender obleas de habilitación de carga de GNC. Cada taller se identifica con un número del 1 al 15.
La información de los talleres puede venir en cualquier orden, pero sin repetir el número de taller.
Mensualmente se registra: número de taller y cantidad total de obleas emitidas. 
Realizar un algoritmo que utilizando subprogramas y estructuras adecuadas permita:

a)	Ingresar por teclado un número de taller y mostrar la cantidad de obleas emitidas.
b)	Indicar la cantidad total de obleas emitidas en la provincia.
c)	Indicar el taller que menos oblea extendió.
d)	Mostrar el número de taller que emitió mayor cantidad de obleas.
e)	Informar si algún taller emitió más de 500 obleas en el mes.

Realizar las modificaciones necesarias para responder a todos los ítems anteriormente planteados, suponiendo que la información viene ordenada por número de taller. 
Es decir, que por cada uno de los 15 talleres se ingresa la cantidad de obleas emitidas.
*/

Algoritmo ENERGAS
constante N = 15

void cargarObleas(entero talleres[N])
Comienzo
	entero taller, cantObl
	Escribir "Introduzca el numero del taller"
	Leer taller

	Mientras(taller != 0)
		Escriba "Introduzca la cantidad de obleas emitidas"
		Leer cantObl

		talleres[taller - 1] = cantObl
		
		Escribir "Introduzca el numero del taller"
		Leer taller
	FinMientras
	retorna()
Fin

void mostrar(entero obleasTotales, entero MIN_taller, entero MAX_taller, entero MAS_500)
Comienzo
	Escribir "La cantidad total de obleas emitidas fue: ", obleasTotales
	Escribir "El taller que menos obleas emitio es el: ", MIN_taller
	Escribir "El taller que mas obleas emitio es el: ", MAX_taller
	Si(MAS_500)
		Entonces Escribir "Hay un taller que emitió mas de 500 obleas"
	FinSi
	retorna()
Fin

void selector(entero talleres[N])
Comienzo
	entero taller

	Escribir "Introduzca el numero del taller"
	Leer taller

	Mientras(taller != 0)
		Escribir "El taller ", taller, " emitio ", talleres[taller - 1], " obleas"

		Escribir "Introduzca el numero del taller"
		Leer taller
	FinMientras
	retorna()
Fin

Comienzo
	entero talleres[N], taller, cantObl, obleasTotales,
		MIN_obleas, MIN_taller,
		MAX_obleas, MAX_taller
	booleano MAS_500

	MIN_obleas = 100000
	MAX_obleas = 0
	MAS_500 = falso

	cargarObleas(talleres)

	Para taller desde 1 hasta N
		cantObl = talleres[taller - 1]
		obleasTotales += cantObl

		Si(cantObl < MIN_obleas)
			Entonces 
				MIN_obleas = cantObl
				MIN_taller = taller
		FinSi
		Si(cantObl > MAX_obleas)
			Entonces 
				MAX_obleas = cantObl
				MAX_taller = taller
		FinSi
		Si(cantObl > 500)
			Entonces MAS_500 = verdadero
		FinSi
	FinMientras

	mostrar(obleasTotales, MIN_taller, MAX_taller, MAS_500)
	selector(talleres)
Fin

/*
	Carga ordenada:

	void cargarObleas(entero talleres[N])
	Comienzo
		entero taller, cantObl

		Para taller desde 1 hasta N
			Escriba "Introduzca la cantidad de obleas emitidas por el taller: ", N
			Leer cantObl

			talleres[taller - 1] = cantObl
		FinPara
		retorna()
	Fin
*/
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

void tallerMasObleas(entero talleres[N])
Comienzo
	entero taller, max_t, max_o, cantObl

	Para taller desde 1 hasta N
		cantObl = talleres[taller - 1]

		Si(cantObl > max_o)
			Entonces 
				max_o = cantObl
				max_t = taller
		FinSi
	FinPara

	Escribir "El taller que mas obleas emitio es el: ", max_t
Fin

entero menosObleas(entero talleres[N])
Comienzo
	entero taller, min

	Para taller desde 0 hasta N - 1
		Si(talleres[taller] > min)
			Entonces min = talleres[taller]
		FinSi
	FinPara

	retorna(min)
Fin

void talleresMenosObleas(entero talleres[N])
Comienzo
	entero taller, min

	min = menosObleas(talleres)

	Para taller desde 0 hasta N - 1
		Si(talleres[taller] == min)
			Entonces Escribir "El taller ", i + 1, " fue uno de los que menos obleas emitio"
		FinSi
	FinPara
Fin

void mas500obleas(entero talleres[N])
Comienzo
	entero taller

	Para taller desde 1 hasta N
		Si(talleres[taller - 1] > 500)
			Escribir "Hay un taller que emitió mas de 500 obleas"

			retorna()
		FinSi
	FinPara
Fin

void obleasTotales(entero talleres[N])
Comienzo
	entero obleasTotales, taller

	Para taller desde 1 hasta N
		obleasTotales += talleres[taller - 1]
	FinPara

	Escribir "La cantidad total de obleas emitidas fue: ", obleasTotales
Fin

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

void selector(entero talleres[N])
Comienzo
	entero taller

	Escribir "Introduzca el numero del taller"
	Leer taller

	Escribir "El taller ", taller, " emitio ", talleres[taller - 1], " obleas"

	retorna()
Fin

Comienzo
	entero talleres[N]

	cargarObleas(talleres)

	tallerMasObleas(talleres)
	tallerMenosObleas(talleres)
	mas500obleas(talleres)
	obleasTotales(talleres)

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
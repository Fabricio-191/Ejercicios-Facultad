/*
Ejercicio 10
Se cuenta con los datos de cada uno de los 300 corredores de una maratón de enero del 2020, auspiciada por el gobierno de San Juan. 
Los mismos son Número de corredor (1 a 300) Tiempo total de carrera (en minutos) y Edad.

Construya un algoritmo que usando subprogramas permita:

	1. Generar las estructuras adecuadas para almacenar y guardar la información de los corredores de la maratón (hacer uso de arreglos paralelos).
	2. Indicar la edad promedio y el número de corredor que supera esa Edad.
	3. Generar una nueva estructura que a partir de la anterior guarde el Tiempo total de carrera de aquellos corredores mayores de 50 años.
	4. A partir de la estructura generada en el ítem 3, hacer un listado que muestre el Número de corredor y su Tiempo total de carrera.
*/


constante N = 300

void carga(real tiempos[N], real edades[N])
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		Escribir "Introduzca la edad del corredor: ", i + 1
		Leer edades[i]
		Escribir "Introduzca el tiempo de carrera del corredor: ", i + 1
		Leer tiempos[i]
	FinPara
	retorna()
Fin

real calcularEdadPromedio(real edades[N])
Comienzo
	real acc
	entero i

	Para i desde 0 hasta N - 1
		acc += edades[i]
	FinPara

	retorna(acc / N)
Fin

void edadPromedio(real edades[N])
Comienzo
	real edadProm

	edadProm = calcularEdadPromedio(edades)

	Escribir "La edad promedio es ", edadProm

	Para i desde 0 hasta N - 1
		Si(edades[i] > edadProm)
			Entonces Escribir "El corredor ", i + 1, " supera la edad promedio"
		FinSi
	FinPara

	retorna()
Fin

void mostrarMayores50(real tiemposMayoresA50[N], entero numerosMayoresA50[N], entero NT)
Comienzo
	entero i

	Para i desde 0 hasta NT - 1
		Escribir "El corredor ", numerosMayoresA50[i], ": "
		Escribir "Tiene mas de 50 años"
		Escribir "y su tiempo fue: ", tiemposMayoresA50[i]
	FinPara
	retorna()
Fin

void mayores50(real edades[N], real tiempos[N])
Comienzo
	entero NT, numerosMayoresA50[N]
	real tiemposMayoresA50[N]

	NT = 0

	Para i desde 0 hasta N - 1
		Si(edades[i] > 50)
			Entonces
				numerosMayoresA50[NT] = i + 1
				tiemposMayoresA50[NT] = edades[i]
				NT++
		FinSi
	FinPara

	mostrarMayores50(tiemposMayoresA50, numerosMayoresA50, NT)
	retorna()
Fin

Comienzo
	real tiempos[N], edades[N]

	carga(tiempos, edades)

	edadPromedio(edades
	mayores50(edades, tiempos)
Fin




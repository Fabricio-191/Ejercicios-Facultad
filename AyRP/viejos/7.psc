/*
Se conoce la información de 6 cursos de capacitación. 
Se procesa información ordenada por cursos, 
de cada uno se ingresa por alumno su edad y sexo (M: mujeres, V: varones).
Construya un algoritmo que usando subprogramas permita:

1.	Registrar para cada curso la edad promedio, cantidad de mujeres y cantidad de varones.
2.	Decir el número de curso y edad promedio en donde la cantidad de mujeres es igual a la cantidad de varones.
3.	Informar cuantos cursos tienen la misma edad promedio de mujeres y varones
*/
constante N = 6

Registro curso {
	entero cantM, edadPromM, cantV, edadPromV
}

curso carga(curso cur)
Comienzo
	entero edad
	caracter sexo
	
	Escribir "Introduzca la edad del alumno (0 para terminar)"
	Leer edad

	Mientras(edad != 0)
		Escribir "Introduzca el sexo del alumno M o V"
		Leer sexo

		Si((sexo == 'M') o (sexo == 'm'))
			Entonces 
				cur.cantM++
				cur.edadPromM += edad
			Sino 
				cur.cantV++
				cur.edadPromV += edad
		FinSi

		Escribir "Introduzca la edad del alumno (0 para terminar)"
		Leer edad
	FinMientras

	cur.edadPromV /= cur.cantV
	cur.edadPromM /= cur.cantM

	retorna(cur)
Fin

void cargaCursos(curso cursos[N])
Comienzo
	entero i
	Para i desde 0 hasta N - 1
		cursos[i].cantV = 0
		cursos[i].cantM = 0
		cursos[i].edadPromV = 0
		cursos[i].edadPromM = 0

		Escribir "Introduzca los datos de los alumnos del curso: ", i + 1
		cursos[i] = carga(cursos[i])
	FinPara	
	retorna()
Fin

void cantIguales(curso cursos[N])
Comienzo
	entero i, prom

	Para i desde 0 hasta N - 1
		Si(cursos[i].cantV == cursos[i].cantM)
			Entonces 
				prom = (cursos[i].edadPromM + cursos[i].edadPromV) / 2
				Escribir "En el curso ", i + 1, " la cantidad de mujeres es igual a la de hombres"
				Escribir "y la edad promedio es: ", prom
		FinSi
	FinPara
	retorna()
Fin

void mismaEdadProm(curso cursos[N])
Comienzo
	entero i, cont 

	cont = 0

	Para i desde 0 hasta N - 1
		Si(cursos[i].edadPromM == cursos[i].edadPromV)
			Entonces cont++
		FinSi
	FinPara

	Escribir "Hay ", cont, " cursos con la misma edad promedio entre mujeres y hombres" 

	retorna()
Fin

Comienzo
	curso cursos[N]

	cargaCursos(cursos)
	cantIguales(cursos)
	mismaEdadProm(cursos)
Fin
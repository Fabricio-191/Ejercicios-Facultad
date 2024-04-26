constante N = 110

Registo aspirante{
	cadena aYn
	entero sueldo, cantIn, DNI
}

void carga(aspirante aps[N])
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		Escribir "Introduzca la info del aspirante nRo: ", i + 1
		Leer aps[i].aYn, aps[i].DNI, aps[i].sueldo, aps[i].cantIn
	FinPara

	retorna()
Fin

void contar(aspirante aps[N])
Comienzo
	entero cont, i
	cont = 0

	Para i desde 0 hasta N - 1
		Si((aps[i].sueldo > 80000) y (aps[i].cantIn > 5))
			Entonces cont++
		FinSi
	FinPara

	Escribir "Hay ", cont, " aspirantes con mas de 5 miembros en la familia y con un sueldo mayor a 80000"
Fin

entero buscar(aspirante arreglo[N], entero DNI)
Comienzo
	entero inf , sup , medio
	inf = 0
	sup = N - 1
	medio = (inf + sup) div 2

	Mientras ((inf <= sup) y (DNI != arreglo[medio].DNI)
		Si (DNI < arreglo[medio].DNI)
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

booleano aspiranteSueldos(aspirante aps[N])
Comienzo
	entero i
	booleano encontro

	i=0
	encontro=falso

	Mientras((i < N) y (!encontro))
		Si ((aps[i].sueldo > 95000) y (aps[i].sueldo < 120000))
			Entonces encontro = verdadero
			Sino i++
		FinSi
	FinMientras

	retorna (encontro)
Fin

Comienzo
	aspirante aps[N]
	entero i, DNI

	carga(aps)
	contar(aps)

	Escribir "Introduzca el DNI a buscar"
	Leer DNI

	i = buscar(aps, DNI)

	Si(i != -1)
		Entonces
			Escribir "DNI: ", aps[i].DNI
			Escribir "Nombre: ", aps[i].aYn
			Escribir "sueldo: ", aps[i].sueldo
			Escribir "cantIn: ", aps[i].cantIn
	FinSi

	Si(aspiranteSueldos(aps))
		Entonces Escribir "Hay alguien con un sueldo entre 95 y 120 mil"
	FinSi
Fin
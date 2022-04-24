/*
Una empresa de venta de artículos para el hogar cuenta con 36 sucursales, las cuales están identificadas por un número de 1 a 36.
Por cada sucursal se ingresa el importe total recaudado, esto hace se hace consecutivamente en forma ordenada por número de sucursal.
Realizar un algoritmo que usando subprogramas y estructuras de datos adecuadas permita:

a)	Calcular cual fue la mayor recaudación de la empresa.
b)	Indicar la o las sucursales que registraron la mayor recaudación.
c)	Informar cuál es la sucursal con menor recaudación.
d)	Mostrar el porcentaje que recaudó la sucursal 19 respecto del total recaudado.
e)	Realizar las modificaciones necesarias para responder a todos los ítems anteriormente planteados, suponiendo que, 
de cada sucursal se registra la siguiente información: número de sucursal e importe total recaudado, la información viene desordenada.
*/

Algoritmo ArticulosHogar
constante N = 36

void mostrar(real sucursales[N], entero MIN_suc, real MAX_rec, real totalRecaudado)
Comienzo
	entero i
	real porcentaje

	Escribir "La mayor recaudación fue: ", MAX_rec

	Para i desde 1 hasta N
		Si(sucursales[i - 1] == MAX_rec)
			Entonces Escribir "La sucursal ", i, " fue una de las de mayor recaudación"
		FinSi
	FinPara
	Escribir "La sucursal de menor recaudación es la: ", MIN_suc

	porcentaje = (sucursales[18] / totalRecaudado) * 100
	Escribir "El porcentaje que recaudó la sucursal 19 respecto del total recaudado es: ", porcentaje
Fin

void cargar(real sucursales[N])
Comienzo
	real recaudado
	entero sucursal
	
	Para sucursal desde 1 hasta N
		Escribir "Introduzca el importe total recaudado de la sucursal: ", sucursal
		Leer recaudado

		sucursales[sucursal - 1] = recaudado
	FinPara
Fin

void procesar(real sucursales[N])
Comienzo
	entero MIN_suc, sucursal
	real MIN_rec, MAX_rec, recaudado, totalRecaudado
	
	MIN_rec = 100000000
	MAX_rec = -100000000
	
	Para sucursal desde 1 hasta N
		recaudado = sucursales[sucursal - 1]
		totalRecaudado += recaudado

		Si(recaudado > MAX_rec)
			Entonces
				MAX_rec = recaudado
		FinSi
		Si(recaudado < MIN_rec)
			Entonces
				MIN_suc = sucursal
				MIN_rec = recaudado
		FinSi
	FinPara
	
	mostrar(sucursales, MIN_suc, MAX_rec, totalRecaudado)
Fin

Comienzo
	real sucursales[N]

	cargar(sucursales)
	procesar(sucursales)
Fin

/*
	Carga desordenada:

	void cargar(real sucursales[N])
	Comienzo
		real recaudado
		entero sucursal

		Mientras(sucursal != 0)
			Escribir "Introduzca el importe total recaudado de la sucursal: ", sucursal
			Leer recaudado

			sucursales[sucursal - 1] = recaudado
			
			Escribir "Introduzca el numero de sucursal"
			Leer sucursal
		FinMientras
	Fin
*/
/*
Una fábrica de unis posee los siguientes datos de c/u de los 42 unis que fabrica: Nombre del uni, stock y precio unitario.

1. Almacenar en un arreglo de registros los datos de los 42 unis.
2. Informar el nombre de el/los uni/s con mayor stock.
3. Ingresar un nombre de uni e indicar el total de dinero que representa su stock.
*/

Algoritmo ejercicio3
constante N = 42

Registro uni{
	cadena nombre
	entero stock
	real valorU
}

void carga(uni unis[N])
Comienzo
	entero i
	Para i desde 0 hasta N - 1
		Escribir "Introduzca los datos de un unirforme"
		Leer unis[i].nombre, unis[i].stock, unis[i].valorU
	FinPara
	retorna()
Fin

entero mayorStock(uni unis[N])
Comienzo
	entero i, max

	Para i desde 0 hasta N - 1
		Si(unis[i].stock > max)
			Entonces max = unis[i].stock
		FinSi
	FinPara

	retorna(max)
Fin

void mostrarMayorStock(uni unis[N], entero mayor)
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		Si(unis[i] == mayor)
			Entonces Escribir "El unifrome ", unis[i].nombre, " fue uno de los que mas vendio"
		FinSi
	FinPara
	retorna()
Fin

entero buscar(uni unis[N], cadena nombre)
Comienzo
	entero i
	i = 0

	Mientras((i < N) y (unis[i].nombre != nombre))
		i += 1
	FinMientras

	retorna (i)
Fin

void selector(uni unis[N])
Comienzo
	cadena nombre
	entero i

	Escribir "Introduzca el nombre del uni"
	Leer nombre

	i = buscar(unis, nombre)

	Si(i == N)
		Entonces "El uni no existe"
		Sino "El stock de ese uni representa un total de ", unis[i].valorU * unis[i].stock
	FinSi
	retorna()
Fin

Comienzo
	uni unis[N]

	carga(unis)
	mostrarMayorStock(unis, mayorStock(unis))
	selector(unis)
Fin
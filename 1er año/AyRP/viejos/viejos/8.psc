/*
Un gremio ha comprado una finca y la dividió en 164 lotes, de cada lote se conoce su número (entre 1 y 164) y su superficie. 
La información se ingresa ordenada ascendentemente por superficie.

Construya un algoritmo que usando subprogramas permita:

1. Almacenar solamente la información de aquellos lotes cuya superficie sea mayor a 650 metros cuadrados.
2. Ingresar una superficie mayor a 650 metros cuadrados y decir si algún lote tiene una superficie igual.
3. Decir cuántos lotes tienen una superficie mayor a la superficie promedio
*/

constante N = 164

entero carga(real sups[N])
Comienzo
	entero i, LT
	real sup

	LT = 0

	Para i desde 1 hasta N
		Escribir "Ingrese la superficie del lote: ", i
		Leer sup

		Si(sup > 650)
			Entonces
				sups[LT] = sup
				LT += 1
		FinSi
	FinPara

	retorna(LT)
Fin

void mostrarSup(real sups[N], entero LT, real sup)
Comienzo
	entero i
	bool band

	i = 0
	band = falso

	Mientras((i < LT) y !band)
		Si(sups[i] == sup)
			Entonces band = verdadero
		FinSi

		i += 1
	FinMientras

	Si(band)        
		Entonces Escribir "Hay al menos un lote con la superficie: ", sup
	FinSi
Fin

real calcularPromedio(real sups[N], entero LT)
Comienzo
	Entero i
	real acc

	Para i desde 0 hasta LT - 1
		acc += sups[i]
	FinPara

	retorna acc / LT
Fin

void mayorPromedio(real sups[N], entero LT)
Comienzo
	entero i, cont
	real prom 

	cont = 0
	prom = calcularPromedio(sups, LT)

	Para i desde 0 hasta LT - 1
		Si(sups[i] > prom)
			Entonces cont += 1
		FinSi
	FinPara

	Escribir "Hay ", cont, " lotes con una superficie mayor a la promedio"
Fin

Comienzo
	real sups[N], sup, prom
	entero NT

	LT = carga(sups)    

	Escribir "Introduzca una superficie mayor a 650"
	Leer sup    
	mostrarSup(sups, LT, sup)

	mayorPromedio(sups, LT)
Fin
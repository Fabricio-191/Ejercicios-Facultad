/*
Una distribuidora de bebidas de nuestra provincia comercializa 50 productos. 
Estos productos son vendidos a 20 comercios locales. 

Por cada comercio se ingresan los siguientes datos: 
CUIL del comercio y la información de las compras realizadas por ese comercio a la distribuidora de bebidas. 

De cada compra, los datos ingresados son: 
Nombre del producto comprado y cantidad de unidades de éste.

1. Almacenar, en estructuras adecuadas, por cada uno de los 50 productos: el nombre y el precio unitario.
2. Mostrar para los comercios, un listado ordenado descendentemente por importe total que muestre el número de CUIL.
3. Generar una estructura que contenga el CUIL de aquellos comercios que compraron más de 500 unidades, indicar cuántos son.
4. Dado el CUIL de un comercio indicar si se encuentra entre los comercios que compraron más de 500 unidades
5. Mostrar por cada uno de los 50 productos la cantidad total de unidades que la distribuidora 
debe tener para satisfacer los pedidos realizados.
*/
constante N1 = 20
constante N2 = 50

Registro producto {
	cadena nombre
	real precioU
	entero unidadesVendidas
}

Registro compra{
	cadena producto
	entero unidades
	real precioUnidad
	real importeTotal
}

Registro comercio {
	cadena CUIL
	compra compras[N1]
	entero NroCompras
}

void carga_productos(producto productos[N2])
Comienzo
	entero i

	Para i desde 0 hasta N2 - 1
		producto[i].unidadesVendidas = 0

		Escribir "Introduzca el nombre del producto"
		Leer productos[i].nombre
		Escribir "Introduzca el precio del producto"
		Leer productos[i].precioU
	FinPara
Fin

void sumarVentas(producto productos[N2], cadena nombre, entero cant)
Comienzo
	entero i
	booleano encontro

	encontro = falso
	i = 0

	Mientras((i < N2) y !encontro)
		Si(productos[i].nombre == nombre)
			Entonces 
				encontro = verdadero 
				productos[i].unidadesVendidas += cant
			Sino 
				i++
		FinSi
	FinMientras
	
	retorna()
Fin

void carga_comercios(comercio comercios[N1], producto productos[N2])
Comienzo
	entero i, j, cantComp

	Para i desde 0 hasta N1 - 1 //iteramos una vez por cada comercio
		Escribir "Introduzca el CUIL de un comercio"
		Leer comercios[i].CUIL

		Escribir "Introduzca la cantidad de compras de ese comercio"
		Leer cantComp

		comercios[i].NroCompras = cantComp

		Para j desde 0 hasta cantComp - 1 //iteramos una vez por cada compra del comercio
			Escribir "Introduzca el nombre de producto"
			Leer comercios[i].compras[j].nombreProd
			Escribir "Introduzca la cantidad de unidades compradas"
			Leer comercios[i].compras[j].cant
		FinPara
	FinPara
Fin

void ordenar(comercio arreglo[N1])
Comienzo
	entero k, i, aux, cota

	cota = N - 1
	k = 1

	Mientras(k != -1)
		k = -1

		Para i desde 0 hasta cota - 1
			Si(arreglo[i] < arreglo[i + 1]) //descendentemente
				Entonces
					aux = arreglo[i]
					arreglo[i] = arreglo[i + 1]
					arreglo[i + 1] = aux
					k = i
			FinSi
		FinPara

		cota = k
	FinMientras

	retorna()
Fin

real importeTotal(comercio com)
Comienzo
	
Fin

entero unidadesTotales(comercio com)
Comienzo
	entero total, i

	Para i desde 0 hasta com.NroCompras - 1
		total += com.compras[i].cant
	FinPara

	retorna(total)
Fin

void encontrarCUIL(comercio comercios500[N1], entero LT)
Comienzo
	cadena CUIL
	entero i
	booleano band

	band = falso
	i = 0

	Escribir "Introduzca el CUIL del comercio"
	leer CUIL

	Mientras((i < LT) y !band)
		Si(comercios500[i].CUIL == CUIL)
			Entonces band = verdadero
			Sino i++
		FinSi
	FinMientras

	Si(band)
		Entonces Escribir "Ese comercio se encuentra entre los que compraron mas de 500 unidades"
		Sino Escribir "Ese comercio no se encuentra entre los que compraron mas de 500 unidades"
	FinSi
Fin

void mas500unidades(comercio comercios[N1])
Comienzo
	entero i, LT
	comercio comercios500[N1]

	LT = 0

	Para i desde 0 hasta LT - 1
		Si(unidadesTotales(comercios[i]) > 500)
			Entonces 
				comercios500[LT] = comercios[i]
				LT++
		FinSi
	FinPara

	Escribir "Hay ", LT, " comercios que compraron mas de 500 unidades"

	encontrarCUIL(comercios500, LT)
Fin

Comienzo
	comercio comercios[N1]
	producto productos[N2]

	carga_productos(productos) //inciso 1
	carga_comercios(comercios)

	ordenar(comercios)

	mas500unidades(comercios) //inciso 3 y 4
Fin


/*
N es 11, por lo tanto el arreglo tiene 11 componentes:

[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][  ]	
 0  1  2  3  4  5  6  7  8  9  10 posiciones
 
 1  2  3  4  5  6  7  8  9  10 11 componentes
*/
void cargar(entero con[N])
Comienzo
	entero i,
	real nota
	Para i Desde 1 Hasta 200
		Escribir " ingrese nota del alumno ",i
		Leer nota

		con[nota] = con[nota] + 1 // se cuentan los alumnos por nota
	FinPara
	retorna()
Fin
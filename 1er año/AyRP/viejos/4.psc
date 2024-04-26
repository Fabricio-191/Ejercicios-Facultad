/*
Un local de comidas para llevar, premia a los primeros 15 clientes del día con 15% de descuento. 
Los datos que se registran de cada cliente son Nombre y apellido, DNI, Edad, Domicilio, Importe pagado.

Realizar un algoritmo que usando subprogramas permita:

1. Cargar la información en un arreglo de registros.
2. Mostrar los datos de los clientes que pagaron más y de los clientes que pagaron menos.
3. Escribir la edad promedio de los clientes.
*/
constante N = 15

Registro cliente {
	cadena nombre
	cadena DNI
	cadena domicilio
	entero edad
	real importe
}

void cargar(cliente clientes[N])
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		Escribir "Introduzca los datos del cliente"
		Leer clientes[i].nombre, 
			 clientes[i].DNI, 
			 clientes[i].domicilio, 
			 clientes[i].edad, 
			 clientes[i].importe
	FinPara
Fin

real importeMax(cliente clientes[N])
Comienzo
	real max
	entero i

	Para i desde 0 hasta N - 1
		Si(clientes[i].importe > max)
			Entonces max = clientes[i].importe
		FinSi
	FinPara

	retorna(max)
Fin

real importeMin(cliente clientes[N])
Comienzo
	real min
	entero i

	Para i desde 0 hasta N - 1
		Si(clientes[i].importe < min)
			Entonces min = clientes[i].importe
		FinSi
	FinPara

	retorna(min)
Fin

void mostrar(cliente clientes[N], real importe, cadena texto)
Comienzo
	entero i
	cliente cli

	Para i desde 0 hasta N - 1
		Si(clientes[i].importe == importe)
			cli = clientes[i]
			Entonces 
				Escribir "El cliente: ", cli.nombre, " fue uno de los que ", texto, " pago"
				Escribir "DNI: ", cli.DNI
				Escribir "Domicilio: ", cli.domicilio
				Escribir "edad: ", cli.edad
				Escribir "Importe: ", cli.importe
		FinSi
	FinPara
Fin

void edadProm(cliente clientes[N])
Comienzo
	entero i, edades
	real prom

	edades = 0

	Para i desde 0 hasta N - 1
		edades += clientes[i].edad
	FinPara

	Escribir "La edad promedio de los 15 clientes es: ", edades / N
Fin

Comienzo 
	cliente clientes[N]

	cargar(clientes)
	
	mostrar(clientes, importeMax(clientes), "mas")
	mostrar(clientes, importeMin(clientes), "menos")
	edadProm(clientes)
Fin
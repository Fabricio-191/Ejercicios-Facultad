/*
Una consultora procesa los datos de 600 empresas. 
De cada llamada conoce: código de localidad (número entre 1 y 19), cantidad de empleados.
Construya un algoritmo que usando subprogramas permita:

1. Decir para cada localidad la cantidad de empresas.
2. Informar para cada localidad la cantidad promedio de empleados.
*/
constante N = 600
constante N1 = 19

Registro empr {
	entero localidad
	entero cantidadEmpl
}

void carga(empr empresas[N])
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		Escribir "Introduzca el codigo de localidad"
		Leer empresas[i].localidad
		Escribir "Introduzca la cantidad de empleados"
		Leer empresas[i].cantidadEmpl
	FinPara
Fin

entero cantidadEmpresas(empr empresas[N], entero localidad)
Comienzo
	entero i, cont

	cont = 0

	Para i desde 0 hasta N - 1
		Si(empresas[i].localidad == localidad)
			Entonces cont++
		FinSi
	FinPara

	retorna(cont)
Fin

real promedioEmpleados(empr empresas[N], entero cantidadEmpr)
Comienzo
	entero i, acc

	acc = 0

	Para i desde 0 hasta N - 1
		Si(empresas[i].localidad == localidad)
			Entonces acc += empresas[i].cantidadEmpl
		FinSi
	FinPara

	retorna(acc / cantidadEmpr)
Fin

void porLocalidad(empr empresas[N])
Comienzo
	entero i, cantidadEmpr, promedioEmpl

	Para i desde 1 hasta N1
		cantidadEmpr = cantidadEmpresas(empresas, i)
		promedioEmpl = promedioEmpleados(empresas, cantidadEmpr)

		Escribir "En la localidad N° ", i, " hay ", cantidadEmpr, " empresas"
		Escribir "Y un promedio de ", promedioEmpl, " de empleados por empresa"
	FinPara
Fin

Comienzo
	empr empresas[N]

	carga(empresas)
	porLocalidad(empresas)
Fin
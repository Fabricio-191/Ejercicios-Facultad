constante N = 19

Registro dept {
	cadena nombre
	entero edadTotal
	entero nRoParticipantes
}

void cargaDepts(dept departamentos[N])
Comienzo
	entero i
	cadena nombre

	Para i desde 0 hasta N - 1
		Escribir "Introduzca el nombre del departamento: ", i + 1
		Leer nombre

		departamentos[i].nombre = nombre
		departamentos[i].edadProm = 0
		departamentos[i].nRoParticipantes = 0
	FinPara

	retorna()
Fin

void carga(dept departamentos[N])
Comienzo
	entero edad, nRoDept

	Escribir "Introduzca el numero del departamento (0 para terminar)"
	Leer nRoDept

	Mientras(nRoDept != 0)
		Escribir "Introduzca la edad del participante"
		Leer edad

		departamentos[nRoDept].nRoParticipantes++
		departamentos[nRoDept].edadProm += edad

		Escribir "Introduzca el numero del departamento (0 para terminar)"
		Leer nRoDept
	FinMientras

	departamentos[nRoDept].edadProm /= departamentos[nRoDept].nRoParticipantes
	retorna()
Fin

void mostrarEdades(dept departamentos[N])
Comienzo
	entero i
	Para i desde 0 hasta N - 1
		Escribir "La edad promedio en el departamento ", departamentos[i].nombre, " es: ", departamentos[i].edadProm
	FinPara
	retorna()
Fin

entero subarreglo(dept departamentos[N], dept subarreglo[N], entero valor)
Comienzo
	entero i, LT
	LT = 0
	Para i desde 0 hasta N - 1
		Si(departamentos[i].cantParticipantes > valor)
			Entonces
				subarreglo[LT] = departamentos[i]
				LT++
		FinSi
	FinPara

	retorna()
Fin

void ordenar(dept subarreglo[N], entero LT) //metodo burbuja mejorado
Comienzo
	entero k, i, aux, cota

	cota = LT - 1
	k = 1

	Mientras(k != -1)
		k = -1

		Para i desde 0 hasta cota - 1
			Si(arreglo[i].cantParticipantes > arreglo[i + 1].cantParticipantes)  //ascendente
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

void mostrarSubarreglo(dept subarreglo[N], entero LT)
Comienzo
	entero i
	Para i desde 0 hasta LT - 1
		Escribir "Nro: ", i
		Escribir "Nombre: ", subarreglo[i].nombre
		Escribir "Participantes: ", subarreglo[i].nRoParticipantes
		Escribir "Edad promedio: ", subarreglo[i].edadProm
	FinPara
Fin

Comienzo
	dept departamentos[N], subarreglo[N]
	entero LT, cantParticipantes

	cargaDepts(departamentos)
	carga(departamentos)
	mostrarEdades(departamentos)

	Escribir "Introduzca la cantidad de participantes"
	Leer cantParticipantes
	LT = subarreglo(departamentos, subarreglo, cantParticipantes)
	ordenar(subarreglo, LT)
	mostrarSubarreglo(subarreglo, LT)
Fin
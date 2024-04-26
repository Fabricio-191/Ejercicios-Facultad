/*
Hacer un algoritmo que resuelva el siguiente enunciado:
Se cuenta con el número de día y la temperatura registrada a las 16 horas, de cada uno de los 30 días del mes de abril.

a)	Almacenar esas temperaturas en un arreglo, teniendo en cuenta que el número de día es aleatorio.
b)	Imprimir las temperaturas registradas en los días impares.
c)	Mostrar los números de los días donde se registró la menor temperatura.
d)	Mostrar los números de los días donde se registró la mayor temperatura.
e)	Ingresar por teclado dos números de días e intercambie las temperaturas registradas en los mismos.
*/

Algoritmo temperaturasAbril
constante N = 30

void mostrar(real temperaturas[N], real min_temp, real max_temp)
Comienzo
	entero dia
	real temp

	Para dia desde 1 hasta N
		temp = temperaturas[dia - 1]

		Si((dia % 2) == 1)
			Entonces Escribir "El dia ", dia, " se registro la temperatura ", temp
		FinSi

		Si(temp == max_temp)
			Entonces Escribir "El dia ", dia, " fue uno donde se registro la mayor temperatura"
		FinSi
		Si(temp == min_temp)
			Entonces Escribir "El dia ", dia, " fue uno donde se registro la menor temperatura"
		FinSi
	FinPara
Fin

void intercambiarTemps(real temperaturas[N])
Comienzo
	entero d1, d2
	real temp

	Escribir "Introducir los 2 dias en los cuales intercambiar temperaturas (0 en alguno para cancelar)"
	Leer d1, d2

	Si((d1 < 1) o (d2 < 1) o (d1 > 30) o (d2 > 30))
		Entonces retorna()
	FinSi

	d1 -= 1
	d2 -= 1

	temp = temperaturas[d1]
	temperaturas[d1] = temperaturas[d2]
	temperaturas[d2] = temp

	retorna()
Fin

Comienzo
	entero dia
	real temperaturas[N], temp, MIN_temp, MAX_temp

	MIN_temp = 100000
	MAX_temp = -100000

	Escribir "Introduzca el numero del dia"
	Leer dia

	Mientras(dia != 0)
		Escriba "Introduzca la temperatura"
		Leer temp

		temperaturas[dia - 1] = temp

		Si(temp < MIN_temp)
			Entonces MIN_temp = temp
		FinSi
		Si(temp > MAX_temp)
			Entonces MAX_temp = temp
		FinSi

		Escribir "Introduzca el numero del dia"
		Leer dia
	FinMientras

	intercambiarTemps(temperaturas)
	mostrar(temperaturas, MIN_temp, MAX_temp)
Fin


entero buscar(entero arr[N], entero valor)
Comienzo
	entero i

	Para i desde 0 hasta N - 1
		Si(arr[i] == valor) retorna(i)
	FinPara

	retorna(-1)
Fin
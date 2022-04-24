Registro usuario {
	cadena nombre
	entero edad
}

void ordenar (usuario a[n])
Comienzo
	entero k, i, aux, cota
	cota = n - 1
	k = 1

	Mientras (k != -1)
		k = -1
		Para i Desde 0 Hasta cota - 1
			Si (a.edad[i] > a.edad[i+1])
				entonces
					aux = a[i]
					a[i] = a[i+1]
					a[i+1] = aux
					k = i
			FinSi
		FinPara
		cota = k
	FinMientras

	retorna ()
Fin
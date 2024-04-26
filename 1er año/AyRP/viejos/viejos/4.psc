
// dice si x numero tiene 4 divisores
booleano divisores4(entero num)
Comienzo
	int i, cont

	cont = 2 //num y 1
	i = 2
	
	Si(num < 0)
		retorna (falso)
	FinSi

	Mientras((i < num) y (cant < 4))
		Si((num % i) == 0)
			Entonces cont += 1
		FinSi
		
		i++
	FinMientras

	retorna(cont == 4)
Fin
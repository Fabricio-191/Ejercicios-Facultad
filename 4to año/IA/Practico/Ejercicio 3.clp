(deffacts numeros
	; Hechos que son todos los numeros posibles
	(numero 0)
	(numero 1)
	(numero 2)
	(numero 3)
	(numero 4)
	(numero 5)
	(numero 6)
	(numero 7)
	(numero 8)
	(numero 9)
)

(defrule buscarSolucion
	; Se asignan valores a las variables y se comprueban que sean valores distintos a las variables previamentes asignadas
	(numero ?a)
	(numero ?g &~ ?a)
	(numero ?u &~ ?a &~ ?g)
	(numero ?s &~ ?a &~ ?g &~ ?u)
	(numero ?l &~ ?a &~ ?g &~ ?u &~ ?s)
	(numero ?d &~ ?a &~ ?g &~ ?u &~ ?s &~ ?l)
	; Luego nos fijamos si estas asignaciones de numeros a las variables cumplen la ecuacion
	; A * 3000 + G * 300 + U * 30 + A * 3 = S * 10000 + A * 1000 + L * 100 + U * 10 + D
	(test (eq
		(+ (* ?a 3000) (* ?g 300) (* ?u 30) (* ?a 3))
		(+ (* ?s 10000) (* ?a 1000) (* ?l 100) (* ?u 10) ?d)
	))
	=>
	; Si cumplen, esto significa que son solucion
	(printout t "Solucion: A = " ?a ", G = " ?g ", U = " ?u ", S = " ?s ", L = " ?l ", D = " ?d crlf)
	(assert (solucion ?a ?g ?u ?s ?l ?d))
)
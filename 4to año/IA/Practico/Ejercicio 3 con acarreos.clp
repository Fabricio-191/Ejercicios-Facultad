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
	(acarreo 0)
	(acarreo 1)
	(acarreo 2)
)

(defrule buscarSolucion
	; Se asignan valores a las variables y se comprueba a medida que se puede las distintas ecuaciones de la representacion con acarreos
	(acarreo ?x)
	(numero ?s &~ 0)
	(test (eq ?x ?s)) ; X = S

	(acarreo ?y)
	(numero ?a &~ ?s &~ 0)
	(test (eq (+ ?y (* 3 ?a)) (+ ?a (* 10 ?x)))) ; Y + 3 * A = A + 10 * X

	(acarreo ?w)
	(numero ?d &~ ?s &~ ?a &~ 0)
	(test (eq (* 3 ?a) (+ ?d (* 10 ?w))))        ; 3 * A = D + 10 * W
	
	(acarreo ?z)
	(numero ?u &~ ?s &~ ?a &~ ?d &~ 0)
	(test (eq (+ ?w (* 3 ?u)) (+ ?u (* 10 ?z)))) ; W + 3 * U = U + 10 * Z

	(numero ?g &~ ?s &~ ?a &~ ?d &~ ?u &~ 0)
	(numero ?l &~ ?s &~ ?a &~ ?d &~ ?u &~ ?g &~ 0)
	(test (eq (+ ?z (* 3 ?g)) (+ ?l (* 10 ?y)))) ; Z + 3 * G = L + 10 * Y
	=>
	; Si cumplen las ecuaciones, eso significa que estos valores son una solucion
	(printout t "Solucion: A = " ?a ", G = " ?g ", U = " ?u ", S = " ?s ", L = " ?l ", D = " ?d " , Acarreos: X = " ?x ", Y = " ?y ", W = " ?w ", Z = " ?z crlf)
	(assert (solucion ?a ?g ?u ?s ?l ?d ?x ?y ?w ?z))
)

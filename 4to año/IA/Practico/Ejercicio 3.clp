;  AGUA
;  AGUA
;  AGUA
; SALUD

; A * 3000 + G * 300 + U * 30 + A * 3 = S * 10000 + A * 1000 + L * 100 + U * 10 + D
; A, G, U, S, L, D

; A * 3000 + G * 300 + U * 30 + A * 3 = S * 10000 + A * 1000 + L * 100 + U * 10 + D

(deffunction distintos (?a ?b ?c ?d ?e ?f)
 	; check all numbers are different
	(and
		(neq ?a ?b)
		(neq ?a ?c) (neq ?b ?c)
		(neq ?a ?d) (neq ?b ?d) (neq ?c ?d)
		(neq ?a ?e) (neq ?b ?e) (neq ?c ?e) (neq ?d ?e)
		(neq ?a ?f) (neq ?b ?f) (neq ?c ?f) (neq ?d ?f) (neq ?e ?f)
	)
)

(deffacts numeros
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
	(numero ?a)
	(numero ?g)
	(numero ?u)
	(numero ?s)
	(numero ?l)
	(numero ?d)
	(test (distintos ?a ?g ?u ?s ?l ?d))
	(test (eq (+ (* ?a 3000) (* ?g 300) (* ?u 30) (* ?a 3)) (+ (* ?s 10000) (* ?a 1000) (* ?l 100) (* ?u 10) ?d)))
	=>
	(printout t "Solucion: " crlf)
	(printout t "A = " ?a crlf)
	(printout t "G = " ?g crlf)
	(printout t "U = " ?u crlf)
	(printout t "S = " ?s crlf)
	(printout t "L = " ?l crlf)
	(printout t "D = " ?d crlf)
	(assert (solucion ?a ?g ?u ?s ?l ?d))
)
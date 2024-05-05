;  AGUA
;  AGUA
;  AGUA
; SALUD

; A * 3000 + G * 300 + U * 30 + A * 3 = S * 10000 + A * 1000 + L * 100 + U * 10 + D
; A, G, U, S, L, D

; A * 3000 + G * 300 + U * 30 + A * 3 = S * 10000 + A * 1000 + L * 100 + U * 10 + D

(defrule solucion ; all values are different
	(combinacion ?a &~ ?g &~ ?u &~ ?s &~ ?l &~ ?d)
	(test (eq (+ (* ?a 3000) (* ?g 300) (* ?u 30) (* ?a 3)) (+ (* ?s 10000) (* ?a 1000) (* ?l 100) (* ?u 10) ?d)))
	=>
	(printout t "Solucion: " crlf)
	(printout t "A = " ?a crlf)
	(printout t "G = " ?g crlf)
	(printout t "U = " ?u crlf)
	(printout t "S = " ?s crlf)
	(printout t "L = " ?l crlf)
	(printout t "D = " ?d crlf)
)

(defrule inicio
	=>
	(assert (numero 0))
	(assert (numero 1))
	(assert (numero 2))
	(assert (numero 3))
	(assert (numero 4))
	(assert (numero 5))
	(assert (numero 6))
	(assert (numero 7))
	(assert (numero 8))
	(assert (numero 9))
)

(deffunction distintos (?a ?g ?u ?s ?l ?d)
 	; check all numbers are different
	(and
		(<> ?a ?g) (<> ?a ?u) (<> ?a ?s) (<> ?a ?l) (<> ?a ?d)
		(<> ?g ?u) (<> ?g ?s) (<> ?g ?l) (<> ?g ?d)
		(<> ?u ?s) (<> ?u ?l) (<> ?u ?d)
		(<> ?s ?l) (<> ?s ?d)
		(<> ?l ?d)
	)
)
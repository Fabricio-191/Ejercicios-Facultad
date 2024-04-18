
(deftemplate Reina 
	(slot fila)
	(slot columna)
)

(defrule init										;- Inicializar espacio de busqueda
=>
	(loop-for-count (?i 1 4) do						; Para i de 1 a 4
	(loop-for-count (?j 1 4) do						; Para j de 1 a 4
	(assert (Reina (fila ?i)(columna ?j)))))		; assert Reina[i][j]
)

(defrule 4-Reinas
	
	?R1 <-
	(Reina (fila 1) (columna ?y1))					; R1 se ubica en una columna sin restriccion

	?R2 <-
	(Reina 
		(fila 2)
		(columna ?y2 & ~?y1 &:(and 					; R2 no esté en la misma columna que R1 y..
			(<> ?y1 (+ ?y2 1))						; R2 no esté en la diagonal decreciente de R1
			(<> ?y1 (- ?y2 1)))						; R2 no esté en la diagonal creciente de R1
		)
	)

	?R3 <-
 	(Reina 
 		(fila 3)
 		(columna ?y3 & ~?y1 & ~?y2 &:(and			; R3 no esté en la misma columna que R1, R2 y..
 			(<> ?y1 (+ ?y3 2))						; R3 no esté en la diagonal decreciente de R1
 			(<> ?y1 (- ?y3 2))						; R3 no esté en la diagonal creciente de R1
 			(<> ?y2 (+ ?y3 1))						; R3 no esté en la diagonal decreciente de R2
 			(<> ?y2 (- ?y3 1)))						; R3 no esté en la diagonal creciente de R1
 		)
 	)

 	?R4 <-
 	(Reina 
 		(fila 4)
 		(columna ?y4 & ~?y1 & ~?y2 &~?y3 &: (and	; R4 no esté en la misma columna que R1, R2, R3 y..
 			(<> ?y1 (+ ?y4 3))						; R4 no esté en la diagonal decreciente de R1
 			(<> ?y1 (- ?y4 3))						; R4 no esté en la diagonal creciente de R1
 			(<> ?y2 (+ ?y4 2))						; R4 no esté en la diagonal decreciente de R2
 			(<> ?y2 (- ?y4 2))						; R4 no esté en la diagonal creciente de R2
 			(<> ?y3 (+ ?y4 1))						; R4 no esté en la diagonal decreciente de R3
 			(<> ?y3 (- ?y4 1)))						; R4 no esté en la diagonal creciente de R3
 		)
 	)

=>
	(printout t "Solucion:" crlf)
	(printout t " - R1:" crlf)
	(printout t "        Fila " 1 crlf)
	(printout t "        Columna " ?y1 crlf)
	(printout t " - R2:" crlf)
	(printout t "        Fila " 2 crlf)
	(printout t "        Columna " ?y2 crlf)
	(printout t " - R3:" crlf)
	(printout t "        Fila " 3 crlf)
	(printout t "        Columna " ?y3 crlf)
	(printout t " - R4:" crlf)
	(printout t "        Fila " 4 crlf)
	(printout t "        Columna " ?y4 crlf)

	(printout t " Siguiente solucion..")
 	(readline)
 	(printout t crlf crlf)

)

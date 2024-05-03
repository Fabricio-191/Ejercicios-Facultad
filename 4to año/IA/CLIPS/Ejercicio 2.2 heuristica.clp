(deftemplate nodo
   (multislot estado (type INTEGER) (cardinality 16 16) (range 0 15)) 
   (slot heuristica (type INTEGER))
)

(defglobal ?*estadoFinal* = (create$ 0 14 13 3 11 5 6 8 7 9 10 4 12 2 1 15))

(deffunction calcularHeuristica (?estado)
	(bind ?heu 0)
	(loop-for-count (?i 1 9) 
		(if (neq (nth ?i $?estado) (nth ?i ?*estadoFinal*))
			then (bind ?heu (+ ?heu 1))
		)
	)
	;(bind ?i 0)
	;(while (<= ?i 15)
	;	(bind ?j 0)
	;	(while (<= ?j 15)
	;		(if (and (<> ?i ?j) (<> (nth$ ?i ?contenidos) 0) (<> (nth$ ?j ?contenidos) 0))
	;			(if (and (<= (nth$ ?i ?contenidos) (nth$ ?j ?contenidos)) (<> (nth$ ?i ?contenidos) 0))
	;				(bind ?heuristica (+ ?heuristica 1))
	;			)
	;		)
	;		(bind ?j (+ ?j 1))
	;	)
	;	(bind ?i (+ ?i 1))
	;)
	(return ?heu)
)

(defrule inicio
	=> 
	(assert (movimiento -4))
	(assert (movimiento -1))
	(assert (movimiento  1))
	(assert (movimiento  4))
	(assert (nodo (estado 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15) (heuristica 32)))
)

(defrule estadoFinal
	(declare (salience 10000))
	(estado (contenido ?*estadoFinal*) (heuristica 0))
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule moverPieza
	(movimiento ?diff)
	(estado (contenido $?contenidos) (heuristica ?heu))
	(not (estado (heuristica ?h2&:(< ?h2 ?heu))))
	
	=>
	
	(assert (estado
		(contenido ?contenidos)
		(heuristica (calcularHeuristica ?contenidos))
	))
)

(defrule eliminarEstadosSinSalida
	(declare (salience -50))
	?fact <- (jarras (heuristica ?heu) (contenido $?contenido))
	(not (jarras (heuristica ?h2&:(< ?h2 ?heu))))
	=>
	(retract ?fact)
	(assert (estadoSinSalida ?contenido))
)

;  24  0   0   0
;  13  0   11  0
;  8   0   11  5
;  8   5   11  0
;  8   13  3   0
;  8   8   3   5
;  8   8   8   0
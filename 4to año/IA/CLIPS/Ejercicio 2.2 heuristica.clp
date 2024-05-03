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
	(assert (nodo (estado 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15) (heuristica 32)))
)

(defrule estadoFinal
	(declare (salience 10000))
	(estado (contenido ?*estadoFinal*) (heuristica 0))
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule arriba 
	(nodo (estado $?a ?b ?c ?d H $?e) (heuristica ?heu)) 
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	=> 
	(bind ?nuevo-estado (create$ $?a H ?c ?d ?b $?e)) 
	(assert (nodo (estado ?nuevo-estado) (heuristica (calcularHeuristica $?nuevo-estado))))
)

(defrule abajo 
	(nodo (estado $?a H ?b ?c ?d $?e) (heuristica ?heu)) 
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	=> 
	(bind ?nuevo-estado (create$ $?a ?d ?b ?c H $?e)) 
	(assert (nodo (estado ?nuevo-estado) (heuristica (calcularHeuristica $?nuevo-estado))))
)

(defrule derecha 
	(nodo (estado $?a H ?b $?c&:(neq (mod (length $?c) 3) 2)) (heuristica ?heu))
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu)))) 
	=> 
	(bind ?nuevo-estado (create$ $?a ?b H $?c)) 
	(assert (nodo (estado ?nuevo-estado) (heuristica (calcularHeuristica $?nuevo-estado))))
)

(defrule izquierda 
	(nodo (estado $?a&:(neq (mod (length $?a) 3) 2) ?b H $?c) (heuristica ?heu))
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	=> 
	(bind ?nuevo-estado (create$ $?a H ?b $?c)) 
	(assert (nodo (estado ?nuevo-estado) (heuristica (calcularHeuristica $?nuevo-estado))))
)

(defrule eliminarEstadosSinSalida
	(declare (salience -50))
	?fact <- (jarras (heuristica ?heu) (estado $?estado))
	(not (jarras (heuristica ?h2&:(< ?h2 ?heu))))
	=>
	(retract ?fact)
	(assert (estadoSinSalida ?estado))
)


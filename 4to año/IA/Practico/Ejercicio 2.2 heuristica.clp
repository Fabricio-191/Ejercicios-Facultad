(deftemplate nodo 
   (multislot estado) 
   (slot heuristica) 
   (slot clase (default abierto))
)

(defglobal MAIN 
   ?*estadoInicial* = (create$ 0  1  2 3  4 5 6 7 8 9 10 11 12 13 14 15)
   ?*estadoFinal*   = (create$ 0 14 13 3 11 5 6 8 7 9 10  4 12  2  1 15) 
)

(deffunction heuristica ($?estado)
	(bind ?res 0)
	(loop-for-count (?i 1 16) 
		(if (neq (nth ?i $?estado) (nth ?i ?*estadoFinal*))
			then (bind ?res (+ ?res 1))
		)
	)
	(if (neq (subseq$ $?estado 13 16) (create$ 12 2 1 15))
		then (bind ?res (+ ?res 1000))
	) 
	?res
)


(defrule inicio
	=> 
	(assert (nodo
		(estado ?*estadoInicial*) 
		(heuristica (heuristica ?*estadoInicial*)) 
		(clase cerrado)
	))
	; (podrian declararse como hechos pero al hacerlo como regla no hace falta usar reset al comenzar)
)


(defrule final 
	(declare (salience 10000))
	(nodo (estado 0 14 13 3 11 5 6 8 7 9 10 4 12 2 1 15) (heuristica 0))
	=>
	(printout t "Se encontro la solucion" crlf)
	(halt) 
)

;Movimientos del espacio blanco
(defrule arriba 
	(nodo (estado $?a ?b ?c ?d ?e 0 $?f) (clase cerrado)) 
	=> 
	(bind $?nuevo-estado (create$  $?a 0 ?c ?d ?e ?b $?f)) 
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado))))
)

(defrule abajo 
	(nodo (estado $?a 0 ?b ?c ?d ?e $?f) (clase cerrado)) 
	=> 
	(bind $?nuevo-estado (create$ $?a ?e ?b ?c ?d 0 $?f)) 
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado))))
)

(defrule derecha 
	(nodo (estado $?a 0 ?b $?c&:(neq (mod (length $?c) 4) 3)) (clase cerrado)) 
	=> 
	(bind $?nuevo-estado (create$ $?a ?b 0 $?c)) 
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado))))
)

(defrule izquierda 
	(nodo (estado $?a&:(neq (mod (length $?a) 4) 3) ?b 0 $?c) (clase cerrado))
	=> 
	(bind $?nuevo-estado (create$ $?a 0 ?b $?c)) 
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado))))
)

(defrule cerrarMejorNodo
	(declare (salience -10)) 
	?nodo <- (nodo (clase abierto) (heuristica ?h1)) 
	(not (nodo (clase abierto) (heuristica ?h2&:(< ?h2 ?h1)))) 
	=> 
	(modify ?nodo (clase cerrado))
)
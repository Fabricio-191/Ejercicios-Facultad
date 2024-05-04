(deftemplate nodo
	(multislot estado (type INTEGER) (cardinality 16 16) (range 0 15))
	(slot index (type INTEGER) (range 1 16))
	(slot heuristica (type INTEGER))
)

;  1  2  3  4
;  5  6  7  8
;  9 10 11 12
; 13 14 15 16

(defglobal
	?*estadoFinal* = (create$ 0 14 13 3 11 5 6 8 7 9 10 4 12 2 1 15)
	?*limiteIzquierdo* = (create$ 1 5 9 13)
	?*limiteDerecho* = (create$ 4 8 12 16)
)

(deffunction calcularHeuristica (?estado)
	(bind ?heu 0)
	(loop-for-count (?i 1 9)
		(if (neq (nth ?i $?estado) (nth ?i ?*estadoFinal*))
			then (bind ?heu (+ ?heu 1))
		)
	)
	(return ?heu)
)

(deffunction mover (?estado ?idx ?mov)
	(bind ?newIdx (+ ?idx ?mov))
	(bind ?estado (replace$ ?estado ?idx ?idx (nth$ ?newIdx ?estado)))
	(bind ?estado (replace$ ?estado ?newIdx ?newIdx 0))
	(assert (nodo (estado ?estado) (index ?newIdx) (heuristica (calcularHeuristica ?estado))))
)

(defrule inicio
	=>
	(assert (nodo (estado 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15) (index 1) (heuristica 32)))
	
)

(defrule estadoFinal
	(declare (salience 10000))
	(nodo (estado 0 14 13 3 11 5 6 8 7 9 10 4 12 2 1 15) (heuristica 0))
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule moverArriba
	(nodo (estado $?estado) (index ?idx) (heuristica ?heu))
	(not (estadoSinSalida $?estado))
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	(test (and (>= ?idx 1) (<= ?idx 12)))
	=>
	(mover ?estado ?idx 4)
)

(defrule moverAbajo
	(nodo (estado $?estado) (index ?idx) (heuristica ?heu))
	(not (estadoSinSalida $?estado))
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	(test (and (>= ?idx 5) (<= ?idx 16)))
	=>
	(mover ?estado ?idx -4)
)

(defrule moverIzquierda
	(nodo (estado $?estado) (index ?idx) (heuristica ?heu))
	(not (estadoSinSalida $?estado))
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	(test (not (member$ ?idx ?*limiteIzquierdo*)))
	=>
	(mover ?estado ?idx -1)
)

(defrule moverDerecha
	(nodo (estado $?estado) (index ?idx) (heuristica ?heu))
	(not (estadoSinSalida $?estado))
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	(test (not (member$ ?idx ?*limiteDerecho*)))
	=>
	(mover ?estado ?idx 1)
)

(defrule eliminarEstadosSinSalida
	(declare (salience -50))
	?fact <- (nodo (heuristica ?heu) (estado $?estado))
	(not (nodo (heuristica ?h2&:(< ?h2 ?heu))))
	=>
	(retract ?fact)
	(assert (estadoSinSalida ?estado))
)
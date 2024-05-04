(deftemplate jarras
	(multislot contenido (type INTEGER) (range 0 24) (cardinality 4 4))
	(slot heuristica (type INTEGER))
)

(defglobal ?*capacidades* = (create$ 24 13 11 5))

(deffunction calcularHeuristica (?contenidos)
	(+
		(abs (- 8 (nth$ 1 ?contenidos)))
		(abs (- 8 (nth$ 2 ?contenidos)))
		(abs (- 8 (nth$ 3 ?contenidos)))
		(nth$ 4 ?contenidos)
	)
	; (+
	; 	(if (> ?c1 8) then (* (- ?c1 8) 2) else (- 8 ?c1))
	; 	(if (> ?c2 8) then (* (- ?c2 8) 2) else (- 8 ?c2))
	; 	(if (> ?c3 8) then (* (- ?c3 8) 2) else (- 8 ?c3))
	; )
)

(defrule inicio
	=> 
	(assert (numero 1))
	(assert (numero 2))
	(assert (numero 3))
	(assert (numero 4))
	(assert (jarras (contenido 24 0 0 0) (heuristica 32)))
)

(defrule estadoFinal
	(declare (salience 10000))
	(jarras (contenido 8 8 8 0) (heuristica 0))
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule moverDeJarraEnJarra
	(numero ?origen)
	(numero ?destino)
	(test (neq ?origen ?destino))
	(jarras (contenido $?contenidos) (heuristica ?heu))
	(not (jarras (heuristica ?h2&:(< ?h2 ?heu))))
	(not (estadoSinSalida ?contenido))
	=>
	(bind ?conOrigen (nth$ ?origen ?contenidos))
	(bind ?capDestino (nth$ ?destino ?*capacidades*))
	(bind ?conDestino (nth$ ?destino ?contenidos))
	(bind ?litros (min ?conOrigen (- ?capDestino ?conDestino)))
	(bind ?contenidos (replace$ ?contenidos ?origen  ?origen  (- ?conOrigen  ?litros)))
	(bind ?contenidos (replace$ ?contenidos ?destino ?destino (+ ?conDestino ?litros)))
	(assert (jarras (contenido ?contenidos) (heuristica (calcularHeuristica ?contenidos)) ))
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
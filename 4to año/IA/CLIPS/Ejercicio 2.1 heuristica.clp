(deftemplate jarras
	(multislot contenido (type INTEGER) (range 0 24) (cardinality 4 4))
	(slot heuristica (type INTEGER))
	(slot estado (type SYMBOL) (allowed-values nuevo en_uso usado no_usar))
)

(defglobal ?*capacidades* = (create$ 24 13 11 5))


(deffunction calcularHeuristica (?contenidos)
	(bind ?c1 (- 8 (nth$ 1 ?contenidos)))
	(bind ?c2 (- 8 (nth$ 2 ?contenidos)))
	(bind ?c3 (- 8 (nth$ 3 ?contenidos)))
	(+
		(if (> ?c1 8) then (* (- ?c1 8) 2) else (- 8 ?c1))
		(if (> ?c2 8) then (* (- ?c2 8) 2) else (- 8 ?c2))
		(if (> ?c3 8) then (* (- ?c3 8) 2) else (- 8 ?c3))
	)
)


(defrule inicio
	=>
	(assert (numero 1))
	(assert (numero 2))
	(assert (numero 3))
	(assert (numero 4))
	(assert (jarras (contenido 24 0 0 0) (heuristica 32) (estado nuevo)))
)

(defrule estadoFinal
	(declare (salience 10000))
	(jarras (contenido 8 8 8 0) (heuristica 0))
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule eliminarRepetidos
	(declare (salience 1000))
	(jarras (contenido $?contenidos) (estado~nuevo))
	?fact <- (jarras (contenido $?contenidos) (estado nuevo))
	=>
	(retract ?fact)
)

(defrule moverDeJarraEnJarra
	(numero ?jarraOrigen)
	(numero ?jarraDestino)
	(test (neq ?jarraOrigen ?jarraDestino))
	(jarras (contenido $?contenidos) (estado en_uso))
	=>
	(bind ?contenidoOrigen (nth$ ?jarraOrigen ?contenidos))
	(bind ?capacidadDestino (nth$ ?jarraDestino ?*capacidades*))
	(bind ?contenidoDestino (nth$ ?jarraDestino ?contenidos))
	(bind ?litros (min ?contenidoOrigen (- ?capacidadDestino ?contenidoDestino)))
	(bind ?contenidos (replace$ ?contenidos ?jarraOrigen  ?jarraOrigen  (- ?contenidoOrigen  ?litros)))
	(bind ?contenidos (replace$ ?contenidos ?jarraDestino ?jarraDestino (+ ?contenidoDestino ?litros)))
	(assert (jarras
		(contenido ?contenidos)
		(heuristica (calcularHeuristica ?contenidos))
		(estado nuevo)
	))
)

(defrule marcarUsado
	(declare (salience -5))
	?fact <- (jarras (estado en_uso))
	=>
	(modify ?fact (estado usado))
)

(defrule borrarMayorHeuristica
	(declare (salience -10))
	(jarras (heuristica ?h1) (estado nuevo))
	?fact <- (jarras (heuristica ?h2) (estado nuevo))
	(test (< ?h1 ?h2))
	=>
	(modify ?fact (estado no_usar))
)

(defrule seleccionarMenorHeuristica
	(not (jarras (estado en_uso)))
	?jarras <- (jarras (contenido $?contenidos) (heuristica ?h) (estado nuevo))
	(not (jarras (heuristica ?h2&:(< ?h2 ?h)) (estado nuevo)))
	; (not (jarras (contenido $?contenidos) (estado usado)))
	=>
	(printout t "Contenido de las jarras: " ?contenidos crlf)
	(modify ?jarras (estado en_uso))
)

;  24   0   0   0
;  13   0  11   0
;   8   0  11   5
;   8   5  11   0
;   8  13   3   0
;   8   8   3   5
;   8   8   8   0

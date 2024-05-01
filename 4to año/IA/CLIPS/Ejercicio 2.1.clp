(deftemplate jarras
	(slot jarra1 (type INTEGER) (range 0 24))
	(slot jarra2 (type INTEGER) (range 0 13))
	(slot jarra3 (type INTEGER) (range 0 11))
	(slot jarra4 (type INTEGER) (range 0 5))
)

(deffacts estadoInicial (jarras (jarra1 24) (jarra2 0) (jarra3 0) (jarra4 0)))
(assert (jarras (jarra1 24) (jarra2 0) (jarra3 0) (jarra4 0)))

(defrule estadoFinal
	(jarras (jarra1 8) (jarra2 8) (jarra3 8) (jarra4 0))
	=>
	(printout t "Estado Final" crlf)
	(facts)
	(halt)
)

(defrule vaciarJarra1
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra1 0))
	=>
	(assert (jarras (jarra1 0) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule vaciarJarra2
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra2 0))
	=>
	(assert (jarras (jarra1 ?jarra1) (jarra2 0) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule vaciarJarra3
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra3 0))
	=>
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 0) (jarra4 ?jarra4)))
)

(defrule vaciarJarra4
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra4 0))
	=>
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 0)))
)

(defrule llenarJarra1
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (< ?jarra1 24))
	=>
	(assert (jarras (jarra1 24) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule llenarJarra2
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (< ?jarra2 13))
	=>
	(assert (jarras (jarra1 ?jarra1) (jarra2 13) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule llenarJarra3
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (< ?jarra3 11))
	=>
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 11) (jarra4 ?jarra4)))
)

(defrule llenarJarra4
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (< ?jarra4 5))
	=>
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 5)))
)

(defrule moverDeJarra1aJarra2
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra1 0))
	(test (<= ?jarra2 13))
	=> 
	(bind ?diff (min (- 13 ?jarra2) ?jarra1))
	(bind ?jarra1 (- ?jarra1 ?diff))
	(bind ?jarra2 (+ ?jarra2 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra1aJarra3
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra1 0))
	(test (<= ?jarra3 11))
	=> 
	(bind ?diff (min (- 11 ?jarra3) ?jarra1))
	(bind ?jarra1 (- ?jarra1 ?diff))
	(bind ?jarra3 (+ ?jarra3 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra1aJarra4
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra1 0))
	(test (<= ?jarra4 5))
	=> 
	(bind ?diff (min (- 5 ?jarra4) ?jarra1))
	(bind ?jarra1 (- ?jarra1 ?diff))
	(bind ?jarra4 (+ ?jarra4 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra2aJarra1
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra2 0))
	(test (<= ?jarra1 24))
	=> 
	(bind ?diff (min (- 24 ?jarra1) ?jarra2))
	(bind ?jarra2 (- ?jarra2 ?diff))
	(bind ?jarra1 (+ ?jarra1 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra2aJarra3
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra2 0))
	(test (<= ?jarra3 11))
	=> 
	(bind ?diff (min (- 11 ?jarra3) ?jarra2))
	(bind ?jarra2 (- ?jarra2 ?diff))
	(bind ?jarra3 (+ ?jarra3 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra2aJarra4
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra2 0))
	(test (<= ?jarra4 5))
	=> 
	(bind ?diff (min (- 5 ?jarra4) ?jarra2))
	(bind ?jarra2 (- ?jarra2 ?diff))
	(bind ?jarra4 (+ ?jarra4 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra3aJarra1
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra3 0))
	(test (<= ?jarra1 24))
	=> 
	(bind ?diff (min (- 24 ?jarra1) ?jarra3))
	(bind ?jarra3 (- ?jarra3 ?diff))
	(bind ?jarra1 (+ ?jarra1 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra3aJarra2
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra3 0))
	(test (<= ?jarra2 13))
	=> 
	(bind ?diff (min (- 13 ?jarra2) ?jarra3))
	(bind ?jarra3 (- ?jarra3 ?diff))
	(bind ?jarra2 (+ ?jarra2 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra3aJarra4
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra3 0))
	(test (<= ?jarra4 5))
	=> 
	(bind ?diff (min (- 5 ?jarra4) ?jarra3))
	(bind ?jarra3 (- ?jarra3 ?diff))
	(bind ?jarra4 (+ ?jarra4 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra4aJarra1
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra4 0))
	(test (<= ?jarra1 24))
	=> 
	(bind ?diff (min (- 24 ?jarra1) ?jarra4))
	(bind ?jarra4 (- ?jarra4 ?diff))
	(bind ?jarra1 (+ ?jarra1 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra4aJarra2
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra4 0))
	(test (<= ?jarra2 13))
	=> 
	(bind ?diff (min (- 13 ?jarra2) ?jarra4))
	(bind ?jarra4 (- ?jarra4 ?diff))
	(bind ?jarra2 (+ ?jarra2 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarra4aJarra3
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarra4 0))
	(test (<= ?jarra3 11))
	=> 
	(bind ?diff (min (- 11 ?jarra3) ?jarra4))
	(bind ?jarra4 (- ?jarra4 ?diff))
	(bind ?jarra3 (+ ?jarra3 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)
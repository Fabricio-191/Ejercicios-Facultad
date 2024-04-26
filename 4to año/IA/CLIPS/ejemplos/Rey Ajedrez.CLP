;c:columna y f:fila
(deftemplate Rey
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8))
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8))
)

(deftemplate Pieza
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8))
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8))
)

(deftemplate Destino
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8))
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8))
)

;Solucion
(defrule Solucion
	(declare(salience 1000))
	(Rey(c ?xc)(f ?xf))
	(Destino(c ?xco)(f ?xfo))
	(test (= ?xc ?xco))
	(test (= ?xf ?xfo))
=>
	(printout t "Movimiento valido. El rey se desplazo a la posicion: " "(" ?xco "," ?xfo ")" crlf)
	(halt)
)

;Movimientos
(defrule Regla1
	(declare(salience 1000))
	(Destino(c ?xcd)(f ?xfd))
	(Pieza(c ?xcp)(f ?xfp))
	(test (= ?xcd ?xcp))
	(test (= ?xfd ?xfp))
=>
	(printout t "El destino y la posicion de la pieza es el mismo." crlf)
	(halt)
)


;Movimiento a la izquierda
(defrule Regla2
	(Destino(c ?xco)(f ?xfo))
	?Rey<- (Rey(c ?xc)(f ?xf))
	(test (> ?xc ?xco))
	(test (= ?xf ?xfo))	

=>
	(bind ?aux1(- ?xc 1))
	(modify ?Rey(c ?aux1)(f ?xf))
)


;Movimiento a la derecha
(defrule Regla3
	(Destino(c ?xco)(f ?xfo))
	?Rey <- (Rey(c ?xc)(f ?xf))
	(test (< ?xc ?xco))
	(test (= ?xf ?xfo))	

=>
	(bind ?aux1(+ ?xc 1))
	(modify ?Rey(c ?aux1)(f ?xf))
)


;Movimiento hacia arriba
(defrule Regla4
	(Destino(c ?xco)(f ?xfo))
	?Rey <- (Rey(c ?xc)(f ?xf))
	(test (= ?xc ?xco))
	(test (> ?xf ?xfo))	

=>
	(bind ?aux2(- ?xf 1))
	(modify ?Rey(c ?xc)(f ?aux2))
)


;Movimiento hacia abajo
(defrule Regla5
	(Destino(c ?xco)(f ?xfo))
	?Rey <- (Rey(c ?xc)(f ?xf))
	(test (= ?xc ?xco))
	(test (< ?xf ?xfo))	

=>
	(bind ?aux2(+ ?xf 1))
	(modify ?Rey(c ?xc)(f ?aux2))
)


;Movimiento diagonal hacia arriba a la izquierda
(defrule Regla6
	(Destino(c ?xco)(f ?xfo))
	?Rey <- (Rey(c ?xc)(f ?xf))
	(test (= ?xc (+ ?xco 1)))
	(test (= ?xf (+ ?xfo 1)))
=>
	(bind ?aux1(- ?xc 1))
	(bind ?aux2(- ?xf 1))
	(modify ?Rey(c ?aux1)(f ?aux2))
)


;Movimiento diagonal hacia arriba a la derecha
(defrule Regla7
	(Destino(c ?xco)(f ?xfo))
	?Rey <- (Rey(c ?xc)(f ?xf))
	(test (= ?xc (- ?xco 1)))
	(test (= ?xf (+ ?xfo 1)))
=>
	(bind ?aux1(+ ?xc 1))
	(bind ?aux2(- ?xf 1))
	(modify ?Rey(c ?aux1)(f ?aux2))
)


;Movimiento diagonal hacia abajo a la izquierda
(defrule Regla8
	(Destino(c ?xco)(f ?xfo))
	?Rey <- (Rey(c ?xc)(f ?xf))
	(test (= ?xc (+ ?xco 1)))
	(test (= ?xf (- ?xfo 1)))
=>
	(bind ?aux1(- ?xc 1))
	(bind ?aux2(+ ?xf 1))
	(modify ?Rey(c ?aux1)(f ?aux2))
)


;Movimiento diagonal hacia abajo a la derecha 
(defrule Regla9
	(Destino(c ?xco)(f ?xfo))
	?Rey <- (Rey(c ?xc)(f ?xf))
	(test (= ?xc (- ?xco 1)))
	(test (= ?xf (- ?xfo 1)))
=>
	(bind ?aux1(+ ?xc 1))
	(bind ?aux2(+ ?xf 1))
	(modify ?Rey(c ?aux1)(f ?aux2))
)


(defrule Regla10
	
=>
	(printout t "Posicion inicial del Rey: " crlf)
	(printout t "-Introducir columna: ")
	(bind ?xc(read))
	(printout t "-Introducir fila: ")
	(bind ?xf(read))
	(assert (Rey (c ?xc) (f ?xf)))

	(printout t "Posicion de la Pieza:" crlf)
	(printout t "-Introducir columna: ")
	(bind ?xcp(read))
	(printout t "-Introducir Fila: ")
	(bind ?xfp(read))
	(assert (Pieza (c ?xcp) (f ?xfp)))

	(printout t "Posicion de Destino del Rey:" crlf)	
	(printout t "-Introducir columna: ")
	(bind ?xco(read))
	(printout t "-Introducir fila: ")
	(bind ?xfo(read))
	(assert (Destino (c ?xco) (f ?xfo)))

	(if (or (or (> ?xfo (+ ?xf 1)) (< ?xfo (- ?xf 1)))
		(or (> ?xco (+ ?xc 1)) (< ?xco (- ?xc 1)))
	    )
		then
		(printout t "No se puede realizar en un solo movimiento." crlf)
		(halt)
	)
)
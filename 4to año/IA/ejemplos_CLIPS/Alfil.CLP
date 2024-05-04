(deftemplate Alfil
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;columna y sus valores permitidos
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;fila y sus valores permitidos
)

(deftemplate Pieza
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;columna para una pieza arbitraria
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;fila para una pieza arbitraria
)

(deftemplate Destino
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;columna destino del alfil
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;fila destino del alfil
)

(defrule Sol
	(declare(salience 1000))
	(Alfil(c ?xc)(f ?xf))
	(Destino(c ?xco)(f ?xfo))
	(test (= ?xc ?xco))
	(test (= ?xf ?xfo))
=>
	(printout t "Movimiento valido. El Alfil se desplazo a la posicion: " "(" ?xco "," ?xfo ")"crlf)
	(halt)
)

(defrule Regla2
	(declare(salience 1000))
	(Alfil(c ?xc)(f ?xf))
	(Pieza(c ?xcp)(f ?xfp))
	(test (= ?xc ?xcp))
	(test (= ?xf ?xfp))
=>
	(printout t "El Alfil no puede desplazarse hacia el destino por hay otra pieza en medio."crlf)
	(halt)
)

(defrule Regla3
	(declare(salience 1000))
	(Alfil(c ?xc)(f ?xf))
      (test (> ?xc 8))
	(test (> ?xf 8))
	(test (< ?xc 1))
	(test (< ?xf 1))
=>
	(printout t "Valor incorrecto. Ingrese valores entre 1 y 8."crlf)
	(halt)
)

(defrule Regla4
	(declare(salience 1000))
	(Destino(c ?xcp)(f ?xfp))
	(Pieza(c ?xcp)(f ?xfp))
	(test (= ?xcp ?xcp))
	(test (= ?xfp ?xfp))
=>
	(printout t "El destino y la posicion de la pieza es el mismo." crlf)
	(halt)
)

(defrule Regla5
	(declare(salience 10000))
	(Alfil(c ?xc)(f ?xf))
      	(Destino (c ?xco)(f ?xfo))
      	(test (!= (abs (- ?xc ?xco)) (abs (- ?xf ?xfo))))

=>
	(printout t "El movimiento no es valido."crlf)
	(halt)
)

(defrule Regla6
	(Destino(c ?xco)(f ?xfo))
	?Alfil <- (Alfil(c ?xc)(f ?xf))
	(test (> ?xc ?xco))
	(test (< ?xf ?xfo))	

=>
	(bind ?aux1(- ?xc 1))
	(bind ?aux2(+ ?xf 1))
	(modify ?Alfil(c ?aux1)(f ?aux2))
)

(defrule Regla7
	(Destino(c ?xco)(f ?xfo))
	?Alfil <- (Alfil(c ?xc)(f ?xf))
	(test (< ?xc ?xco))
	(test (< ?xf ?xfo))	

=>
	(bind ?aux1(+ ?xc 1))
	(bind ?aux2(+ ?xf 1))
	(modify ?Alfil(c ?aux1)(f ?aux2))
)

(defrule Regla8
	(Destino(c ?xco)(f ?xfo))
	?Alfil <- (Alfil(c ?xc)(f ?xf))
	(test (> ?xc ?xco))
	(test (> ?xf ?xfo))	

=>
	(bind ?aux1(- ?xc 1))
	(bind ?aux2(- ?xf 1))
	(modify ?Alfil(c ?aux1)(f ?aux2))
)


(defrule Regla9
	(Destino(c ?xco)(f ?xfo))
	?Alfil <- (Alfil(c ?xc)(f ?xf))
	(test (< ?xc ?xco))
	(test (> ?xf ?xfo))	

=>
	(bind ?aux1(+ ?xc 1))
	(bind ?aux2(- ?xf 1))
	(modify ?Alfil(c ?aux1)(f ?aux2))
)

(defrule Regla10
	
=>
	(printout t "Introduzca la posicion del Alfil: " crlf)
	(printout t "-Columna: ")
	(bind ?xc(read))
	(printout t "-Fila: ")
	(bind ?xf(read))
	(assert (Alfil (c ?xc) (f ?xf)))
	(printout t "Posicion de Pieza:" crlf)
	(printout t "Introduzca la columna: ")
	(bind ?xcp(read))
	(printout t "-Fila: ")
	(bind ?xfp(read))
	(assert (Pieza (c ?xcp) (f ?xfp)))
	(printout t "Destino:" crlf)	
	(printout t "-Columna: ")
	(bind ?xco(read))
	(printout t "-Fila: ")
	(bind ?xfo(read))
	(assert (Destino (c ?xco) (f ?xfo)))

)
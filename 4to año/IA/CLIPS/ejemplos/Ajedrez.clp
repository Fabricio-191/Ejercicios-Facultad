(deftemplate torre
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;fila y sus valores permitidos
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;columna y sus valores permitidos
)

(deftemplate pieza
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;fila y sus valores permitidos
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;columna y sus valores permitidos
)

(deftemplate destino
	(slot f (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;fila y sus valores permitidos
	(slot c (type INTEGER)(allowed-values 1 2 3 4 5 6 7 8));;;columna y sus valores permitidos
)

(defrule cargar
	
=>
	(printout t "Introduzca la posicion de la Torre: " crlf)
	(printout t "-Fila: ")
	(bind ?xf(read))
	(printout t "-Columna: ")
	(bind ?xc(read))
	(assert (torre (f ?xf) (c ?xc)))
	
	(printout t "Posicion de la Pieza:" crlf)
	(printout t "-Fila: ")
	(bind ?xfp(read))
	(printout t "Introduzca la columna: ")
	(bind ?xcp(read))
	(assert (pieza (f ?xfp) (c ?xcp)))
	
	(printout t "Destino:" crlf)
	(printout t "-Fila: ")
	(bind ?xfo(read))	
	(printout t "-Columna: ")
	(bind ?xco(read))
	
	(assert (destino (f ?xfo) (c ?xco)))
	
	(if (and (neq ?xfo ?xf) (neq ?xco ?xc))
		then
		(printout t "No se puede realizar en un solo movimiento." crlf)
		(halt)
	)
)



(defrule solucion
	(declare(salience 1000))
	(torre(f ?xf)(c ?xc))
	(destino(f ?xfo)(c ?xco))
	(test (= ?xc ?xco))
	(test (= ?xf ?xfo))
=>
	(printout t "Movimiento valido. La torre se desplazo a la posicion: " "(" ?xfo "," ?xco ")"crlf)
	(halt)
)

(defrule destinoOcupado
	(declare(salience 1000))
	(torre(f ?xf)(c ?xc))
	(pieza(f ?xfp)(c ?xcp))
	(test (= ?xc ?xcp))
	(test (= ?xf ?xfp))
=>
	(printout t "La torre no puede desplazarse hacia el destino ya que existe otra pieza en medio."crlf)
	(halt)
)

(defrule destinoYaUsado
	(declare(salience 1000))
	(destino(c ?xcp)(f ?xfp))
	(pieza(c ?xcp)(f ?xfp))
	(test (= ?xcp ?xcp))
	(test (= ?xfp ?xfp))
=>
	(printout t "En el destino ya existe una pieza colocada." crlf)
	(halt)
)

(defrule abajo
	(destino (f ?xfd) (c ?))
	?torre <-(torre (f ?xft) (c ?))
	(test (< ?xfd ?xft))
	=>
	(bind ?aux (- ?xft 1))
	(modify ?torre (f ?aux))
	(printout t "La torre se desplazó hacia abajo" crlf)
)

(defrule arriba
	(destino (f ?xfd) (c ?))
	?torre <-(torre (f ?xft) (c ?))
	(test (> ?xfd ?xft))
	=>
	(bind ?aux (+ ?xft 1))
	(modify ?torre (f ?aux))
	(printout t "La torre se desplazó hacia arriba" crlf)
)

(defrule izquierda
	(destino (f ?) (c ?xcd))
	?torre <-(torre (f ?) (c ?xct))
	(test (< ?xcd ?xct))
	=>
	(bind ?aux (- ?xct 1))
	(modify ?torre (c ?aux))
	(printout t "La torre se desplazó hacia la izquierda" crlf)
)

(defrule derecha
	(destino (f ?) (c ?xcd))
	?torre <-(torre (f ?) (c ?xct))
	(test (> ?xcd ?xct))
	=>
	(bind ?aux (+ ?xct 1))
	(modify ?torre (c ?aux))
	(printout t "La torre se desplazó hacia la derecha" crlf)
)

	
	


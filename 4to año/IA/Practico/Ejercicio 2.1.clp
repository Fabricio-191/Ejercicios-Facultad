(defrule inicio
	=> 
	(assert (numero 1))
	(assert (numero 2))
	(assert (numero 3))
	(assert (numero 4))
	(assert (contenido 24 0 0 0))
)

(defglobal ?*capacidades* = (create$ 24 13 11 5))

(defrule estadoFinal
	(declare (salience 1000))
	(contenido 8 8 8 0)
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule moverDeJarraEnJarra
	(declare (salience 10))
	(numero ?jarraOrigen)
	(numero ?jarraDestino)
	(test (neq ?jarraOrigen ?jarraDestino))
	(contenido $?contenidos)
	=>
	(bind ?contenidoOrigen (nth$ ?jarraOrigen ?contenidos))
	(bind ?capacidadDestino (nth$ ?jarraDestino ?*capacidades*))
	(bind ?contenidoDestino (nth$ ?jarraDestino ?contenidos))
	(bind ?litros (min ?contenidoOrigen (- ?capacidadDestino ?contenidoDestino)))
	(bind ?nuevoContenidoOrigen (- ?contenidoOrigen ?litros))
	(bind ?nuevoContenidoDestino (+ ?contenidoDestino ?litros))
	(bind ?contenidos (replace$ ?contenidos ?jarraOrigen  ?jarraOrigen  ?nuevoContenidoOrigen))
	(bind ?contenidos (replace$ ?contenidos ?jarraDestino ?jarraDestino ?nuevoContenidoDestino))
	(assert (contenido $?contenidos))
)
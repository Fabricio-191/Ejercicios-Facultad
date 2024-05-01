(deffacts jarras
	(contenido 24 0 0 0)
	(numero 1)
	(numero 2)
	(numero 3)
	(numero 4)
)

(defglobal ?*capacidades* = (create$ 24 13 11 8))

(defrule estadoFinal
	(declare (salience 1000))
	(contenido 8 8 8 0)
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule moverDeJarraEnJarra
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


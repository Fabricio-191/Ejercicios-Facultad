(deftemplate jarras
	(multislot contenido (type INTEGER) (range 0 24) (default 0) (cardinality 4))
	(multislot capacidad (type INTEGER) (cardinality 4))
)

(deftemplate
	(slot numero (type INTEGER) (range 1 4))
)

(deffacts jarras
	(numero 1)
	(numero 2)
	(numero 3)
	(numero 4)
)

(deffacts inicio
	(jarras (contenido 0 0 0 0) (capacidad 24 13 11 8))
)

/*
(defrule moverDeJarraaJarra
	(jarras (contenido ?c1 ?c2 ?c3 ?c4) (capacidad ?cap1 ?cap2 ?cap3 ?cap4))
	=>
	(bind ?jarraOrigen (read))
	(bind ?jarraDestino (read))
	(bind ?capacidadOrigen (nth$ ?jarraOrigen ?cap1 ?cap2 ?cap3 ?cap4))
	(bind ?contenidoOrigen (nth$ ?jarraOrigen ?c1 ?c2 ?c3 ?c4))
	(bind ?capacidadDestino (nth$ ?jarraDestino ?cap1 ?cap2 ?cap3 ?cap4))
	(bind ?contenidoDestino (nth$ ?jarraDestino ?c1 ?c2 ?c3 ?c4))
	(bind ?litros (min ?contenidoOrigen (- ?capacidadDestino ?contenidoDestino))
	(bind ?nuevoContenidoOrigen (- ?contenidoOrigen ?litros))
	(bind ?nuevoContenidoDestino (+ ?contenidoDestino ?litros))
	(assert (jarras (contenido ?nuevoContenidoOrigen ?nuevoContenidoDestino ?c3 ?c4) (capacidad ?cap1 ?cap2 ?cap3 ?cap4)))
)
*/

(defrule moverDeJarraEnJarra
	(jarras (contenido ?c1 ?c2 ?c3 ?c4) (capacidad ?cap1 ?cap2 ?cap3 ?cap4))
	(numero ?jarraOrigen)
	(numero ?jarraDestino)
	(test (neq ?jarraOrigen ?jarraDestino))
	(test (<= ?c? ?cap?))
	=>
	(bind ?capacidadOrigen (nth$ ?jarraOrigen ?cap1 ?cap2 ?cap3 ?cap4))
	(bind ?contenidoOrigen (nth$ ?jarraOrigen ?c1 ?c2 ?c3 ?c4))
	(bind ?capacidadDestino (nth$ ?jarraDestino ?cap1 ?cap2 ?cap3 ?cap4))
	(bind ?contenidoDestino (nth$ ?jarraDestino ?c1 ?c2 ?c3 ?c4))
	(bind ?litros (min ?contenidoOrigen (- ?capacidadDestino ?contenidoDestino)))
	(bind ?nuevoContenidoOrigen (- ?contenidoOrigen ?litros))
	(bind ?nuevoContenidoDestino (+ ?contenidoDestino ?litros))
	(assert (jarras (contenido ?nuevoContenidoOrigen ?nuevoContenidoDestino ?c3 ?c4) (capacidad ?cap1 ?cap2 ?cap3 ?cap4)))
)

(deffacts inicio
	(capacidad 24 13 11 8)
	(jarras 0 0 0 0)
	(numero 1)
	(numero 2)
	(numero 3)
	(numero 4)
)
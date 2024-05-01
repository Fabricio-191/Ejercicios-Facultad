(deffacts jarras
	(capacidad 24 13 11 8)
	(contenido 24 0 0 0)
	(numero 1)
	(numero 2)
	(numero 3)
	(numero 4)
)

(defglobal MAIN ?*capacidades* = (create$ 24 13 11 8))

(defrule MAIN::estadoFinal
	(declare (salience 1000))
	(contenido 8 8 8 0)
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule MAIN::moverDeJarraEnJarra
	(numero ?jarraOrigen)
	(numero ?jarraDestino)
	(test (neq ?jarraOrigen ?jarraDestino))
	(contenido $?contenidos)
	=>
	(bind ?contenidoOrigen (nth$ ?jarraOrigen ?contenidos))
	(bind ?capacidadDestino (nth$ ?jarraDestino ?capacidades))
	(bind ?contenidoDestino (nth$ ?jarraDestino ?contenidos))
	(bind ?litros (min ?contenidoOrigen (- ?capacidadDestino ?contenidoDestino)))
	(bind ?nuevoContenidoOrigen (- ?contenidoOrigen ?litros))
	(bind ?nuevoContenidoDestino (+ ?contenidoDestino ?litros))
	(bind ?contenidos (replace$ ?contenidos ?jarraOrigen  ?jarraOrigen  ?nuevoContenidoOrigen))
	(bind ?contenidos (replace$ ?contenidos ?jarraDestino ?jarraDestino ?nuevoContenidoDestino))
	(assert (contenido $?contenidos))
)

;	(defrule llenarJarra
;		(numero ?jarra)
;		(contenido ?c1 ?c2 ?c3 ?c4)
;		(capacidad ?cap1 ?cap2 ?cap3 ?cap4)
;		=>
;		(bind ?nuevoContenido (nth$ ?jarra (create$ ?cap1 ?cap2 ?cap3 ?c4)))
;		(assert (contenido
;			(if (eq ?jarra 1) then ?nuevoContenido else ?c1)
;			(if (eq ?jarra 2) then ?nuevoContenido else ?c2)
;			(if (eq ?jarra 3) then ?nuevoContenido else ?c3)
;			(if (eq ?jarra 4) then ?nuevoContenido else ?c4)
;		))
;	
;	)
;	
;	(defrule vaciarJarra
;		(numero ?jarra)
;		(contenido ?c1 ?c2 ?c3 ?c4)
;		=>
;		(assert (contenido
;			(if (eq ?jarra 1) then 0 else ?c1)
;			(if (eq ?jarra 2) then 0 else ?c2)
;			(if (eq ?jarra 3) then 0 else ?c3)
;			(if (eq ?jarra 4) then 0 else ?c4)
;		))
;	)
(deffacts jarras
	(contenido 24 0 0 0)
	(numero 1)
	(numero 2)
	(numero 3)
	(numero 4)
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

; (defrule vaciarJarra
; 	(numero ?jarra)
; 	(contenido $?contenidos)
; 	(test (< 0 (nth$ ?jarra ?contenidos)))
; 	=>
; 	(bind ?contenidos (replace$ ?contenidos ?jarra ?jarra 0))
; 	(assert (contenido $?contenidos))
; )
; 
; (defrule llenarJarra
; 	(numero ?jarra)
; 	(contenido $?contenidos)
; 	(test (< (nth$ ?jarra ?contenidos) (nth$ ?jarra ?*capacidades*)))
; 	=>
; 	(bind ?capacidad (nth$ ?jarra ?*capacidades*))
; 	(bind ?contenidos (replace$ ?contenidos ?jarra ?jarra ?capacidad))
; 	(assert (contenido $?contenidos))
; )

; con reglas de llenar y vaciar
; ==> Activation 1000   estadoFinal: f-1345
; FIRE 11354 estadoFinal: f-1345

; sin reglas de llenar y vaciar
; ==> Activation 1000   estadoFinal: f-156
; FIRE 1106 estadoFinal: f-156
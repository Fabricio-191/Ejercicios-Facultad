; Define la plantilla para la jarra
(deftemplate jarra
  (slot litros
    (type INTEGER)
    (default 0))
  (slot capacidad
    (type INTEGER))
)

; Inicializa la base de hechos
; (defrule estado-inicial
;  =>
;  (assert (jarra (capacidad 3)))
;  (assert (jarra (capacidad 4))))

(deffacts estado_inicial_jarras
  (jarra (capacidad 3))
  (jarra (capacidad 4))
)

; Llena jarra1
(defrule llena-jarra1
  ?jarra <- (jarra (capacidad ?capacidad) (litros ?litros))
  (test (< ?litros ?capacidad))
  =>
  (modify ?jarra (litros 3)))
; Llena jarra2
(defrule llena-jarra2
  ?jarra <- (jarra (capacidad ?capacidad) (litros ?litros))
  (test (< ?litros 4))
  =>
  (modify ?jarra (litros ?capacidad)))

; Vacía jarra
(defrule vaciar-jarra
  ?jarra <- (jarra (litros ?litros))
  (test (> ?litros 0))
  =>
  (modify ?jarra (litros 0)))

; Vuelca el contenido de una jarra en la otra: jarra1 -> jarra2
(defrule volcar-jarra
  ?jarra1 <- (jarra (litros ?litros1) (capacidad ?capacidad1))
  ?jarra2 <- (jarra (litros ?litros2) (capacidad ?capacidad2))
  (test (neq ?jarra1 ?jarra2))
  (test (<= (+ ?litros1 ?litros2) ?capacidad2))
  =>
  (modify ?jarra1 (litros 0))
  (modify ?jarra2 (litros (+ ?litros1 ?litros2)))
)

; Vuelca todo lo que quepa de una jarra en la otra: jarra1 -> jarra2
(defrule verter-jarra
  ?jarra1 <- (jarra (litros ?litros1) (capacidad ?capacidad1))
  ?jarra2 <- (jarra (litros ?litros2) (capacidad ?capacidad2))
  (test (neq ?jarra1 ?jarra2))
  (test (> (+ ?litros1 ?litros2) ?capacidad2))
  =>
  (modify ?jarra1 (litros (- ?litros1 (- ?capacidad2 ?litros2))))
  (modify ?jarra2 (litros ?capacidad2))
)

  
; Comprueba terminacion
(defrule acabar
  (declare (salience 1000))
  ?jarra <- (jarra (capacidad 4) (litros 2))
  =>
  (printout t "Lo he conseguido" crlf)
  (halt)
)
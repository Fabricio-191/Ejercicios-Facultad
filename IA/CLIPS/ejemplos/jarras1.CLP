;Plantilla para representar las jarras
(deftemplate jarra
  (slot contenido (type INTEGER) (default ?NONE))
  (slot capacidad (type INTEGER) (default ?DERIVE)) 
)

(deftemplate estado
  (slot x (type INTEGER) (default 0))
  (slot y (type INTEGER) (default 0))
)

;Reglas a aplicar
(defrule R1 "Llenar jarra J1"
  	?jarra <- (jarra (contenido ?x) (capacidad 4))
        (jarra (contenido ?y) (capacidad 3))
        (not (estado (x 4) (y ?y)))
	(test (< ?x 4))
      =>
	(modify ?jarra (contenido 4))
        (assert (estado (x 4) (y ?y)))
)

(defrule R2 "Llenar jarra J2"
 	?jarra <- (jarra (contenido ?y) (capacidad 3))
        (jarra (contenido ?x) (capacidad 4))
        (not (estado (x ?x) (y 3)))
	(test (< ?y 3))
      =>
	(modify ?jarra (contenido 3))
        (assert (estado (x ?x) (y 3)))
)

(defrule R3 "Vaciar Jarra J1"
   ?jarra <- (jarra (contenido ?x) (capacidad 4))
  (jarra (contenido ?y) (capacidad  3))
  (not (estado (x 0) (y ?y))) 
  (test (> ?x 0))
   =>
  (modify ?jarra (contenido 0))
  (assert (estado (x 0) (y ?y)))
)

(defrule R4 "Vaciar Jarra J2"
   ?jarra <- (jarra (contenido ?y) (capacidad 3))
  (jarra (contenido ?x) (capacidad 4))
  (not (estado (x ?x) (y 0)))
  (test (> ?y 0))
=>
  (modify ?jarra (contenido 0))
  (assert (estado (x ?x) (y 0)))
)

(defrule R5 "Volcar el contenido de J1 en J2"
  ?jarra1 <- (jarra (capacidad 4) (contenido ?x))
  ?jarra2 <- (jarra (capacidad 3) (contenido ?y))
  (test (<= (+ ?x ?y) 3))
  (test (> ?x 0))
  (not (estado (x 0) (y =(+ ?x ?y))))
=>
  (bind ?z (+ ?x ?y))
  (modify ?jarra1 (contenido 0))
  (modify ?jarra2 (contenido ?z))
  (assert (estado (x 0) (y ?z)))
)

(defrule R6 "Volcar el contenido de J2 en J1"
  ?jarra1 <- (jarra (capacidad 4) (contenido ?x))
  ?jarra2 <- (jarra (capacidad 3) (contenido ?y))
  (test (<= (+ ?x ?y) 4))
  (test (> ?y 0))
  (not (estado (y 0) (x =(+ ?x ?y))))
=>
  (bind ?z (+ ?x ?y))
  (modify ?jarra1 (contenido ?z))
  (modify ?jarra2 (contenido 0))
  (assert (estado (x ?z) (y 0)))
)

(defrule R7 "Volcar el contenido de J1 en J2 hasta llenar J2"
 (declare (salience -1000))
  ?jarra1 <- (jarra (capacidad 4) (contenido ?x))
  ?jarra2 <- (jarra (capacidad 3) (contenido ?y))
  (test (> (+ ?x ?y) 3))
  (test (> ?x 0))
 
=>
  (bind ?z (+ ?x ?y))
  (bind ?w (- ?z 3))
  
  (modify ?jarra1 (contenido ?w))
  (modify ?jarra2 (contenido 3))
  (assert (estado (x ?w) (y 3)))
)

(defrule R8 "Volcar el contenido de J2 en J1 hasta llenar J1"
;(declare (salience -10000))
  ?jarra1 <- (jarra (capacidad 4) (contenido ?x))
  ?jarra2 <- (jarra (capacidad 3) (contenido ?y))
  (test (> (+ ?x ?y) 4))
  (test (> ?y 0))
 =>
  (bind ?z (+ ?x ?y))
  (bind ?w (- ?z 4))
  (modify ?jarra1 (contenido 4))
  (modify ?jarra2 (contenido ?w))
  (assert (estado (x 4) (y ?w)))
 )

  
; Comprueba terminacion
(defrule acabar
   (declare (salience 10000))
   ?jarra <- (jarra (capacidad 4) (contenido ?x))
   (jarra (capacidad 3) (contenido ?y))
   (test (= ?x 2))
  
  =>
  (printout t "Lo he conseguido" crlf)
  (printout t "jarra 1 con capacidad 4   contenido " ?x  "  jarra 2  con capacidad 3  contenido "?y crlf)
  (halt)
)


;Hechos iniciales
(deffacts hecho-inicial
  (jarra (contenido 0) (capacidad 4))
  (jarra (contenido 0) (capacidad 3))
  (estado (x 0) (y 0)) 
)

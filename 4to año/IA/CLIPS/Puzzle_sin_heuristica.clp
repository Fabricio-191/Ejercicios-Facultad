(deftemplate MAIN::nodo 
   (multislot estado) 
)

(defglobal MAIN 
   ?*estado-inicial* = (create$ 1 2 3 4 5 6 7 8 H ) 
   ?*estado-final* = (create$ 4 H 2 3 5 7 8 1 6  )
)

;Estado inicial
(defrule MAIN::inicial 
   => 
   (assert (nodo (estado ?*estado-inicial*)))
)


;Movimientos del espacio blanco
(defrule MAIN::arriba 
   (nodo (estado $?a ?b ?c ?d H $?e)) 
   (not (nodo (estado $?a H ?c ?d ?b $?e)))
=> 
   (bind $?nuevo-estado (create$  $?a H ?c ?d ?b $?e)) 
   (assert (nodo (estado $?nuevo-estado)))
)


(defrule MAIN::abajo 
   (nodo (estado $?a H ?b ?c ?d  $?e)) 
	(not (nodo (estado $?a ?d ?b ?c H $?e)))
=> 
   (bind $?nuevo-estado (create$ $?a ?d ?b ?c H $?e)) 
   (assert (nodo (estado $?nuevo-estado)))
)


(defrule MAIN::derecha 
   (nodo (estado $?a H ?b $?c&:(neq (mod (length $?c) 3) 2))) 
   (not (nodo (estado $?a ?b H $?c)))
 => 
   (bind $?nuevo-estado (create$ $?a ?b H $?c)) 
   (assert (nodo (estado $?nuevo-estado)))
)

(defrule MAIN::izquierda 
   (nodo (estado $?a&:(neq (mod (length $?a) 3) 2) ?b H $?c)) 
   (not (nodo (estado $?a H ?b $?c)))
=> 
   (bind $?nuevo-estado (create$ $?a H ?b $?c)) 
   (assert (nodo (estado $?nuevo-estado)))
)

;Solución (se encuentra al tener la heur�stica con valor 0)
(defrule MAIN::encuentra-solucion 
	(declare (salience 100))
	(nodo (estado 4 H 2 3 5 7 8 1 6))
	=> 
	(printout t "Solucion: 4 H 2 3 5 7 8 1 6" crlf)
	(halt) 
)
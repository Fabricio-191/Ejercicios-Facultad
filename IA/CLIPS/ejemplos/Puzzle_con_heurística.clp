(deftemplate MAIN::nodo 
   (multislot estado) 
   (multislot camino) 
   (slot heuristica) 
   (slot clase (default abierto)))

(defglobal MAIN 
   ?*estado-inicial* = (create$ 1 2 3 4 5 6 7 8 H ) 
   ?*estado-final* = (create$ 4 H 2 3 5 7 8 1 6  )
)

;Heur√stica
(deffunction MAIN::heuristica ($?estado) 
   (bind ?res 0) 
   (loop-for-count (?i 1 9) 
    (if (neq (nth ?i $?estado) (nth ?i ?*estado-final*)) 
         then (bind ?res (+ ?res 1)) 
     ) 
    ) 
   ?res)


;Estado inicial
(defrule MAIN::inicial 
   => 
   (assert (nodo (estado ?*estado-inicial*) 
                  (camino) 
                  (heuristica (heuristica ?*estado-inicial*)) 
                  (clase cerrado)))
)


;Movimientos del espacio blanco
(defrule MAIN::arriba 
   (nodo (estado $?a ?b ?c ?d H $?e) 
          (camino $?movimientos) 
          (clase cerrado)) 
=> 
   (bind $?nuevo-estado (create$  $?a H ?c ?d ?b $?e)) 
   (assert (nodo (estado $?nuevo-estado) 
                 (camino $?movimientos) 
                 (heuristica (heuristica $?nuevo-estado))))
)


(defrule MAIN::abajo 
   (nodo (estado $?a H ?b ?c ?d  $?e) 
          (camino $?movimientos) 
          (clase cerrado)) 
=> 
   (bind $?nuevo-estado (create$ $?a ?d ?b ?c H $?e)) 
   (assert (nodo (estado $?nuevo-estado) 
                 (camino $?movimientos) 
                 (heuristica (heuristica $?nuevo-estado))))
)


(defrule MAIN::derecha 
   (nodo (estado $?a H ?b 
                 $?c&:(neq (mod (length $?c) 3) 2)) 
          (camino $?movimientos) 
          (clase cerrado)) 
 => 
   (bind $?nuevo-estado (create$ $?a ?b H $?c)) 
   (assert (nodo (estado $?nuevo-estado) 
                 (camino $?movimientos) 
                 (heuristica (heuristica $?nuevo-estado))))
)


(defrule MAIN::izquierda 
   (nodo (estado $?a&:(neq (mod (length $?a) 3) 2) 
                   ?b H $?c) 
          (camino $?movimientos) 
          (clase cerrado)) 
=> 
   (bind $?nuevo-estado (create$ $?a H ?b $?c)) 
   (assert (nodo (estado $?nuevo-estado) 
                 (camino $?movimientos) 
                 (heuristica (heuristica $?nuevo-estado))))
)


(defrule MAIN::pasa-el-mejor-a-cerrado 
   (declare (salience -10)) 
   ?nodo <- (nodo (clase abierto) 
                  (heuristica ?h1)) 
   (not (nodo (clase abierto) 
              (heuristica ?h2&:(< ?h2 ?h1)))) 
=> 
   (modify ?nodo (clase cerrado))
)


;Restricciones 
(defrule MAIN::repeticiones-de-nodo 
   (declare (auto-focus TRUE)) 
   (nodo (estado $?actual) 
         (camino $?movimientos-1)) 
   ?nodo <- (nodo (estado $?actual) 
                  (camino $?movimientos-1 ? $?)) 
 => 
   (retract ?nodo)
)


;Soluci√≥n (se encuentra al tener la heur√stica con valor 0)
(defrule MAIN::encuentra-solucion 
   (declare (auto-focus TRUE)) 
   ?nodo <- (nodo (heuristica 0) 
               (camino $?movimientos)) 
 => 
   (retract ?nodo) 
   (assert (solucion $?movimientos))
)


(defrule MAIN::escribe-solucion 
   (solucion $?estado) 
  => 
   (printout t "Solucion: 4 H 2 3 5 7 8 1 6" crlf)
 (halt) 
) 

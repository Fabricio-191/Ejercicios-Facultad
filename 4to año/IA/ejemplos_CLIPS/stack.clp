
; The following examples of CLIPS code are
; from Expert Systems by J.Giarratano and G.Riley

; Stack implementation in CLIPS (p.380)

(defrule push-value 
  ?push-value <- (push-value ?value)
  ?stack <- (stack $?rest)
 => 
  (retract ?push-value ?stack)
  (assert (stack ?value $?rest))
  (printout t "Pushing value " ?value crlf)
) 

(defrule pop-value-valid 
  ?pop-val <- (pop-value) ; this is correct! 
  ?stack <- (stack ?value $?rest) 
  => 
  (retract ?pop-val ?stack) 
                  (assert (stack $?rest)) 
                  (printout t "Popping value " ?value crlf)) 
                

              (defrule pop-value-invalid 
                  ?pop-val <- (pop-value) 
                  (stack) 
               => 
                  (retract ?pop-val) 
                  (printout t "Popping from empty stack " crlf)) 

; EOF











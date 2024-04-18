
(defrule definicion_de_hechos_iniciales
  =>
  (printout t "!==============! Inicio de la ejecución !=============!" t crlf)
  (assert (numero_valido 0))
  (assert (numero_valido 2))
  (assert (numero_valido 3))
  (assert (numero_valido 4))
  (assert (numero_valido 5))
  (assert (numero_valido 6))
  (assert (numero_valido 7))
  (assert (numero_valido 8))
  (assert (numero_valido 9))
  (assert (letra A))
  (assert (letra U))
  (assert (letra B))
  (assert (letra M))
  (assert (letra N))
  (assert (letra P))
  (assert (letra R))
  (assert (combinacion S 1))
)

(defrule combinaciones_posibles
  (numero_valido ?a)
  (letra ?b)
  =>
  (assert (combinacion ?b ?a)))



(defrule funcion_objetivo
  (combinacion A ?a&~1)
  (combinacion U ?u&~?a&~1)
  (test (= (mod (+ ?a ?u) 10) 1))
  (combinacion B ?b&~?u&~?a&~1)
  (combinacion N ?n&~?b&~?u&~?a&~1)
  (combinacion R ?r&~?n&~?b&~?u&~?a&~1)
  (test (= (mod (+ ?u ?a
		            (* 10 ?b) (* 10 ?n))
		            100
            )
           (+ (* 10 ?r) 1))
  )
  (test (= (mod (+ ?u ?a
                   (* 10 ?b) (* 10 ?n) 
                   (* 100 ?n) (* 100 ?a)
                   )
                1000)
           (+ (* 100 ?u) (* 10 ?r) 1)))
  (combinacion M ?m&~?r&~?n&~?b&~?u&~?a&~1)
  (combinacion P ?p&~?m&~?r&~?n&~?b&~?u&~?a&~1)
  (test (=  (+ ?u ?a
                   (* 10 ?b) (* 10 ?n)
                   (* 100 ?n) (* 100 ?a)
                   (* 1000 ?m))
           (+ 10000  (* 1000 ?p) (* 100 ?u) (* 10 ?r) 1))
  )
  
  =>
  (printout t t t "Una solucion posible es:" t crlf)
  (printout t "A = " ?a ", ")
  (printout t "B = " ?b ", ")
  (printout t "M = " ?m ", ")
  (printout t "N = " ?n ", ")
  (printout t "P = " ?p ", ")
  (printout t "R = " ?r ", ")
  (printout t "S = 1, ")
  (printout t "U = " ?u ", ")
  (printout t crlf)
  (printout t "***********************" crlf)
  (printout t "*    " ?n ?b ?a"              *"   crlf)
  (printout t "* +                   *" crlf)
  (printout t "*   " ?m ?a ?n ?u "              *" crlf) 
  (printout t "* ______________      *" crlf)
  (printout t "*  1"?p ?u ?r "1              *" crlf)
  (printout t "***********************" crlf)) 

 

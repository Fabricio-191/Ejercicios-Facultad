(defrule startup
  =>
  (printout t crlf "The problem is" crlf crlf)
  (printout t "    CROSS" crlf)
  (printout t " +  ROADS" crlf)
  (printout t "   ------" crlf)
  (printout t " = DANGER" crlf crlf)
  (assert (number 0)
          (number 1)
          (number 2)
          (number 3)
          (number 4)
          (number 5)
          (number 6)
          (number 7)
          (number 8)
          (number 9)
          (letter C)
          (letter R)
          (letter O)
          (letter S)
          (letter A)
          (letter D)
          (letter N)
          (letter G)
          (letter E)))
          

(defrule generate-combinations
  (number ?x)
  (letter ?a)
  =>
  (assert (combination ?a ?x)))

(defrule find-solution
  (combination S ?s)
  (combination R ?r&~?s)
  (test (= (mod (+ ?s ?s) 10) ?r))

  
  (combination D ?d&~?r&~?s)
  (combination E ?e&~?d&~?r&~?s)
  (test (= (mod (+ ?s ?s
                   (* 10 ?s) (* 10 ?d))
                100)
           (+ (* 10 ?e) ?r)))

  (combination O ?o&~?e&~?d&~?r&~?s)
  (combination A ?a&~?o&~?e&~?d&~?r&~?s)
  (combination G ?g&~?a&~?o&~?e&~?d&~?r&~?s)
  (test (= (mod (+ ?s ?s
                   (* 10 ?s) (* 10 ?d)
                   (* 100 ?o) (* 100 ?a))
                1000)
           (+ (* 100 ?g) (* 10 ?e) ?r)))

  (combination N ?n&~?g&~?a&~?o&~?e&~?d&~?r&~?s)
  
  (test (= (mod (+ ?s ?s
                   (* 10 ?s) (* 10 ?d)
                   (* 100 ?o) (* 100 ?a)
                   (* 1000 ?r) (* 1000 ?o))
                10000)
           (+ (* 1000 ?n) (* 100 ?g) (* 10 ?e) ?r)))

  (combination C ?c&~?n&~?g&~?a&~?o&~?e&~?d&~?r&~?s)

  (test (= (mod(+ ?s ?s
              (* 10 ?s) (* 10 ?d)
              (* 100 ?o) (* 100 ?a)
              (* 1000 ?r) (* 1000 ?o)
              (* 10000 ?c) (* 10000 ?r))
                100000)
              
           (+ (* 10000 ?a) (* 1000 ?n) (* 100 ?g) (* 10 ?e) ?r)))

(test (= (+ ?s ?s
              (* 10 ?s) (* 10 ?d)
              (* 100 ?o) (* 100 ?a)
              (* 1000 ?r) (* 1000 ?o)
              (* 10000 ?c) (* 10000 ?r))
                
              
           (+ (* 100000 ?d)(* 10000 ?a) (* 1000 ?n) (* 100 ?g) (* 10 ?e) ?r)))




  =>
  (printout t "A Solution is:" crlf crlf)
  (printout t "  C = " ?c crlf)
  (printout t "  R = " ?r crlf)
  (printout t "  O = " ?o crlf)
  (printout t "  S = " ?s crlf)
  (printout t "  A = " ?a crlf)
  (printout t "  D = " ?d crlf)
  (printout t "  N = " ?n crlf)
  (printout t "  G = " ?g crlf)
  (printout t "  E = " ?e crlf)

  (printout t crlf)
  (printout t "   " 	?c ?r ?o ?s ?s crlf)
  (printout t " + " 	?r ?o ?a ?d ?s crlf) 
  (printout t "   " "------" crlf)
  (printout t " = " ?d ?a ?n ?g ?e ?r crlf crlf))  
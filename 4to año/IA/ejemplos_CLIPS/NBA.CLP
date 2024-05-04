(defrule startup
  =>
  (printout t crlf "The problem is" crlf crlf)
  (printout t "    	NBA" crlf)
  (printout t " +      MANU" crlf)
  (printout t "       ------" crlf)
  (printout t " =     SPURS" crlf crlf)
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
          (letter N)
          (letter B)
          (letter A)
          (letter S)
          (letter P)
          (letter U)
          (letter R)
          (letter M)))

          

(defrule generate-combinations
  (number ?x)
  (letter ?a)
  =>
  (assert (combination ?a ?x)))

(defrule find-solution
  (combination A ?a)
  (combination U ?u&~?a)
  (combination S ?s&~?u&~?a)
  (test (= (mod (+ ?a ?u) 10) ?s))

  
  (combination B ?b&~?s&~?u&~?a)
  (combination N ?n&~?b&~?s&~?u&~?a)
  (combination R ?r&~?n&~?b&~?s&~?u&~?a)
  (test (= (mod (+ ?a ?u
                   (* 10 ?b) (* 10 ?n))
                100)
           (+ (* 10 ?r) ?s)))

  (test (= (mod (+ ?a ?u
                   (* 10 ?b) (* 10 ?n)
                   (* 100 ?n) (* 100 ?a))
                1000)
           (+ (* 100 ?u) (* 10 ?r) ?s)))

      	(combination M ?m&~?r&~?n&~?b&~?s&~?u&~?a)  
  	(combination P ?p&~?m&~?r&~?n&~?b&~?s&~?u&~?a)  
  (test (= (mod (+ ?a ?u
                   (* 10 ?b) (* 10 ?n)
                   (* 100 ?n) (* 100 ?a)
                   (* 1000 ?m))
 		   10000)
           (+ (* 1000 ?p) (* 100 ?u) (* 10 ?r) ?s)))

    

(test (= (+ ?a ?u
              (* 10 ?b) (* 10 ?n)
              (* 100 ?n) (* 100 ?a)
              (* 1000 ?m) )

                
              
           (+ (* 10000 ?s) (* 1000 ?p) (* 100 ?u) (* 10 ?r) ?s)))




  =>
  (printout t "A Solution is:" crlf crlf)
  (printout t "  N = " ?n crlf)
  (printout t "  B = " ?b crlf)
  (printout t "  A = " ?a crlf)
  (printout t "  S = " ?s crlf)
  (printout t "  P = " ?p crlf)
  (printout t "  U = " ?u crlf)
  (printout t "  R = " ?r crlf)
  (printout t "  M = " ?m crlf)


  (printout t crlf)
  (printout t "   " 		?n ?b ?a crlf)
  (printout t " + " 		?m ?a ?n ?u crlf) 
  (printout t "   "             "--------" crlf)
  (printout t " = " 	  ?s ?p ?u ?r ?s crlf crlf))  
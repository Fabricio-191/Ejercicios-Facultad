
;;;======================================================
;;;   Number Puzzle Problem
;;;     
;;;     Solves the number puzzle problem in which
;;;
;;;           CROSS 
;;;        +  ROADS
;;;          ------
;;;        = DANGER
;;;
;;;     CLIPS Version 6.0 Example
;;;
;;;     To execute, merely load, reset and run.
;;;     This example takes alot of memory to execute.
;;;======================================================

(defrule startup
  =>
  (printout t t "The problem is" t t)
  (printout t "    CROSS" t)
  (printout t " +  ROADS" t)
  (printout t "   ------" t)
  (printout t " = DANGER" t t)
  (assert (number 0)
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
  (combination E ?e&~?s&~?r)
  (test (= (mod (+ ?s ?s
                   10 (* 10 ?s))
                100)
           (+ (* 10 ?e) ?r)))
  (combination O ?o&~?s&~?r&~?e)
  (combination A ?a&~?s&~?r&~?e&~?o)
  (combination G ?g&~?s&~?r&~?e&~?o&~?a)
  (test (= (mod (+ ?s ?s
                   (* 10 ?s) 10
                   (* 100 ?o) (* 100 ?a))
                1000)
           (+ (* 100 ?g) (* 10 ?e) ?r)))
  (combination N ?n&~?s&~?r&~?e&~?o&~?a&~?g)
  (test (= (mod (+ ?s ?s
                   (* 10 ?s) 10
                   (* 100 ?o) (* 100 ?a)
                   (* 1000 ?r) (* 1000 ?o))
                10000)
           (+ (* 1000 ?n) (* 100 ?g) (* 10 ?e) ?r)))
  (combination C ?c&~?s&~?r&~?e&~?o&~?a&~?g&~?n)
  (test (= (+ ?s ?s
              (* 10 ?s) 10
              (* 100 ?o) (* 100 ?a)
              (* 1000 ?r) (* 1000 ?o)
              (* 10000 ?c) (* 10000 ?r))
           (+ 100000 (* 10000 ?a) (* 1000 ?n) (* 100 ?g) (* 10 ?e) ?r)))
  =>
  (printout t "Una solucion es:" t t)
  (printout t "  C = " ?c t)
  (printout t "  R = " ?r t)
  (printout t "  O = " ?o t)
  (printout t "  S = " ?s t)
  (printout t "  A = " ?a t)
  (printout t "  D = 1"  t)
  (printout t "  N = " ?n t)
  (printout t "  G = " ?g t)
  (printout t "  E = " ?e t)
  (printout t t)
  (printout t "    "    ?c ?r ?o ?s ?s t)
  (printout t " +  "    ?r ?o ?a "1" ?s t) 
  (printout t "   " "------" t)
  (printout t " = 1" ?a ?n ?g ?e ?r t t))  
  
 
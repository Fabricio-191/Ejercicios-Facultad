(deftemplate solucion
        (slot x1 (type STRING))
        (slot y1 (type STRING))
        (slot z1 (type STRING))
        (slot w1 (type STRING))

        (slot x2 (type STRING))
        (slot y2 (type STRING))
        (slot z2 (type STRING))
        (slot w2 (type STRING))

        (slot x3 (type STRING))
        (slot y3 (type STRING))
        (slot z3 (type STRING))
        (slot w3 (type STRING))

        (slot x4 (type STRING))
        (slot y4 (type STRING))
        (slot z4 (type STRING))
        (slot w4 (type STRING))
)
(deftemplate estado
        (multislot state)
         (slot padre
            (type SYMBOL FACT-ADDRESS)
            (allowed-symbols sin-padre)
            (default sin-padre))
        (slot nivel
            (type INTEGER)
            )
        (slot max-nivel
            (type INTEGER)
            )
        (slot h (type INTEGER))

        (multislot hijos)
)
(deffacts startup
        (solucion
         (x1 " 1")(y1 " 2")(z1 " 0")(w1 " 3")
         (x2 " 4")(y2 " 5")(z2 " 6")(w2 " 7")
         (x3 " 8")(y3 " 9")(z3 "10")(w3 "11")
         (x4 "12")(y4 "13")(z4 "14")(w4 "15"))
        (estado (state " 0" " 1" " 2" " 3" " 4" " 5" " 6" " 7" " 8" " 9" "10" "11" "12" "13" "14" "15")
                (nivel 0)
                (h 10000)
                (max-nivel 20))
	(cargar-distancias)
)
(deffunction print-estado (?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
		(printout t "-------------" crlf)
                (printout t "[" ?A " " ?B " " ?C " " ?D "]" crlf)
                (printout t "[" ?E " " ?F " " ?G " " ?H "]" crlf)
                (printout t "[" ?I " " ?J " " ?K " " ?L "]" crlf)
                (printout t "[" ?M " " ?N " " ?O " " ?P "]" crlf)
)
(defrule movimientos_x1
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
	(test (= (str-compare ?A " 0") 0))
	(test (< ?n ?mn))
        (not (solucion  (x1 ?A) (y1 ?B) (z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?E ?B ?C ?D
                                        ?A ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?B ?A ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)
(defrule movimientos_y1
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
	(test (= (str-compare ?B " 0") 0))
	(test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
               (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)

                (duplicate ?fact (state ?B ?A ?C ?D
                                         ?E ?F ?G ?H
                                         ?I ?J ?K ?L
                                         ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?C ?B ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?F ?C ?D
                                        ?E ?B ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)
(defrule movimientos_z1
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
	    (test (= (str-compare ?C " 0") 0))
	(test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?C ?B  ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P)(nivel (+ ?n 1) ) (padre ?fact))
                (duplicate ?fact (state ?A ?B ?D ?C
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P)(nivel (+ ?n 1) ) (padre ?fact))
                (duplicate ?fact (state ?A ?B ?G ?D
                                        ?E ?F ?C ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P)(nivel (+ ?n 1) ) (padre ?fact))
)
(defrule movimientos_w1
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?D " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?D ?C
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P)(nivel (+ ?n 1) ) (padre ?fact))
                (duplicate ?fact (state ?A ?B ?C ?H
                                        ?E ?F ?G ?D
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P)(nivel (+ ?n 1) ) (padre ?fact))
)
(defrule movimientos_x2
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?E " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?E ?B ?C ?D
                                        ?A ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?F ?E ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?I ?F ?G ?H
                                        ?E ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)

(defrule movimientos_y2
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?F " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?F ?E ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?G ?F ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?F ?C ?D
                                        ?E ?B ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?J ?G ?H
                                        ?I ?F ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)

(defrule movimientos_z2
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?G " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?G ?F ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?G ?D
                                        ?E ?F ?C ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?H ?G
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?K ?H
                                        ?I ?J ?G ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)

(defrule movimientos_w2
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?H " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?H
                                        ?E ?F ?G ?D
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?L
                                        ?I ?J ?K ?H
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?H ?G
                                        ?I ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                                        
)

(defrule movimientos_x3
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?I " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?I ?F ?G ?H
                                        ?E ?J ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?M ?J ?K ?L
                                        ?I ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?J ?I ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)
(defrule movimientos_y3
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?J " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?J ?G ?H
                                        ?I ?F ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?N ?K ?L
                                        ?M ?J ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?J ?I ?K ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?K ?J ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)

(defrule movimientos_z3
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?K " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?K ?H
                                        ?I ?J ?G ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?L ?K
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?K ?J ?L
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?O ?L
                                        ?M ?N ?K ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)


(defrule movimientos_w3
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?L " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?L
                                        ?I ?J ?K ?H
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?P
                                        ?M ?N ?O ?L) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?L ?K
                                        ?M ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)

(defrule movimientos_x4
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?M " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?M ?J ?K ?L
                                        ?I ?N ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?N ?M ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)

(defrule movimientos_y4
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?N " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?N ?K ?L
                                        ?M ?J ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                 (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?N ?M ?O ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                 (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?O ?N ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)


(defrule movimientos_z4
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?O " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?O ?L
                                        ?M ?N ?K ?P) (nivel (+ ?n 1) ) (padre ?fact) )
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?P ?O) (nivel (+ ?n 1) ) (padre ?fact) )
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?O ?N ?P) (nivel (+ ?n 1) ) (padre ?fact) )
)

(defrule movimientos_w4
        ?fact <- (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)(nivel ?n) (max-nivel ?mn))
        (test (= (str-compare ?P " 0") 0))
        (test (< ?n ?mn))
        (not (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                        (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                        (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                        (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P)))
                =>
                (print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?P
                                        ?M ?N ?O ?L) (nivel (+ ?n 1) ) (padre ?fact) )
                (duplicate ?fact (state ?A ?B ?C ?D
                                        ?E ?F ?G ?H
                                        ?I ?J ?K ?L
                                        ?M ?N ?P ?O) (nivel (+ ?n 1) ) (padre ?fact) )
)
(defrule check
        (estado (state  ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P) (padre ?p))
        (solucion (x1 ?A)(y1 ?B)(z1 ?C) (w1 ?D)
                  (x2 ?E) (y2 ?F) (z2 ?G) (w2 ?H)
                  (x3 ?I) (y3 ?J) (z3 ?K) (w3 ?L)
                  (x4 ?M) (y4 ?N) (z4 ?O) (w4 ?P))
        =>
        (halt)
        (printout t "Se alcanzo el objetivo" crlf)
	(print-estado ?A ?B ?C ?D ?E ?F ?G ?H ?I ?J ?K ?L ?M ?N ?O ?P)
)

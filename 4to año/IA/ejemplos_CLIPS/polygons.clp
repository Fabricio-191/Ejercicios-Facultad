;;
;; Serguei A. Mokhov <mokhov@cs.concordia.ca>
;; COMP474 - Assignment #1
;; Instructor: Sabine Bergler
;; Lab Instructor: Alina Andreevskaia
;; Ex. 4, p. 118 (Frames & Inheritance in CLIPS)
;;

;;
;; README
;;
;; The program can be run in either 'clips' or
;; 'xclips' enviroment. It has been developed and
;; tested in the labs 962/966 under UNIX OS.
;;
;; To execute the program one has to 
;;  o load it: (load "polygons.CLP")
;;  o reset initial facts: (reset)
;;  o to activate the demons:
;;    - (send [square-one] sides)
;;    - (send [square-one] area)
;;
;; The program on implements a polygon hierarchy as
;; described in pp. 110-112, with few corrections to
;; the info in the BOX6.1 (such as it conforms to the
;; picture on page 110, i.e. recatangle is a parallelogram
;; and not a direct trapezium). When program is being
;; run it's just generates requeested output of the 
;; no-of-sides and the area for a square.
;;
;; Sample output is in output.poly.txt (Rules and Facts
;; trace rules are ON)
;;


(defclass polygon (is-a USER)
  (role abstract)
  (slot no-of-sides (default 4))
)

(defclass quadrilateral (is-a polygon)
  (role concrete)
)

(defclass trapezium (is-a quadrilateral)
  (role concrete)
) 

(defclass parallelogram (is-a trapezium)
  (role concrete)
)

(defclass rectangle (is-a parallelogram)
  (role concrete)
)

(defclass square (is-a rectangle)
  (role concrete)
  (slot length-of-side (create-accessor write))
  (slot area (create-accessor write))
)

; square-one with side length of 10
(definstances geometry
  (square-one of square (length-of-side 10))
)

; sides() message handler
(defmessage-handler polygon sides()
  ?self:no-of-sides
)

; area() message-handler
; NOTE: it uses CLIPS-genereate member accessor
; put-area created with create-accessor
(defmessage-handler square area()
  put-area->(* ?self:length-of-side ?self:length-of-side)
)

; EOF

;; Immortal "Hello, World!"

; To run:
;
; o Load program: 
;   (load "hello-world.clp") 
;   (or select equivalent option from the menu of XCLIPS)
;
; o Reset fact base: 
;   (reset)
;
; o Execute:
;   (run)

(defrule start
	(initial-fact)
=>
	(printout t "Hello, World!" crlf)
)

; EOF











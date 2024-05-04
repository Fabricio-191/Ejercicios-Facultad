;A simplified version of expert system to classify bacteria
;by Alina Andreevskaia

;define characteristics to be used in rules:

(deftemplate shape (slot form))
(deftemplate gramStain (slot value))
(deftemplate bacteria (slot type))

;rules to define to which category the bacteria belongs
(defrule actinomycete
(shape (form rod | filamentous | unknown))
       (gramStain (value positiove | unknown))
=>
	(assert (bacteria (type actinomycete)))
	(printout t "The bacteria might be ctinomycete." crlf))

(defrule coccoid
	(shape (form spherical | uncknown))
	(gramStain (value positive | unknown))
=>
	(assert (bacteria (type coccoid)))
	(printout t "the bacteria might be coccoid" crlf))

;constructs dealing with the dialog with the user

(defrule welcome
=>
	(printout t "Welcome. " crlf crlf))

(defrule enter_shape
=>
	(printout t "Please enter the shape (rod, filamentous, spherical, or unknown)" crlf)
	(bind ?the_form (read))
	(assert (shape (form ?the_form))))

(defrule enter_gramStain
	=>
	(printout t "Please enter the gramStain (positive or unknown)" crlf)
	(bind ?Stain (read))
	(assert (gramStain (value ?Stain))))


defglobal (?*reloj* = 30)

deftemplate persona
(
	(slot nombre)
	(slot lado)
	(slot tiempo)
)

(defrule inicio
	(declare (salience 1000))
	(initial-fact)
=>
	(assert (persona (nombre A) (lado D) (tiempo 1)))
	(assert (persona (nombre B) (lado D) (tiempo 3)))
	(assert (persona (nombre C) (lado D) (tiempo 6)))
	(assert (persona (nombre D) (lado D) (tiempo 8)))
	(assert (persona (nombre E) (lado D) (tiempo 12)))
)

(defrule opuesto
	assert (opuesto I D)
	assert (opuesto D I)
)

(defrule moverAB
	?h1 <- (persona (nombre A) (lado ?l) (tiempo ?x)
	?h2 <- (persona (nombre B) (lado ?l) (tiempo ?y)
	opuesto (?l ?opuesto)
=>
	(modify ?h1 (lado ?opuesto))
	(modify ?h2 (lado ?opuesto))
	(bind ?*time* (- ?*time* ?y))
)

(defrule volverA
	?h3 <- (persona (nombre A) (lado ?l) (tiempos ?x)
	opuesto (?l ?opuesto)
=>
	(modify ?h3 (lado ?opuesto))
	(bind ?*time* (- ?*time* ?x))
)

(defrule moverDE
	?h4 <- (persona (nombre D) (lado ?l) (tiempo ?x)
	?h5 <- (persona (nombre E) (lado ?l) (tiempo ?y)
	opuesto (?l ?opuesto)
=>
	(modify ?h4 (lado ?opuesto))
	(modify ?h5 (lado ?opuesto))
	(bind ?*time* (- ?*time* ?y))
)

(defrule volverB
	?h6 <- (persona (nombre B) (lado ?l) (tiempos ?x)
	opuesto (?l ?opuesto)
=>
	(modify ?h6 (lado ?opuesto))
	(bind ?*time* (- ?*time* ?x))
)

(defrule moverCA
	?h7 <- (persona (nombre C) (lado ?l) (tiempo ?x)
	?h8 <- (persona (nombre A) (lado ?l) (tiempo ?y)
	opuesto (?l ?opuesto)
=>
	(modify ?h7 (lado ?opuesto))
	(modify ?h8 (lado ?opuesto))
	(bind ?*time* (- ?*time* ?y))
)

(defrule volverA
	?h9 <- (persona (nombre A) (lado ?l) (tiempos ?x)
	opuesto (?l ?opuesto)
=>
	(modify ?h9 (lado ?opuesto))
	(bind ?*time* (- ?*time* ?x))
)

(defrule moverAB
	?h10 <- (persona (nombre A) (lado ?l) (tiempo ?x)
	?h11 <- (persona (nombre B) (lado ?l) (tiempo ?y)
	opuesto (?l ?opuesto)
=>
	(modify ?h10 (lado ?opuesto))
	(modify ?h11 (lado ?opuesto))
	(bind ?*time* (- ?*time* ?y))
)
(printout t "quedaron " ?*time* "segundos" crlf)

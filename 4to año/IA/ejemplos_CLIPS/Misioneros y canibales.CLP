(deftemplate Persona
  (slot tipo (type SYMBOL)(allowed-symbols M C))
  (slot cant (type INTEGER)(allowed-values 1 2 3))
  (slot lado (type SYMBOL)(allowed-values inicial objetivo)) 
)

(deftemplate balsa
   (slot lado (type SYMBOL)(allowed-values inicial objetivo))
)

(deftemplate lado-inicial
  (slot nummisioneros (type INTEGER)(allowed-values 0 1 2 3))
  (slot numcanibales (type INTEGER)(allowed-values 0 1 2 3)) 
  )

(deftemplate lado-objetivo
  (slot nummisioneros (type INTEGER)(allowed-values 0 1 2 3))
  (slot numcanibales (type INTEGER)(allowed-values 0 1 2 3)) 
  )


(deffacts hechos
  (Persona (tipo M) (cant 1)(lado inicial))
  (Persona (tipo M) (cant 2)(lado inicial))
  (Persona (tipo M) (cant 3)(lado inicial))
  (Persona (tipo C) (cant 1)(lado inicial))
  (Persona (tipo C) (cant 2)(lado inicial))
  (Persona (tipo C) (cant 3)(lado inicial))
  (balsa (lado inicial))
  (lado-objetivo (nummisioneros 0)(numcanibales 0))
  (lado-inicial (nummisioneros 3)(numcanibales 3))
  

)
;(defrule Regla1
;	(declare (salience 1000))
;	?lb<- (lado-objetivo(nummisioneros 3)(numcanibales 3))
;=>
;	(printout t OBJETIVO LOGRADO! crlf)
;  	(halt)
;)


(defrule Regla2 "Viaja un Canibal y un Misionero"
	?var1 <- (Persona(tipo C)(lado inicial))
	?var2 <- (Persona(tipo M)(lado inicial))
	?bal <- (balsa(lado inicial))
	?la <- (lado-inicial(nummisioneros ?miA)(numcanibales ?caA))
	?lb <- (lado-objetivo(nummisioneros ?miB)(numcanibales ?caB))
	(test(>= (+ ?miB 1) (+ ?caB 1)))
=>
	(modify ?var1 (lado objetivo))
	(modify ?var2 (lado objetivo))
	(modify ?bal(lado objetivo))
	(bind ?aux1(+ ?miB 1))
	(bind ?aux2(+ ?caB 1))
	(modify ?lb (nummisioneros ?aux1)(numcanibales ?aux2))
	(bind ?aux1(- ?miA 1))
	(bind ?aux2(- ?caA 1))
	(modify ?la (nummisioneros ?aux1)(numcanibales ?aux2))
	 printout t "Cruza Canibal -  Misionero" crlf)
)

(defrule Regla3
	(declare (salience 1))
	?var1 <- (Persona(tipo M)(cant ?n1)(lado inicial))
	?var2 <- (Persona(tipo M)(cant ?n2)(lado inicial))
	?bal <- (balsa(lado inicial))
	(test(!= ?n1 ?n2))
	?lb <- (lado-objetivo(nummisioneros ?miB)(numcanibales ?caB))
	(test(>= (+ ?miB 2) ?caB))
	?la <- (lado-inicial(nummisioneros ?miA)(numcanibales ?caA))
	(or(test(>= (- ?miA 2) ?caA))
	   (test(= (- ?miA 2) 0)))
=>
	(modify ?var1 (lado objetivo))
	(modify ?var2 (lado objetivo))
	(modify ?bal(lado objetivo))
	(bind ?aux1(+ ?miB 2))
	(modify ?lb (nummisioneros ?aux1))
	(bind ?aux1(- ?miA 2))
	(modify ?la (nummisioneros ?aux1))
	(printout t "Cruza Misionero - Misionero" crlf)
)

(defrule Regla4	
	?var1 <- (Persona(tipo C)(cant ?n1)(lado inicial))
	?var2 <- (Persona(tipo C)(cant ?n2)(lado inicial))
	?bal <- (balsa(lado inicial))
	?la <- (lado-inicial(nummisioneros ?miA)(numcanibales ?caA))
	?lb <- (lado-objetivo(nummisioneros ?miB)(numcanibales ?caB))
	(test(!= ?n1 ?n2))
	(or   (test(= ?miB 0))
		(test(>= ?miB (+ ?caB 2))))
=>
	(modify ?var1 (lado objetivo))
	(modify ?var2 (lado objetivo))
	(modify ?bal(lado objetivo))
	(bind ?aux1(+ ?caB 2))
	(modify ?lb (numcanibales ?aux1))
	(bind ?aux1(- ?caA 2))
	(modify ?la (numcanibales ?aux1))
	(printout t "Cruza Canibal - Canibal" crlf)
)


(defrule Regla5
	?var <- (Persona(tipo C)(lado objetivo))
	?bal <- (balsa(lado objetivo))
	?la <- (lado-inicial(nummisioneros ?miA)(numcanibales ?caA))
	?lb <- (lado-objetivo(nummisioneros ?miB)(numcanibales ?caB))
	(or   (test(= ?miA 0))
		(test(>= ?miA (+ ?caA 1))))
=>
	(modify ?var(lado inicial))
	(modify ?bal(lado inicial))
	(bind ?aux1(- ?caB 1))
	(modify ?lb (numcanibales ?aux1))
	(bind ?aux1(+ ?caA 1))
	(modify ?la (numcanibales ?aux1))
	(printout t "Vuelve Canibal" crlf)
)

(defrule Regla6
	?var <- (Persona(tipo M)(lado objetivo))
	?bal <- (balsa(lado objetivo))
	?la <- (lado-inicial(nummisioneros ?miA)(numcanibales ?caA))
	?lb <- (lado-objetivo(nummisioneros ?miB)(numcanibales ?caB))
	(or
	(test(= (- ?miB 1) 0))
	(and
	(test(>= (- ?miB 1) ?caB))
	(test(>= (+ ?miA 1) ?caA))))
=>
	(modify ?var(lado inicial))
	(modify ?bal(lado inicial))
	(bind ?aux1(- ?miB 1))
	(modify ?lb (nummisioneros ?aux1))
	(bind ?aux1(+ ?miA 1))
	(modify ?la (nummisioneros ?aux1))
	(printout t "Vuelve Misionero" crlf)
)

(defrule Regla7
	?var1 <- (Persona(tipo C)(lado objetivo))
	?var2 <- (Persona(tipo M)(lado objetivo))
	?bal <- (balsa(lado objetivo))
	?la <- (lado-inicial(nummisioneros ?miA)(numcanibales ?caA))
	?lb <- (lado-objetivo(nummisioneros ?miB)(numcanibales ?caB))
	(test(>= (+ ?miA 1) (+ ?caA 1)))
=>
	(modify ?var1 (lado inicial))
	(modify ?var2 (lado inicial))
	(modify ?bal(lado inicial))
	(bind ?aux1(- ?miB 1))
	(bind ?aux2(- ?caB 1))
	(modify ?lb (nummisioneros ?aux1)(numcanibales ?aux2))
	(bind ?aux1(+ ?miA 1))
	(bind ?aux2(+ ?caA 1))
	(modify ?la (nummisioneros ?aux1)(numcanibales ?aux2))
	(printout t "Vuelve Canibal - Misionero" crlf)
)


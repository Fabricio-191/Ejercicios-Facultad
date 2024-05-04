(deftemplate Esposos (slot Hombre) (slot Mujer))
(deftemplate Hermanos (slot Hermano1) (slot Hermano2))
(deftemplate Hijo (slot Hombre) (slot Mujer) (slot Hijo1))


(deffacts Inicia 
(Hermanos (Hermano1 ANA)(Hermano2 CAROLINA))
(Hermanos (Hermano1 CAROLINA)(Hermano2 ANA))
(Esposos (Hombre LUIS)(Mujer ANA))
(Hijo (Hombre LUIS)(Mujer ANA)(Hijo1 SUSANA)) 
(Esposos (Hombre DAVID)(Mujer CAROLINA))
(Hijo (Hombre DAVID)(Mujer CAROLINA)(Hijo1 TOMAS))
(Esposos (Hombre TOMAS)(Mujer SUSANA))
(Hijo (Hombre TOMAS)(Mujer SUSANA)(Hijo1 JUAN))
) 

(defrule Abuelo 
(Hijo (Hombre ?Padre) (Mujer ?Madre) (Hijo1 ?Hijo))
(Esposos (Hombre ?Hijo) (Mujer ?Conyuge))
(Hijo (Hombre ?Hijo)(Mujer ?Conyuge)(Hijo1 ?Hijo2))
=>
(printout t ?Padre " Es Abuelo de " ?Hijo2 crlf)
(printout t ?Madre " Es Abuela de " ?Hijo2 crlf)
(assert(Abuelo ?Padre ?Hijo2))
(assert(Abuela ?Madre ?Hijo2))
(assert(Nieto ?Padre ?Madre ?Hijo2))
)

(defrule Cuniadas
(Esposos (Hombre ?h1)(Mujer ?m1))
(Esposos (Hombre ?h2&~?h1) (Mujer ?m2&~?m1))
(Hermanos (Hermano1 ?m1)(Hermano2 ?m2))
=>
(printout t ?m1 " Es cuniada de " ?h2 crlf)
(assert (Cuniada ?m1 ?h2))
) 

(defrule Tios
(Esposos (Hombre ?h1)(Mujer ?m1))
(Esposos (Hombre ?h2&~?h1) (Mujer ?m2&~?m1))
(Hermanos (Hermano1 ?m1)(Hermano2 ?m2))
(Hijo (Hombre ?h2)(Mujer ?m2)(Hijo1 ?sobrino))
=>
(printout t ?m1 " y " ?h1 " son tios de " ?sobrino crlf)
(assert (Tio ?h1 ?sobrino))
(assert (Tia ?m1 ?sobrino))
)

(defrule Primos
(Esposos (Hombre ?h1)(Mujer ?m1))
(Esposos (Hombre ?h2&~?h1) (Mujer ?m2&~?m1))
(Hermanos (Hermano1 ?m1)(Hermano2 ?m2))
(Hijo (Hombre ?h1)(Mujer ?m1)(Hijo1 ?hijo1))
(Hijo (Hombre ?h2)(Mujer ?m2)(Hijo1 ?hijo2))
(not (Primos ?hijo2 ?hijo1))
=>
(printout t ?hijo1 " y " ?hijo2 " son primos " crlf)
(assert (Primos ?hijo1 ?hijo2))
) 
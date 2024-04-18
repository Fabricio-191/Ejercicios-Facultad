(deffacts personas
   (mujer ana)
   (mujer maria)
   (mujer susana)
   (mujer carolin)
   (hombre luis)
   (hombre juan)
   (hombre david)
   (hombre tomas)
   (hombre pedro))

(deffacts estado-inicial
   (esposo-de ana luis)
   (esposo-de carolin david)
   (esposo-de susana tomas)
   (esposa-de luis ana)
   (esposa-de david carolin)
   (esposa-de tomas susana)
   (madre-de susana ana)
   (madre-de tomas carolin)
   (madre-de juan susana)
   (madre-de pedro maria)
   (padre-de susana luis)
   (padre-de tomas david)
   (padre-de juan tomas)
   (padre-de pedro tomas))

(defrule abuela-de
   (mujer ?x)
   (madre-de ?y ?x)
   (or  (madre-de ?a ?y)
        (padre-de ?a ?y))
   =>
   (printout t ?x " es abuela de " ?a crlf))


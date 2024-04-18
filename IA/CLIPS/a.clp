(deftemplate elemento (slot valor)) 

 

(deffacts valores 
   (elemento (valor 1)) 
   (elemento (valor 2)) 
   (elemento (valor 3))) 

(defrule sumar-elementos 
   (declare (salience -10)) 
   => 
   (bind ?suma 0) 
   (forall (elemento (valor ?valor)) 
      (bind ?suma (+ ?suma ?valor))) 
   (printout t "La suma de los elementos es: " ?suma crlf))  

(defrule asd
	=> 
	(assert (resultado 1))
) 

(defrule asd
	(printout t "A" crlf)
	(printout t "B" crlf)
	=> 
	(printout t "La suma de los elementos es: " crlf))  
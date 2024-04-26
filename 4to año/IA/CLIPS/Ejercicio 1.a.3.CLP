Mariana y Gustavo se casaron y formaron una bella familia, teniendo dos bellos hijos Pablo y Laura. Ambos 
cónyuges tenían un hijo cada uno antes del matrimonio, Agustín y Santiago respectivamente. 

(mujer <Nombre>) 
(hombre <Nombre>) 
(hijx-de  <Hijo/a>   <Padre/Madre>) 
(esposa-de <Esposa> <Esposo>) 
(marido-de <Esposo> <Esposa>) 


(deffacts base "1) Ingresar los hechos correspondientes a los integrantes de la familia."
	(mujer Mariana)
	(mujer Laura)
	(hombre Gustavo)
	(hombre Pablo)
	(hombre Agustín)
	(hombre Santiago)
	(hijx-de Pablo Mariana)
	(hijx-de Laura Mariana)
	(hijx-de Pablo Gustavo)
	(hijx-de Laura Gustavo)
	(hijx-de Agustín Mariana)
	(hijx-de Santiago Gustavo)
	(esposa-de Mariana Gustavo)
	(marido-de Gustavo Mariana)
)


(defrule hermanos "2) Mostrar los nombres de los hermanos hijos del matrimonio y agregar los hechos (hermano <Nombre> <Nombre>) a la MT."
	(marido-de ?padre1 ?padre2) 
	(hijx-de ?hijo1 ?padre1)
	(hijx-de ?hijo2 ?padre1)
	(hijx-de ?hijo1 ?padre2)
	(hijx-de ?hijo2 ?padre2)
	(test (neq ?hijo1 ?hijo2))
	=>
	(printout t ?hijo1 " y " ?hijo2 " son hermanos y pertenecen al matrimonio" crlf))  
	(assert (hermano ?hijo1 ?hijo2))
	(assert (hermano ?hijo2 ?hijo1))
)

(defrule hijos-antes-matrimonio "3) Mostrar el nombre del hijo y su progenitor que no pertenecen al matrimonio."
	(hijx-de ?hijo ?padre1)
	(or (esposa-de ?padre1 ?padre2) (marido-de ?padre1 ?padre2))
	(not (hijx-de ?hijo ?padre2))
	=>
	(printout t "El hijo " ?hijo " de " ?padre1 " no pertenece al matrimonio" crlf))  
)
 
(defrule padrastro "4) Mostrar el nombre del padrastro y la madrastra de los hijos fuera del matrimonio y agregarlos a la MT (padrastro <> <>)  (madrastra <> <>)"
	(hijx-de ?hijo ?madre)
	(esposa-de ?madre ?padre)
	(not (hijx-de ?hijo ?padre))
	=>
	(printout t ?padre " es el padrasto de " ?hijo crlf))  
	(assert (padrastro ?hijo ?padre))
)

(defrule madrastra "4) Mostrar el nombre del padrastro y la madrastra de los hijos fuera del matrimonio y agregarlos a la MT (padrastro <> <>)  (madrastra <> <>)"
	(hijx-de ?hijo ?padre)
	(marido-de ?padre ?madre)
	(not (hijx-de ?hijo ?madre))
	=>
	(printout t ?madre " es la madrastra de " ?hijo crlf))  
	(assert (madrastra ?hijo ?madre))
)
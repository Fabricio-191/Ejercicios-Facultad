;  1) Ingresar los hechos correspondientes a los integrantes de la familia.
(deffacts base
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

;  2) Mostrar los nombres de los hermanos hijos del matrimonio y agregar los hechos (hermano <Nombre> <Nombre>) a la MT.
(defrule hermanos 
	(marido-de ?padre1 ?padre2) 
	(hijx-de ?hijo1 ?padre1)
	(hijx-de ?hijo2 ?padre1)
	(hijx-de ?hijo1 ?padre2)
	(hijx-de ?hijo2 ?padre2)
	(test (neq ?hijo1 ?hijo2))
	=>
	(printout t ?hijo1 " y " ?hijo2 " son hermanos y pertenecen al matrimonio" crlf)
	(assert (hermano ?hijo1 ?hijo2))
	(assert (hermano ?hijo2 ?hijo1))
)

;  3) Mostrar el nombre del hijo y su progenitor que no pertenecen al matrimonio.
(defrule hijos-antes-matrimonio 
	(hijx-de ?hijo ?padre1)
	(or (esposa-de ?padre1 ?padre2) (marido-de ?padre1 ?padre2))
	(not (hijx-de ?hijo ?padre2))
	=>
	(printout t "El hijo " ?hijo " de " ?padre1 " no pertenece al matrimonio" crlf)
)

;  4) Mostrar el nombre del padrastro y la madrastra de los hijos fuera del matrimonio y agregarlos a la MT (padrastro <> <>)  (madrastra <> <>)
(defrule padrastro
	(hijx-de ?hijo ?madre)
	(esposa-de ?madre ?padre)
	(not (hijx-de ?hijo ?padre))
	=>
	(printout t ?padre " es el padrasto de " ?hijo crlf)  
	(assert (padrastro ?hijo ?padre))
)

;  4) Mostrar el nombre del padrastro y la madrastra de los hijos fuera del matrimonio y agregarlos a la MT (padrastro <> <>)  (madrastra <> <>)
(defrule madrastra
	(hijx-de ?hijo ?padre)
	(marido-de ?padre ?madre)
	(not (hijx-de ?hijo ?madre))
	=>
	(printout t ?madre " es la madrastra de " ?hijo crlf)
	(assert (madrastra ?hijo ?madre))
)

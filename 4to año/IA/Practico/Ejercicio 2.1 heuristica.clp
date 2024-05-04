; Definicion de una plantilla para representar un estado del juego de las jarras en un momento especifico
(deftemplate jarras
	(multislot contenido (type INTEGER) (range 0 24) (cardinality 4 4)) ; Puede verse como una "tupla" de 4 elementos que representan la cantidad de litros en cada jarra
	; Los valores contenidos en la tupla pueden variar entre 0 y 24, que es la capacidad maxima de la jarra mas grande
	; La cardinalidad es 4 4, lo que significa que la tupla siempre tendra 4 elementos (minimo 4 y maximo 4)
	(slot heuristica (type INTEGER)) ; Valor de la heuristica para el estado actual, a menor valor, mas cercano a la solucion
)

(defglobal ?*capacidades* = (create$ 24 13 11 5)) ; Definicion de una variable global que contiene las capacidades de las jarras

(deffunction calcularHeuristica (?contenidos) ; Funcion que calcula la heuristica para un estado dado
	; La heuristica se calcula como la suma de las diferencias absolutas entre la cantidad de litros en cada jarra en comparacion con estado final
	(+
		(abs (- 8 (nth$ 1 ?contenidos)))
		(abs (- 8 (nth$ 2 ?contenidos)))
		(abs (- 8 (nth$ 3 ?contenidos)))
		(nth$ 4 ?contenidos)
	)
)


(defrule inicio
	; Se definen los estados iniciales
	; Podria hacerse usando deffacts, pero al hacerlo como regla no hace falta usar (reset) para ejecutar el programa
	=> 
	(assert (numero 1))
	(assert (numero 2))
	(assert (numero 3))
	(assert (numero 4))
	(assert (jarras (contenido 24 0 0 0) (heuristica 32)))
)

(defrule estadoFinal
	; Regla que se ejecuta una vez se llego al estado final, se declara la prioridad maxima (10000) y se detiene el programa
	(declare (salience 10000))
	(jarras (contenido 8 8 8 0) (heuristica 0))
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

(defrule moverDeJarraEnJarra
	; Regla que se encarga de mover el contenido de una jarra origen a una jarra destino
	(numero ?origen)
	(numero ?destino)
	(test (neq ?origen ?destino)) ; No se puede mover de una jarra a si misma
	(jarras (contenido $?contenidos) (heuristica ?heu)) ; Se obtiene el estado actual
	(not (jarras (heuristica ?h2&:(< ?h2 ?heu)))) ; Se verifica que no haya un estado con mejor heuristica (puede haber otro de igual heuristica)
	(not (estadoSinSalida ?contenido)) ; Se verifica que no sea un estado sin salida
	=>
	(bind ?conOrigen (nth$ ?origen ?contenidos))      ; Se obtiene la cantidad de litros en la jarra origen
	(bind ?conDestino (nth$ ?destino ?contenidos))    ; Se obtiene la cantidad de litros en la jarra destino
	(bind ?capDestino (nth$ ?destino ?*capacidades*)) ; Se obtiene la capacidad de la jarra destino
	(bind ?litros (min ?conOrigen (- ?capDestino ?conDestino))) ; Se calcula la cantidad de litros a mover, que seria la cantidad de litros en la jarra origen o el faltante en la jarra destino para llenarse
	(bind ?contenidos (replace$ ?contenidos ?origen  ?origen  (- ?conOrigen  ?litros))) ; Se actualiza la cantidad de litros en la jarra origen
	(bind ?contenidos (replace$ ?contenidos ?destino ?destino (+ ?conDestino ?litros))) ; Se actualiza la cantidad de litros en la jarra destino
	(assert (jarras (contenido ?contenidos) (heuristica (calcularHeuristica ?contenidos)) )) ; Se agrega el nuevo estado
)

(defrule eliminarEstadosSinSalida
	(declare (salience -50)) ; Se declara una prioridad negativa para que se ejecute al final cuando la regla de moverDeJarraEnJarra ya no pueda hacer nada, es decir que los estados con la menor heuristica fueron explorados completamente
	?fact <- (jarras (heuristica ?heu) (contenido $?contenido)) ; Se obtiene un estado
	(not (jarras (heuristica ?h2&:(< ?h2 ?heu)))) ; Se verifica que sea uno de los estados con menor heuristica
	=>
	(retract ?fact) ; Se elimina el estado
	(assert (estadoSinSalida ?contenido)) ; Se agrega el estado a la lista de estados sin salida
	; Al eliminar todos los estados con menor heuristica, la menor heuristica "sube" por asi decirlo, lo que permite que en la regla moverDeJarraEnJarra se puedan explorar otros estados debido a que ciertos estados pasarian a cumplir la condicion de tener la menor heuristica
)

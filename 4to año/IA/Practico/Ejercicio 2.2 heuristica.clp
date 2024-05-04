; Se define un nodo como un estado del juego, con su heuristica y su clase (abierto o cerrado)
(deftemplate nodo 
   (multislot estado (type INTEGER) (range 0 15) (cardinality 16 16))
   ; Puede verse como una "tupla" de 16 elementos, que almacena donde esta cada pieza
   ; Los primeros 4 elementos son la primera fila, los siguientes 4 la segunda, y asi sucesivamente
   (slot heuristica (type INTEGER)) ; La heuristica del nodo, mientras mas pequeña mejor
   (slot clase (default abierto)) ; La clase del nodo, puede ser abierto o cerrado, se usa para saber si debe ser explorado o no
)

; Se define el estado inicial y final del juego
(defglobal MAIN 
   ?*estadoInicial* = (create$ 0  1  2 3  4 5 6 7 8 9 10 11 12 13 14 15)
   ?*estadoFinal*   = (create$ 0 14 13 3 11 5 6 8 7 9 10  4 12  2  1 15) 
)

(deffunction heuristica ($?estado)
	; Se define la heuristica como la cantidad de piezas mal ubicadas + 1000 si la ultima fila no esta con los valores correctos
	; Esto se hace para que una vez la ultima fila este ordenada, el algoritmo no la desordene. Esto acorta el espacio de busqueda y tiempo enormemente
	(bind ?res 0)
	(loop-for-count (?i 1 16) ; Por cada una de las piezas
		(if (neq (nth ?i $?estado) (nth ?i ?*estadoFinal*)) ; Si la pieza no esta en su lugar se suma 1
			then (bind ?res (+ ?res 1))
		)
	)
	(if (neq (subseq$ $?estado 13 16) (create$ 12 2 1 15)) ; Si la ultima fila no es igual a la ultima fila del estado final
		then (bind ?res (+ ?res 1000)) ; Se suma 1000
	) 
	?res
)


(defrule inicio
	; Se define el nodo inicial con su heuristica con el cual se comienza la busqueda
	=> 
	(assert (nodo
		(estado ?*estadoInicial*) 
		(heuristica (heuristica ?*estadoInicial*)) 
		(clase cerrado)
	))
	; (podrian declararse como hechos pero al hacerlo como regla no hace falta usar reset al comenzar)
)


(defrule final 
	; Se define el nodo final con su heuristica, al encontrarlo se imprime un mensaje y se detiene el programa
	; Notar que la regla tiene prioridad maxima (10000) para que se ejecute apenas sea posible
	(declare (salience 10000))
	(nodo (estado 0 14 13 3 11 5 6 8 7 9 10 4 12 2 1 15) (heuristica 0))
	=>
	(printout t "Se encontro la solucion" crlf)
	(halt) 
)

; Movimientos
; Como mencionamos anteriormente, el nodo que representa un estado del juego puede tener dos clases: abierto o cerrado
; Solo se exploran los nodos cerrados, y solo se cierran los nodos con mejor heuristica que no han sido cerrados

(defrule arriba 
	; Se busca un nodo cerrado donde el 0 tenga como minimo 4 elementos antes que el, para poder moverse arriba sin salirse del tablero
	; $?a y $?f seran variables multicampo que almacenaran el resto de piezas del tablero (pueden quedar vacias)
	(nodo (estado $?a ?b ?c ?d ?e 0 $?f) (clase cerrado)) 
	=> 
	(bind $?nuevo-estado (create$  $?a 0 ?c ?d ?e ?b $?f)) ; Se crea un nuevo estado con el 0 movido arriba y ?b movido abajo
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado)))) ; Se agrega el nuevo nodo a la base de hechos
)

(defrule abajo 
	; Lo mismo que arriba pero para abajo 👍
	(nodo (estado $?a 0 ?b ?c ?d ?e $?f) (clase cerrado)) 
	=> 
	(bind $?nuevo-estado (create$ $?a ?e ?b ?c ?d 0 $?f)) 
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado))))
)

(defrule derecha 
	; Se busca un nodo cerrado donde el 0 tenga un elemento a la derecha (?b) para poder moverse a la derecha
	; Sin embargo, debido a nuestra representacion secuencial hay que tener cuidado con los bordes de la derecha, es decir cuando el 0 esta en la casilla 4, 8, 12 o 16
	; Para revisar esto se revisa que la cantidad de elementos a la derecha de ?b no sea (3 + un multiplo de 4) esto querria decir que el 0 esta en una de las casillas mencionadas
	(nodo (estado $?a 0 ?b $?c&:(neq (mod (length $?c) 4) 3)) (clase cerrado)) 
	=> 
	(bind $?nuevo-estado (create$ $?a ?b 0 $?c)) 
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado))))
)

(defrule izquierda 
	; Lo mismo que derecha pero para la izquierda 👍
	(nodo (estado $?a&:(neq (mod (length $?a) 4) 3) ?b 0 $?c) (clase cerrado))
	=> 
	(bind $?nuevo-estado (create$ $?a 0 ?b $?c)) 
	(assert (nodo (estado $?nuevo-estado) (heuristica (heuristica $?nuevo-estado))))
)

(defrule cerrarMejorNodo
	(declare (salience -10)) ; Se declara una prioridad negativa para que se ejecute al final cuando ya no se puedan explorar mas los nodos cerrados
	; Se busca un nodo abierto con la mejor heuristica (podria haber otros de igual heuristica) y se cierra
	?nodo <- (nodo (clase abierto) (heuristica ?h1))            
	(not (nodo (clase abierto) (heuristica ?h2&:(< ?h2 ?h1)))) 
	=> 
	(modify ?nodo (clase cerrado))
)
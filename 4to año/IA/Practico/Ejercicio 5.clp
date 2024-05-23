; Asumiendo que los conceptos anteriores son variables linguísticas con sus respectivos valores. Los valores de entrada son los marcados en  rojo, determinar la certidumbre de las conclusiones.  
; 
; (el problema es NULO | GRAVE | MEDIO)
; 
; 1) if LLUVIA = BAJA then NULO                                                         (valor de certeza de la regla: 0.8)
; 2) if LLUVIA = IMPORTANTE and SUELO = EMPAPADO then GRAVE                             (valor de certeza de la regla: 0.7) 
; 3) if LLUVIA = IMPORTANTE and SUELO = HUMEDO then MEDIO                               (valor de certeza de la regla: 0.9) 
; 4) if LLUVIA = INTENSA and SUELO = EMPAPADO then GRAVE                                (valor de certeza de la regla: 0.5) 
; 5) if LLUVIA = INTENSA and SUELO = HUMEDO and TOPOGRAFIA = ESCARPADA then GRAVE       (valor de certeza de la regla: 0.7) 
; 6) if LLUVIA = INTENSA and SUELO = HUMEDO and TOPOGRAFIA = SUAVE then MEDIO           (valor de certeza de la regla: 0.7) 
; 
; Se sabe además, que los sensores utilizados tienen una precisión del 95% (certeza del 0.95) o sea ante una medida de 100 puede medir 95 o 105. 
; 
; A) Realice los cálculos manuales considerando: 
; 	1) Conclusiones no borrosas,
; 	2) Conclusiones borrosas. 
; 
; Represéntelo en SUMMERS(conclusiones no borrosas) y/o fuzziclipsy compruebe las conclusiones logradas.
; Objetivo: Cuantificar la  incertidumbre mediante LB y una herramienta de software específica. 


(defglobal
	; valores medidos
	?*lluvia* = 32
	?*suelo* = 69
	?*topografia* = 19
)

(defrule lluvia-baja
	(declare (salience 10))
	=>
	(if (<= ?*lluvia* 25) then (assert (lluvia BAJA)))
	(if (<= ?*lluvia* 40) then (assert (lluvia BAJA) CF (+ (* -0.06666667 ?*lluvia*) 2.6666667)))
)

(defrule lluvia-importante
	(declare (salience 10))
	=>
	(if (and (<= 20 ?*lluvia*) (<= ?*lluvia* 50)) then (assert (lluvia IMPORTANTE) CF (+ (* 0.03333333 ?*lluvia*) -0.6666667)))
	(if (and (<= 50 ?*lluvia*) (<= ?*lluvia* 70)) then (assert (lluvia IMPORTANTE) CF (+ (* -0.05 ?*lluvia*) 3.5)))
)

(defrule lluvia-intensa
	(declare (salience 10))
	=>
	(if (<= 70 ?*lluvia*) then (assert (lluvia INTENSA)))
	(if (<= 60 ?*lluvia*) then (assert (lluvia INTENSA) CF (+ (* 0.1 ?*lluvia*) -6)))
)

(defrule suelo-humedo
	(declare (salience 10))
	=>
	(if (and (<= 15 ?*suelo*) (<= ?*suelo* 35)) then (assert (suelo HUMEDO) CF (+ (* 0.05 ?*suelo*) -0.75)))
	(if (and (<= 35 ?*suelo*) (<= ?*suelo* 80)) then (assert (suelo HUMEDO) CF (+ (* -0.022222222 ?*suelo*) 1.77777777778)))
)

(defrule suelo-empapado
	(declare (salience 10))
	=>
	(if (<= 70 ?*suelo*) then (assert (suelo EMPAPADO)))
	(if (<= 45 ?*suelo*) then (assert (suelo EMPAPADO) CF (+ (* 0.04 ?*suelo*) -1.8)))
)

(defrule topografia-suave
	(declare (salience 10))
	=>
	(if (and (<= 2 ?*topografia*) (<= ?*topografia* 4)) then (assert (topografia SUAVE) CF (+ (* 0.5 ?*topografia*) -1)))
	(if (and (<= 4 ?*topografia*) (<= ?*topografia* 15)) then (assert (topografia SUAVE)))
	(if (and (<= 15 ?*topografia*) (<= ?*topografia* 25)) then (assert (topografia SUAVE) CF (+ (* -0.1 ?*topografia*) 2.5)))
)

(defrule topografia-escarpada
	(declare (salience 10))
	=>
	(if (and (<= 10 ?*topografia*) (<= ?*topografia* 20)) then (assert (topografia ESCARPADA) CF (+ (* 0.1 ?*topografia*) -1)))
	(if (and (<= 20 ?*topografia*) (<= ?*topografia* 30)) then (assert (topografia ESCARPADA)))
	(if (and (<= 30 ?*topografia*) (<= ?*topografia* 50)) then (assert (topografia ESCARPADA) CF (+ (* -0.05 ?*topografia*) 2.5)))
)

(defrule regla1
	(declare (CF 0.8))
	(lluvia BAJA)
	=>
	(assert (problema NULO))
)

(defrule regla2
	(declare (CF 0.7))
	(lluvia IMPORTANTE)
	(suelo EMPAPADO)
	=>
	(assert (problema GRAVE))
)

(defrule regla3
	(declare (CF 0.9))
	(lluvia IMPORTANTE)
	(suelo HUMEDO)
	=>
	(assert (problema MEDIO))
)

(defrule regla4
	(declare (CF 0.5))
	(lluvia INTENSA)
	(suelo EMPAPADO)
	=>
	(assert (problema GRAVE))
)

(defrule regla5
	(declare (CF 0.7))
	(lluvia INTENSA)
	(suelo HUMEDO)
	(topografia ESCARPADA)
	=>
	(assert (problema GRAVE))
)

(defrule regla6
	(declare (CF 0.7))
	(lluvia INTENSA)
	(suelo HUMEDO)
	(topografia SUAVE)
	=>
	(assert (problema MEDIO))
)

; Lluvia baja           {
;	si  0 <= x <= 25:   1
;	si 25 <= x <= 40:  -0.06666667 x + 2.6666667
;	0 en otro caso
; }

; Lluvia importante     {
;	si 20 <= x <= 50:   0.03333333x - 0.6666667
;	si 50 <= x <= 70:  -0.05x + 3.5
;   0 en otro caso
; }

; Lluvia intensa        { 
;   si 60 <= x <= 70:   0.1x - 6
;   si 70 <= x:         1
;   0 en otro caso
; }

; Suelo humedo          {
;	si 15 <= x <= 35:   0.05x - 0.75
;   si 35 <= x <= 80:  -0.022222222x + 1.77777777778
;   0 en otro caso
; }

; Suelo empapado        {
;	si 45 <= x <= 70:   0.04x - 1.8
;	si 70 <= x:         1
;   0 en otro caso
; }

; Topografia suave      {
;	si 2 <= x <= 4:     0.5x - 1
;	si 4 <= x <= 15:    1
;   si 15 <= x <= 25:  -0.1x + 2.5
;   0 en otro caso
; }

; Topografia escarpada  {
;	si 10 <= x <= 20:   0.1x - 1
;	si 20 <= x <= 30:   1
;   si 30 <= x <= 50:  -0.05x + 2.5
;   0 en otro caso
; }

; (deftemplate lluvia
;     0 1000
;     (
;         (BAJA (25 1) (40 0))
;         (IMPORTANTE (20 0) (50 1) (70 0))
;         (INTENSA (60 0) (70 1))
;     )
; )
; 
; (deftemplate humedad
;     0 100
;     (
;         (HUMEDO (15 0) (35 1) (80 0))
;         (EMPAPADO (45 0) (70 1))
;     )
; )
; 
; (deftemplate suelo
;     0 100
;     (
;         (SUAVE (2 0) (4 1) (15 1) (25 0))
;         (ESCARPADA (10 0) (20 1) (30 1) (50 0))
;     )
; )
; 
; (defrule inicio
;     =>
;     (assert lluvia 32)
;     (assert humedad 69)
;     (assert suelo 19)
; )
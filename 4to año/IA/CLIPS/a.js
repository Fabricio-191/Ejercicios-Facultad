// @ts-nocheck
const capacidades = [null, 24, 13, 11, 5];

/*
(defrule moverDeJarra1aJarra2
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (>= ?jarra1 0))
	(test (<= ?jarra2 13))
	=> 
	(bind ?diff (min (- 13 ?jarra2) ?jarra1))
	(bind ?jarra1 (- ?jarra1 ?diff))
	(bind ?jarra2 (+ ?jarra2 ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)

(defrule moverDeJarraIaJarraJ
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (>= ?jarraI 0))
	(test (<= ?jarraJ 13))
	=> 
	(bind ?diff (min (- 13 ?jarraJ) ?jarraI))
	(bind ?jarraI (- ?jarraI ?diff))
	(bind ?jarraJ (+ ?jarraJ ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)
*/

function makeRule(i, j) {
	return `
(defrule moverDeJarraXaJarraY
	(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))
	(test (> ?jarraX 0))
	(test (<= ?jarraY CAPACIDAD_J))
	=> 
	(bind ?diff (min (- CAPACIDAD_J ?jarraY) ?jarraX))
	(bind ?jarraX (- ?jarraX ?diff))
	(bind ?jarraY (+ ?jarraY ?diff))
	(assert (jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4)))
)`.replaceAll('CAPACIDAD_J', capacidades[j]).replaceAll('X', i).replaceAll('Y', j);
};

const strJarras = `(jarras (jarra1 ?jarra1) (jarra2 ?jarra2) (jarra3 ?jarra3) (jarra4 ?jarra4))`;

console.clear();
for(let i = 1; i < capacidades.length; i++) {
	for(let j = 1; j < capacidades.length; j++) {
		if(i != j) console.log(makeRule(i, j));
	}
}
/**
Descubra el método más simple para que ambos trenes puedan pasar.
En esta clase de ferrocarril primitivo tenemos una máquina y cuatro vagones enfrentados a una máquina con tres
vagones. El problema consiste en descubrir el modo más expeditivo para que ambos trenes pasen por medio de la vía
lateral, que por su longitud sólo puede albergar una locomotora o un vagón por vez.No se pueden utilizar sogas ni
varas, y se comprende que no se puede unir un vagón delante de la locomotora.¿Cuántas veces será necesario invertir
el sentido de marcha de las locomotoras para lograr el paso, contando como un movimiento cada cambio de sentido de
una locomotora?Objetivo: Plantear problemas del tipo de resolución secuencial o scheduling donde una tarea está
secuenciada tras otra
 */

const state = {
	left: ['A4', 'A3', 'A2', 'A1', 'A0'],
	auxiliar: null,
	right: ['B0', 'B1', 'B2', 'B3'],
}

let movements = 0;
function move(from, to){
	movements++;
	let value;
	if(from === 'auxiliar'){
		value = state[from];
		state[from] = null;
	}
	else value = state[from].pop();

	if(to === 'auxiliar') state[to] = value;
	else state[to].push(value);
}

function moveAll(from, to){
	while(state[from].length){
		move(from, to);
	}
}

function moveWagon(from, to){
	moveAll(from, to)
	move(to, 'auxiliar');
	moveAll(to, from);
	move('auxiliar', to);
}

const min_side = state.left.length < state.right.length ? 'left' : 'right';
const min = state[min_side].length;

console.log(min_side, min);

const oposite = min_side === 'left' ? 'right' : 'left';

for(let i = 0; i < min; i++){
	moveWagon(min_side, oposite);
}

console.log(state);
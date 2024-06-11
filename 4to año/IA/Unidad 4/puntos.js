// @ts-nocheck
// square = [esquina inferior izquierda x, esquina inferior izquierda y, esquina superior derecha x, esquina superior dercha y]
const multiplicador = 3
const square1 = [1, 1, 9, 9].map(x => x * multiplicador);
const square2 = [3, 3, 7, 7].map(x => x * multiplicador);
const square3 = [4, 4, 6, 6].map(x => x * multiplicador);

function inSquare(x, y, [x1, y1, x2, y2]){
	return  x1 <= x && x <= x2 &&
			y1 <= y && y <= y2
}

const arr = [['x', 'y', 'type']]
const a = Array(10 * multiplicador).fill(' ').map(x => Array(10 * multiplicador).fill(' '))

for(let i = 0; i < 10 * multiplicador; i++){
	for(let j = 0; j < 10 * multiplicador; j++){
		if(inSquare(i, j, square3)){
			a[i][j] = 'y'
			arr.push([i / multiplicador, j / multiplicador, 'y'])
		}else if(inSquare(i, j, square1) && !inSquare(i, j, square2)){
			a[i][j] = 'x';
			arr.push([i / multiplicador, j / multiplicador, 'x'])
		}
		
	}
}

// console.log(a.map(x => x.join('')).join('\n'));

require('fs').writeFileSync('./data.csv', arr.map(x => x.join(',')).join('\n'))
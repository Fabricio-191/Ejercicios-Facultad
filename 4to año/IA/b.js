// @ts-nocheck
/*
Find a solution to the problem of the 4 jars, where you have 4 jars with capacities of 24, 13, 11 and 5 liters, and you have to measure get the first three jars with 8 liters each one, and 0 in the fourth. You can only move water from one jar to another, and you can't measure the water in any way. No way to refill or empty the jars.
*/

const capacities = [24, 13, 11, 5];

const start = [24, 0, 0, 0];
const goal = [8, 8, 8, 0];

function moveWater(jars, i, j) {
	jars = jars.slice();
	const diff = Math.min(capacities[j] - jars[j], jars[i]);
	jars[i] -= diff;
	jars[j] += diff;
	return jars;
}

function solve1(start, goal, visited) { // deep first search
	if(start.join('') == goal.join('')) return visited;

	for(let i = 0; i < capacities.length; i++) {
		for(let j = 0; j < capacities.length; j++) {
			if(i != j) {
				const next = moveWater(start, i, j);
				if(!visited.some(v => v.join('') == next.join(''))) {
					const solution = solve(next, goal, [...visited, next]);
					if(solution) return solution;
				}
			}
		}
	}
}

let i = 0;
function solve2(start, goal, visited) { // breadth first search
	const queue = [[start, visited]];
	while(queue.length) {
		const [current, visited] = queue.shift();
		if(current.join('') == goal.join('')){
			console.log(visited.map(x => x.join(' ')).join(' - '))
			if(i++ > 10) return;
		};

		for(let i = 0; i < capacities.length; i++) {
			for(let j = 0; j < capacities.length; j++) {
				if(i != j) {
					const next = moveWater(current, i, j);
					if(!visited.some(v => v.join('') == next.join(''))) {
						queue.push([next, [...visited, next]]);
					}
				}
			}
		}
	}
}

console.log(solve2(start, goal, [start]))

/*
[
  [ 24, 0, 0, 0 ],
  [ 13, 0, 11, 0 ],
  [ 8, 0, 11, 5 ],
  [ 8, 5, 11, 0 ],
  [ 8, 13, 3, 0 ],
  [ 8, 8, 3, 5 ],
  [ 8, 8, 8, 0 ]
]
*/
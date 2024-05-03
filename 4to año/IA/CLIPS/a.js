const paths = [
	['A', 'B'],
	['A', 'C'],
	['B', 'F'],
	['B', 'D'],
	['C', 'D'],
	['D', 'E'],
	['E', 'R'],
	['F', 'G'],
	['F', 'K'],
	['G', 'H'],
	['G', 'I'],
	['H', 'I'],
	['H', 'K'],
	['I', 'J'],
	['I', 'L'],
	['J', 'M'],
	['M', 'N'],
	['L', 'N'],
	['N', 'O'],
	['N', 'P'],
	['P', 'R'],
	['K', 'O'],
	['K', 'Q'],
	['O', 'R'],
	['Q', 'R']
]

// get paths from A to Q

function getPaths(paths, start, end, visited = []) {
	if(start == end) return visited.concat(start);
	const next = paths.filter(p => p[0] == start && !visited.includes(p[1]));
	for(const n of next) {
		const result = getPaths(paths, n[1], end, visited.concat(start));
		if(result) console.log(result);
	}
}

console.log(getPaths(paths, 'A', 'Q'))
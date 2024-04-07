const solution = [
	[20, 34, 40, 5, 1],
	[20, 9, 11, 29, 31],
	[20, 23, 21, 19, 17],
	[20, 27, 25, 15, 13],
	[20, 7, 3, 32, 38],
];
const n = 5;

const copy = obj => JSON.parse(JSON.stringify(obj));
const sum = values => values.flat().reduce((a, b) => a + b, 0);

const solutionsSet = new Set();
function checkSolution(sol){
	// all columns (except the first) add up to 100
	// all rows add up to 100
	const a = JSON.stringify(sol);

	if(solutionsSet.has(a)) return false;

	// check rows
	for(const row of sol){
		if(sum(row) !== 100) return false;
	}

	// check columns
	for(let i = 1; i < n; i++){
		if(sum(sol.map(a => a[i])) !== 100) return false;
	}

	solutionsSet.add(a);

	return true;
}


function exchangeRow(sol, i, j){
	const temp = sol[i];
	sol[i] = sol[j];
	sol[j] = temp;
	return sol;
}

function exchangeColumn(sol, i, j){
	for(let k = 0; k < n; k++){
		const temp = sol[k][i];
		sol[k][i] = sol[k][j];
		sol[k][j] = temp;
	}
	return sol;
}

// try all posible permutations of row and columns at the same time
function permute(sol, startRow, startCol){
	if(startRow === n && startCol === n){
		checkSolution(sol);
	} else {
		for(let i = startRow; i < n; i++){
			for(let j = startCol; j < n; j++){
				sol = exchangeRow(sol, startRow, i);
				sol = exchangeColumn(sol, startCol, j);
				permute(copy(sol), startRow, startCol + 1);
				sol = exchangeRow(sol, startRow, i);
				sol = exchangeColumn(sol, startCol, j);
			}
		}
		if(startRow < n){
			permute(copy(sol), startRow + 1, startCol);
		}
	}
}

permute(solution, 0, 0);


checkSolution(solution);
console.log(solutionsSet.size);

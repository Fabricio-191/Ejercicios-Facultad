const odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31];
const even = [20, 32, 34, 38, 40];
const nums = [...odds, ...even].sort((a, b) => a - b);
const differentValues = (...values) => new Set(values).size === values.length;

for(const indexes of range(0, nums.length - 1, 21, true)){
	if(!differentValues(...indexes)) continue;

	const values = indexes.map(i => nums[i]);
	if(isSolution(values)) console.log(values);
}

function isSolution(values){
	const [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21] = values;
	if(v1 + v2 + v3 + v4 + v5 !== 100) return false;
	if(v1 + v6 + v7 + v8 + v9 !== 100) return false;
	if(v1 + v10 + v11 + v12 + v13 !== 100) return false;
	if(v1 + v14 + v15 + v16 + v17 !== 100) return false;
	if(v1 + v18 + v19 + v20 + v21 !== 100) return false;

	if(v2 + v6 + v10 + v14 + v18 !== 100) return false;
	if(v3 + v7 + v11 + v15 + v19 !== 100) return false;
	if(v4 + v8 + v12 + v16 + v20 !== 100) return false;
	if(v5 + v9 + v13 + v17 + v21 !== 100) return false;

	return true;
}

function* range(start, end, size, triangular = false){
	const range = Array(size).fill(start);

	if(triangular){
		while(range[0] <= end){
			yield range.slice();
			range[size - 1]++;
			
			for(let i = size - 1; i > 0; i--){
				if(range[i] > end) range[i - 1]++;
			}

			for(let i = 0; i < size; i++){
				if(range[i] > end) range[i] = range[i - 1];
			}
		}
	}else while(range[0] <= end){
		yield range.slice();
		range[size - 1]++;
		for(let i = size - 1; i > 0; i--){
			if(range[i] > end){
				range[i] = start;
				range[i - 1]++;
			}
		}
	}
}

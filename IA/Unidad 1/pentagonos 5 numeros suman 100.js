const nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 20, 32, 34, 38, 40].sort((a, b) => a - b);

// find combinations of 5 numbers that add up to 100
const combinations = [];

const differentValues = (...values) => new Set(values).size === values.length;

/*
for(let i = 0; i < nums.length; i++){
	for(let j = i + 1; j < nums.length; j++){
		for(let k = j + 1; k < nums.length; k++){
			for(let l = k + 1; l < nums.length; l++){
				for(let m = l + 1; m < nums.length; m++){
					if(nums[i] + nums[j] + nums[k] + nums[l] + nums[m] === 100){
						combinations.push([nums[i], nums[j], nums[k], nums[l], nums[m]]);
					}
				}
			}
		}
	}
}
*/

for(const [i, j, k, l, m] of range(0, nums.length - 1, 5, true)){
	if(!differentValues(i, j, k, l, m)) continue;

	if(nums[i] + nums[j] + nums[k] + nums[l] + nums[m] === 100){
		combinations.push([nums[i], nums[j], nums[k], nums[l], nums[m]]);
	}
}

console.log(combinations.length);

const frequencies = {};

for(const combination of combinations){
	for(const num of combination){
		frequencies[num] = (frequencies[num] || 0) + 1;
	}
}

console.log(frequencies);

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

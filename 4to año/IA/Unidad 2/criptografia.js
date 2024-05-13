// A * 3000 + G * 300 + U * 30 + A * 3 = S * 10000 + A * 1000 + L * 100 + U * 10 + D

const all = Object.freeze({ // possible values for each letter
	A: [1, 2, 3, 4, 5, 6, 7, 8, 9],
	G: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	U: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	S: [1, 2, 3, 4, 5, 6, 7, 8, 9],
	L: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	D: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
});
const VARS = ['A', 'G', 'U', 'S', 'L', 'D'];

const copy = obj => JSON.parse(JSON.stringify(obj));
const random = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

// A * 2000 + G * 300 + U * 20 + A * 3 = S * 10000 + L * 100 + D

function getRanges(all){
	const mins = Object.fromEntries(Object.keys(all).map(k => [k, Math.min(...all[k])]));
	const maxs = Object.fromEntries(Object.keys(all).map(k => [k, Math.max(...all[k])]));

	const minLeft = mins.A * 2000 + mins.G * 300 + mins.U * 20 + mins.A * 3;
	const maxLeft = maxs.A * 2000 + maxs.G * 300 + maxs.U * 20 + maxs.A * 3;
	const minRight = mins.S * 10000 + mins.L * 100 + mins.D;
	const maxRight = maxs.S * 10000 + maxs.L * 100 + maxs.D;
	const min = Math.max(minLeft, minRight);
	const max = Math.min(maxLeft, maxRight);

	return `{${minLeft}:${maxLeft}} = {${minRight}:${maxRight}}\n       {${min}:${max}}`
}

console.log(getRanges(all));